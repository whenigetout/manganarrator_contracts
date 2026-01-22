export type EmotionParams = {
    exaggeration: number;
    cfg: number;
};
export type SpeakerCfg = {
    voice: string;
    emotions: Record<string, EmotionParams>;
};
export declare const TTS_CFG: {
    readonly neutral: {
        readonly neutral: {
            readonly voice: "male/male_1.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
    };
    readonly male: {
        readonly neutral: {
            readonly voice: "male/male_1.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly mc: {
            readonly voice: "male/male_mc.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly narrator: {
            readonly voice: "male/male_narrator.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly "speaker 1": {
            readonly voice: "male/male_mc.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly "speaker 2": {
            readonly voice: "male/male_1.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly "speaker 3": {
            readonly voice: "male/male_1.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly "speaker 4": {
            readonly voice: "male/male_1.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.6;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.5;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
    };
    readonly female: {
        readonly neutral: {
            readonly voice: "female/adjest.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.7;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly mc: {
            readonly voice: "female/romantica.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.7;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly romantica: {
            readonly voice: "female/romantica.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.7;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly adjest: {
            readonly voice: "female/adjest.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.7;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly "speaker 1": {
            readonly voice: "female/romantica.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.7;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
        readonly "speaker 2": {
            readonly voice: "female/adjest.wav";
            readonly emotions: {
                readonly neutral: {
                    readonly exaggeration: 0.5;
                    readonly cfg: 0.7;
                };
                readonly happy: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.65;
                };
                readonly sad: {
                    readonly exaggeration: 0.3;
                    readonly cfg: 0.3;
                };
                readonly angry: {
                    readonly exaggeration: 1.3;
                    readonly cfg: 0.6;
                };
                readonly excited: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly surprised: {
                    readonly exaggeration: 1.2;
                    readonly cfg: 0.7;
                };
                readonly nervous: {
                    readonly exaggeration: 0.4;
                    readonly cfg: 0.3;
                };
                readonly aroused: {
                    readonly exaggeration: 0.2;
                    readonly cfg: 0.4;
                };
                readonly scared: {
                    readonly exaggeration: 0.8;
                    readonly cfg: 0.9;
                };
                readonly curious: {
                    readonly exaggeration: 0.7;
                    readonly cfg: 0.4;
                };
                readonly playful: {
                    readonly exaggeration: 1;
                    readonly cfg: 0.4;
                };
                readonly serious: {
                    readonly exaggeration: 1.1;
                    readonly cfg: 0.5;
                };
                readonly calm: {
                    readonly exaggeration: 0.6;
                    readonly cfg: 0.4;
                };
            };
        };
    };
};
export type GenderKey = keyof typeof TTS_CFG;
export type ResolvedTTS = {
    gender: GenderKey;
    speaker: string;
    emotion: string;
    voice: string;
    params: EmotionParams;
};
export declare function resolveTTS(gender: GenderKey, speaker: string, emotion: string): ResolvedTTS;
