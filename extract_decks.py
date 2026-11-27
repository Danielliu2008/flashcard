import json
import os

brain_steps = r'C:/Users/Administrator/.gemini/antigravity/brain/182c5c8b-f64f-4a0c-9ffc-370962898b2c/.system_generated/steps'
assets_dir = r'd:/Code/Android/flashcard/app/src/main/assets/decks'
os.makedirs(assets_dir, exist_ok=True)

step_mapping = {
    '222': ('nervous_system.json', '神经系统 闪卡', 'f6547ce8-694a-434e-a60e-b5f4fd98baca'),
    '225': ('skeletal_system.json', '人体骨骼 闪卡', 'e4085f89-2ba4-40da-bb43-c492adf52943'),
    '228': ('muscular_system.json', '肌肉闪卡', '1fb801ff-44c0-4093-b92a-e4d9e116acf4'),
}

for step, (filename, title, aid) in step_mapping.items():
    file_path = os.path.join(brain_steps, step, 'output.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    raw_json_str = content.split('```json\n')[1].rsplit('```', 1)[0].strip()
    deck_json_str = json.loads(raw_json_str)
    if isinstance(deck_json_str, str):
        deck_data = json.loads(deck_json_str)
    else:
        deck_data = deck_json_str
    
    deck_data['id'] = aid
    deck_data['title'] = title
    
    cards = deck_data.get('flashcards', [])
    print(f'Step {step}: {title} has {len(cards)} cards.')
    out_path = os.path.join(assets_dir, filename)
    with open(out_path, 'w', encoding='utf-8') as out:
        json.dump(deck_data, out, ensure_ascii=False, indent=2)
    print(f'Wrote to {out_path}')

# Clean up any bad files like deck_0.json
deck_0 = os.path.join(assets_dir, 'deck_0.json')
if os.path.exists(deck_0):
    os.remove(deck_0)

print('All 3 decks successfully extracted and saved!')
