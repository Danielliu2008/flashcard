import docx
import fitz # pymupdf
import json
import os
import re
import random

random.seed(42)

ASSETS_DIR = r"d:\Code\Android\flashcard\app\src\main\assets"
SUBJECTS_ANATOMY_DIR = os.path.join(ASSETS_DIR, "subjects", "anatomy")

def clean_text(t):
    return re.sub(r'\s+', ' ', t).strip()

def save_json(rel_dir, filename, data):
    p1 = os.path.join(ASSETS_DIR, rel_dir, filename)
    p2 = os.path.join(SUBJECTS_ANATOMY_DIR, rel_dir, filename)
    with open(p1, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(p2, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {rel_dir}/{filename}")

def shuffle_options(opts, correct_indices, rationale=""):
    # opts: list of string
    # correct_indices: list of int
    indexed = []
    for i, opt in enumerate(opts):
        indexed.append((opt, i in correct_indices))
    random.shuffle(indexed)
    res = []
    for opt_text, is_corr in indexed:
        res.append({
            "text": opt_text,
            "isCorrect": is_corr,
            "rationale": rationale if is_corr else ""
        })
    return res

print("Engine base ready.")
