from pydantic import BaseModel
from pathlib import Path
from typing import Union, Optional
import json
import mn_contracts.ocr as o
import traceback

def log_exception(context: str = "Unhandled exception", label: str = "💀"):
    print(f"\n{label} {context}:")
    traceback.print_exc()

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

def build_media_Ref(
        namespace: o.MediaNamespace,
        path: str | Path,
        media_root: Optional[str | Path] = None
        ) -> o.MediaRef:
    try:
        path = Path(path)

        # calculate relative path if media_root is passed, else use the given path
        if media_root:
            path = path.relative_to(Path(media_root) / namespace.value)
        
        media_ref = o.MediaRef(
            namespace=namespace,
            path=str(path.as_posix()),
        )
        return media_ref
    except Exception as e:
        raise ValueError("Invalid path passed") from e

def load_yaml(path: Path | str):
    import yaml
    
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing YAML config: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)