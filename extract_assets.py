import json
import os
import re

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\182c5c8b-f64f-4a0c-9ffc-370962898b2c\.system_generated\logs\transcript_full.jsonl'
mindmaps_dir = r'd:\Code\Android\flashcard\app\src\main\assets\mindmaps'
quizzes_dir = r'd:\Code\Android\flashcard\app\src\main\assets\quizzes'

os.makedirs(mindmaps_dir, exist_ok=True)
os.makedirs(quizzes_dir, exist_ok=True)

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        idx = data.get('step_index')
        content = data.get('content', '')
        
        # Step 263 is the output of analyze all 3 mindmaps
        if idx == 263:
            print("Processing step 263 (Mindmaps)...")
            # Extract JSON block
            m = re.search(r'```json\s*(\{.*?\})\s*```', content, re.DOTALL)
            if m:
                raw_json = m.group(1)
                maps = json.loads(raw_json)
                for map_name, val in maps.items():
                    print(f"Mindmap: {map_name}, nodes: {val.get('nodeCount')}")
                    mindmap_tree = json.loads(val['jsonStr'])
                    
                    filename = None
                    if "神经" in map_name:
                        filename = "nervous_system.json"
                    elif "肌肉" in map_name:
                        filename = "muscular_system.json"
                    elif "骨" in map_name:
                        filename = "skeletal_system.json"
                    
                    if filename:
                        out_path = os.path.join(mindmaps_dir, filename)
                        with open(out_path, 'w', encoding='utf-8') as out_f:
                            json.dump(mindmap_tree, out_f, ensure_ascii=False, indent=2)
                        print(f"Saved {map_name} to {out_path}")

        # Step 256 was Fetch mindmaps and existing quiz
        if idx == 256:
            print("Processing step 256 (Existing Quiz: 人体骨骼测验)...")
            m = re.search(r'```json\s*(\[\s*\{.*?\}\s*\])\s*```', content, re.DOTALL)
            if m:
                items = json.loads(m.group(1))
                for it in items:
                    if "骨骼测验" in it.get('name', ''):
                        pass

print("Done extract check.")
