from pydantic import BaseModel, Field, ConfigDict, field_validator
from enum import Enum
from typing import Optional, Literal, List
from pathlib import Path
import mn_contracts.ocr as o
from enum import Enum
from mn_contracts.tts_cfg import EmotionParams

class TTSInput(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str
    gender: str
    emotion: str
    speaker: str
    image_ref: o.MediaRef

    customSettings: Optional[EmotionParams] = None
    run_id: Optional[str] = None
    custom_filename: Optional[str] = None
    dialogue_id: Optional[int] = None

class TTSOutput(BaseModel):
    model_config = ConfigDict(frozen=True)

    ttsInput: TTSInput
    audio_ref: o.MediaRef

class EmotionOptionsOutput(BaseModel):
    model_config = ConfigDict(frozen=True)

    emotionOptions: List[str]

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

    ns = media_namespace.value

    base_dir = (
        media_root
        / ns
        / run_id
        / f"{img_path_without_ext}_{img_ext}"
        / f"dialogue__{dialogue_id}"
    )

    ensure_dir(base_dir)

    version = get_next_version(base_dir)
    filename = f"v{version}__{suffix}.{ext}"

    out_path = base_dir / filename
    out_path.write_bytes(content)

    return MediaRef(
        namespace=media_namespace,
        path=out_path.relative_to(media_root / ns).as_posix()
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
