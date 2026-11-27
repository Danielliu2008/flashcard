import docx
doc = docx.Document(r'E:\Documents\课件\解剖\01 概论-组织-皮肤-答案(1).docx')
for i, p in enumerate(doc.paragraphs):
    t = p.text.strip()
    if t:
        print(f"P{i}: {t[:80]}")
