# scratch/generate_all_units_full.py
import docx
import fitz
import json
import os
import re
import random

random.seed(42)

ASSETS_DIR = r"d:\Code\Android\flashcard\app\src\main\assets"
SUBJECTS_ANATOMY_DIR = os.path.join(ASSETS_DIR, "subjects", "anatomy")

for sub in ["decks", "quizzes", "mindmaps"]:
    os.makedirs(os.path.join(ASSETS_DIR, sub), exist_ok=True)
    os.makedirs(os.path.join(SUBJECTS_ANATOMY_DIR, sub), exist_ok=True)

def save_json(rel_dir, filename, data):
    p1 = os.path.join(ASSETS_DIR, rel_dir, filename)
    p2 = os.path.join(SUBJECTS_ANATOMY_DIR, rel_dir, filename)
    with open(p1, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(p2, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def make_card(cid, front, back, ptype="核心解剖结构", stars="★★★", imp=3):
    return {
        "c": cid,
        "f": { "flashcardContentBlock": [{ "type": "text", "content": front }] },
        "b": { "flashcardContentBlock": [{ "type": "text", "content": back }] },
        "pointType": ptype,
        "starRating": stars,
        "importance": imp
    }

def shuffle_opts(opts_with_bool, rat=""):
    shuffled = opts_with_bool[:]
    random.shuffle(shuffled)
    return [{
        "text": text,
        "isCorrect": is_c,
        "rationale": rat if is_c else ""
    } for text, is_c in shuffled]

print("Script template ready.")
