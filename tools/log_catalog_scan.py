#!/usr/bin/env python3
"""Offline source-only Java logging inventory. No external dependencies or runtime access.
Usage: python tools/log_catalog_scan.py /path/to/chat-server --commit <sha> --output inventory.json
Limitations: regex-based candidate scanner; human validation required for multiline,
wrapper aliases, commented blocks, methods, and runtime semantics.
"""
import argparse
import json
import pathlib
import re
import subprocess
from collections import Counter

PATTERN = re.compile(r"\b(?P<alias>[A-Za-z_$][\w$]*)\s*\.\s*(?P<level>trace|debug|info|warn|error|fatal|log)\s*\(", re.I)
FACTORY = re.compile(r"(?:LoggerFactory|LogManager|Logger)\s*\.\s*getLogger\s*\(")
def main():
    p = argparse.ArgumentParser()
    p.add_argument("repo", type=pathlib.Path)
    p.add_argument("--commit", required=True)
    p.add_argument("--output", default="log-catalog-inventory.json")
    a = p.parse_args()
    repo = a.repo.resolve()
    actual = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    if actual != a.commit:
        raise SystemExit(f"Commit mismatch: expected {a.commit}, found {actual}; checkout exact source commit first")
    files = sorted((repo / "src/main/java").rglob("*.java"))
    records, aliases, failures = [], [], []
    for file in files:
        rel = file.relative_to(repo).as_posix()
        try:
            lines = file.read_text(encoding="utf-8").splitlines()
        except Exception as exc:
            failures.append({"path": rel, "error": str(exc)})
            continue
        for number, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith(("//", "*", "/*")):
                continue
            if FACTORY.search(line):
                aliases.append({"path": rel, "line": number, "text": stripped})
            for m in PATTERN.finditer(line):
                records.append({"key": f"{a.commit}:{rel}:{number}:{m.group('alias')}:{m.group('level').lower()}",
                                "path": rel, "line": number, "alias": m.group("alias"),
                                "level": m.group("level").lower(), "text": stripped,
                                "status": "CANDIDATE_REQUIRES_SOURCE_REVIEW"})
    result = {"source_commit": a.commit, "eligible_java_files": len(files),
              "scanned_java_files": len(files)-len(failures), "failed_files": failures,
              "candidate_callsites": len(records),
              "candidate_emitter_files": len(set(r["path"] for r in records)),
              "candidate_aliases": aliases, "candidate_calls": records,
              "confidence": "REGEX_CANDIDATES_ONLY_NOT_VERIFIED_EMITTERS",
              "behavioral_tests": "NOT_RUN", "runtime": "UNKNOWN",
              "warnings": ["Regex cannot reliably exclude block comments or strings",
                           "Multiline and custom wrappers require manual validation",
                           "Method identity and branch triggers require semantic inspection",
                           "Never report candidate count as verified callsite coverage"]}
    pathlib.Path(a.output).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in ("candidate_calls", "candidate_aliases")}, indent=2))
if __name__ == "__main__":
    main()
