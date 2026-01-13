// mn_contracts/video.ts
/**
 * Default RenderConfig (mirrors Pydantic defaults)
 */
export const DEFAULT_RENDER_CONFIG = {
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
    default_silent_clip_duration: 3,
    verbose: true,
    capture_stdout: false,
    capture_stderr: false,
    keep_segments: false,
};
