import docx
for name, fpath in [
    ("u11", r"E:\Documents\课件\解剖\11 泌尿系统 答案.docx"),
    ("u12", r"E:\Documents\课件\解剖\12 生殖系统 答案.docx"),
    ("u13", r"E:\Documents\课件\解剖\13 体温调节和能量代谢 答案.docx")
]:
    doc = docx.Document(fpath)
    print(f"\n===== {name} ({fpath}) =====")
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if t and (any(k in t for k in ['填空', '选择', '多选', '判断', '名词', '简答', '问答']) or i < 10):
            print(f"P{i}: {t[:75]}")
