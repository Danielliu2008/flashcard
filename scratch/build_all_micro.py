# -*- coding: utf-8 -*-
"""
Build all 8 chapters of Microbiology flashcards and quizzes.
Validates schemas, writes to assets directory, and verifies integrity.
"""

import os
import sys
import json

# Add scratch to path
scratch_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, scratch_dir)

from data_micro_01 import DECK_01, QUIZ_01
from data_micro_02 import DECK_02, QUIZ_02
from data_micro_03 import DECK_03, QUIZ_03
from data_micro_04 import DECK_04, QUIZ_04
from data_micro_05 import DECK_05, QUIZ_05
from data_micro_06 import DECK_06, QUIZ_06
from data_micro_07 import DECK_07, QUIZ_07
from data_micro_08 import DECK_08, QUIZ_08

MODULES = [
    (1, "01 绪论", DECK_01, QUIZ_01),
    (2, "02 细菌形态与结构", DECK_02, QUIZ_02),
    (3, "03 细菌的生理", DECK_03, QUIZ_03),
    (4, "04 细菌的遗传与变异", DECK_04, QUIZ_04),
    (5, "05 细菌的感染与免疫", DECK_05, QUIZ_05),
    (6, "06 病毒的基本性状", DECK_06, QUIZ_06),
    (7, "07 病毒的感染", DECK_07, QUIZ_07),
    (8, "08 真菌学总论", DECK_08, QUIZ_08),
]

def validate_deck(deck, ch_num):
    cards = deck.get("flashcards", [])
    assert len(cards) >= 12, f"Chapter {ch_num} deck has only {len(cards)} cards"
    for idx, c in enumerate(cards):
        assert "c" in c, f"Ch {ch_num} card {idx} missing 'c'"
        assert "f" in c and "b" in c, f"Ch {ch_num} card {idx} missing 'f' or 'b'"
        f_blocks = c["f"].get("flashcardContentBlock", [])
        b_blocks = c["b"].get("flashcardContentBlock", [])
        assert len(f_blocks) > 0 and len(b_blocks) > 0, f"Ch {ch_num} card {idx} empty content block"
        f_text = f_blocks[0].get("content", "").strip()
        b_text = b_blocks[0].get("content", "").strip()
        assert len(f_text) > 0, f"Ch {ch_num} card {idx} front text empty"
        assert len(b_text) > 0, f"Ch {ch_num} card {idx} back text empty"

def validate_quiz(quiz_data, ch_num):
    questions = quiz_data.get("quiz", [])
    assert len(questions) >= 15, f"Chapter {ch_num} quiz has only {len(questions)} questions"
    for idx, q in enumerate(questions):
        qid = q.get("id")
        qtype = q.get("type")
        prompt = q.get("question", "")
        hint = q.get("hint", "")
        rationale = q.get("rationale", "")
        assert prompt, f"Ch {ch_num} Q{idx} missing prompt"
        assert qtype in ["multiple_choice", "true_false", "multiple_select", "fill_blank"], f"Ch {ch_num} Q{idx} invalid type {qtype}"
        
        if qtype in ["multiple_choice", "true_false"]:
            opts = q.get("options", [])
            assert len(opts) >= 2, f"Ch {ch_num} Q{qid} options < 2"
            correct_opts = [o for o in opts if o.get("isCorrect")]
            assert len(correct_opts) == 1, f"Ch {ch_num} Q{qid} {qtype} expected exactly 1 correct, got {len(correct_opts)}"
        elif qtype == "multiple_select":
            opts = q.get("options", [])
            assert len(opts) >= 3, f"Ch {ch_num} Q{qid} multiple_select options < 3"
            correct_opts = [o for o in opts if o.get("isCorrect")]
            assert len(correct_opts) >= 2, f"Ch {ch_num} Q{qid} multiple_select expected >= 2 correct, got {len(correct_opts)}"
        elif qtype == "fill_blank":
            blanks = q.get("blankAnswers", [])
            assert len(blanks) >= 1, f"Ch {ch_num} Q{qid} fill_blank missing blankAnswers"

def main():
    base_assets = r"d:\Code\Android\flashcard\app\src\main\assets\subjects\microbiology"
    decks_dir = os.path.join(base_assets, "decks")
    quizzes_dir = os.path.join(base_assets, "quizzes")
    
    os.makedirs(decks_dir, exist_ok=True)
    os.makedirs(quizzes_dir, exist_ok=True)
    
    print("Validating and writing Microbiology content...")
    for ch_num, ch_title, deck, quiz in MODULES:
        uid = f"micro_0{ch_num}"
        validate_deck(deck, ch_num)
        validate_quiz(quiz, ch_num)
        
        deck_cards_count = len(deck["flashcards"])
        quiz_q_count = len(quiz["quiz"])
        
        print(f"[{uid}] {ch_title}: {deck_cards_count} flashcards, {quiz_q_count} quiz questions.")
        
        # 1. Write Decks (both micro_0X.json and Chinese named file)
        deck_json = json.dumps(deck, ensure_ascii=False, indent=2)
        p1 = os.path.join(decks_dir, f"{uid}.json")
        p2 = os.path.join(decks_dir, f"{ch_title} 闪卡.json")
        with open(p1, "w", encoding="utf-8") as f:
            f.write(deck_json)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(deck_json)
            
        # 2. Write Quizzes (both micro_0X.json and Chinese named file)
        quiz_json = json.dumps(quiz, ensure_ascii=False, indent=2)
        q1 = os.path.join(quizzes_dir, f"{uid}.json")
        q2 = os.path.join(quizzes_dir, f"{ch_title} 测验.json")
        with open(q1, "w", encoding="utf-8") as f:
            f.write(quiz_json)
        with open(q2, "w", encoding="utf-8") as f:
            f.write(quiz_json)

    print("\nALL 8 CHAPTERS SUCCESSFULLY BUILT AND WRITTEN TO ASSETS!")

if __name__ == "__main__":
    main()
