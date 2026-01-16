import { MediaRef } from "./ocr.js";

/* ---------------- responses ---------------- */

export interface MangaDirViewResponse {
    folders: MediaRef[];
    files: MediaRef[];
}

export interface LatestTTSResponse {
    status: "success" | "error";
    audio_path?: string;
    error?: string;
}

export type MediaType = "audio" | "video"

export interface SaveMediaRequest {
    // identity
    run_id: string

    // location / association
    image_id?: number
    image_ref: MediaRef
    dialogue_id?: number

    // media description
    media_type?: MediaType
    ext?: string
    suffix?: string

    // optional metadata
    source?: string
}
