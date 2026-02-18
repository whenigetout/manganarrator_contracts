// mn_contracts/video.ts

import type {
    OriginalImageBBox,
    MediaRef,
    ImageInfo,
    OCRRun,
} from "./ocr.js";

/* ============================
    Render / FFmpeg config
   ============================ */

export interface RenderConfig {
    fps: number;

    viewport_w: number;
    viewport_h: number;
    side_margin_px: number;
    first_dialog_top_padding: number;
    last_dialog_bottom_padding: number;

    vcodec: string;
    preset: string;
    tune: string;
    cq: number;
    pix_fmt: string;

    acodec: string;
    audio_bitrate: string;
    audio_default_sample_rate: number;
    default_silent_clip_duration: number;

    verbose: boolean;
    capture_stdout: boolean;
    capture_stderr: boolean;
    keep_segments: boolean;
}

/**
 * Default RenderConfig (mirrors Pydantic defaults)
 */
export const DEFAULT_RENDER_CONFIG: RenderConfig = {
    fps: 24,

    viewport_w: 1080,
    viewport_h: 1920,
    side_margin_px: 0,
    first_dialog_top_padding: 10,
    last_dialog_bottom_padding: 10,

    vcodec: "h264_nvenc",
    preset: "p5",
    tune: "hq",
    cq: 23,
    pix_fmt: "yuv420p",

    acodec: "aac",
    audio_bitrate: "192k",
    audio_default_sample_rate: 44100,
    default_silent_clip_duration: 3,

    verbose: true,
    capture_stdout: false,
    capture_stderr: false,
    keep_segments: false,
};

/* ============================
    Geometry helpers
   ============================ */

export interface Size {
    w: number;
    h: number;
}

/* ============================
    Dialogue-level video data
   ============================ */

export interface VideoDialogueLine {
    id: number;
    image_id: number;
    text: string;
    speaker: string;
    emotion: string;
    original_bbox: OriginalImageBBox;
    audio_ref: MediaRef;
}

/* ============================
    Render span (ffmpeg-safe)
   ============================ */

/**
 * SegmentRenderSpan describes the FINAL, ffmpeg-safe render intent.
 *
 * All coordinates are expressed in a padded, scaled-image space:
 * - image_scale: uniform scale applied to the original image
 * - empty_space_top / bottom: black space to be added before cropping
 * - crop_y1 / crop_y2: crop box AFTER padding is applied
 *
 * This guarantees that preview rendering and ffmpeg rendering
 * produce identical visuals.
 */
export interface SegmentRenderSpan {
    crop_y1: number;
    crop_y2: number;
    render_height: number;
    image_scale: number;

    empty_space_top: number;
    empty_space_bottom: number;
    empty_space_left: number;
    empty_space_right: number;
}

/* ============================
    Segments
   ============================ */

export interface Segment {
    segment_id: number;
    image_id: number;
    run_id: number;
    base_y1: number;
    base_y2: number;
    image_info: ImageInfo;
    video_dialogue_ids: number[];
}

/* ============================
    Rendered segment
   ============================ */

export interface RenderedSegment {
    segment: Segment;
    render_span: SegmentRenderSpan;
    viewport_size: Size;
}

/* ============================
    Preview timeline
   ============================ */

export interface SegmentPreview {
    rendered_segment: RenderedSegment;
    duration: number;
    video_dialogue_lines: VideoDialogueLine[];
    out_dir_ref: MediaRef;
    out_file_ref: MediaRef;
}

export interface ImagePreview {
    run_id: string;
    image_id: number;
    base_timeline: SegmentPreview[];
    out_dir_ref: MediaRef;
    out_file_ref: MediaRef;
}

export interface VideoPreview {
    run_id: string;
    image_previews: ImagePreview[];
    out_dir_ref: MediaRef;
    out_file_ref: MediaRef;
}

/* ============================
    Build input
   ============================ */

export interface BuildVideoInput {
    ocr_run: OCRRun;
    render_config: RenderConfig;
}
