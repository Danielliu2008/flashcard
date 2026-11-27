import json
import os

microbiology_blanks = {
    '01': [
        {
            "type": "fill_in_blank",
            "question": "微生物按细胞结构和化学组成特点可分为三大类：（1）_______型微生物（如真菌）、（2）_______型微生物（如细菌、支原体）和（3）_______型微生物（如病毒）。",
            "blankAnswers": ["真核细胞", "原核细胞", "非细胞"],
            "rationale": "标准答案及考点解析：三大类微生物包括：1. 真核细胞型（细胞核分化程度高，有核膜、核仁、细胞器，如真菌）；2. 原核细胞型（原始核质，无核膜核仁，如细菌）；3. 非细胞型（无细胞结构，仅含一种核酸，如病毒）。",
            "hint": "核心考点：微生物三大类别的分类依据与代表生物。"
        }
    ],
    '02': [
        {
            "type": "fill_in_blank",
            "question": "细菌的基本结构包括细胞壁、（1）_______、（2）_______和（3）_______；特殊结构包括荚膜、（4）_______、菌毛和芽胞。",
            "blankAnswers": ["细胞膜", "细胞质", "核质", "鞭毛"],
            "rationale": "标准答案及考点解析：细菌基本结构是所有细菌都具备的（壁、膜、质、核），特殊结构仅部分细菌具备（鞭毛、菌毛、荚膜、芽胞）。",
            "hint": "核心考点：细菌基本结构与特殊结构的划分。"
        },
        {
            "type": "fill_in_blank",
            "question": "革兰阳性菌（G+）细胞壁的主要成分是聚糖骨架、（1）_______侧链和（2）_______交联桥构成的致密肽聚糖；革兰阴性菌（G-）细胞壁特有的外膜层由脂质双层、脂蛋白和（3）_______（LPS，即内毒素）组成。",
            "blankAnswers": ["四肽", "五肽", "脂多糖"],
            "rationale": "标准答案及考点解析：G+菌肽聚糖占干重50%-80%，含磷壁酸；G-菌肽聚糖仅占5%-20%，外膜含有脂多糖（LPS），由脂质A、核心多糖和O特异多糖组成。",
            "hint": "核心考点：革兰阳性菌与阴性菌细胞壁构造对比。"
        }
    ],
    '03': [
        {
            "type": "fill_in_blank",
            "question": "细菌生长繁殖的群体生长曲线可分为四个时期：（1）_______期、（2）_______期（细菌形态染色最典型）、稳定期和衰亡期。",
            "blankAnswers": ["迟缓", "对数", "衰亡"],
            "rationale": "标准答案及考点解析：细菌群体生长曲线：1. 迟缓期（适应期）；2. 对数期（生长迅速，形态最典型，抗生素敏感性最高）；3. 稳定期（产生产物如芽胞、抗生素、毒素）；4. 衰亡期。",
            "hint": "核心考点：细菌生长曲线的四个时期及对数期特征。"
        }
    ],
    '04': [
        {
            "type": "fill_in_blank",
            "question": "细菌基因转移和重组的方式主要包括：（1）_______（受体菌直接摄取游离供体DNA片段）、（2）_______（以噬菌体为媒介）、接合（通过性菌毛）和原生质体融合。",
            "blankAnswers": ["转化", "转导"],
            "rationale": "标准答案及考点解析：基因转移四种机制：转化（Transformation，摄取外源游离DNA）、转导（Transduction，温和噬菌体介导）、接合（Conjugation，性菌毛介导质粒传递）。",
            "hint": "核心考点：细菌基因转移方式的定义与区别。"
        }
    ],
    '05': [
        {
            "type": "fill_in_blank",
            "question": "细菌毒素主要分为（1）_______毒素（多数为活菌分泌的蛋白质，毒性强、特异性高、可制成类毒素）和（2）_______毒素（G-菌细胞壁裂解后释放的脂多糖LPS，耐热、毒性作用类似）。",
            "blankAnswers": ["外", "内"],
            "rationale": "标准答案及考点解析：外毒素（Exotoxin）为蛋白质，抗原性强可脱毒为类毒素；内毒素（Endotoxin）为脂多糖（LPS），耐热，不能制备类毒素，引起发热、休克和DIC。",
            "hint": "核心考点：内毒素与外毒素的生物学特性对比。"
        }
    ],
    '06': [
        {
            "type": "fill_in_blank",
            "question": "病毒体结构最基本由中心的（1）_______（核心）和外周包被的（2）_______组成，二者共同构成核衣壳；部分病毒在核衣壳外还包被一层（3）_______。",
            "blankAnswers": ["核酸", "衣壳", "包膜"],
            "rationale": "标准答案及考点解析：最简单的病毒由核衣壳构成（核心为DNA或RNA单一核酸，衣壳由壳粒构成），包膜病毒外被宿主细胞膜衍生的包膜与刺突。",
            "hint": "核心考点：病毒的基本结构与包膜构成。"
        }
    ],
    '07': [
        {
            "type": "fill_in_blank",
            "question": "病毒在宿主细胞内的增殖过程称为自我复制，其复制周期包括吸附、（1）_______、脱壳、（2）_______合成、组装与成熟、释放六个连续步骤。",
            "blankAnswers": ["侵入", "生物"],
            "rationale": "标准答案及考点解析：病毒增殖经历吸附、穿入（侵入）、脱壳、生物合成（核酸复制与蛋白质合成）、组装成熟及释放等阶段。",
            "hint": "核心考点：病毒复制周期的六个核心阶段。"
        }
    ],
    '08': [
        {
            "type": "fill_in_blank",
            "question": "真菌属于（1）_______细胞型微生物，具有典型细胞核与细胞器；根据菌落形态可分为（2）_______菌（单细胞）和（3）_______菌（丝状菌）。",
            "blankAnswers": ["真核", "酵母", "霉"],
            "rationale": "标准答案及考点解析：真菌是真核细胞型微生物，有核膜核仁和多种细胞器；按形态分为酵母菌（单细胞真菌）和丝状菌/霉菌（多细胞真菌，由菌丝和孢子构成）。",
            "hint": "核心考点：真菌的细胞类型与基本形态分类。"
        }
    ]
}

