import docx
import json
import random
import re

def parse_respiratory_docx(docx_path):
    doc = docx.Document(docx_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    
    fill_blanks = []
    single_choices = []
    multi_choices = []
    judgments = []
    
    current_section = None
    
    i = 0
    while i < len(paragraphs):
        p = paragraphs[i]
        if '一. 填空题' in p or '一、填空题' in p:
            current_section = 'fill'
            i += 1
            continue
        elif '二. 选择题' in p or '二、选择题' in p:
            current_section = 'single'
            i += 1
            continue
        elif '三．多选题' in p or '三、多选题' in p:
            current_section = 'multi'
            i += 1
            continue
        elif '判断对错题' in p:
            current_section = 'judge'
            i += 1
            continue
        elif '名词解释' in p or '简答' in p:
            current_section = 'other'
            i += 1
            continue
            
        if current_section == 'fill':
            # e.g.: "1. 呼吸系统由呼吸道和 肺 构成，上呼吸道包括  鼻  、  咽  、  喉  ..."
            m = re.match(r'^\d+[\.、]\s*(.*)', p)
            if m:
                text = m.group(1)
                # Find words with surrounding spaces or underlined, or we can look for standard pattern
                fill_blanks.append(text)
        elif current_section == 'single':
            # Question line, e.g. "下列不是肺活量的组成部分的是  D   。" or "2. 氧气在血液中运输时主要与  C    结合在一起运输。"
            if re.match(r'^(\d+[\.、])?.*[A-D]\s*[。．\._]*$', p) or (i + 1 < len(paragraphs) and 'A.' in paragraphs[i+1]):
                q_text = p
                options_text = ""
                note_text = ""
                i += 1
                if i < len(paragraphs) and 'A.' in paragraphs[i]:
                    options_text = paragraphs[i]
                    i += 1
                if i < len(paragraphs) and paragraphs[i].startswith('注：'):
                    note_text = paragraphs[i]
                    i += 1
                single_choices.append((q_text, options_text, note_text))
                continue
        elif current_section == 'multi':
            # e.g.: "1. 平静吸气时收缩的是     。AC"
            if re.match(r'^\d+[\.、].*', p):
                q_text = p
                i += 1
                options_lines = []
                while i < len(paragraphs) and not re.match(r'^\d+[\.、]', paragraphs[i]) and not '判断对错题' in paragraphs[i]:
                    options_lines.append(paragraphs[i])
                    i += 1
                multi_choices.append((q_text, options_lines))
                continue
        elif current_section == 'judge':
            # e.g.: "二氧化碳主要靠物理溶解在血液中进行运输。  ×"
            if '√' in p or '×' in p:
                note = ""
                if i + 1 < len(paragraphs) and paragraphs[i+1].startswith('注：'):
                    note = paragraphs[i+1]
                    i += 1
                judgments.append((p, note))
                
        i += 1
        
    return {
        'fill_blanks': fill_blanks,
        'single_choices': single_choices,
        'multi_choices': multi_choices,
        'judgments': judgments
    }

parsed = parse_respiratory_docx(r'E:\Documents\课件\解剖\09 呼吸系统 答案.docx')
print(f"Fill blanks: {len(parsed['fill_blanks'])}")
print(f"Single choices: {len(parsed['single_choices'])}")
print(f"Multi choices: {len(parsed['multi_choices'])}")
print(f"Judgments: {len(parsed['judgments'])}")
