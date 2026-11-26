import argparse
import os
import hashlib
from pathlib import Path
import shutil

EXPECTED_HASH = "cbfbdd569597763c0db75d85ab59296abc2606205d83f21360b41305ff22bd07"

def main():
    parser = argparse.ArgumentParser(description="Make.fun competition entry")
    parser.add_argument("--output-dir", help="Override output directory")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    source_path = script_dir / "entry.png"

    if not source_path.is_file():
        raise FileNotFoundError(f"entry.png not found at {source_path}")

    sha256_src = hashlib.sha256()
    with open(source_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256_src.update(chunk)
    src_hash = sha256_src.hexdigest()

    if src_hash != EXPECTED_HASH:
        raise RuntimeError(f"Source file hash mismatch: expected {EXPECTED_HASH}, got {src_hash}")

    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
        output_dir = Path(output_dir_env) if output_dir_env else Path("/output")
    output_path = output_dir / "entry.png"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_path, output_path)

    sha256_dst = hashlib.sha256()
    with open(output_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256_dst.update(chunk)
    dst_hash = sha256_dst.hexdigest()

    if dst_hash != src_hash:
        raise RuntimeError(f"Destination file hash mismatch: source hash {src_hash}, destination hash {dst_hash}")

    print(f"Successfully copied to {output_path} with verified SHA-256: {dst_hash}")

if __name__ == "__main__":
    main()
