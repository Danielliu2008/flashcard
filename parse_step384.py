import json

path = r'C:\Users\Administrator\.gemini\antigravity\brain\182c5c8b-f64f-4a0c-9ffc-370962898b2c\.system_generated\steps\384\output.txt'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.splitlines()
json_lines = []
recording = False
for line in lines:
    if line.strip() == '```json':
        recording = True
        continue
    if recording:
        if line.strip() == '```':
            break
        json_lines.append(line)

raw_str = '\n'.join(json_lines)
parsed = json.loads(raw_str)
if isinstance(parsed, str):
    parsed = json.loads(parsed)

print("Parsed successfully!")
print("Nervous Quiz questions count:", len(parsed.get('quiz', [])))

out_file = r'd:\Code\Android\flashcard\app\src\main\assets\quizzes\nervous_system.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(parsed, f, ensure_ascii=False, indent=2)

print(f"Saved to {out_file}")
