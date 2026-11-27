# scratch/build_all_remaining.py
import json
import os
import random

random.seed(42)

ASSETS_DIR = r"d:\Code\Android\flashcard\app\src\main\assets"
SUBJECTS_DIR = os.path.join(ASSETS_DIR, "subjects", "anatomy")

def save_json(rel_dir, filename, data):
    for base in [ASSETS_DIR, SUBJECTS_DIR]:
        path = os.path.join(base, rel_dir, filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
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

def shuffle_opts(opts_tuples, rat=""):
    shuffled = opts_tuples[:]
    random.shuffle(shuffled)
    return [{
        "text": text,
        "isCorrect": is_c,
        "rationale": rat if is_c else ""
    } for text, is_c in shuffled]

print("Ready to process units 08-13.")