micro_files = [
    ('01', ['app/src/main/assets/subjects/microbiology/quizzes/01 绪论 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_01.json']),
    ('02', ['app/src/main/assets/subjects/microbiology/quizzes/02 细菌形态与结构 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_02.json']),
    ('03', ['app/src/main/assets/subjects/microbiology/quizzes/03 细菌的生理 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_03.json']),
    ('04', ['app/src/main/assets/subjects/microbiology/quizzes/04 细菌的遗传与变异 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_04.json']),
    ('05', ['app/src/main/assets/subjects/microbiology/quizzes/05 细菌的感染与免疫 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_05.json']),
    ('06', ['app/src/main/assets/subjects/microbiology/quizzes/06 病毒的基本性状 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_06.json']),
    ('07', ['app/src/main/assets/subjects/microbiology/quizzes/07 病毒的感染 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_07.json']),
    ('08', ['app/src/main/assets/subjects/microbiology/quizzes/08 真菌学总论 测验.json', 'app/src/main/assets/subjects/microbiology/quizzes/micro_08.json'])
]

def add_blanks_to_file(filepath, new_blanks):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    quiz = data.get('quiz', [])
    existing_questions = {q.get('question') for q in quiz if q.get('type') == 'fill_in_blank'}
    
    added = 0
    for b in new_blanks:
        if b['question'] not in existing_questions:
            quiz.append(b)
            existing_questions.add(b['question'])
            added += 1
            
    data['quiz'] = quiz
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {filepath}: added {added} fill-in-the-blank questions (Total now: {len(quiz)})")

for ch_id, paths in micro_files:
    blanks = microbiology_blanks.get(ch_id, [])
    for p in paths:
        add_blanks_to_file(p, blanks)

print("\n--- Finished adding microbiology fill-in-the-blank questions ---")
