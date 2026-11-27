import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\86936054-279e-46be-a513-513779b4f440\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        step = data.get('step_index')
        tc = data.get('tool_calls', [])
        for call in tc:
            script = call.get('args', {}).get('script', '')
            print(f"Step {step}: script len={len(script)}, preview={repr(script[:80])}")
