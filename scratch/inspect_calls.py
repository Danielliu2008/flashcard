import json

transcript_path = r'C:\Users\Administrator\.gemini\antigravity\brain\182c5c8b-f64f-4a0c-9ffc-370962898b2c\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        tc = data.get('tool_calls', [])
        for call in tc:
            fn = call.get('args', {}).get('function', '')
            if 'v9rmvd' in fn or 'create-artifact' in fn or 'Studio' in fn or 'artifacts' in fn:
                print(f"Step {data.get('step_index')}: {call.get('args', {}).get('toolSummary')}")
                if any(k in fn for k in ['create', 'generate', 'list', 'artifacts']):
                    print("Function snippet:", fn[:300])
                    print("---")
