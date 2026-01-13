from pydantic import BaseModel
from pathlib import Path
from typing import Union
import json

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
