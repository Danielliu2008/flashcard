import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\86936054-279e-46be-a513-513779b4f440\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f]

for l in lines[-5:]:
    print(f"Step {l.get('step_index')}: type={l.get('type')}, source={l.get('source')}")
    tc = l.get('tool_calls', [])
    if tc:
        print("  TC:", tc[0].get('name'))
    if l.get('content'):
        print("  Content preview:", repr(l['content'][:200]))
