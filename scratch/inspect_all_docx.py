import docx
import glob
import os

docx_files = glob.glob(r'E:\Documents\课件\解剖\*答案*.docx')
for f in sorted(docx_files):
    try:
        doc = docx.Document(f)
        texts = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        print(f"File: {os.path.basename(f)}, Paragraphs: {len(texts)}")
        # Check sections
        sections = [t for t in texts if any(k in t for k in ['填空', '选择', '多选', '判断', '名词', '问答', '简答'])]
        print("  Sections:", sections[:6])
    except Exception as e:
        print(f"File: {os.path.basename(f)}, Error: {e}")
