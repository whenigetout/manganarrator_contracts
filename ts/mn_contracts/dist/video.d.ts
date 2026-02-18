import type { OriginalImageBBox, MediaRef, ImageInfo, OCRRun } from "./ocr.js";
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
export declare const DEFAULT_RENDER_CONFIG: RenderConfig;
export interface Size {
    w: number;
    h: number;
}
export interface VideoDialogueLine {
    id: number;
    image_id: number;
    text: string;
    speaker: string;
    emotion: string;
    original_bbox: OriginalImageBBox;
    audio_ref: MediaRef;
}
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
export interface Segment {
    segment_id: number;
    image_id: number;
    run_id: number;
    base_y1: number;
    base_y2: number;
    image_info: ImageInfo;
    video_dialogue_ids: number[];
}
export interface RenderedSegment {
    segment: Segment;
    render_span: SegmentRenderSpan;
    viewport_size: Size;
}
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
export interface BuildVideoInput {
    ocr_run: OCRRun;
    render_config: RenderConfig;
}
