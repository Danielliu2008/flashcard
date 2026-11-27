import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\86936054-279e-46be-a513-513779b4f440\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f]

for l in lines[-6:]:
    if l.get('tool_calls'):
        print(f"Step {l.get('step_index')}:")
        tc = l['tool_calls'][0]
        print("Name:", tc.get('name'))
        print("Script:", tc.get('args', {}).get('script', '')[:400])
        print("---")
