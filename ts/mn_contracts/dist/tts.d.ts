import { MediaRef } from "./ocr.js";
import { EmotionParams } from "./tts_cfg.js";
export type GenderValue = "female" | "male" | "neutral";
export declare enum Gender {
    FEMALE = "female",
    MALE = "male",
    NEUTRAL = "neutral"
}
export interface TTSInput {
    text: string;
    gender: Gender;
    emotion: string;
    speaker: string;
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
    emotionOptions: string[];
}
