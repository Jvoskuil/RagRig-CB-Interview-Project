#!/usr/bin/env python3
"""Extract Prompt 2 comparison and overall summaries from JSON files into CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

SECTIONS = (
    "evaluation_metadata",
    "comparison_ready_summary",
    "overall_evaluation_summary",
)


def flatten(value: Any, prefix: str = "") -> dict[str, str]:
    result: dict[str, str] = {}
    if isinstance(value, dict):
        for key, item in value.items():
            name = f"{prefix}.{key}" if prefix else str(key)
            result.update(flatten(item, name))
    elif isinstance(value, list):
        result[prefix] = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    elif value is None:
        result[prefix] = ""
    elif isinstance(value, bool):
        result[prefix] = str(value).lower()
    else:
        result[prefix] = str(value)
    return result


def make_row(path: Path) -> dict[str, str]:
    row: dict[str, str] = {
        "source_file": path.name,
        "source_path": str(path),
        "extraction_status": "ok",
        "extraction_error": "",
    }
    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        row["extraction_status"] = "error"
        row["extraction_error"] = str(exc)
        return row

    if not isinstance(data, dict):
        row["extraction_status"] = "error"
        row["extraction_error"] = "Top-level JSON value is not an object."
        return row

    missing = []
    for section in SECTIONS:
        if section not in data:
            missing.append(section)
            continue
        row.update(flatten(data[section], section))

    if missing:
        row["extraction_status"] = "partial"
        row["extraction_error"] = "Missing section(s): " + ", ".join(missing)

    return row


def find_json_files(folder: Path, recursive: bool) -> list[Path]:
    iterator = folder.rglob("*") if recursive else folder.iterdir()
    return sorted(
        path for path in iterator
        if path.is_file() and path.suffix.lower() == ".json"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create one CSV row per Prompt 2 evaluator JSON file, extracting "
            "comparison_ready_summary and overall_evaluation_summary."
        )
    )
    parser.add_argument(
        "input_folder",
        nargs="?",
        default=".",
        help="Folder containing Prompt 2 JSON output files (default: current folder).",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output CSV path (default: prompt2_summaries.csv in input_folder).",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Also search subfolders. Default searches only the specified folder.",
    )
    args = parser.parse_args()

    input_folder = Path(args.input_folder).expanduser().resolve()
    if not input_folder.is_dir():
        parser.error(f"Input folder does not exist or is not a directory: {input_folder}")

    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else input_folder / "prompt2_summaries.csv"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    json_files = find_json_files(input_folder, args.recursive)
    if not json_files:
        parser.error(f"No .json files found in: {input_folder}")

    rows = [make_row(path) for path in json_files]
    preferred = [
        "source_file",
        "source_path",
        "extraction_status",
        "extraction_error",
        "evaluation_metadata.benchmark_run_metadata.benchmark_run_id",
        "evaluation_metadata.benchmark_run_metadata.interview_id",
        "evaluation_metadata.benchmark_run_metadata.system_prompt_id",
        "evaluation_metadata.benchmark_run_metadata.system_prompt_generator",
        "evaluation_metadata.benchmark_run_metadata.rag_model_id",
        "evaluation_metadata.benchmark_run_metadata.corpus_condition",
        "evaluation_metadata.benchmark_run_metadata.replicate_id",
        "evaluation_metadata.condition",
        "evaluation_metadata.scenario_id",
        "comparison_ready_summary.primary_recommended_comparison_threshold",
    ]
    all_fields = {field for row in rows for field in row}
    fieldnames = [field for field in preferred if field in all_fields]
    fieldnames += sorted(all_fields - set(fieldnames))

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    ok = sum(row["extraction_status"] == "ok" for row in rows)
    partial = sum(row["extraction_status"] == "partial" for row in rows)
    errors = sum(row["extraction_status"] == "error" for row in rows)
    print(f"Wrote {len(rows)} row(s) to: {output_path}")
    print(f"Status: {ok} ok, {partial} partial, {errors} error")


if __name__ == "__main__":
    main()
