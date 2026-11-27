import json
import os
import re
import random
import docx
import fitz # pymupdf

random.seed(42)

ASSETS_DIR = r"d:\Code\Android\flashcard\app\src\main\assets"
SUBJECTS_ANATOMY_DIR = os.path.join(ASSETS_DIR, "subjects", "anatomy")

for sub in ["decks", "quizzes", "mindmaps"]:
    os.makedirs(os.path.join(ASSETS_DIR, sub), exist_ok=True)
    os.makedirs(os.path.join(SUBJECTS_ANATOMY_DIR, sub), exist_ok=True)

print("Directories prepared.")
