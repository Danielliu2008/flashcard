import docx
import os

docx_path = r'E:\Documents\课件\解剖\09 呼吸系统 答案.docx'
doc = docx.Document(docx_path)

print(f"Total paragraphs: {len(doc.paragraphs)}")
print(f"Total tables: {len(doc.tables)}")

for i in range(min(50, len(doc.paragraphs))):
    text = doc.paragraphs[i].text.strip()
    if text:
        print(f"P{i}: {text[:100]}")
