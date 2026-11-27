import fitz # pymupdf
import os

pdf_list = [
    ("overview_01", r"E:\Documents\课件\解剖\01概论与细胞.pdf"),
    ("overview_02", r"E:\Documents\课件\解剖\02 组织.pdf"),
    ("overview_03", r"E:\Documents\课件\解剖\03 皮肤.pdf"),
    ("circulatory_heart", r"E:\Documents\课件\解剖\09 循环系统-心脏.pdf"),
    ("circulatory_vessel", r"E:\Documents\课件\解剖\09 循环系统-血管.pdf"),
    ("blood", r"E:\Documents\课件\解剖\10 血液.pdf"),
    ("lymph", r"E:\Documents\课件\解剖\11 淋巴系统和免疫.pdf"),
    ("respiratory", r"E:\Documents\课件\解剖\12 呼吸系统.pdf"),
    ("digestive", r"E:\Documents\课件\解剖\13 消化系统.pdf"),
    ("urinary", r"E:\Documents\课件\解剖\14 泌尿系统.pdf"),
    ("reproductive_male", r"E:\Documents\课件\解剖\15 生殖系统1-男性生殖系统.pdf"),
    ("reproductive_female", r"E:\Documents\课件\解剖\15 生殖系统2-女性生殖系统.pdf"),
    ("metabolism", r"E:\Documents\课件\解剖\16 体温和能量代谢.pdf")
]

for label, p in pdf_list:
    doc = fitz.open(p)
    print(f"\n--- {label} ({os.path.basename(p)}) Pages: {len(doc)} ---")
    for page_idx in range(min(4, len(doc))):
        txt = doc[page_idx].get_text()
        if "本章要点" in txt or "要点" in txt or page_idx in [1, 2]:
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            print(f"Page {page_idx+1}: " + " | ".join(lines[:6]))
