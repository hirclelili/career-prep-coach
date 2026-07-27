#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_name="career-prep-coach"
source_dir="$repo_root/skills/$skill_name"
output_dir="$repo_root/dist"
work_dir="$(mktemp -d)"

trap 'rm -rf "$work_dir"' EXIT

mkdir -p "$output_dir"
cp -R "$source_dir" "$work_dir/$skill_name"
find "$work_dir/$skill_name" -name '.DS_Store' -delete
find "$work_dir/$skill_name" -type d -name '__pycache__' -prune -exec rm -rf {} +
find "$work_dir/$skill_name" -name '*.pyc' -delete

rm -f "$output_dir/$skill_name.zip"
(
  cd "$work_dir"
  zip -qr "$output_dir/$skill_name.zip" "$skill_name"
)

echo "$output_dir/$skill_name.zip"
