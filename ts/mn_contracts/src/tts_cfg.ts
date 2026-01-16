// AUTO-GENERATED FILE — DO NOT EDIT
// Source: cfg/tts_emotions.yaml

export type EmotionParams = {
  exaggeration?: number
  cfg?: number
  // future fields allowed (e.g. volume_boost)
}

export type SpeakerCfg = {
  voice: string
  emotions: Record<string, EmotionParams>
}

export const TTS_CFG = {
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
} as const

export type GenderKey = keyof typeof TTS_CFG
export type SpeakerKey<G extends GenderKey> = keyof typeof TTS_CFG[G]
export type EmotionKey = string

export function resolveTTS(
  gender: GenderKey,
  speaker: string,
  emotion: string
): { voice: string; params: EmotionParams } {
  const genderCfg = TTS_CFG[gender] ?? TTS_CFG['neutral']
  if (!genderCfg) throw new Error("No 'neutral' gender defined")

  const speakerCfg = (genderCfg as any)[speaker] ?? (genderCfg as any)['neutral']
  if (!speakerCfg) throw new Error("No 'neutral' speaker defined")

  const params = speakerCfg.emotions[emotion] ?? speakerCfg.emotions['neutral']
  if (!params) throw new Error("No 'neutral' emotion defined")

  return { voice: speakerCfg.voice, params }
}
