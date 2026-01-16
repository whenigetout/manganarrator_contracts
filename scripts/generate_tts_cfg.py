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
    for gender, speakers in cfg.items():
        if not isinstance(speakers, dict):
            raise ValueError(f"{gender} must map to speakers")

        for speaker, data in speakers.items():
            if not isinstance(data, dict):
                raise ValueError(f"{gender}.{speaker} must be a mapping")

            if "voice" not in data:
                raise ValueError(f"{gender}.{speaker} missing 'voice'")

            if "emotions" not in data:
                raise ValueError(f"{gender}.{speaker} missing 'emotions'")

            if not isinstance(data["emotions"], dict):
                raise ValueError(f"{gender}.{speaker}.emotions must be a mapping")


# -----------------------------
# Python generation (PYDANTIC)
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
        "    # future fields allowed automatically (e.g. volume_boost)\n\n\n"
        "class SpeakerCfg(BaseModel):\n"
        "    model_config = ConfigDict(frozen=True)\n\n"
        "    voice: str\n"
        "    emotions: Dict[str, EmotionParams]\n\n\n"
        "TTSCFG_RAW = "
        + json.dumps(cfg, indent=2)
        + "\n\n"
        "_TTSCFG_ADAPTER = TypeAdapter(dict[str, dict[str, SpeakerCfg]])\n"
        "TTSCFG: dict[str, dict[str, SpeakerCfg]] = _TTSCFG_ADAPTER.validate_python(TTSCFG_RAW)\n\n\n"
        "def resolve_tts(\n"
        "    gender: str,\n"
        "    speaker: str,\n"
        "    emotion: str,\n"
        ") -> tuple[str, EmotionParams]:\n"
        "    \"\"\"\n"
        "    Returns (voice_filename, emotion_params)\n"
        "    Predictable fallback: gender → neutral, speaker → neutral, emotion → neutral\n"
        "    \"\"\"\n\n"
        "    gender_cfg = TTSCFG.get(gender) or TTSCFG.get('neutral')\n"
        "    if not gender_cfg:\n"
        "        raise KeyError(\"No 'neutral' gender defined in TTSCFG\")\n\n"
        "    speaker_cfg = gender_cfg.get(speaker) or gender_cfg.get('neutral')\n"
        "    if not speaker_cfg:\n"
        "        raise KeyError(\"No 'neutral' speaker defined\")\n\n"
        "    params = (\n"
        "        speaker_cfg.emotions.get(emotion)\n"
        "        or speaker_cfg.emotions.get('neutral')\n"
        "    )\n\n"
        "    if not params:\n"
        "        raise KeyError(\"No 'neutral' emotion defined\")\n\n"
        "    return speaker_cfg.voice, params\n"
    )

    PY_OUT.write_text(content, encoding="utf-8")


# -----------------------------
# TypeScript generation (UNCHANGED)
# -----------------------------

def generate_ts(cfg: Dict[str, Any]) -> None:
    content = (
        "// AUTO-GENERATED FILE — DO NOT EDIT\n"
        "// Source: cfg/tts_emotions.yaml\n\n"
        "export type EmotionParams = {\n"
        "  exaggeration?: number\n"
        "  cfg?: number\n"
        "  // future fields allowed (e.g. volume_boost)\n"
        "}\n\n"
        "export type SpeakerCfg = {\n"
        "  voice: string\n"
        "  emotions: Record<string, EmotionParams>\n"
        "}\n\n"
        "export const TTS_CFG = "
        + json.dumps(cfg, indent=2)
        + " as const\n\n"
        "export type GenderKey = keyof typeof TTS_CFG\n"
        "export type SpeakerKey<G extends GenderKey> = keyof typeof TTS_CFG[G]\n"
        "export type EmotionKey = string\n\n"
        "export function resolveTTS(\n"
        "  gender: GenderKey,\n"
        "  speaker: string,\n"
        "  emotion: string\n"
        "): { voice: string; params: EmotionParams } {\n"
        "  const genderCfg = TTS_CFG[gender] ?? TTS_CFG['neutral']\n"
        "  if (!genderCfg) throw new Error(\"No 'neutral' gender defined\")\n\n"
        "  const speakerCfg = (genderCfg as any)[speaker] ?? (genderCfg as any)['neutral']\n"
        "  if (!speakerCfg) throw new Error(\"No 'neutral' speaker defined\")\n\n"
        "  const params = speakerCfg.emotions[emotion] ?? speakerCfg.emotions['neutral']\n"
        "  if (!params) throw new Error(\"No 'neutral' emotion defined\")\n\n"
        "  return { voice: speakerCfg.voice, params }\n"
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
    print("✓ Generated TTS contracts (Python=Pydantic, TS unchanged)")


if __name__ == "__main__":
    main()
