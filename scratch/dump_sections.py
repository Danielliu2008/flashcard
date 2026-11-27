import docx
import os
import re

files = [
    ("overview_system", r"E:\Documents\课件\解剖\01 概论-组织-皮肤-答案(1).docx"),
    ("circulatory_system", r"E:\Documents\课件\解剖\07 循环系统-答案.docx"),
    ("blood_system", r"E:\Documents\课件\解剖\08 血液系统 答案.docx"),
    ("respiratory_system", r"E:\Documents\课件\解剖\09 呼吸系统 答案.docx"),
    ("digestive_system", r"E:\Documents\课件\解剖\10 消化系统 答案.docx"),
    ("urinary_system", r"E:\Documents\课件\解剖\11 泌尿系统 答案.docx"),
    ("reproductive_system", r"E:\Documents\课件\解剖\12 生殖系统 答案.docx"),
    ("metabolism_system", r"E:\Documents\课件\解剖\13 体温调节和能量代谢 答案.docx")
]

for uid, fpath in files:
    doc = docx.Document(fpath)
    print(f"\n==================== {uid} ====================")
    sec = "NONE"
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if not t: continue
        if any(k in t for k in ['填空', '选择', '多选', '判断', '名词', '问答', '简答']):
            sec = t
            print(f"[{sec}] P{i}: {t}")
        elif i < 15 or (i % 20 == 0):
            print(f"  P{i}: {t[:60]}")
