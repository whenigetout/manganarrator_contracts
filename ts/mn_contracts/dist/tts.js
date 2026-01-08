export const EMOTIONS = {
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
};
export const DEFAULT_EMOTION = "neutral";
export const GENDERS = {
    female: { value: "female" },
    male: { value: "male" },
    neutral: { value: "neutral" },
};
export const DEFAULT_GENDER = "neutral";
export const SPEAKER_GROUPS = {
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
