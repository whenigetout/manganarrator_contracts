import { MediaRef } from "./ocr";

/* ---------------- emotion ---------------- */

export interface EmotionParams {
    cfg: number;          // >= 0.0
    exaggeration: number; // >= 0.0
}

export interface Emotion {
    name: string;
    params: EmotionParams;
}

export const EMOTIONS: Record<string, Emotion> = {
    neutral: {
        name: "neutral",
        params: { cfg: 0.5, exaggeration: 0.5 },
    },
    calm: {
        name: "calm",
        params: { cfg: 0.45, exaggeration: 0.4 },
    },
    happy: {
        name: "happy",
        params: { cfg: 0.65, exaggeration: 0.7 },
    },
    sad: {
        name: "sad",
        params: { cfg: 0.55, exaggeration: 0.6 },
    },
    angry: {
        name: "angry",
        params: { cfg: 0.75, exaggeration: 0.85 },
    },
} as const;

export const DEFAULT_EMOTION = "neutral";

/* ---------------- gender ---------------- */

export type GenderValue = "female" | "male" | "neutral";

export interface Gender {
    value: GenderValue;
}

export const GENDERS: Record<GenderValue, Gender> = {
    female: { value: "female" },
    male: { value: "male" },
    neutral: { value: "neutral" },
};

export const DEFAULT_GENDER: GenderValue = "neutral";

/* ---------------- speaker ---------------- */

export interface Speaker {
    name: string;
    wav_file: string;
    gender: Gender;
}

export const SPEAKER_GROUPS: Record<
    string,
    Record<string, Speaker>
> = {
    female: {
        default: {
            name: "default",
            wav_file: "female_default.wav",
            gender: GENDERS.female,
        },
        soft: {
            name: "soft",
            wav_file: "female_soft.wav",
            gender: GENDERS.female,
        },
        dominant: {
            name: "dominant",
            wav_file: "female_dom.wav",
            gender: GENDERS.female,
        },
    },
    male: {
        default: {
            name: "default",
            wav_file: "male_default.wav",
            gender: GENDERS.male,
        },
    },
    unknown: {
        default: {
            name: "default",
            wav_file: "neutral.wav",
            gender: GENDERS[DEFAULT_GENDER],
        },
    },
};

export const DEFAULT_GROUP = "unknown";
export const DEFAULT_SPEAKER = "default";

/* ---------------- tts io ---------------- */

export interface TTSInput {
    text: string;
    gender: Gender;
    emotion: Emotion;
    speaker: Speaker;
    image_ref: MediaRef;

    customSettings?: EmotionParams;
    run_id?: string;
    custom_filename?: string;
    dialogue_id?: number;
}

export interface TTSOutput {
    ttsInput: TTSInput;
    audio_ref: MediaRef;
}

export interface EmotionOptionsOutput {
    emotionOptions: Emotion[];
}
