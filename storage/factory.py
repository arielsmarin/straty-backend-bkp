"""
Storage backend factory.
Selects R2 as the storage backend.
"""
import os
import logging

STORAGE_BACKEND = os.getenv("STORAGE_BACKEND", "r2")

if STORAGE_BACKEND != "r2":
    logging.warning("⚠️ STORAGE_BACKEND=%s ignorado; forçando backend R2.", STORAGE_BACKEND)
    STORAGE_BACKEND = "r2"

logging.info(f"📂 Storage backend: {STORAGE_BACKEND}")

from storage.storage_r2 import (
        exists,
        upload_file,
        download_file,
        get_json,
        append_jsonl,
        read_jsonl_slice,
        get_public_url,
        upload_tiles_parallel,
)
logging.info("✅ Using R2 storage backend")

__all__ = [
    "exists",
    "upload_file",
    "download_file",
    "get_json",
    "append_jsonl",
    "read_jsonl_slice",
    "get_public_url",
    "upload_tiles_parallel",
]
