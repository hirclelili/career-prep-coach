#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def heading_present(text, heading):
    return re.search(rf"^#+\s*{re.escape(heading)}\s*$", text, re.MULTILINE) is not None


def validate_experience(text):
    errors = []
    required = ["完整经历档案", "经历底稿", "单段经历简历表达", "完整经历故事", "面试表达"]
    for heading in required:
        if not heading_present(text, heading):
            errors.append(f"缺少标题：{heading}")
    if "诱饵金句" in text:
        errors.append("不应包含诱饵金句模块")
    if len(re.findall(r"^\s*[-•]\s+\S+", text, re.MULTILINE)) < 3:
        errors.append("可识别的 bullet 数量过少")
    if "### 30 秒开场" not in text:
        errors.append("缺少 30 秒开场")
    if "### 90 秒完整讲法" not in text:
        errors.append("缺少 90 秒完整讲法")
    if len(re.findall(r"\*\*追问\s*\d+\*\*", text)) < 5:
        errors.append("高频追问少于 5 个")
    return errors


def validate_manual(text):
    errors = []
    for number in range(1, 8):
        if not re.search(rf"^##\s*第{['零','一','二','三','四','五','六','七'][number]}章[：:]", text, re.MULTILINE):
            errors.append(f"缺少第{number}章")
    questions = len(re.findall(r"^###\s*Q\d+[：:]", text, re.MULTILINE | re.IGNORECASE))
    if questions < 15 or questions > 20:
        errors.append(f"面试问题数量应为 15-20，当前为 {questions}")
    if "<!--" in text or "MANUAL_COMPLETE" in text:
        errors.append("不应包含 HTML 完成标记")
    if "```mindmap" in text or "# 模块一" in text:
        errors.append("面试手册不应包含知识体系正文")
    return errors


def validate_knowledge(text):
    errors = []
    if "```mermaid" not in text or "mindmap" not in text:
        errors.append("缺少 Mermaid 思维导图")
    modules = len(re.findall(r"^#\s*模块", text, re.MULTILINE))
    if modules < 2 or modules > 4:
        errors.append(f"知识模块应为 2-4 个，当前为 {modules}")
    if not re.search(r"^#\s*应用场景总览\s*$", text, re.MULTILINE):
        errors.append("缺少应用场景总览")
    if "```mindmap-json" in text:
        errors.append("独立 Skill 不应输出 mindmap-json")
    return errors


VALIDATORS = {
    "experience": validate_experience,
    "manual": validate_manual,
    "knowledge": validate_knowledge,
}


def main():
    parser = argparse.ArgumentParser(description="Validate career-prep-coach Markdown artifacts.")
    parser.add_argument("kind", choices=VALIDATORS)
    parser.add_argument("path")
    args = parser.parse_args()

    try:
        text = read_text(args.path)
    except OSError as error:
        print(f"ERROR: 无法读取文件：{error}", file=sys.stderr)
        return 2

    errors = VALIDATORS[args.kind](text)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
