import os
import sys
import json
import socket
import zipfile
import argparse
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# 路径定位
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
ASSETS_DIR = os.path.join(PROJECT_DIR, "app", "src", "main", "assets")
CUSTOM_DIR = os.path.join(PROJECT_DIR, "custom_data")
os.makedirs(CUSTOM_DIR, exist_ok=True)

CUSTOM_SUBJECTS_FILE = os.path.join(CUSTOM_DIR, "custom_subjects.json")

# 内置学科配置
DEFAULT_SUBJECTS = [
    {
        "id": "anatomy",
        "name": "系统解剖学",
        "emoji": "🫀",
        "description": "骨骼、肌肉、神经系统知识导图、闪卡与考题",
        "isBuiltIn": True,
        "colorHex": "#1A73E8"
    },
    {
        "id": "microbiology",
        "name": "医学微生物学",
        "emoji": "🦠",
        "description": "细菌学、病毒学、真菌学8大章节知识导图、闪卡与考题",
        "isBuiltIn": True,
        "colorHex": "#188038"
    },
    {
        "id": "immunology",
        "name": "医学免疫学",
        "emoji": "🧬",
        "description": "免疫系统、固有免疫、抗原MHC、淋巴细胞应答与应用知识导图、闪卡与考题",
        "isBuiltIn": True,
        "colorHex": "#9334E6"
    },
    {
        "id": "physiology",
        "name": "生理学",
        "emoji": "⚡",
        "description": "细胞、神经、循环与各系统生理机制调节",
        "isBuiltIn": False,
        "colorHex": "#188038"
    },
    {
        "id": "pathology",
        "name": "病理学",
        "emoji": "🔬",
        "description": "疾病病理变化、发病机理与形态学特征",
        "isBuiltIn": False,
        "colorHex": "#D93025"
    },
    {
        "id": "pharmacology",
        "name": "药理学",
        "emoji": "💊",
        "description": "药物作用机制、药代动力学与不良反应",
        "isBuiltIn": False,
        "colorHex": "#F29900"
    }
]

