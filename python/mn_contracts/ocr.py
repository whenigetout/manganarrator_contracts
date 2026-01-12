from pydantic import BaseModel, field_validator, model_validator
from pathlib import Path
from typing import Literal, Any, Optional, List
from enum import Enum

class MediaNamespace(str, Enum):
    INPUTS = "inputs"
    OUTPUTS = "outputs"

class MediaRef(BaseModel):
    namespace: MediaNamespace
    path: str

    @field_validator("path")
    @classmethod
    def validate_path(cls, v: str) -> str:
        p = Path(v)

        # must be relative
        if p.is_absolute():
            raise ValueError("MediaRef.path must be a relative path")

        # no traversal
        if ".." in p.parts:
            raise ValueError("MediaRef.path must not contain '..'")

        # normalize to posix
        return p.as_posix()

    @property
    def filename(self) -> str:
        return Path(self.path).name

    @property
    def suffix(self) -> str:
        return Path(self.path).suffix
    
    @property
    def posix_path_from_media_root(self) -> str:
        return str(Path(self.namespace.value) / self.path)
    
    @property
    def posix_path_from_namespace(self) -> str:
        return str(Path(self.path).as_posix)
    
    def namespace_path(self, media_root: Path) -> Path:
        return media_root / self.namespace.value 
    
    def resolve(self, media_root: Path) -> Path:
        return media_root / self.namespace.value / self.path

class ImageInfo(BaseModel):
    image_ref: MediaRef
    image_width: int
    image_height: int

class OriginalImageBBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float

    def scaled(self, scale: float) -> "OriginalImageBBox":
        return OriginalImageBBox(
            x1=int(self.x1 * scale),
            y1=int(self.y1 * scale),
            x2=int(self.x2 * scale),
            y2=int(self.y2 * scale),
        )

class DialogueLine(BaseModel):
    id: int
    image_id: str
    speaker: str
    gender: str
    emotion: str
    text: str
    status: Literal["ok", "failed"]
    error: Optional[str] = None
    original_bbox: Optional[OriginalImageBBox] = None

class OCRImage(BaseModel):
    image_id: str
    has_text: bool
    image_info: ImageInfo
    dialogue_lines: list[DialogueLine]

class OCRRun(BaseModel):
    # path to THE json file (with bboxes)
    run_id: str
    error: Optional[str] = None
    ocr_json_file: MediaRef
    images: List[OCRImage]
