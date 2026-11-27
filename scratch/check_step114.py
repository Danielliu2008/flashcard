import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\86936054-279e-46be-a513-513779b4f440\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f]

for l in lines:
    if l.get('step_index') == 114:
        print("Step 114 script:")
        print(l['tool_calls'][0]['args']['script'])
