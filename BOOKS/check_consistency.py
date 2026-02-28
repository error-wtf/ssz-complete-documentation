#!/usr/bin/env python3
"""
SSZ Book Consistency Checker
Compares EN and DE Markdown books for formula, term, and structure consistency.

Usage:
    python check_consistency.py
    python check_consistency.py --verbose
    python check_consistency.py --check-decimals
"""

import csv
import re
import sys
import os
from pathlib import Path
from collections import Counter

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
EN_BOOK = SCRIPT_DIR / "SSZ_COMPLETE_BOOK_EN.md"
DE_BOOK = SCRIPT_DIR / "SSZ_COMPLETE_BOOK_DE.md"
TRANSLATION_DB = SCRIPT_DIR / "translation_db.csv"

VERBOSE = "--verbose" in sys.argv
CHECK_DECIMALS = "--check-decimals" in sys.argv

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_translation_db(path: Path) -> list[dict]:
    """Load the EN↔DE translation database from CSV."""
    entries = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append({
                "en": row["en_term"].strip(),
                "de": row["de_term"].strip(),
                "category": row.get("category", "").strip(),
                "notes": row.get("notes", "").strip(),
            })
    return entries


def load_text(path: Path) -> str:
    """Load a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_formulas(text: str) -> list[str]:
    """Extract LaTeX-style formulas from Markdown (inline $...$ and display $$...$$)."""
    # Display math $$...$$
    display = re.findall(r'\$\$(.+?)\$\$', text, re.DOTALL)
    # Inline math $...$  (not $$)
    inline = re.findall(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', text)
    # Also extract \[...\] and \(...\)
    bracket_display = re.findall(r'\\\[(.+?)\\\]', text, re.DOTALL)
    bracket_inline = re.findall(r'\\\((.+?)\\\)', text)
    all_formulas = display + inline + bracket_display + bracket_inline
    # Normalize whitespace
    return [re.sub(r'\s+', ' ', f.strip()) for f in all_formulas]


def extract_headings(text: str) -> list[str]:
    """Extract Markdown headings."""
    return re.findall(r'^(#{1,6}\s+.+)$', text, re.MULTILINE)


def extract_key_values(text: str) -> list[str]:
    """Extract key numerical values like 0.555, 0.802, 1.595, etc."""
    # Match decimal numbers that look like SSZ constants
    return re.findall(r'\b\d+\.\d{2,}\b', text)


def find_german_decimals(text: str) -> list[tuple[int, str]]:
    """Find potential German-style decimal commas (e.g., 0,555 instead of 0.555)."""
    issues = []
    for i, line in enumerate(text.split('\n'), 1):
        # Match patterns like 0,555 but not in CSV-like contexts
        matches = re.findall(r'\b(\d+,\d{2,})\b', line)
        for m in matches:
            # Exclude things that look like thousands separators (1,000)
            if not re.match(r'^\d{1,3},\d{3}$', m):
                issues.append((i, m))
    return issues


def check_term_consistency(en_text: str, de_text: str, db: list[dict]) -> list[str]:
    """Check that EN terms appear in EN book and corresponding DE terms in DE book."""
    issues = []
    for entry in db:
        en_term = entry["en"]
        de_term = entry["de"]

        en_count = en_text.lower().count(en_term.lower())
        de_count = de_text.lower().count(de_term.lower())

        if en_count > 0 and de_count == 0:
            issues.append(
                f"MISSING DE: '{en_term}' appears {en_count}x in EN, "
                f"but '{de_term}' not found in DE"
            )
        if de_count > 0 and en_count == 0 and entry["category"] != "structure":
            issues.append(
                f"MISSING EN: '{de_term}' appears {de_count}x in DE, "
                f"but '{en_term}' not found in EN"
            )

    return issues


def check_formula_consistency(en_formulas: list[str], de_formulas: list[str]) -> list[str]:
    """Check that formulas match between EN and DE."""
    issues = []

    en_set = Counter(en_formulas)
    de_set = Counter(de_formulas)

    only_en = set(en_set.keys()) - set(de_set.keys())
    only_de = set(de_set.keys()) - set(en_set.keys())

    for f in sorted(only_en):
        issues.append(f"FORMULA ONLY IN EN: {f[:80]}...")
    for f in sorted(only_de):
        issues.append(f"FORMULA ONLY IN DE: {f[:80]}...")

    return issues


def check_key_values(en_text: str, de_text: str) -> list[str]:
    """Check that key SSZ constants appear in both books."""
    issues = []
    key_constants = [
        ("0.555", "D_min"),
        ("0.802", "Ξ_max / z_max"),
        ("0.80171", "Ξ(r_s)"),
        ("0.55503", "D(r_s)"),
        ("1.595", "r*/r_s (weak)"),
        ("1.387", "r*/r_s (strong)"),
        ("1.618", "φ (golden ratio)"),
        ("42.98", "Mercury perihelion"),
        ("45.85", "GPS correction"),
        ("1.75", "Eddington lensing"),
    ]

    for value, name in key_constants:
        in_en = value in en_text
        in_de = value in de_text
        if in_en and not in_de:
            issues.append(f"KEY VALUE MISSING IN DE: {value} ({name})")
        if in_de and not in_en:
            issues.append(f"KEY VALUE MISSING IN EN: {value} ({name})")

    return issues


def check_heading_count(en_headings: list[str], de_headings: list[str]) -> list[str]:
    """Check that heading counts match between EN and DE."""
    issues = []
    en_levels = Counter(h.split()[0] for h in en_headings)
    de_levels = Counter(h.split()[0] for h in de_headings)

    for level in sorted(set(list(en_levels.keys()) + list(de_levels.keys()))):
        en_c = en_levels.get(level, 0)
        de_c = de_levels.get(level, 0)
        if en_c != de_c:
            issues.append(
                f"HEADING COUNT MISMATCH ({level}): EN={en_c}, DE={de_c}"
            )

    return issues


def check_deprecated_formulas(text: str, label: str) -> list[str]:
    """Check for deprecated/forbidden formulas."""
    issues = []
    # The forbidden formula pattern: (r_s/r)² × exp(-r/r_φ)
    patterns = [
        r'r_s/r\).*exp\(-r/r',
        r'r_s/r\)².*exp',
        r'\(r_s/r\)\^2.*exp',
    ]
    for pat in patterns:
        matches = re.findall(pat, text)
        if matches:
            issues.append(
                f"DEPRECATED FORMULA in {label}: Found pattern matching "
                f"forbidden Ξ = (r_s/r)²·exp(-r/r_φ)"
            )
    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Force UTF-8 output on Windows
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    print("=" * 70)
    print("SSZ BOOK CONSISTENCY CHECKER")
    print("=" * 70)

    # Check files exist
    missing = []
    if not EN_BOOK.exists():
        missing.append(str(EN_BOOK))
    if not DE_BOOK.exists():
        missing.append(str(DE_BOOK))
    if not TRANSLATION_DB.exists():
        missing.append(str(TRANSLATION_DB))

    if missing:
        print(f"\nERROR: Missing files:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)

    # Load data
    print(f"\nLoading EN book: {EN_BOOK.name}")
    en_text = load_text(EN_BOOK)
    print(f"Loading DE book: {DE_BOOK.name}")
    de_text = load_text(DE_BOOK)
    print(f"Loading translation DB: {TRANSLATION_DB.name}")
    db = load_translation_db(TRANSLATION_DB)

    print(f"\n  EN: {len(en_text):,} chars, {en_text.count(chr(10)):,} lines")
    print(f"  DE: {len(de_text):,} chars, {de_text.count(chr(10)):,} lines")
    print(f"  DB: {len(db)} term pairs")

    all_issues = []

    # 1. Term consistency
    print("\n--- CHECK 1: Term Consistency ---")
    term_issues = check_term_consistency(en_text, de_text, db)
    all_issues.extend(term_issues)
    if term_issues:
        for issue in term_issues[:20]:
            print(f"  [!] {issue}")
        if len(term_issues) > 20:
            print(f"  ... and {len(term_issues) - 20} more")
    else:
        print("  [OK] All terms consistent")

    # 2. Formula consistency
    print("\n--- CHECK 2: Formula Consistency ---")
    en_formulas = extract_formulas(en_text)
    de_formulas = extract_formulas(de_text)
    print(f"  EN formulas: {len(en_formulas)}")
    print(f"  DE formulas: {len(de_formulas)}")
    formula_issues = check_formula_consistency(en_formulas, de_formulas)
    all_issues.extend(formula_issues)
    if formula_issues:
        for issue in formula_issues[:15]:
            print(f"  [!] {issue}")
        if len(formula_issues) > 15:
            print(f"  ... and {len(formula_issues) - 15} more")
    else:
        print("  [OK] All formulas consistent")

    # 3. Key values
    print("\n--- CHECK 3: Key SSZ Constants ---")
    value_issues = check_key_values(en_text, de_text)
    all_issues.extend(value_issues)
    if value_issues:
        for issue in value_issues:
            print(f"  [!] {issue}")
    else:
        print("  [OK] All key values present in both books")

    # 4. Heading structure
    print("\n--- CHECK 4: Heading Structure ---")
    en_headings = extract_headings(en_text)
    de_headings = extract_headings(de_text)
    print(f"  EN headings: {len(en_headings)}")
    print(f"  DE headings: {len(de_headings)}")
    heading_issues = check_heading_count(en_headings, de_headings)
    all_issues.extend(heading_issues)
    if heading_issues:
        for issue in heading_issues:
            print(f"  [!] {issue}")
    else:
        print("  [OK] Heading structure matches")

    # 5. Deprecated formulas
    print("\n--- CHECK 5: Deprecated Formula Scan ---")
    dep_en = check_deprecated_formulas(en_text, "EN")
    dep_de = check_deprecated_formulas(de_text, "DE")
    all_issues.extend(dep_en + dep_de)
    if dep_en or dep_de:
        for issue in dep_en + dep_de:
            print(f"  [!!] {issue}")
    else:
        print("  [OK] No deprecated formulas found")

    # 6. German decimal commas (optional)
    if CHECK_DECIMALS:
        print("\n--- CHECK 6: German Decimal Commas in DE ---")
        decimal_issues = find_german_decimals(de_text)
        if decimal_issues:
            for line_no, value in decimal_issues[:20]:
                issue = f"GERMAN DECIMAL in DE line {line_no}: {value}"
                all_issues.append(issue)
                print(f"  [!] {issue}")
            if len(decimal_issues) > 20:
                print(f"  ... and {len(decimal_issues) - 20} more")
        else:
            print("  [OK] No German decimal commas found")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    if all_issues:
        print(f"\n  [!] {len(all_issues)} issue(s) found")
        print(f"\n  Run with --verbose for full details")
    else:
        print(f"\n  [OK] ALL CHECKS PASSED -- Books are consistent!")

    if VERBOSE and all_issues:
        print("\n--- FULL ISSUE LIST ---")
        for i, issue in enumerate(all_issues, 1):
            print(f"  {i:3d}. {issue}")

    print()
    return 0 if not all_issues else 1


if __name__ == "__main__":
    sys.exit(main())
