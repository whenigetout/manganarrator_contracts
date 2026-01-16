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
# Python generation
# -----------------------------

def generate_python(cfg: Dict[str, Any]) -> None:
    content = (
        "# AUTO-GENERATED FILE — DO NOT EDIT\n"
        "# Source: cfg/tts_emotions.yaml\n\n"
        "from typing import Dict, TypedDict\n\n\n"
        "class EmotionParams(TypedDict, total=False):\n"
        "    exaggeration: float\n"
        "    cfg: float\n"
        "    # future fields allowed (e.g. volume_boost)\n\n\n"
        "class SpeakerCfg(TypedDict):\n"
        "    voice: str\n"
        "    emotions: Dict[str, EmotionParams]\n\n\n"
        "TTSCFG: Dict[str, Dict[str, SpeakerCfg]] = "
        + json.dumps(cfg, indent=2)
        + "\n\n\n"
        "def resolve_tts(\n"
        "    gender: str,\n"
        "    speaker: str,\n"
        "    emotion: str,\n"
        ") -> tuple[str, EmotionParams]:\n"
        "    \"\"\"\n"
        "    Returns (voice_filename, emotion_params)\n"
        "    Safe fallback if speaker/emotion is unknown.\n"
        "    \"\"\"\n\n"
        "    gender_cfg = TTSCFG.get(gender) or {}\n"
        "    speaker_cfg = gender_cfg.get(speaker)\n\n"
        "    if speaker_cfg is None:\n"
        "        speaker_cfg = next(iter(gender_cfg.values()), None)\n\n"
        "    if speaker_cfg is None:\n"
        "        raise KeyError(f\"No speakers defined for gender '{gender}'\")\n\n"
        "    emotions = speaker_cfg['emotions']\n"
        "    params = emotions.get(emotion) or emotions.get('neutral')\n\n"
        "    if params is None:\n"
        "        raise KeyError(f\"No emotion '{emotion}' or 'neutral' defined\")\n\n"
        "    return speaker_cfg['voice'], params\n"
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
        "  const genderCfg = TTS_CFG[gender]\n"
        "  const speakerCfg =\n"
        "    (genderCfg as any)[speaker] ?? Object.values(genderCfg)[0]\n\n"
        "  if (!speakerCfg) {\n"
        "    throw new Error(`No speakers defined for gender ${gender}`)\n"
        "  }\n\n"
        "  const emotions = speakerCfg.emotions\n"
        "  const params = emotions[emotion] ?? emotions['neutral']\n\n"
        "  if (!params) {\n"
        "    throw new Error(`No emotion '${emotion}' or 'neutral' defined`)\n"
        "  }\n\n"
        "  return {\n"
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
    print("✓ Generated TTS contracts for Python and TypeScript")


if __name__ == "__main__":
    main()
