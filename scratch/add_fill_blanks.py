import json
import os

with open('scratch/extracted_anatomy_blanks.json', 'r', encoding='utf-8') as f:
    anatomy_blanks = json.load(f)

# Anatomy file pairs
anatomy_pairs = [
    ('skeletal_system', [
        'app/src/main/assets/quizzes/skeletal_system.json',
        'app/src/main/assets/subjects/anatomy/quizzes/skeletal_system.json'
    ]),
    ('muscular_system', [
        'app/src/main/assets/quizzes/muscular_system.json',
        'app/src/main/assets/subjects/anatomy/quizzes/muscular_system.json'
    ]),
    ('nervous_system', [
        'app/src/main/assets/quizzes/nervous_system.json',
        'app/src/main/assets/subjects/anatomy/quizzes/nervous_system.json'
    ]),
    ('endocrine_system', [
        'app/src/main/assets/quizzes/endocrine_system.json',
        'app/src/main/assets/subjects/anatomy/quizzes/endocrine_system.json'
    ]),
    ('sensory_system', [
        'app/src/main/assets/quizzes/sensory_system.json',
        'app/src/main/assets/subjects/anatomy/quizzes/sensory_system.json'
    ])
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

for key, paths in anatomy_pairs:
    blanks = anatomy_blanks.get(key, [])
    for p in paths:
        add_blanks_to_file(p, blanks)

# Immunology Fill-in-the-blanks by chapter
immunology_blanks = {
    '01': [
        {
            "type": "fill_in_blank",
            "question": "人类中枢免疫器官由（1）_______和（2）_______组成，是免疫细胞分化成熟的场所。",
            "blankAnswers": ["骨髓", "胸腺"],
            "rationale": "标准答案及考点解析：人类中枢免疫器官由骨髓和胸腺组成。骨髓是B细胞发育成熟的场所，胸腺是T细胞发育成熟的场所。",
            "hint": "核心考点：中枢免疫器官与外周免疫器官的区别与组成。"
        },
        {
            "type": "fill_in_blank",
            "question": "外周免疫器官包括淋巴结、（1）_______和（2）_______（MALT）。",
            "blankAnswers": ["脾脏", "黏膜相关淋巴组织"],
            "rationale": "标准答案及考点解析：外周免疫器官包括淋巴结、脾脏和黏膜相关淋巴组织（MALT），是免疫细胞定居和发生免疫应答的场所。",
            "hint": "核心考点：外周免疫器官的组成及功能。"
        },
        {
            "type": "fill_in_blank",
            "question": "B淋巴细胞和T淋巴细胞分化成熟的场所分别是（1）_______和（2）_______。",
            "blankAnswers": ["骨髓", "胸腺"],
            "rationale": "标准答案及考点解析：B细胞在骨髓中经历阴性选择分化成熟；前T细胞迁移至胸腺，在胸腺微环境中经历阳性选择与阴性选择分化成熟。",
            "hint": "核心考点：T/B细胞中枢分化成熟的器官。"
        }
    ],
    '02': [
        {
            "type": "fill_in_blank",
            "question": "机体固有免疫的屏障结构主要包括物理屏障、（1）_______屏障和（2）_______屏障。",
            "blankAnswers": ["化学", "生物"],
            "rationale": "标准答案及考点解析：固有免疫的组织屏障包括皮肤与黏膜物理屏障、分泌抑菌物质的化学屏障，以及共生菌群构成的生物屏障（微生物屏障）。",
            "hint": "核心考点：固有免疫三道屏障机制。"
        },
        {
            "type": "fill_in_blank",
            "question": "固有免疫系统识别病原体的分子受体统称为（1）_______（PRR），其识别的病原体共有保守结构称为（2）_______（PAMP）。",
            "blankAnswers": ["模式识别受体", "病原体相关分子模式"],
            "rationale": "标准答案及考点解析：PRR（Pattern Recognition Receptor）是模式识别受体，PAMP（Pathogen-Associated Molecular Pattern）是病原体相关分子模式，如LPS、肽聚糖等。",
            "hint": "核心考点：PRR 与 PAMP 的缩写及生物学定义。"
        }
    ],
    '03': [
        {
            "type": "fill_in_blank",
            "question": "完全抗原指既有（1）_______又有（2）_______的物质；半抗原仅具备（3）_______而缺乏（4）_______。",
            "blankAnswers": ["免疫原性", "抗原性", "抗原性", "免疫原性"],
            "rationale": "标准答案及考点解析：完全抗原既能诱导免疫应答（免疫原性），又能与免疫应答产物结合（抗原性/反应原性）；半抗原只有抗原性，单独无免疫原性，需与蛋白质载体偶联才获得免疫原性。",
            "hint": "核心考点：完全抗原与半抗原的概念对比。"
        },
        {
            "type": "fill_in_blank",
            "question": "根据抗原刺激机体产生抗体是否需要辅助性T细胞协助，抗原可分为（1）_______（TD-Ag）和（2）_______（TI-Ag）。",
            "blankAnswers": ["胸腺依赖性抗原", "胸腺非依赖性抗原"],
            "rationale": "标准答案及考点解析：TD-Ag（Thymus-Dependent Antigen）需要Th细胞辅助产生抗体，引起体液和细胞免疫及免疫记忆；TI-Ag（Thymus-Independent Antigen）不依赖Th即可直接刺激B细胞。",
            "hint": "核心考点：TD-Ag 与 TI-Ag 分类标准。"
        },
        {
            "type": "fill_in_blank",
            "question": "抗原免疫原性的首要决定本质是（1）_______；与种属无关、存在于人、动物及微生物之间的共同抗原称为（2）_______（Forssman抗原）。",
            "blankAnswers": ["异物性", "异嗜性抗原"],
            "rationale": "标准答案及考点解析：异物性是抗原具备免疫原性的物质基础，种系关系越远异物性越强；不同种属间存在的共同抗原被称为异嗜性抗原。",
            "hint": "核心考点：抗原性质与异嗜性抗原概念。"
        }
    ],
    '04': [
        {
            "type": "fill_in_blank",
            "question": "经典的专职抗原提呈细胞（APC）主要包括（1）_______（DC）、（2）_______和（3）_______细胞。",
            "blankAnswers": ["树突状细胞", "单核-巨噬细胞", "B淋巴"],
            "rationale": "标准答案及考点解析：专职APC表达MHC-II类分子和共刺激分子，包括树突状细胞（抗原提呈能力最强）、单核/巨噬细胞以及B淋巴细胞。",
            "hint": "核心考点：三大专职抗原提呈细胞。"
        },
        {
            "type": "fill_in_blank",
            "question": "人类的主要组织相容性复合体（MHC）基因产物又被称为（1）_______（HLA）。MHC-I类分子主要提呈（2）_______抗原，MHC-II类分子主要提呈（3）_______抗原。",
            "blankAnswers": ["人类白细胞抗原", "内源性", "外源性"],
            "rationale": "标准答案及考点解析：HLA即人类白细胞抗原；MHC-I类分子提呈由蛋白酶体加工的内源性抗原给CD8+ T细胞；MHC-II类分子提呈经溶酶体降解的外源性抗原给CD4+ T细胞。",
            "hint": "核心考点：HLA 与 MHC I/II 提呈抗原途径。"
        }
    ],
    '05': [
        {
            "type": "fill_in_blank",
            "question": "成熟T细胞表面的特异性抗原识别受体是（1）_______（TCR），其辅助受体中，辅助性T细胞表达（2）_______，细胞毒性T细胞表达（3）_______。",
            "blankAnswers": ["T细胞受体", "CD4", "CD8"],
            "rationale": "标准答案及考点解析：T细胞受体为TCR；CD4分子与MHC-II类分子的非多态区结合，表达于Th细胞；CD8分子与MHC-I类分子非多态区结合，表达于CTL细胞。",
            "hint": "核心考点：TCR及CD4/CD8表面标志。"
        }
    ],
    '06': [
        {
            "type": "fill_in_blank",
            "question": "B细胞表面的特征性抗原识别受体是（1）_______（BCR），本质是膜表面结合型的（2）_______分子（mIg）。",
            "blankAnswers": ["B细胞受体", "免疫球蛋白"],
            "rationale": "标准答案及考点解析：BCR复合体由膜结合型免疫球蛋白（mIgM或mIgD）与CD79a/CD79b（Igα/Igβ）异二聚体组成，负责识别抗原表位。",
            "hint": "核心考点：BCR的分子构成与本质。"
        },
        {
            "type": "fill_in_blank",
            "question": "人类免疫球蛋白（抗体）的基本结构由两条完全相同的（1）_______链和两条完全相同的（2）_______链通过二硫键连接组成对称的“Y”字形四肽链结构。",
            "blankAnswers": ["重", "轻"],
            "rationale": "标准答案及考点解析：单体抗体分子由2条相同的重链（H链）和2条相同的轻链（L链）通过链间二硫键连接构成。",
            "hint": "核心考点：抗体四肽链单体结构。"
        }
    ],
    '07': [
        {
            "type": "fill_in_blank",
            "question": "适应性免疫应答的基本过程通常分为三个阶段：（1）_______阶段、（2）_______阶段和（3）_______阶段。",
            "blankAnswers": ["感应", "反应", "效应"],
            "rationale": "标准答案及考点解析：免疫应答包括：1. 感应阶段（抗原识别与提呈）；2. 反应阶段（淋巴细胞活化、增殖与分化）；3. 效应阶段（产生效应分子和效应细胞发挥清除作用）。",
            "hint": "核心考点：适应性免疫应答的三大阶段。"
        },
        {
            "type": "fill_in_blank",
            "question": "特异性免疫应答根据主要效应机制可分为B细胞介导的（1）_______免疫和T细胞介导的（2）_______免疫两大类。",
            "blankAnswers": ["体液", "细胞"],
            "rationale": "标准答案及考点解析：体液免疫由B细胞活化产生抗体介导；细胞免疫由特异性T淋巴细胞（CTL、Th1）直接杀伤靶细胞或释放细胞因子介导。",
            "hint": "核心考点：特异性免疫应答的两大类型。"
        }
    ],
    '08': [
        {
            "type": "fill_in_blank",
            "question": "人工主动免疫是给机体输入（1）_______物质，诱导机体自主产生免疫力；人工被动免疫是给机体输入（2）_______等制剂，使机体立即获得抗感染能力。",
            "blankAnswers": ["疫苗", "抗体"],
            "rationale": "标准答案及考点解析：人工主动免疫接种疫苗/类毒素，起效慢但免疫力持久；人工被动免疫注射抗毒素/丙种球蛋白抗体，起效迅速但维持时间短暂（2-3周）。",
            "hint": "核心考点：人工主动免疫与被动免疫的异同。"
        }
    ]
}

immu_files = [
    ('01', ['app/src/main/assets/subjects/immunology/quizzes/01 绪论与免疫系统 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_01.json']),
    ('02', ['app/src/main/assets/subjects/immunology/quizzes/02 固有免疫 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_02.json']),
    ('03', ['app/src/main/assets/subjects/immunology/quizzes/03 抗原 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_03.json']),
    ('04', ['app/src/main/assets/subjects/immunology/quizzes/04 抗原提呈与MHC 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_04.json']),
    ('05', ['app/src/main/assets/subjects/immunology/quizzes/05 T淋巴细胞与免疫分子 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_05.json']),
    ('06', ['app/src/main/assets/subjects/immunology/quizzes/06 B淋巴细胞和抗体 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_06.json']),
    ('07', ['app/src/main/assets/subjects/immunology/quizzes/07 免疫应答 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_07.json']),
    ('08', ['app/src/main/assets/subjects/immunology/quizzes/08 免疫学应用 测验.json', 'app/src/main/assets/subjects/immunology/quizzes/immu_08.json'])
]

for ch_id, paths in immu_files:
    blanks = immunology_blanks.get(ch_id, [])
    for p in paths:
        add_blanks_to_file(p, blanks)

print("\n--- Finished adding fill-in-the-blank questions to all subjects ---")
