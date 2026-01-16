from pathlib import Path
import yaml
import json
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]

YAML_SRC = ROOT / "cfg" / "tts_emotions.yaml"

PY_OUT = ROOT / "python" / "mn_contracts" / "tts_cfg.py"
TS_OUT = ROOT / "ts" / "mn_contracts" / "src" / "tts_cfg.ts"


# -----------------------------
# Load + validate YAML
# -----------------------------

def load_yaml() -> Dict[str, Any]:
    with open(YAML_SRC, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError("Top-level YAML must be a mapping")

    validate_schema(data)
    return data


def validate_schema(cfg: Dict[str, Any]) -> None:
    if "neutral" not in cfg:
        raise ValueError("Top-level 'neutral' gender is required")

    for gender, speakers in cfg.items():
        if not isinstance(speakers, dict):
            raise ValueError(f"{gender} must map to speakers")

        if "neutral" not in speakers:
            raise ValueError(f"{gender} must define a 'neutral' speaker")

        for speaker, data in speakers.items():
            if not isinstance(data, dict):
                raise ValueError(f"{gender}.{speaker} must be a mapping")

            if "voice" not in data:
                raise ValueError(f"{gender}.{speaker} missing 'voice'")

            if "emotions" not in data or not isinstance(data["emotions"], dict):
                raise ValueError(f"{gender}.{speaker}.emotions must be a mapping")

            if "neutral" not in data["emotions"]:
                raise ValueError(f"{gender}.{speaker} must define 'neutral' emotion")


# -----------------------------
# Python generation (Pydantic)
# -----------------------------

def generate_python(cfg: Dict[str, Any]) -> None:
    content = (
        "# AUTO-GENERATED FILE — DO NOT EDIT\n"
        "# Source: cfg/tts_emotions.yaml\n\n"
        "from typing import Dict\n"
        "from pydantic import BaseModel, ConfigDict, TypeAdapter\n\n\n"
        "class EmotionParams(BaseModel):\n"
        "    model_config = ConfigDict(frozen=True)\n\n"
        "    exaggeration: float | None = None\n"
        "    cfg: float | None = None\n"
        "    # future fields allowed automatically\n\n\n"
        "class SpeakerCfg(BaseModel):\n"
        "    model_config = ConfigDict(frozen=True)\n\n"
        "    voice: str\n"
        "    emotions: Dict[str, EmotionParams]\n\n\n"
        "class ResolvedTTS(BaseModel):\n"
        "    model_config = ConfigDict(frozen=True)\n\n"
        "    gender: str\n"
        "    speaker: str\n"
        "    emotion: str\n"
        "    voice: str\n"
        "    params: EmotionParams\n\n\n"
        "TTSCFG_RAW = "
        + json.dumps(cfg, indent=2)
        + "\n\n"
        "_TTSCFG_ADAPTER = TypeAdapter(dict[str, dict[str, SpeakerCfg]])\n"
        "TTSCFG: dict[str, dict[str, SpeakerCfg]] = _TTSCFG_ADAPTER.validate_python(TTSCFG_RAW)\n\n\n"
        "def resolve_tts(\n"
        "    gender: str,\n"
        "    speaker: str,\n"
        "    emotion: str,\n"
        ") -> ResolvedTTS:\n"
        "    \"\"\"\n"
        "    Predictable fallback:\n"
        "      gender → neutral\n"
        "      speaker → neutral\n"
        "      emotion → neutral\n"
        "    Returns fully resolved names + params.\n"
        "    \"\"\"\n\n"
        "    resolved_gender = gender if gender in TTSCFG else 'neutral'\n"
        "    gender_cfg = TTSCFG.get(resolved_gender)\n\n"
        "    if not gender_cfg:\n"
        "        raise KeyError(\"No 'neutral' gender defined in TTSCFG\")\n\n"
        "    resolved_speaker = speaker if speaker in gender_cfg else 'neutral'\n"
        "    speaker_cfg = gender_cfg.get(resolved_speaker)\n\n"
        "    if not speaker_cfg:\n"
        "        raise KeyError(\"No 'neutral' speaker defined\")\n\n"
        "    resolved_emotion = (\n"
        "        emotion if emotion in speaker_cfg.emotions else 'neutral'\n"
        "    )\n"
        "    params = speaker_cfg.emotions.get(resolved_emotion)\n\n"
        "    if not params:\n"
        "        raise KeyError(\"No 'neutral' emotion defined\")\n\n"
        "    return ResolvedTTS(\n"
        "        gender=resolved_gender,\n"
        "        speaker=resolved_speaker,\n"
        "        emotion=resolved_emotion,\n"
        "        voice=speaker_cfg.voice,\n"
        "        params=params,\n"
        "    )\n"
    )

    PY_OUT.write_text(content, encoding="utf-8")


# -----------------------------
# TypeScript generation
# -----------------------------

def generate_ts(cfg: Dict[str, Any]) -> None:
    content = (
        "// AUTO-GENERATED FILE — DO NOT EDIT\n"
        "// Source: cfg/tts_emotions.yaml\n\n"
        "export type EmotionParams = {\n"
        "  exaggeration?: number\n"
        "  cfg?: number\n"
        "}\n\n"
        "export type SpeakerCfg = {\n"
        "  voice: string\n"
        "  emotions: Record<string, EmotionParams>\n"
        "}\n\n"
        "export const TTS_CFG = "
        + json.dumps(cfg, indent=2)
        + " as const\n\n"
        "export type GenderKey = keyof typeof TTS_CFG\n\n"
        "export type ResolvedTTS = {\n"
        "  gender: GenderKey\n"
        "  speaker: string\n"
        "  emotion: string\n"
        "  voice: string\n"
        "  params: EmotionParams\n"
        "}\n\n"
        "export function resolveTTS(\n"
        "  gender: GenderKey,\n"
        "  speaker: string,\n"
        "  emotion: string\n"
        "): ResolvedTTS {\n"
        "  const resolvedGender =\n"
        "    gender in TTS_CFG ? gender : 'neutral'\n\n"
        "  const genderCfg = TTS_CFG[resolvedGender]\n"
        "  if (!genderCfg) {\n"
        "    throw new Error(\"No 'neutral' gender defined in TTS_CFG\")\n"
        "  }\n\n"
        "  const resolvedSpeaker =\n"
        "    speaker in genderCfg ? speaker : 'neutral'\n\n"
        "  const speakerCfg = (genderCfg as any)[resolvedSpeaker]\n"
        "  if (!speakerCfg) {\n"
        "    throw new Error(\"No 'neutral' speaker defined\")\n"
        "  }\n\n"
        "  const resolvedEmotion =\n"
        "    emotion in speakerCfg.emotions ? emotion : 'neutral'\n\n"
        "  const params = speakerCfg.emotions[resolvedEmotion]\n"
        "  if (!params) {\n"
        "    throw new Error(\"No 'neutral' emotion defined\")\n"
        "  }\n\n"
        "  return {\n"
        "    gender: resolvedGender,\n"
        "    speaker: resolvedSpeaker,\n"
        "    emotion: resolvedEmotion,\n"
        "    voice: speakerCfg.voice,\n"
        "    params,\n"
        "  }\n"
        "}\n"
    )

    TS_OUT.write_text(content, encoding="utf-8")


# -----------------------------
# Entry point
# -----------------------------

def main() -> None:
    cfg = load_yaml()
    generate_python(cfg)
    generate_ts(cfg)
    print("✓ Generated TTS contracts with resolved output (Python + TS)")


if __name__ == "__main__":
    main()
