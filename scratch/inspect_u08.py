import docx
doc = docx.Document(r'E:\Documents\课件\解剖\08 血液系统 答案.docx')
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    if t:
        print(f"P{i}: {t[:80]}")
