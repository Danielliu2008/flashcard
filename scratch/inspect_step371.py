import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\182c5c8b-f64f-4a0c-9ffc-370962898b2c\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') == 371:
            print("Step 371 found:")
            print(json.dumps(data.get('tool_calls'), ensure_ascii=False, indent=2))
            break
