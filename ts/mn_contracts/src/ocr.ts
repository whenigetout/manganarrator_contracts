export enum MediaNamespace {
    INPUTS = "inputs",
    OUTPUTS = "outputs",
}

export interface MediaRef {
    namespace: MediaNamespace
    path: string
}

export interface ImageInfo {
    image_ref: MediaRef
    image_text: any
    image_width: number
    image_height: number
}

export interface OriginalImageBBox {
    x1: number
    y1: number
    x2: number
    y2: number
}

export interface DialogueLine {
    id: number
    image_id: string
    speaker: string
    gender: string
    emotion: string
    text: string
    original_bbox?: OriginalImageBBox
}

export interface OCRImage {
    image_id: string
    image_info?: ImageInfo
    dlg_lines?: DialogueLine[]
}

export interface OCRRun {
    run_id: string
    error?: string
    ocr_json_file: MediaRef
    images?: OCRImage[]
}
