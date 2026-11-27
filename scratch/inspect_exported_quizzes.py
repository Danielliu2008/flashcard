import zipfile
import json

zip_path = r'C:\Users\Administrator\Downloads\Anatomy_Studio_Export.zip'
with zipfile.ZipFile(zip_path, 'r') as z:
    for name in z.namelist():
        if '06 感觉器官 测验' in name or '05 内分泌' in name or '04 神经' in name:
            print(f"=== {name} ===")
            data = json.loads(z.read(name).decode('utf-8'))
            quiz = data.get('quiz', [])
            print(f"Total questions: {len(quiz)}")
            for i, q in enumerate(quiz[:3]):
                print(f"Q{i+1} ({q.get('type')}): {q.get('question')}")
                for opt in q.get('answerOptions', []):
                    mark = " [CORRECT]" if opt.get('isCorrect') else ""
                    print(f"   - {opt.get('text')}{mark}")
                    if opt.get('rationale'):
                        print(f"     解析: {opt.get('rationale')}")
                print(f"   Hint: {q.get('hint')}")
