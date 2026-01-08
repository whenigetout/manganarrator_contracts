import { MediaRef } from "./ocr";
export interface EmotionParams {
    cfg: number;
    exaggeration: number;
}
export interface Emotion {
    name: string;
    params: EmotionParams;
}
export declare const EMOTIONS: Record<string, Emotion>;
export declare const DEFAULT_EMOTION = "neutral";
export type GenderValue = "female" | "male" | "neutral";
export interface Gender {
    value: GenderValue;
}
export declare const GENDERS: Record<GenderValue, Gender>;
export declare const DEFAULT_GENDER: GenderValue;
export interface Speaker {
    name: string;
    wav_file: string;
    gender: Gender;
}
export declare const SPEAKER_GROUPS: Record<string, Record<string, Speaker>>;
export declare const DEFAULT_GROUP = "unknown";
export declare const DEFAULT_SPEAKER = "default";
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
