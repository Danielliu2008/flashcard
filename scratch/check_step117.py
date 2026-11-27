import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\86936054-279e-46be-a513-513779b4f440\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f]

for l in lines[-3:]:
    print(f"Step {l.get('step_index')}: {l.get('type')}")
    if l.get('content'):
        print(l['content'][:600])
    if l.get('tool_calls'):
        print("Script:", l['tool_calls'][0]['args'].get('script', '')[:400])
