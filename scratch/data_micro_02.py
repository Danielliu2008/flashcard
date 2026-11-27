# -*- coding: utf-8 -*-
"""
Microbiology Chapter 2: 细菌的形态与结构
Based strictly on 01-C02细菌学-01细菌的形态与结构52(2).pdf page 4 掌握要求
"""

DECK_02 = {
    "id": "micro_02",
    "title": "02 细菌形态与结构 闪卡",
    "description": "医学微生物学·细菌大小形态、基本结构（细胞壁肽聚糖/G+与G-对比/L型）、特殊结构（荚膜/鞭毛/菌毛/芽胞）与革兰染色法核心考点",
    "topics": {
        "covered": [
            "细菌大小度量单位与三大基本形态",
            "细菌基本结构（细胞壁、细胞膜、细胞质、核质）",
            "肽聚糖三联分子结构与青霉素/溶菌酶作用机制",
            "革兰阳性菌与革兰阴性菌细胞壁全维度横向对比",
            "脂多糖（LPS/内毒素）分子三层结构与致病中心脂质A",
            "细菌L型的概念、诱因与临床耐药复发意义",
            "细菌四大特殊结构（荚膜、鞭毛、菌毛、芽胞）特性与功能",
            "革兰染色法原理、四步操作程序、结果与三大医学意义"
        ],
        "followUp": [
            "细菌的营养摄取与生长曲线各期生物学特性",
            "细菌内毒素与外毒素的致病机制与免疫原性差异"
        ]
    },
    "flashcards": [
        {
            "c": 1,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【测量与形态】细菌大小的度量单位是什么？其三大基本形态包括哪些？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **度量单位**：**微米（$\\mu\\text{m}$）**。通常在普通光学显微镜油镜下观察。\n2. **三大形态**：\n   - **球菌**（Coccus）：直径约$1\\,\\mu\\text{m}$，按分裂平面分为双球菌、链球菌、葡萄球菌、四联/八叠球菌；\n   - **杆菌**（Bacillus）：长$1\\sim 5\\,\\mu\\text{m}$，粗细长短各异（大肠埃希菌、结核分枝杆菌）；\n   - **螺形菌**（Spiral bacterium）：弧菌（呈弧形一个弯曲如霍乱弧菌）或螺菌（多个弯曲如幽门螺杆菌）。"}]},
            "pointType": "形态基础",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 2,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心组成】细菌细胞壁的主要共同骨架成分是什么？由哪三部分构成？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "**主要成分：肽聚糖（Peptidoglycan，又称黏肽）**\n由三部分通过共价键紧密交联而成：\n1. **聚糖骨架**：由**N-乙酰葡糖胺（NAG）**和**N-乙酰胞壁酸（NAM）**通过**$\\beta$-1,4糖苷键**交替连接；\n2. **四肽侧链**：连接在N-乙酰胞壁酸上；\n3. **五肽交联桥**（或直接肽键连接）：连接相邻四肽侧链，将平行的聚糖链交织成立体坚固网状结构。"}]},
            "pointType": "分子结构",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 3,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【药理机制】溶菌酶（Lysozyme）与青霉素（Penicillin）破坏细菌细胞壁的机制有何不同？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **溶菌酶**：特异性水解聚糖骨架中的**$\\beta$-1,4糖苷键**，直接切断已合成的聚糖链，导致原有细胞壁崩解（对静止期和繁殖期细菌均有效）；\n2. **青霉素**：竞争性抑制细菌合成细胞壁的**转肽酶（青霉素结合蛋白PBPs）**，阻断四肽侧链与交联桥之间的交叉联结，使新合成的肽聚糖无法成网（**仅对繁殖期细菌有效**）。"}]},
            "pointType": "作用机制",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 4,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】简述革兰阳性菌（G+）与革兰阴性菌（G-）细胞壁的主要结构差异。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "| 比较项目 | 革兰阳性菌（G+） | 革兰阴性菌（G-） |\n| :--- | :--- | :--- |\n| **厚度** | 较厚（20~80 nm） | 较薄（10~15 nm） |\n| **肽聚糖层数** | 坚厚，多达50层（占干重50%~80%） | 疏松，仅1~2层（占干重5%~20%） |\n| **特有成分** | **磷壁酸（Teichoic acid）** | **外膜（Outer membrane）** |\n| **外膜组成** | 无外膜 | 脂质双层、脂蛋白、**脂多糖（LPS）** |\n| **五肽交联桥** | 有（如甘氨酸五肽交联） | 无（侧链直接形成肽键交联） |\n| **对青霉素/溶菌酶** | 高度敏感 | 较不敏感（外膜屏障保护） |"}]},
            "pointType": "核心对比",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 5,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【高危致病】什么是脂多糖（LPS）？由哪三部分构成？其毒性活性的核心中心是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：脂多糖（LPS）是革兰阴性菌外膜最外层的特有成分，即细菌的**内毒素（Endotoxin）**。\n2. **三层结构**：\n   - **脂质A（Lipid A）**：内层，由二糖脂构成，是内毒素的**主要毒性成分和生物学活性中心**（引起发热、休克、DIC等）；\n   - **核心多糖（Core polysaccharide）**：中层，属属特异性抗原；\n   - **O特异性多糖（O antigen）**：最外层寡糖长链，亲水性，决定细菌的**菌株特异性抗原**。"}]},
            "pointType": "高频考点",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 6,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【临床高频】什么是细菌L型（Bacterial L-form）？其主要诱因与临床意义是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：细胞壁缺陷型细菌。在溶菌酶、抗体、补体或β-内酰胺类抗生素作用下，细菌细胞壁肽聚糖受损或缺失，但仍能在**高渗环境**下生存和分裂繁殖的菌株。\n2. **生物学特性**：高度多形性，革兰染色多转为阴性，需高渗培养基培养，菌落呈典型**“荷包蛋”状（油煎蛋状）**。\n3. **临床意义**：\n   - 常导致常规细菌培养阴性而发生漏诊；\n   - 导致抗生素耐药（对作用于细胞壁的青霉素/头孢菌素完全天然耐药）；\n   - 停药后可恢复原有细胞壁与毒力，引起感染迁延不愈或反复复发。"}]},
            "pointType": "临床意义",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 7,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【特殊结构】什么是细菌荚膜（Capsule）？有何关键功能与医学意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：某些细菌在细胞壁外包绕的一层边界清楚、厚度超过$0.2\\,\\mu\\text{m}$的黏液性胶状结构（化学本质绝大多数为**多糖**，炭疽芽胞杆菌为**多肽**）。\n2. **四大功能与医学意义**：\n   - **抗吞噬作用**（最关键毒力因素）：阻碍吞噬细胞的摄取与消化（如肺炎链球菌）；\n   - **抗体液杀伤作用**：阻止补体活化与溶菌杀伤；\n   - **黏附作用**：利于定植在组织表面；\n   - **抗原性**（K抗原）：可用于细菌血清学分型和制备荚膜多糖疫苗。"}]},
            "pointType": "特殊结构",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 8,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【特殊结构】什么是细菌鞭毛（Flagellum）？其主要分类与功能是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：生长在某些细菌菌体表面细长、波状弯曲的丝状蛋白质构件，由鞭毛蛋白（Flagellin）组成。\n2. **分类**：单毛菌（霍乱弧菌）、双毛菌、丛毛菌、周毛菌（大肠埃希菌、伤寒沙门菌）。\n3. **主要功能**：\n   - **细菌的运动器官**：使细菌具有趋化性与活泼动力，半固体培养基穿刺线可见云雾羽毛状扩散；\n   - **致病性**：协助细菌穿透黏液层黏附定植；\n   - **抗原性（H抗原）**：特异性强，用于细菌鉴定与血清学分型。"}]},
            "pointType": "特殊结构",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 9,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【横向对比】普通菌毛（Common pilus）与性菌毛（Sex pilus）有何功能区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "菌毛是细菌表面短细坚硬的丝状微管蛋白突起，分为两类：\n1. **普通菌毛**：数量极多（数百根），遍布菌体表面。**核心功能是黏附**于宿主上皮细胞受体，是细菌定植并引起感染的重要致病因子（如淋病奈瑟菌、大肠埃希菌）。\n2. **性菌毛**（F菌毛）：数量极少（1~4根），仅见于雄性菌株（F+或Hfr菌）。呈中空管状，**核心功能是接合转移**：性菌毛与雌性受体菌（F-）结合形成接合通道，将质粒DNA（如耐药R质粒）直接传递给受体菌。"}]},
            "pointType": "考点对比",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 10,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【重要考点】什么是细菌芽胞（Spore）？为什么说芽胞不是细菌的繁殖方式？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：某些革兰阳性菌（如炭疽芽胞杆菌、破伤风梭菌、肉毒梭菌）在恶劣营养匮乏环境下，在菌体内形成的圆形或卵圆形致密**休眠体**。\n2. **为什么不是繁殖方式**：一个细菌细胞在环境恶化时只能形成**一个**芽胞，而在条件适宜时一个芽胞也只能萌发恢复为**一个**营养体繁殖体，细菌数量没有增加，故属于休眠防御结构而非繁殖方式。"}]},
            "pointType": "概念辨析",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 11,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【灭菌标准】芽胞为何具有极强的理化抵抗力？在消毒灭菌实践中有何指标意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **极强抵抗力原因**：\n   - 芽胞壁厚，含致密外壳蛋白层与皮质层；\n   - 核心含水率极低，代谢极度停滞；\n   - 含有特有的高浓度**吡啶二羧酸钙（DPA-Ca）**，极强稳定蛋白质与DNA结构。\n2. **医学灭菌指标意义**：\n   - 芽胞是抵抗力最强的微生物结构，普通沸水煮沸无法在短时间内杀死；\n   - 临床和实验室将**杀灭芽胞作为衡量物理与化学消毒灭菌方法是否彻底的绝对黄金指标**。"}]},
            "pointType": "指标意义",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 12,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【染色精要】简述革兰染色法（Gram Staining）的四步操作流程与各试剂作用。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **初染**：滴加**结晶紫**染色液（约1 min），水洗——所有细菌初染均染成深紫色；\n2. **媒染**：滴加**碘液**（约1 min），水洗——碘与结晶紫形成不溶性大分子复合物；\n3. **脱色（关键步骤）**：滴加**95%乙醇**脱色约30秒至无紫色流出，立即水洗；\n4. **复染**：滴加**稀释复红**（或沙黄）复染约30秒，水洗吸干油镜镜检。"}]},
            "pointType": "实验原理",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 13,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【实验机制】革兰染色法中95%乙醇脱色的根本原理是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "根本原因在于**G+与G-细胞壁化学组成与结构的巨大差异**：\n1. **革兰阳性菌（G+）**：细胞壁厚、肽聚糖致密交联度高、脂质极少。乙醇脱色时细胞壁脱水使孔径缩小，结晶紫-碘复合物无法渗漏，菌体保持**紫色**；\n2. **革兰阴性菌（G-）**：细胞壁薄、肽聚糖仅1~2层、脂多糖及外膜脂质含量高。乙醇迅速溶解外膜脂质增大通透性，结晶紫-碘复合物被彻底洗脱变成无色，复染后显**红色**。"}]},
            "pointType": "机制原理",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 14,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【医学应用】革兰染色在医学临床与微生物学实践中有哪三大重大意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **鉴别细菌**：迅速将所有细菌分为革兰阳性菌（紫色）和革兰阴性菌（红色）两大类，是指南性细菌分类第一步；\n2. **指导临床抗菌药物选择**：\n   - G+菌多对青霉素类、头孢类、万古霉素、红霉素敏感；\n   - G-菌多对外膜穿透力强或抗阴性菌药物敏感（如氨基糖苷类、喹诺酮类、三代头孢）；\n3. **判断细菌致病性与致病机制**：\n   - G+菌主要释放致病性强的**外毒素**；\n   - G-菌细胞壁本身即为致死性的**内毒素（LPS）**。"}]},
            "pointType": "三大意义",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 15,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【胞质颗粒】什么是异染颗粒（Volutin/Metachromatic granule）？在临床何种细菌诊断中有重要意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：细菌细胞质内的无机多聚偏磷酸盐颗粒，储藏能量与磷源，对碱性染料（如奈瑟染色、阿尔伯特染色）亲和力极强，染色后与菌体颜色不同（异染）；\n2. **临床意义**：在**白喉棒状杆菌（Corynebacterium diphtheriae）**两端尤为显著，是形态学快速鉴别白喉杆菌、排除非致病棒状杆菌的重要诊断指标。"}]},
            "pointType": "颗粒诊断",
            "starRating": "★★☆",
            "importance": 2
        }
    ]
}

