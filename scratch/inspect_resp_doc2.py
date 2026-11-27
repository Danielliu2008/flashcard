import docx

docx_path = r'E:\Documents\课件\解剖\09 呼吸系统 答案.docx'
doc = docx.Document(docx_path)

for i in range(50, len(doc.paragraphs)):
    text = doc.paragraphs[i].text.strip()
    if text:
        print(f"P{i}: {text[:100]}")