DEFAULT_UNITS_CONFIG = {
    "anatomy": [
        {"id": "skeletal", "subjectId": "anatomy", "title": "骨骼系统", "subtitle": "Skeletal System", "description": "涵盖骨学总论、中轴骨（颅骨、椎骨、胸骨）、附肢骨（上肢骨、下肢骨）、关节学构造与足弓功能。", "filename": "skeletal_system"},
        {"id": "nervous", "subjectId": "anatomy", "title": "神经系统", "subtitle": "Nervous System", "description": "涵盖中枢神经系统（脑、脊髓）、周围神经系统（脑神经、脊神经）、传导通路与自主神经系统。", "filename": "nervous_system"},
        {"id": "muscular", "subjectId": "anatomy", "title": "肌肉系统", "subtitle": "Muscular System", "description": "涵盖骨骼肌微细结构、肌节、肌丝滑动学说、头颈躯干及四肢肌群分布与运动学效应。", "filename": "muscular_system"},
        {"id": "endocrine", "subjectId": "anatomy", "title": "内分泌系统", "subtitle": "Endocrine System", "description": "涵盖甲状腺、甲状旁腺、肾上腺、垂体、松果体等内分泌腺及内分泌细胞群的功能与构造。", "filename": "endocrine_system"},
        {"id": "sensory", "subjectId": "anatomy", "title": "感觉器官", "subtitle": "Sensory Organs", "description": "涵盖视器（眼球结构、折光系统、屈光不正）、前庭蜗器（外耳、中耳、内耳平衡与听觉受器）及皮感觉构造。", "filename": "sensory_system"}
    ],
    "microbiology": [
        {"id": "micro_01", "subjectId": "microbiology", "title": "01 绪论", "subtitle": "Introduction", "description": "微生物基本概念、三大类型划分与医学微生物学范畴", "filename": "micro_01"},
        {"id": "micro_02", "subjectId": "microbiology", "title": "02 细菌形态与结构", "subtitle": "Bacterial Morphology", "description": "细菌基本形态、细胞壁、肽聚糖与特殊结构（荚膜、鞭毛、芽胞）", "filename": "micro_02"},
        {"id": "micro_03", "subjectId": "microbiology", "title": "03 细菌的生理", "subtitle": "Bacterial Physiology", "description": "细菌营养摄取、代谢产物、生长繁殖与人工培养条件", "filename": "micro_03"},
        {"id": "micro_04", "subjectId": "microbiology", "title": "04 细菌的遗传与变异", "subtitle": "Genetics & Variation", "description": "质粒、噬菌体、基因重组机制（转化、转导、接合）与变异效应", "filename": "micro_04"},
        {"id": "micro_05", "subjectId": "microbiology", "title": "05 细菌的感染与免疫", "subtitle": "Infection & Immunity", "description": "细菌毒力机制（内毒素、外毒素）、侵袭力与宿主抗感染免疫", "filename": "micro_05"},
        {"id": "micro_06", "subjectId": "microbiology", "title": "06 病毒的基本性状", "subtitle": "Viral Characteristics", "description": "病毒核酸/衣壳构造、复制增殖周期与理化抵抗力", "filename": "micro_06"},
        {"id": "micro_07", "subjectId": "microbiology", "title": "07 病毒的感染", "subtitle": "Viral Infection", "description": "病毒感染类型、致病机制（细胞病变、免疫病理）与持续感染", "filename": "micro_07"},
        {"id": "micro_08", "subjectId": "microbiology", "title": "08 真菌学总论", "subtitle": "Mycology Overview", "description": "真菌形态、孢子繁殖、菌落形态与致病分类", "filename": "micro_08"}
    ],
    "immunology": [
        {"id": "immu_01", "subjectId": "immunology", "title": "01 绪论与免疫系统", "subtitle": "Immune System Overview", "description": "免疫三大功能、中枢与外周免疫器官及免疫细胞分布", "filename": "immu_01"},
        {"id": "immu_02", "subjectId": "immunology", "title": "02 固有免疫", "subtitle": "Innate Immunity", "description": "组织屏障、吞噬细胞、NK细胞及体液固有免疫分子效应", "filename": "immu_02"},
        {"id": "immu_03", "subjectId": "immunology", "title": "03 抗原", "subtitle": "Antigens", "description": "抗原表位、异物性、特异性及佐剂与超抗原", "filename": "immu_03"},
        {"id": "immu_04", "subjectId": "immunology", "title": "04 抗原提呈与MHC", "subtitle": "Antigen Presentation & MHC", "description": "MHC分子结构、多态性与内源性/外源性抗原加工提呈途径", "filename": "immu_04"},
        {"id": "immu_05", "subjectId": "immunology", "title": "05 T淋巴细胞与免疫分子", "subtitle": "T Lymphocytes", "description": "T细胞表面标志（TCR、CD3、CD4/CD8）、亚群分化与细胞因子", "filename": "immu_05"},
        {"id": "immu_06", "subjectId": "immunology", "title": "06 B淋巴细胞和抗体", "subtitle": "B Cells & Antibodies", "description": "BCR复合物、免疫球蛋白IgG/IgM/IgA结构及功能特性", "filename": "immu_06"},
        {"id": "immu_07", "subjectId": "immunology", "title": "07 免疫应答", "subtitle": "Immune Response", "description": "体液与细胞免疫应答的时相、激活信号与效应清除机制", "filename": "immu_07"},
        {"id": "immu_08", "subjectId": "immunology", "title": "08 免疫学应用", "subtitle": "Immunological Applications", "description": "人工被动/主动免疫、抗体应用及免疫治疗原则", "filename": "immu_08"}
    ]
}