QUIZ_02 = {
    "quiz": [
        # --- 单选题 (1~10) ---
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "测量细菌大小最常用的物理单位是：",
            "options": [
                {"text": "微米（μm）", "isCorrect": True, "rationale": "正确。细菌通常在普通光学显微镜下测量，单位为微米（μm）。"},
                {"text": "纳米（nm）", "isCorrect": False, "rationale": "纳米（nm）是测量病毒大小的单位。"},
                {"text": "毫米（mm）", "isCorrect": False, "rationale": "毫米用于描述宏观菌落或寄生虫。"},
                {"text": "埃（Å）", "isCorrect": False, "rationale": "埃通常用于原子尺度分子结构描述。"}
            ],
            "hint": "病毒用纳米（nm），细菌用什么？",
            "rationale": "细菌微小，大小通常在0.5~5 μm之间，度量单位为微米（μm）。"
        },
        {
            "id": 2,
            "type": "multiple_choice",
            "question": "细菌细胞壁的基本骨架成分是肽聚糖，其聚糖链的单糖骨架是由哪两种物质交替连接构成的？",
            "options": [
                {"text": "N-乙酰葡糖胺（NAG）与N-乙酰胞壁酸（NAM）", "isCorrect": True, "rationale": "正确。二者通过β-1,4糖苷键交替连接构成聚糖骨架。"},
                {"text": "葡萄糖与半乳糖", "isCorrect": False, "rationale": "属于常规双糖/多糖原料，非肽聚糖骨架。"},
                {"text": "甘露糖与甘油磷酸", "isCorrect": False, "rationale": "甘露糖是真菌细胞壁成分，甘油磷酸是磷壁酸成分。"},
                {"text": "几丁质与纤维素", "isCorrect": False, "rationale": "几丁质见于真菌，纤维素见于植物。"}
            ],
            "hint": "NAG与NAM。",
            "rationale": "肽聚糖骨架是由N-乙酰葡糖胺（NAG）和N-乙酰胞壁酸（NAM）通过β-1,4糖苷键交替聚合而成的多糖长链。"
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "溶菌酶杀灭细菌的作用机制是特异性水解：",
            "options": [
                {"text": "聚糖骨架中的β-1,4糖苷键", "isCorrect": True, "rationale": "正确。溶菌酶切断NAG与NAM之间的β-1,4糖苷键破坏细胞壁。"},
                {"text": "四肽侧链末端的D-丙氨酸", "isCorrect": False, "rationale": "转肽酶在交联时切除D-丙氨酸，非溶菌酶靶点。"},
                {"text": "细胞膜上的脂质双层", "isCorrect": False, "rationale": "属于多粘菌素等膜靶向药物机制。"},
                {"text": "核糖体30S亚基上的rRNA", "isCorrect": False, "rationale": "属于氨基糖苷类抗生素机制。"}
            ],
            "hint": "切断细胞壁多糖骨架的糖苷键。",
            "rationale": "溶菌酶裂解β-1,4糖苷键，使细菌细胞壁不溶性聚糖骨架水解成可溶性寡糖，造成细胞壁缺损溶解。"
        },
        {
            "id": 4,
            "type": "multiple_choice",
            "question": "下列哪种成分仅存在于革兰阳性（G+）菌细胞壁中，而不存在于革兰阴性（G-）菌细胞壁？",
            "options": [
                {"text": "磷壁酸（Teichoic acid）", "isCorrect": True, "rationale": "正确。磷壁酸是革兰阳性菌细胞壁特有的多聚醇抗原成分。"},
                {"text": "脂多糖（LPS）", "isCorrect": False, "rationale": "脂多糖是革兰阴性菌特有的外膜成分。"},
                {"text": "肽聚糖", "isCorrect": False, "rationale": "G+与G-菌均含有肽聚糖骨架。"},
                {"text": "外膜蛋白", "isCorrect": False, "rationale": "外膜为革兰阴性菌特有。"}
            ],
            "hint": "注意区分磷壁酸与脂多糖分别属于哪一类菌。",
            "rationale": "磷壁酸是革兰阳性菌特有成分，分为膜磷壁酸和壁磷壁酸；而革兰阴性菌细胞壁特有成分为外膜（含脂多糖LPS）。"
        },
        {
            "id": 5,
            "type": "multiple_choice",
            "question": "革兰阴性菌外膜的脂多糖（LPS）即内毒素，其引起宿主发热、微循环休克和DIC的主要毒性活性中心是：",
            "options": [
                {"text": "脂质A（Lipid A）", "isCorrect": True, "rationale": "正确。脂质A是内毒素主要毒性成分和生物学活性中心。"},
                {"text": "核心多糖（Core polysaccharide）", "isCorrect": False, "rationale": "核心多糖具有属特异性，无直接内毒素活性。"},
                {"text": "O特异性多糖（O抗原）", "isCorrect": False, "rationale": "O抗原决定菌体血清型特异性抗原性。"},
                {"text": "外膜微孔蛋白（Porin）", "isCorrect": False, "rationale": "微孔蛋白负责跨膜通道运输，无毒性。"}
            ],
            "hint": "脂质A（Lipid A）是所有内毒素毒性作用的共同结构物质基础。",
            "rationale": "内毒素由脂质A、核心多糖和O特异多糖三部分组成，其中脂质A具有极其恒定的结构，是内毒素的毒性核心。"
        },
        {
            "id": 6,
            "type": "multiple_choice",
            "question": "关于细菌L型（L-form）的生物学特性，下列说法错误的是：",
            "options": [
                {"text": "在低渗培养基中生长良好且形态规整", "isCorrect": True, "rationale": "符合题意。细菌L型丧失了维持渗透压屏障的细胞壁，在低渗环境中极易吸水膨胀裂解，必须在高渗培养基中才能生存！"},
                {"text": "细胞壁肽聚糖受到损伤或完全缺失", "isCorrect": False, "rationale": "叙述正确，L型即细胞壁缺陷型。"},
                {"text": "对青霉素等作用于细胞壁的β-内酰胺类抗生素天然耐药", "isCorrect": False, "rationale": "叙述正确，因缺乏靶结构（肽聚糖），青霉素对其无效。"},
                {"text": "去除诱导诱发因素后，部分菌株可重新合成细胞壁并恢复毒力", "isCorrect": False, "rationale": "叙述正确，这是临床感染复发的重要根源。"}
            ],
            "hint": "细胞壁缺失的细菌在低渗环境中会发生什么？",
            "rationale": "细胞壁主要功能之一是抵抗渗透压。缺乏细胞壁的L型细菌只有在高渗环境下才能稳定存活，在普通低渗环境下会裂解死亡。"
        },
        {
            "id": 7,
            "type": "multiple_choice",
            "question": "肺炎链球菌能在宿主体内抵抗中性粒细胞和巨噬细胞吞噬消化，主要依赖于其表面哪种特殊结构？",
            "options": [
                {"text": "荚膜（Capsule）", "isCorrect": True, "rationale": "正确。荚膜是强效抗吞噬和抗体液杀伤的重要毒力结构。"},
                {"text": "鞭毛（Flagellum）", "isCorrect": False, "rationale": "鞭毛为运动器官。"},
                {"text": "性菌毛（Sex pilus）", "isCorrect": False, "rationale": "性菌毛负责接合传递质粒。"},
                {"text": "芽胞（Spore）", "isCorrect": False, "rationale": "肺炎链球菌不产生芽胞。"}
            ],
            "hint": "光滑黏液层，抗吞噬作用的关键毒力物质。",
            "rationale": "荚膜包裹在菌体外表，具有抗吞噬、抗溶菌酶和抵抗补体介导溶菌的保护功能，是肺炎链球菌等的主要毒力因子。"
        },
        {
            "id": 8,
            "type": "multiple_choice",
            "question": "细菌耐热芽胞的核心含有一种特异性高浓度化学保护物质，能使蛋白质和核酸维持高度热稳定性，该物质是：",
            "options": [
                {"text": "吡啶二羧酸钙（DPA-Ca）", "isCorrect": True, "rationale": "正确。DPA-Ca是芽胞特有的耐热物质，可占芽胞干重10%以上。"},
                {"text": "磷壁酸钙", "isCorrect": False, "rationale": "磷壁酸为G+菌细胞壁成分。"},
                {"text": "二磷酸腺苷（ADP）", "isCorrect": False, "rationale": "常规能量代谢分子。"},
                {"text": "聚-β-羟基丁酸（PHB）", "isCorrect": False, "rationale": "PHB为碳源储藏颗粒。"}
            ],
            "hint": "DPA与钙离子螯合形成的复合物。",
            "rationale": "吡啶二羧酸（DPA）与钙离子结合形成DPA-Ca复合物，是细菌芽胞耐受高温、辐射和脱水破坏的决定性化学成分。"
        },
        {
            "id": 9,
            "type": "multiple_choice",
            "question": "革兰染色法操作程序中，决定染色最终成败的“最关键步骤”是：",
            "options": [
                {"text": "95%乙醇脱色时间与操作", "isCorrect": True, "rationale": "正确。脱色不足会导致G-被误判为G+（假阳性），脱色过度会导致G+被误判为G-（假阴性）。"},
                {"text": "初染结晶紫滴加浓度", "isCorrect": False, "rationale": "初染后所有菌均呈紫色，非分水岭步骤。"},
                {"text": "碘液媒染时间长短", "isCorrect": False, "rationale": "媒染固定染料，非最终颜色分化步骤。"},
                {"text": "复染稀释复红的温度", "isCorrect": False, "rationale": "复染只是对脱色后的菌体上色。"}
            ],
            "hint": "哪一步把两类细菌从相同的紫色中区分开来？",
            "rationale": "乙醇脱色是革兰染色的核心分化步骤，严格掌握脱色时间（通常约30秒至洗脱液无紫色）是确保结果准确的关键。"
        },
        {
            "id": 10,
            "type": "multiple_choice",
            "question": "革兰染色在临床指导抗感染用药方面具有重大意义，通常革兰阳性菌（G+）对下列哪类抗生素高度敏感？",
            "options": [
                {"text": "青霉素G等作用于肽聚糖交联的β-内酰胺类", "isCorrect": True, "rationale": "正确。G+菌细胞壁以厚实肽聚糖为主，且无外膜屏障阻挡，对青霉素类高度敏感。"},
                {"text": "多粘菌素B（Polymyxin B）", "isCorrect": False, "rationale": "多粘菌素专一作用于G-菌外膜脂多糖。"},
                {"text": "两性霉素B（Amphotericin B）", "isCorrect": False, "rationale": "两性霉素B为抗真菌药物，对细菌无效。"},
                {"text": "抗酸菌专用异烟肼", "isCorrect": False, "rationale": "异烟肼专一抑制分枝菌酸合成。"}
            ],
            "hint": "G+菌缺乏外膜屏障，细胞壁富含暴露的厚肽聚糖。",
            "rationale": "G+菌细胞壁肽聚糖层厚且缺乏外膜保护，青霉素能直接到达转肽酶靶点阻碍交联，故G+菌对青霉素类高度敏感。"
        },

        # --- 判断题 (11~15) ---
        {
            "id": 11,
            "type": "true_false",
            "question": "革兰阴性菌（G-）细胞壁肽聚糖层虽然较薄，但在肽聚糖外侧还覆盖着由脂质双层、脂蛋白和脂多糖（LPS）组成的外膜结构。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。外膜是革兰阴性菌细胞壁特有的多层防御屏障。"},
                {"text": "错误", "isCorrect": False, "rationale": "G-菌特有外膜结构。"}
            ],
            "hint": "G-菌细胞壁由薄肽聚糖层加复杂外膜构成。",
            "rationale": "革兰阴性菌的典型特征是肽聚糖薄（1~2层），但其外覆盖复杂的外膜结构，包含极具致病活性的脂多糖（LPS）。"
        },
        {
            "id": 12,
            "type": "true_false",
            "question": "细菌芽胞是细菌的一种繁殖结构，一个菌体在恶劣环境中可以分裂产生多个芽胞以迅速扩大菌群数量。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。芽胞是休眠体而非繁殖方式！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。一个细菌只能形成一个芽胞，一个芽胞萌发也只能恢复成一个营养体，数量不增加，属于休眠抗逆形式。"}
            ],
            "hint": "注意芽胞形成过程中细菌细胞数量是否发生乘积增加。",
            "rationale": "芽胞是部分革兰阳性菌在环境恶劣时形成的休眠体，1个细菌产生1个芽胞，不属于繁殖方式。"
        },
        {
            "id": 13,
            "type": "true_false",
            "question": "性菌毛比普通菌毛更加短小且数量庞大（每个菌体可达数百根），主要负责协助细菌黏附于宿主黏膜上皮细胞。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。这是普通菌毛的特征！性菌毛长而粗，数量极少（仅1~4根）。"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。数量多、协助黏附的是普通菌毛；性菌毛数量极少（1~4根），功能是传递质粒介导接合。"}
            ],
            "hint": "区分普通菌毛（多、黏附）与性菌毛（少、接合传质粒）。",
            "rationale": "普通菌毛数量多（可达数百根），功能为黏附；性菌毛数量仅1~4根，由F质粒编码，负责接合转移遗传物质。"
        },
        {
            "id": 14,
            "type": "true_false",
            "question": "革兰染色最终结果中，革兰阳性菌显紫色，而革兰阴性菌显红色。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。G+保留初染结晶紫显紫色，G-经脱色后被复染液（复红）染成红色。"},
                {"text": "错误", "isCorrect": False, "rationale": "阳紫阴红是微生物学最基础的金标准记忆口诀。"}
            ],
            "hint": "阳紫阴红。",
            "rationale": "革兰染色法中，革兰阳性菌（G+）呈现紫色，革兰阴性菌（G-）呈现红色。"
        },
        {
            "id": 15,
            "type": "true_false",
            "question": "临床微生物实验室和医院手术器械灭菌中，通常以杀灭细菌的‘繁殖体’作为评判物理灭菌是否彻底的标准。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。是以杀灭‘芽胞’作为灭菌合格的黄金标准！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。繁殖体抵抗力弱，芽胞抵抗力最强，必须以彻底杀灭芽胞作为灭菌指标。"}
            ],
            "hint": "一般消毒只需杀灭繁殖体，而彻底灭菌必须杀灭抵抗力最强的结构。",
            "rationale": "芽胞是生物界抵抗力最强的结构，灭菌的定义是指杀灭物体上所有的微生物（包括抵抗力极强的芽胞）。"
        },

        # --- 多选题 (16~19) ---
        {
            "id": 16,
            "type": "multiple_select",
            "question": "属于所有细菌均具有的“基本结构”包括下列哪些？",
            "options": [
                {"text": "细胞壁", "isCorrect": True, "rationale": "绝大多数细菌均有（支原体除外，常规细菌基本结构含细胞壁）。"},
                {"text": "细胞膜", "isCorrect": True, "rationale": "所有活细胞必需的基本半透膜结构。"},
                {"text": "细胞质（含核糖体）", "isCorrect": True, "rationale": "代谢进行的主要场所。"},
                {"text": "核质（拟核）", "isCorrect": True, "rationale": "细菌遗传信息储存中心。"},
                {"text": "荚膜与芽胞", "isCorrect": False, "rationale": "荚膜和芽胞属于特定细菌才有的特殊结构。"}
            ],
            "hint": "区分四种基本结构与四种特殊结构。",
            "rationale": "细菌的基本结构包括：细胞壁、细胞膜、细胞质和核质；特殊结构包括：荚膜、鞭毛、菌毛和芽胞。"
        },
        {
            "id": 17,
            "type": "multiple_select",
            "question": "下列关于细菌特殊结构及其功能的配对中，正确的有：",
            "options": [
                {"text": "荚膜 —— 抗中性粒细胞和巨噬细胞吞噬", "isCorrect": True, "rationale": "正确。荚膜是强效抗吞噬结构。"},
                {"text": "鞭毛 —— 细菌运动器官，提供趋化动力", "isCorrect": True, "rationale": "正确。鞭毛摆动驱动细菌运动。"},
                {"text": "普通菌毛 —— 特异性黏附于易感组织上皮细胞受体", "isCorrect": True, "rationale": "正确。普通菌毛是重要黏附定植致病因子。"},
                {"text": "性菌毛 —— 介导细菌间接合与质粒DNA水平传递", "isCorrect": True, "rationale": "正确。F性菌毛构建通道传递质粒。"},
                {"text": "芽胞 —— 细菌在适宜环境中迅速进行无丝分裂", "isCorrect": False, "rationale": "错误。芽胞是恶劣环境下的休眠体，非适宜环境下的繁殖。"}
            ],
            "hint": "对照四大特殊结构的生物学功能。",
            "rationale": "荚膜抗吞噬、鞭毛管运动、普通菌毛司黏附、性菌毛司接合；芽胞是恶劣条件下的休眠体。"
        },
        {
            "id": 18,
            "type": "multiple_select",
            "question": "下列关于革兰染色法原理与步骤的描述，正确的有：",
            "options": [
                {"text": "四步流程先后为：初染结晶紫、媒染碘液、脱色95%乙醇、复染稀释复红", "isCorrect": True, "rationale": "正确。经典革兰染色四步法。"},
                {"text": "脱色试剂通常为95%乙醇，是区分两类细菌最关键的一步", "isCorrect": True, "rationale": "正确。脱色步骤决定阳性与阴性的分化。"},
                {"text": "革兰阴性菌由于细胞壁外膜脂质丰富，易被乙醇溶出使孔径扩大", "isCorrect": True, "rationale": "正确。脂质溶解使结晶紫-碘复合物迅速渗漏洗脱。"},
                {"text": "革兰阳性菌细胞壁肽聚糖致密，脱水后孔径收缩阻留紫色复合物", "isCorrect": True, "rationale": "正确。G+脱色后依然保持深紫色。"}
            ],
            "hint": "考查革兰染色的试剂次序与物理化学脱色原理。",
            "rationale": "四个选项均准确概括了革兰染色的核心程序与细胞壁结构响应原理。"
        },
        {
            "id": 19,
            "type": "multiple_select",
            "question": "细菌L型在临床医学中的危害与重要特征包括：",
            "options": [
                {"text": "常规缺乏高渗保护的肉汤中极易破裂死亡，易致检验漏检", "isCorrect": True, "rationale": "正确。需高渗特殊培养基才能检出。"},
                {"text": "天然耐受青霉素、头孢菌素等作用于细胞壁的抗生素", "isCorrect": True, "rationale": "正确。失去药物作用的靶分子（肽聚糖）。"},
                {"text": "在机体高渗区域（如肾髓质）容易形成并长期潜伏", "isCorrect": True, "rationale": "正确。肾髓质高渗利于L型细菌存活。"},
                {"text": "停用抗生素等诱导物后，部分菌株可复原成原菌导致复发", "isCorrect": True, "rationale": "正确。重新合成细胞壁并恢复原毒力。"}
            ],
            "hint": "L型细菌的耐药性、漏检率及复发隐患。",
            "rationale": "细菌L型因缺少细胞壁而在低渗中易裂解导致常规培养漏诊，耐受β-内酰胺类抗生素，易在肾髓质等高渗区潜伏并诱发慢性反复感染。"
        },

        # --- 填空题 (20~21) ---
        {
            "id": 20,
            "type": "fill_blank",
            "question": "革兰阳性菌细胞壁较厚，其特有的抗原成分是（1）____酸；而革兰阴性菌细胞壁外膜最外层则含有特有的（2）____，其脂质A部分具有强烈的内毒素活性。",
            "blankAnswers": [
                "磷壁",
                "脂多糖"
            ],
            "hint": "分别填写G+特有成分与G-内毒素成分。",
            "rationale": "磷壁酸（Teichoic acid）为G+菌特有；脂多糖（LPS）为G-菌特有并构成了内毒素。"
        },
        {
            "id": 21,
            "type": "fill_blank",
            "question": "革兰染色法镜检结果中，革兰阳性菌呈（1）____色，革兰阴性菌呈（2）____色；临床及实验室将杀灭细菌的（3）____作为衡量物理化学灭菌效果是否彻底的最可靠指标。",
            "blankAnswers": [
                "紫",
                "红",
                "芽胞"
            ],
            "hint": "颜色口诀为阳紫阴红；最耐热休眠体结构。",
            "rationale": "革兰染色阳性为紫色，阴性为红色；杀灭抵抗力极强的芽胞是衡量灭菌是否彻底的黄金标准。"
        }
    ]
}
