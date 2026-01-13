from pydantic import BaseModel, ValidationError
from typing import List, Optional
import mn_contracts.ocr as d
from pathlib import Path
import mn_contracts.common as c

class MangaDirViewResponse(BaseModel):
    folders: List[d.MediaRef]
    files: List[d.MediaRef]

class LatestTTSResponse(BaseModel):
    status: str                 # "success" | "error"
    audio_path: Optional[str]   # present on success
    error: Optional[str]        # present on error

def latest_tts_audio_ref(
        run_id: str,
        dlg_id: int,
        img_ref: d.MediaRef,
        media_root: str
    ) -> d.MediaRef:
    """
    Returns the latest generated TTS audio file.
    Always returns a consistent JSON response.
    Input is the img file mediaref (namespace and path) and run_id.
    """

    try:
        if not run_id or dlg_id < 0:
            raise ValueError("Invalid run_id or dlg_id passed.")

        def audio_out_dir_path(
                root: Path,
                img_ref: d.MediaRef,
                dlgId: int
        ) -> Path:
            ns = d.MediaNamespace.OUTPUTS.value
            img_path_without_ext = Path(img_ref.path).with_suffix("")
            img_ext_without_dot = img_ref.suffix[1:] # exclude the "."
            out_dir: Path = Path(root)/ns/run_id/f"{img_path_without_ext}_{img_ext_without_dot}/dialogue__{dlgId}"
            return out_dir
        
        base_dir = Path(media_root) / d.MediaNamespace.OUTPUTS.value
        target_path = audio_out_dir_path(
            root=Path(media_root),
            img_ref=img_ref,
            dlgId=dlg_id
        )

        # should be inside outputs folder
        if not c.is_path_inside(target_path, base_dir):
            raise ValueError("Invalid path param passed.")

        if not target_path.exists():
            raise ValueError("TTS not generated yet.")
        
        if not target_path.is_dir():
            raise ValueError("Path is not a folder.")
        
        def extract_version(fname):
            try:
                ver = fname.split("__")[0]
                return int(ver.replace("v", ""))
            except:
                return -1
            
        audio_files = sorted(
            (
                p for p in target_path.glob("*.wav")
                if p.name.startswith("v") and extract_version(p.name) >= 0
            ),
            key=lambda p: extract_version(p.name),
            reverse=True
        )

        if not audio_files:
            raise ValueError("No audio found in folder.")

        latest_audio = audio_files[0]

        # Convert to relative path if needed by frontend
        audio_path_inside_base_dir = str(latest_audio.relative_to(base_dir).as_posix())
        audio_ref = d.MediaRef(
            namespace=d.MediaNamespace.OUTPUTS,
            path=audio_path_inside_base_dir
        )

        return audio_ref

    except Exception as e:
        # --- HARD FAILURE SAFETY NET ---
        raise
