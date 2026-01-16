import { MediaRef } from "./ocr.js";
export interface MangaDirViewResponse {
    folders: MediaRef[];
    files: MediaRef[];
}
export interface LatestTTSResponse {
    status: "success" | "error";
    audio_path?: string;
    error?: string;
}
export type MediaType = "audio" | "video";
export interface SaveMediaRequest {
    run_id: string;
    image_id?: number;
    image_ref: MediaRef;
    dialogue_id?: number;
    media_type?: MediaType;
    ext?: string;
    suffix?: string;
    source?: string;
}
