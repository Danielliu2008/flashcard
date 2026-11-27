import docx
import os
import re
import json

folder = r'E:\Documents\课件\解剖'

chapters = [
    {
        'doc': '02 骨骼系统-答案(1).docx',
        'id': 'skeletal_system',
        'title': '骨骼系统'
    },
    {
        'doc': '03 肌肉系统-答案.docx',
        'id': 'muscular_system',
        'title': '肌肉系统'
    },
    {
        'doc': '04 神经系统-答案.docx',
        'id': 'nervous_system',
        'title': '神经系统'
    },
    {
        'doc': '05 内分泌系统-答案.docx',
        'id': 'endocrine_system',
        'title': '内分泌系统'
    },
    {
        'doc': '06 感觉器官-答案.docx',
        'id': 'sensory_system',
        'title': '感觉器官'
    }
]

def parse_docx_fill_blanks(doc_path):
    doc = docx.Document(doc_path)
    is_fb = False
    items = []
    
    # We want to identify paragraphs in 填空题 section
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t:
            continue
        if '填空题' in t:
            is_fb = True
            continue
        if is_fb and any(k in t for k in ['选择题', '判断题', '名词解释', '问答题', 'A型题', 'B型题', 'X型题']):
            break
        if is_fb:
            # Check runs for answers (underlined or red)
            question_parts = []
            blanks = []
            cur_blank = []
            
            for r in p.runs:
                is_ans = bool(r.underline) or (r.font.color and str(r.font.color.rgb) == 'FF0000')
                if is_ans:
                    txt = r.text
                    if txt.strip():
                        cur_blank.append(txt)
                else:
                    if cur_blank:
                        full_ans = ''.join(cur_blank).strip()
                        if full_ans:
                            blanks.append(full_ans)
                            blank_num = len(blanks)
                            question_parts.append(f'（{blank_num}）_______')
                        cur_blank = []
                    question_parts.append(r.text)
            if cur_blank:
                full_ans = ''.join(cur_blank).strip()
                if full_ans:
                    blanks.append(full_ans)
                    blank_num = len(blanks)
                    question_parts.append(f'（{blank_num}）_______')
            
            if blanks:
                q_text = ''.join(question_parts).strip()
                q_text = re.sub(r'^\d+[\.、．\s]\s*', '', q_text).strip()
                full_orig = re.sub(r'^\d+[\.、．\s]\s*', '', t).strip()
                # Clean up spaces
                q_text = re.sub(r'\s+', ' ', q_text)
                items.append({
                    'type': 'fill_in_blank',
                    'question': q_text,
                    'blankAnswers': blanks,
                    'rationale': f'标准答案及考点解析：{full_orig}',
                    'hint': f'核心考点：共 {len(blanks)} 处填空，注意医学专业名词与解剖学方位的准确书写。'
                })
    return items

results = {}
for ch in chapters:
    fpath = os.path.join(folder, ch['doc'])
    items = parse_docx_fill_blanks(fpath)
    results[ch['id']] = items
    print(f"{ch['title']} ({ch['id']}): {len(items)} fill-in-the-blank questions extracted.")

with open('scratch/extracted_anatomy_blanks.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to scratch/extracted_anatomy_blanks.json")
