#!/usr/bin/env python3
"""
Sync merged GitHub Pull Requests authored by shobhitagnihotri69 into README.md.
Runs automatically via GitHub Actions on a schedule or manually via workflow_dispatch.
Zero third-party dependencies (pure standard library).
"""

from __future__ import annotations

import os
import re
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

USERNAME = "shobhitagnihotri69"
START_TAG = "<!-- START_MERGED_PRS -->"
END_TAG = "<!-- END_MERGED_PRS -->"

def fetch_merged_prs(token: str | None = None) -> list[dict]:
    query = f"is:pr is:merged author:{USERNAME}"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://api.github.com/search/issues?q={encoded_query}&sort=updated&order=desc&per_page=100"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "profile-prs-sync",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
    except Exception as e:
        print(f"Error fetching PRs from GitHub API: {e}", file=sys.stderr)
        raise

    items = data.get("items", [])
    print(f"Successfully fetched {len(items)} merged PRs for @{USERNAME}")
    return items

def format_date(iso_str: str | None) -> str:
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y")
    except Exception:
        return iso_str[:10]

def build_markdown_section(prs: list[dict]) -> str:
    total = len(prs)
    lines = [
        START_TAG,
        "<!-- Do not edit this section manually. It is automatically updated by GitHub Actions. -->",
        f"> **Total Merged Pull Requests: {total}** across frontier AI agent runtimes, robotics foundation data pipelines, and developer tooling.\n",
        "| Repository | PR | Description | Merged Date |",
        "| :--- | :---: | :--- | :---: |",
    ]

    for item in prs:
        repo_parts = item["repository_url"].split("/")
        repo_name = f"{repo_parts[-2]}/{repo_parts[-1]}"
        pr_number = item["number"]
        pr_url = item["html_url"]
        title = item["title"].replace("|", "\\|").strip()
        merged_date = format_date(item.get("closed_at"))
        
        # Link repo and PR
        repo_link = f"[{repo_name}](https://github.com/{repo_name})"
        pr_link = f"[#{pr_number}]({pr_url})"
        
        lines.append(f"| {repo_link} | {pr_link} | `{title}` | {merged_date} |")

    lines.append(END_TAG)
    return "\n".join(lines)

def update_readme(repo_root: Path, new_section: str):
    readme_path = repo_root / "README.md"
    if not readme_path.exists():
        raise FileNotFoundError(f"README not found at {readme_path}")

    content = readme_path.read_text(encoding="utf-8")

    if START_TAG in content and END_TAG in content:
        pattern = re.compile(rf"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}", re.DOTALL)
        updated_content = pattern.sub(new_section, content)
    else:
        # Insert before World Models: (immediately below Education:)
        anchor = "World Models:"
        header = "Open Source Contributions & Merged Pull Requests:\n"
        full_block = f"{header}{new_section}\n\n"
        if anchor in content:
            updated_content = content.replace(anchor, f"{full_block}{anchor}")
        else:
            updated_content = f"{content.rstrip()}\n\n{full_block}"

    if updated_content != content:
        readme_path.write_text(updated_content, encoding="utf-8")
        print(f"Updated {readme_path} successfully.")
        return True
    else:
        print("No changes required in README.md.")
        return False

def main():
    repo_root = Path(__file__).resolve().parent.parent
    token = os.environ.get("GITHUB_TOKEN")
    
    # Fallback to local gh token if running locally without GITHUB_TOKEN set
    if not token:
        try:
            import subprocess
            token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
        except Exception:
            token = None

    prs = fetch_merged_prs(token=token)
    section = build_markdown_section(prs)
    changed = update_readme(repo_root, section)
    sys.exit(0)

if __name__ == "__main__":
    main()
