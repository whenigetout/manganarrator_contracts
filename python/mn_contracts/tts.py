from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum
from typing import Optional, Literal, Final
from pathlib import Path
import ocr as o

class EmotionParams(BaseModel):
    model_config = ConfigDict(frozen=True)

    cfg: float = Field(ge=0.0)
    exaggeration: float = Field(ge=0.0)

class Emotion(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    params: EmotionParams


EMOTIONS: Final[dict[str, Emotion]] = {
    "neutral": Emotion(
        name="neutral",
        params=EmotionParams(cfg=0.5, exaggeration=0.5),
    ),
    "calm": Emotion(
        name="calm",
        params=EmotionParams(cfg=0.45, exaggeration=0.4),
    ),
    "happy": Emotion(
        name="happy",
        params=EmotionParams(cfg=0.65, exaggeration=0.7),
    ),
    "sad": Emotion(
        name="sad",
        params=EmotionParams(cfg=0.55, exaggeration=0.6),
    ),
    "angry": Emotion(
        name="angry",
        params=EmotionParams(cfg=0.75, exaggeration=0.85),
    ),
}

DEFAULT_EMOTION: Final[str] = "neutral"

class Gender(BaseModel):
    model_config = ConfigDict(frozen=True)

    value: Literal["female", "male", "neutral"]

GENDERS: Final[dict[str, Gender]] = {
    "female": Gender(value="female"),
    "male": Gender(value="male"),
    "neutral": Gender(value="neutral"),
}

DEFAULT_GENDER: Final[str] = "neutral"

class Speaker(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    wav_file: str
    gender: Gender

SPEAKER_GROUPS: Final[dict[str, dict[str, Speaker]]] = {
    "female": {
        "default": Speaker(name="default", wav_file="female_default.wav", gender=GENDERS["female"]),
        "soft": Speaker(name="soft", wav_file="female_soft.wav", gender=GENDERS["female"]),
        "dominant": Speaker(name="dominant", wav_file="female_dom.wav", gender=GENDERS["female"]),
    },
    "male": {
        "default": Speaker(name="default", wav_file="male_default.wav", gender=GENDERS["male"]),
    },
    "unknown": {
        "default": Speaker(name="default", wav_file="neutral.wav", gender=GENDERS[DEFAULT_GENDER]),
    },
}

DEFAULT_GROUP: Final[str] = "unknown"
DEFAULT_SPEAKER: Final[str] = "default"

class TTSInput(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str
    gender: Gender
    emotion: Emotion
    speaker: Speaker
    image_ref: o.MediaRef
    customSettings: Optional[EmotionParams] = None
    run_id: str = ""
    custom_filename: str = ""
    dialogue_id: int = -1

class TTSOutput(BaseModel):
    model_config = ConfigDict(frozen=True)

    ttsInput: TTSInput
    audio_ref: o.MediaRef

class EmotionOptionsOutput(BaseModel):
    model_config = ConfigDict(frozen=True)

    emotionOptions: list[Emotion]

# utils.py

from pathlib import Path
from typing import Literal
from mn_contracts.ocr import MediaRef, MediaNamespace
from mn_contracts.common import ensure_dir

def save_versioned_media(
    *,
    media_root: Path,
    media_namespace: MediaNamespace,
    run_id: str,
    image_ref: MediaRef,
    dialogue_id: int,
    ext: str,
    content: bytes,
    suffix: str = "recorded"
) -> MediaRef:
    """
    Save versioned media (audio/video/etc) for a dialogue line.
    """

    img_path_without_ext = Path(image_ref.path).with_suffix("")
    img_ext = image_ref.suffix[1:]

    base_dir = (
        media_root
        / media_namespace
        / run_id
        / f"{img_path_without_ext.name}_{img_ext}"
        / f"dialogue__{dialogue_id}"
    )

    ensure_dir(base_dir)

    version = get_next_version(base_dir)
    filename = f"v{version}__{suffix}.{ext}"

    out_path = base_dir / filename
    out_path.write_bytes(content)

    return MediaRef(
        namespace=media_namespace,
        path=out_path.relative_to(media_root / media_namespace).as_posix()
    )

# Helper to extract version number of tts generated wav file by checking existing files
def get_next_version(
        folder_path: Path | str, 
        media_type: Optional[Literal["tts_or_recorded_audio"]] = "tts_or_recorded_audio"
        ) -> int:
    if media_type != "tts_or_recorded_audio":
        raise ValueError("Unkown mediatype param passed, cannot compute next version.")
    pattern = f"v*.wav"
    versions = []
    folder_path = Path(folder_path)
    if not folder_path.exists() or not folder_path.is_dir():
        raise ValueError("Invalid tts output folder.")
    for file in folder_path.glob(pattern):
        parts = file.stem.split("__")
        if len(parts) > 0 and parts[0].startswith("v"):
            try:
                version_num = int(parts[0][1:])
                versions.append(version_num)
            except ValueError:
                continue
    return max(versions, default=0) + 1