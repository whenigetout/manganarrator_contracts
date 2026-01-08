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