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
