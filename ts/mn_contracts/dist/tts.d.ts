import { MediaRef } from "./ocr.js";
import { EmotionParams } from "./tts_cfg.js";
import { GenderKey } from "./tts_cfg.js";
export interface TTSInput {
    text: string;
    gender: GenderKey;
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
