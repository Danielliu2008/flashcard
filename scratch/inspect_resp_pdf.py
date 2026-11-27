import fitz

doc = fitz.open(r'E:\Documents\课件\解剖\12 呼吸系统.pdf')
print("Pages:", len(doc))
for page_num in range(min(5, len(doc))):
    text = doc[page_num].get_text().strip()
    if "本章要点" in text or "要点" in text or page_num in [1, 2]:
        print(f"--- Page {page_num + 1} ---")
        print(text[:800])
