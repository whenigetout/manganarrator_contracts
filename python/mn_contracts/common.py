from pydantic import BaseModel
from pathlib import Path
from typing import Union
import json
import mn_contracts.ocr as o

def save_model_json(
    model: BaseModel,
    json_path: Union[str, Path],
    *,
    indent: int = 2,
    ensure_ascii: bool = False,
) -> Path:
    """
    Save any Pydantic model to a JSON file.

    - Accepts str or Path
    - Creates parent directories if needed
    - Uses Pydantic v2 model_dump()
    - Returns the resolved output Path
    """
    path = Path(json_path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(
            model.model_dump(),
            f,
            indent=indent,
            ensure_ascii=ensure_ascii,
        )

    return path

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

def is_path_inside(path: Path, base: Path) -> bool:
    try:
        path.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False

def build_media_Ref(namespace: o.MediaNamespace, path: str | Path) -> o.MediaRef:
    try:
        path = Path(path)
        media_ref = o.MediaRef(
            namespace=namespace,
            path=str(path.as_posix()),
        )
        return media_ref
    except Exception as e:
        raise ValueError("Invalid path passed") from e