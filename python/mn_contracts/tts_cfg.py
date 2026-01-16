# AUTO-GENERATED FILE — DO NOT EDIT
# Source: cfg/tts_emotions.yaml

from typing import Dict, TypedDict


class EmotionParams(TypedDict, total=False):
    exaggeration: float
    cfg: float
    # future fields allowed (e.g. volume_boost)


class SpeakerCfg(TypedDict):
    voice: str
    emotions: Dict[str, EmotionParams]


TTSCFG: Dict[str, Dict[str, SpeakerCfg]] = {
  "neutral": {
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
    },
    "male_generic": {
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
    "female_generic": {
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


def resolve_tts(
    gender: str,
    speaker: str,
    emotion: str,
) -> tuple[str, EmotionParams]:
    """
    Returns (voice_filename, emotion_params)
    Safe fallback if speaker/emotion is unknown.
    """

    gender_cfg = TTSCFG.get(gender) or {}
    speaker_cfg = gender_cfg.get(speaker)

    if speaker_cfg is None:
        speaker_cfg = next(iter(gender_cfg.values()), None)

    if speaker_cfg is None:
        raise KeyError(f"No speakers defined for gender '{gender}'")

    emotions = speaker_cfg['emotions']
    params = emotions.get(emotion) or emotions.get('neutral')

    if params is None:
        raise KeyError(f"No emotion '{emotion}' or 'neutral' defined")

    return speaker_cfg['voice'], params