def load_saved_subjects():
    """读取已长期持久化保存的自定义学科"""
    if os.path.exists(CUSTOM_SUBJECTS_FILE):
        try:
            with open(CUSTOM_SUBJECTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("[Server] 读取自定义学科失败:", e)
    return []

def save_custom_subject(subject_obj):
    """持久化保存新学科到磁盘"""
    saved = load_saved_subjects()
    # 查重
    idx = next((i for i, s in enumerate(saved) if s["id"] == subject_obj["id"]), -1)
    if idx >= 0:
        saved[idx] = subject_obj
    else:
        saved.append(subject_obj)
    with open(CUSTOM_SUBJECTS_FILE, "w", encoding="utf-8") as f:
        json.dump(saved, f, ensure_ascii=False, indent=2)

    # 创建学科所属文件夹
    sub_dir = os.path.join(CUSTOM_DIR, subject_obj["id"])
    for cat in ["decks", "quizzes", "mindmaps"]:
        os.makedirs(os.path.join(sub_dir, cat), exist_ok=True)
    return saved

def get_subject_units(subject_id):
    """读取指定学科的单元列表（内置 + 自定义导入）"""
    units = [dict(u) for u in DEFAULT_UNITS_CONFIG.get(subject_id, [])]
    units_file = os.path.join(CUSTOM_DIR, subject_id, "units.json")
    if os.path.exists(units_file):
        try:
            with open(units_file, "r", encoding="utf-8") as f:
                custom_units = json.load(f)
                for cu in custom_units:
                    existing = next((u for u in units if u["id"] == cu["id"] or u.get("title") == cu.get("title")), None)
                    if existing:
                        existing.update(cu)
                    else:
                        units.append(cu)
        except Exception as e:
            print("[Server] 读取单元失败:", e)
    return units

def save_unit_to_subject(subject_id, category, unit_title, unit_id, data):
    """将导入的 JSON 持久化写入学科，并更新章节清单"""
    if not unit_id:
        unit_id = unit_title.replace(" ", "_").replace("/", "_")
    safe_filename = f"{unit_id}.json"

    # 1. 写入 custom_data 目录
    sub_custom_dir = os.path.join(CUSTOM_DIR, subject_id, category)
    os.makedirs(sub_custom_dir, exist_ok=True)
    file_path = os.path.join(sub_custom_dir, safe_filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # 2. 同时同步备份到 app/src/main/assets 目录（这样 Android 客户端也可以直接打包使用）
    sub_asset_dir = os.path.join(ASSETS_DIR, "subjects", subject_id, category)
    os.makedirs(sub_asset_dir, exist_ok=True)
    asset_file_path = os.path.join(sub_asset_dir, safe_filename)
    try:
        with open(asset_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("[Server] 写入 assets 目录警告:", e)

    # 3. 更新该学科的 units.json 清单
    units_file = os.path.join(CUSTOM_DIR, subject_id, "units.json")
    units = []
    if os.path.exists(units_file):
        try:
            with open(units_file, "r", encoding="utf-8") as f:
                units = json.load(f)
        except:
            units = []

    # 查找是否存在同名/同 ID 单元
    existing = next((u for u in units if u["id"] == unit_id or u.get("title") == unit_title), None)
    cat_names = {"decks": "闪卡", "quizzes": "小测", "mindmaps": "导图"}
    if existing:
        existing[f"has_{category}"] = True
        existing["filename"] = unit_id
        if not existing.get("title"):
            existing["title"] = unit_title
        existing["isCustom"] = True
    else:
        new_unit = {
            "id": unit_id,
            "subjectId": subject_id,
            "title": unit_title,
            "subtitle": "自定义章节",
            "description": f"已导入 {cat_names.get(category, category)} 数据",
            "filename": unit_id,
            "isCustom": True,
            f"has_{category}": True
        }
        units.append(new_unit)

    with open(units_file, "w", encoding="utf-8") as f:
        json.dump(units, f, ensure_ascii=False, indent=2)

    try:
        asset_units_file = os.path.join(ASSETS_DIR, "subjects", subject_id, "units.json")
        os.makedirs(os.path.dirname(asset_units_file), exist_ok=True)
        with open(asset_units_file, "w", encoding="utf-8") as f:
            json.dump(units, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("[Server] 备份 units.json 到 assets 警告:", e)

    return {"success": True, "unitId": unit_id, "category": category, "filePath": file_path}

def find_asset_json(subject_id, category, filename):
    """查找 JSON 数据：先查 custom_data，再查 assets"""
    clean_name = filename[:-5] if filename.endswith(".json") else filename
    json_name = clean_name + ".json"

    dirs_to_search = [
        os.path.join(CUSTOM_DIR, subject_id, category),
        os.path.join(ASSETS_DIR, "subjects", subject_id, category),
        os.path.join(ASSETS_DIR, category),
        os.path.join(CUSTOM_DIR, category)
    ]
    for d in dirs_to_search:
        if not os.path.exists(d):
            continue
        # 1. 精确匹配
        p = os.path.join(d, json_name)
        if os.path.exists(p) and os.path.isfile(p):
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        # 2. 包含匹配
        try:
            for f in os.listdir(d):
                if f.endswith(".json"):
                    fn_no_ext = f[:-5]
                    if clean_name == fn_no_ext or clean_name in fn_no_ext or fn_no_ext in clean_name:
                        with open(os.path.join(d, f), "r", encoding="utf-8") as file:
                            return json.load(file)
        except Exception as e:
            print("[Server] 遍历搜索错误:", e)
    return None

class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        # API: 学科列表 (内置 + 自定义持久化学科)
        if path == "/api/subjects":
            customs = load_saved_subjects()
            all_subjects = list(DEFAULT_SUBJECTS)
            for cs in customs:
                if not any(s["id"] == cs["id"] for s in all_subjects):
                    all_subjects.append(cs)
            self.send_json_response(all_subjects)
            return

        # API: 获取指定学科的章节单元
        if path == "/api/units":
            subject_id = qs.get("subjectId", ["anatomy"])[0]
            units = get_subject_units(subject_id)
            self.send_json_response(units)
            return

        # API: 获取闪卡/导图/小测数据
        if path == "/api/data":
            subject_id = qs.get("subjectId", ["anatomy"])[0]
            category = qs.get("category", ["decks"])[0]
            unit_id = qs.get("unitId", [""])[0]

            units = get_subject_units(subject_id)
            target_unit = next((u for u in units if u["id"] == unit_id), None)
            filename = target_unit["filename"] if target_unit else unit_id

            data = find_asset_json(subject_id, category, filename)
            if data is not None:
                self.send_json_response(data)
            else:
                self.send_json_response({"error": f"Asset not found for {subject_id}/{category}/{filename}"}, status=404)
            return

        # 默认静态页面
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        # 1. POST /api/subjects: 新建学科并持久化
        if path == "/api/subjects":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                sub_data = json.loads(post_body.decode("utf-8"))
                save_custom_subject(sub_data)
                self.send_json_response({"success": True, "subject": sub_data})
            except Exception as e:
                self.send_json_response({"error": str(e)}, status=400)
            return

        # 2. POST /api/save-unit: 保存单元 JSON 数据到学科
        if path == "/api/save-unit":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                payload = json.loads(post_body.decode("utf-8"))
                subject_id = payload.get("subjectId", "anatomy")
                category = payload.get("category", "decks")
                unit_title = payload.get("unitTitle", "未命名章节")
                unit_id = payload.get("unitId")
                json_data = payload.get("data")

                res = save_unit_to_subject(subject_id, category, unit_title, unit_id, json_data)
                self.send_json_response(res)
            except Exception as e:
                self.send_json_response({"error": str(e)}, status=400)
            return

        # 3. POST /api/delete-unit: 删除自定义单元
        if path == "/api/delete-unit":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                payload = json.loads(post_body.decode("utf-8"))
                subject_id = payload.get("subjectId")
                unit_id = payload.get("unitId")
                units_file = os.path.join(CUSTOM_DIR, subject_id, "units.json")
                if os.path.exists(units_file):
                    with open(units_file, "r", encoding="utf-8") as f:
                        units = json.load(f)
                    units = [u for u in units if u["id"] != unit_id]
                    with open(units_file, "w", encoding="utf-8") as f:
                        json.dump(units, f, ensure_ascii=False, indent=2)
                    asset_units = os.path.join(ASSETS_DIR, "subjects", subject_id, "units.json")
                    if os.path.exists(asset_units):
                        with open(asset_units, "w", encoding="utf-8") as f:
                            json.dump(units, f, ensure_ascii=False, indent=2)
                self.send_json_response({"success": True})
            except Exception as e:
                self.send_json_response({"error": str(e)}, status=400)
            return

        # 4. POST /api/delete-subject: 删除自定义学科
        if path == "/api/delete-subject":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                payload = json.loads(post_body.decode("utf-8"))
                subject_id = payload.get("subjectId")
                saved = load_saved_subjects()
                saved = [s for s in saved if s["id"] != subject_id]
                with open(CUSTOM_SUBJECTS_FILE, "w", encoding="utf-8") as f:
                    json.dump(saved, f, ensure_ascii=False, indent=2)
                self.send_json_response({"success": True})
            except Exception as e:
                self.send_json_response({"error": str(e)}, status=400)
            return

        self.send_json_response({"error": "Endpoint not found"}, status=404)

    def send_json_response(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def find_free_port(start_port=8765):
    port = start_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
            port += 1
    return start_port

def launch_browser(url, width=440, height=920):
    browser_candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    for b in browser_candidates:
        if os.path.exists(b):
            try:
                cmd = [
                    b,
                    f"--app={url}",
                    f"--window-size={width},{height}",
                    "--user-data-dir=" + os.path.join(os.environ.get("TEMP", "."), "flashcard_preview_profile")
                ]
                subprocess.Popen(cmd)
                print(f"[Desktop Preview] 已使用 {os.path.basename(b)} 启动独立手机窗口: {url}")
                return True
            except Exception as e:
                print(f"[Desktop Preview] 启动 {b} 失败: {e}")
    import webbrowser
    webbrowser.open(url)
    return False

def main():
    parser = argparse.ArgumentParser(description="记忆辅助 App - Windows 极速桌面预览服务")
    parser.add_argument("--port", type=int, default=8765, help="HTTP 端口号")
    parser.add_argument("--no-open", action="store_true", help="不自动弹出浏览器")
    parser.add_argument("--width", type=int, default=440, help="窗口宽度")
    parser.add_argument("--height", type=int, default=920, help="窗口高度")
    args = parser.parse_args()

    port = find_free_port(args.port)
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, PreviewHandler)
    url = f"http://127.0.0.1:{port}"

    print("=" * 60)
    print(" 🚀 记忆辅助 App - Windows 桌面极速预览框架已启动")
    print(f" 🌐 预览服务地址: {url}")
    print(f" 📁 自定义持久化目录: {CUSTOM_DIR}")
    print(f" 📁 核心数据源目录: {ASSETS_DIR}")
    print(" ⌨️  按 Ctrl+C 即可退出服务")
    print("=" * 60)

    if not args.no_open:
        launch_browser(url, args.width, args.height)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Desktop Preview] 服务已停止。")
        httpd.server_close()

if __name__ == "__main__":
    main()
