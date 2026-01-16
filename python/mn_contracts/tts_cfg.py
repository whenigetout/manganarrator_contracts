# AUTO-GENERATED FILE — DO NOT EDIT
# Source: cfg/tts_emotions.yaml

from typing import Dict
from pydantic import BaseModel, ConfigDict, TypeAdapter


class EmotionParams(BaseModel):
    model_config = ConfigDict(frozen=True)

    exaggeration: float | None = None
    cfg: float | None = None
    # future fields allowed automatically


class SpeakerCfg(BaseModel):
    model_config = ConfigDict(frozen=True)

    voice: str
    emotions: Dict[str, EmotionParams]


class ResolvedTTS(BaseModel):
    model_config = ConfigDict(frozen=True)

    gender: str
    speaker: str
    emotion: str
    voice: str
    params: EmotionParams


TTSCFG_RAW = {
  "neutral": {
    "neutral": {
      "voice": "male_default.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 0.6,
          "cfg": 0.4
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    }
  },
  "male": {
    "speaker 1": {
      "voice": "male_default.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.5,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    },
    "neutral": {
      "voice": "male_generic.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.5,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    }
  },
  "female": {
    "speaker 1": {
      "voice": "rote_soft.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.7
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    },
    "neutral": {
      "voice": "male_generic.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.7
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    },
    "female_shelby": {
      "voice": "male_generic.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    },
    "rote_loud": {
      "voice": "male_generic.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    },
    "rote_soft": {
      "voice": "male_generic.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    },
    "rote_very_soft": {
      "voice": "male_generic.wav",
      "emotions": {
        "neutral": {
          "exaggeration": 0.5,
          "cfg": 0.6
        },
        "happy": {
          "exaggeration": 1.1,
          "cfg": 0.65
        },
        "sad": {
          "exaggeration": 0.3,
          "cfg": 0.3
        },
        "angry": {
          "exaggeration": 1.3,
          "cfg": 0.6
        },
        "excited": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "surprised": {
          "exaggeration": 1.2,
          "cfg": 0.7
        },
        "nervous": {
          "exaggeration": 0.4,
          "cfg": 0.3
        },
        "aroused": {
          "exaggeration": 0.2,
          "cfg": 0.4
        },
        "scared": {
          "exaggeration": 0.8,
          "cfg": 0.9
        },
        "curious": {
          "exaggeration": 0.7,
          "cfg": 0.4
        },
        "playful": {
          "exaggeration": 1.0,
          "cfg": 0.4
        },
        "serious": {
          "exaggeration": 1.1,
          "cfg": 0.5
        },
        "calm": {
          "exaggeration": 0.6,
          "cfg": 0.4
        }
      }
    }
  }
}

_TTSCFG_ADAPTER = TypeAdapter(dict[str, dict[str, SpeakerCfg]])
TTSCFG: dict[str, dict[str, SpeakerCfg]] = _TTSCFG_ADAPTER.validate_python(TTSCFG_RAW)


def resolve_tts(
    gender: str,
    speaker: str,
    emotion: str,
) -> ResolvedTTS:
    """
    Predictable fallback:
      gender → neutral
      speaker → neutral
      emotion → neutral
    Returns fully resolved names + params.
    """

    resolved_gender = gender if gender in TTSCFG else 'neutral'
    gender_cfg = TTSCFG.get(resolved_gender)

    if not gender_cfg:
        raise KeyError("No 'neutral' gender defined in TTSCFG")

    resolved_speaker = speaker if speaker in gender_cfg else 'neutral'
    speaker_cfg = gender_cfg.get(resolved_speaker)

    if not speaker_cfg:
        raise KeyError("No 'neutral' speaker defined")

    resolved_emotion = (
        emotion if emotion in speaker_cfg.emotions else 'neutral'
    )
    params = speaker_cfg.emotions.get(resolved_emotion)

    if not params:
        raise KeyError("No 'neutral' emotion defined")

    return ResolvedTTS(
        gender=resolved_gender,
        speaker=resolved_speaker,
        emotion=resolved_emotion,
        voice=speaker_cfg.voice,
        params=params,
    )
