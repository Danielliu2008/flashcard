import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\182c5c8b-f64f-4a0c-9ffc-370962898b2c\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        idx = data.get('step_index')
        if idx in [1814, 1817, 1865]:
            print(f"--- STEP {idx} ---")
            tc = data.get('tool_calls', [])
            print(tc[0]['args']['function'])
