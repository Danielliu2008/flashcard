import docx
import os
import re

units_info = [
    {
        "unit_id": "overview_system",
        "docx": r"E:\Documents\课件\解剖\01 概论-组织-皮肤-答案(1).docx",
        "title": "概论与组织皮肤",
        "pdfs": [r"E:\Documents\课件\解剖\01概论与细胞.pdf", r"E:\Documents\课件\解剖\02 组织.pdf", r"E:\Documents\课件\解剖\03 皮肤.pdf"]
    },
    {
        "unit_id": "circulatory_system",
        "docx": r"E:\Documents\课件\解剖\07 循环系统-答案.docx",
        "title": "循环系统",
        "pdfs": [r"E:\Documents\课件\解剖\09 循环系统-心脏.pdf", r"E:\Documents\课件\解剖\09 循环系统-血管.pdf"]
    },
    {
        "unit_id": "blood_system",
        "docx": r"E:\Documents\课件\解剖\08 血液系统 答案.docx",
        "title": "血液系统",
        "pdfs": [r"E:\Documents\课件\解剖\10 血液.pdf", r"E:\Documents\课件\解剖\11 淋巴系统和免疫.pdf"]
    },
    {
        "unit_id": "respiratory_system",
        "docx": r"E:\Documents\课件\解剖\09 呼吸系统 答案.docx",
        "title": "呼吸系统",
        "pdfs": [r"E:\Documents\课件\解剖\12 呼吸系统.pdf"]
    },
    {
        "unit_id": "digestive_system",
        "docx": r"E:\Documents\课件\解剖\10 消化系统 答案.docx",
        "title": "消化系统",
        "pdfs": [r"E:\Documents\课件\解剖\13 消化系统.pdf"]
    },
    {
        "unit_id": "urinary_system",
        "docx": r"E:\Documents\课件\解剖\11 泌尿系统 答案.docx",
        "title": "泌尿系统",
        "pdfs": [r"E:\Documents\课件\解剖\14 泌尿系统.pdf"]
    },
    {
        "unit_id": "reproductive_system",
        "docx": r"E:\Documents\课件\解剖\12 生殖系统 答案.docx",
        "title": "生殖系统",
        "pdfs": [r"E:\Documents\课件\解剖\15 生殖系统1-男性生殖系统.pdf", r"E:\Documents\课件\解剖\15 生殖系统2-女性生殖系统.pdf"]
    },
    {
        "unit_id": "metabolism_system",
        "docx": r"E:\Documents\课件\解剖\13 体温调节和能量代谢 答案.docx",
        "title": "体温调节和能量代谢",
        "pdfs": [r"E:\Documents\课件\解剖\16 体温和能量代谢.pdf"]
    }
]

for u in units_info:
    doc = docx.Document(u["docx"])
    texts = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    print(f"\n=== Unit: {u['title']} ({u['unit_id']}) ===")
    print(f"Total non-empty paragraphs: {len(texts)}")
    headers = [t for t in texts if any(k in t for k in ['填空', '选择', '多选', '判断', '名词', '简答', '问答'])]
    print("Detected headers:", headers)
