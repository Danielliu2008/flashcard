import json
import glob
import os
import random

random.seed(42)

quiz_files = glob.glob(r'app/src/main/assets/**/quizzes/*.json', recursive=True)
print(f"Found {len(quiz_files)} quiz files to process.")

single_before = {0: 0, 1: 0, 2: 0, 3: 0, 'other': 0}
single_after = {0: 0, 1: 0, 2: 0, 3: 0, 'other': 0}
multi_before = {}
multi_after = {}

for fpath in quiz_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    quiz = data.get('quiz', [])
    modified = False
    
    for q in quiz:
        q_type = q.get('type', 'multiple_choice')
        opts = q.get('answerOptions', [])
        if not opts or len(opts) < 2:
            continue
        
        # Record before stats
        correct_indices = [i for i, o in enumerate(opts) if o.get('isCorrect')]
        if q_type == 'multiple_choice':
            if len(correct_indices) == 1:
                idx = correct_indices[0]
                single_before[idx] = single_before.get(idx, 0) + 1
        elif q_type == 'multiple_select':
            pat = ','.join(str(i) for i in correct_indices)
            multi_before[pat] = multi_before.get(pat, 0) + 1
        
        # Shuffle options
        random.shuffle(opts)
        q['answerOptions'] = opts
        modified = True
        
        # Record after stats
        new_correct_indices = [i for i, o in enumerate(opts) if o.get('isCorrect')]
        if q_type == 'multiple_choice':
            if len(new_correct_indices) == 1:
                idx = new_correct_indices[0]
                single_after[idx] = single_after.get(idx, 0) + 1
        elif q_type == 'multiple_select':
            pat = ','.join(str(i) for i in new_correct_indices)
            multi_after[pat] = multi_after.get(pat, 0) + 1

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print("\n--- Single Choice Correct Index Before vs After ---")
print("Before:", single_before)
print("After: ", single_after)

print("\n--- Multi Select Top Patterns Before vs After ---")
print("Before Top 5:", sorted(multi_before.items(), key=lambda x: x[1], reverse=True)[:5])
print("After Top 5: ", sorted(multi_after.items(), key=lambda x: x[1], reverse=True)[:5])
