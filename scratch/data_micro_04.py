# -*- coding: utf-8 -*-
"""
Microbiology Chapter 4: 细菌的遗传与变异
Based strictly on 03-C02细菌学-03细菌的遗传与变异.pdf (Page 2 目录 & Page 65-66 小结与复习题)
"""

DECK_04 = {
    "id": "micro_04",
    "title": "04 细菌的遗传与变异 闪卡",
    "description": "医学微生物学·变异现象（L型/卡介苗/耐药）、质粒特性、噬菌体（溶菌/溶原/溶原性转换）、基因转移四大方式（转化/接合/转导/溶原性转换）核心考点",
    "topics": {
        "covered": [
            "细菌表型变异与基因型变异的本质差异",
            "细菌变异的形态、毒力（卡介苗BCG）与菌落变异（S-R）",
            "质粒（Plasmid）的双链环状特性、分类及非生命必需性",
            "可移动遗传元件（插入序列IS、转座子Tn）",
            "噬菌体分类：毒性噬菌体（溶菌周期/噬斑PFU）与温和噬菌体",
            "前噬菌体、溶原性细菌与溶原性转换经典实例（白喉外毒素）",
            "基因转移四大机制横向深度对比（转化、接合、转导、溶原性转换）",
            "接合作用与性菌毛（F质粒/R质粒扩散）",
            "普遍性转导与局限性转导的机制区别",
            "细菌遗传变异在医学耐药防控与疫苗研发中的意义"
        ],
        "followUp": [
            "细菌外毒素与内毒素的毒力基因调控机制",
            "病毒的基因重组与抗原漂移/抗原转变"
        ]
    },
    "flashcards": [
        {
            "c": 1,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心对比】什么是表型变异（饰变）？与基因型变异有何本质区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **表型变异（饰变）**：在环境因素诱导下细菌形态或生理性状发生暂时性改变，**遗传物质（基因型）没有改变，变异不可遗传**。当外界环境诱因去除后，细菌可迅速完全恢复原状（如葡萄球菌在青霉素诱导下形成L型）。\n2. **基因型变异**：由细菌基因结构发生改变（突变或基因转移重组）所引起，**变异稳定且可代代遗传**，不受环境有无直接逆转（如自发突变产生的链霉素耐药菌株）。"}]},
            "pointType": "概念辨析",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 2,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【毒力变异】卡介苗（BCG）是如何研制成功的？属于细菌的何种变异类型？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **研制历程**：法国科学家卡默特（Calmette）和介兰（Guérin）将毒性强烈的牛型结核分枝杆菌接种在含有**胆汁、甘油、马铃薯**的特制培养基上，历经**13年、连续人工传代培养230代**，获得了丧失致病性但保持极强免疫原性的稳定减毒活疫苗株。\n2. **变异类型**：属于细菌的**毒力基因减毒变异（基因型变异）**，用于人工主动免疫预防结核病。"}]},
            "pointType": "经典疫苗",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 3,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】什么是质粒（Plasmid）？质粒具有哪些关键生物学特性？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：细菌染色体以外的遗传物质，为双链闭环共价闭合的超螺旋DNA分子。\n2. **五大生物学特性**：\n   - **自主复制性**：能独立于染色体进行自我自主复制并稳定分配到子代；\n   - **非生命必需性**：质粒缺失后细菌仍能在普通环境中正常生存繁殖；\n   - **编码特定表型**：编码耐药性（R质粒）、性菌毛（F质粒）、毒力（Vi质粒）、细菌素（Col质粒）等；\n   - **可转移性**：可通过性菌毛接合转移扩散到其他宿主菌中；\n   - **可自发或人工消除**：经溴化乙锭、吖啶橙等处理可彻底消除。"}]},
            "pointType": "物质基础",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 4,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【耐药扩散】什么是耐药质粒（R质粒）？在临床多重耐药性扩散中为何起主导作用？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **结构组成**：R质粒由两部分组成：\n   - **耐药传递因子（RTF）**：编码性菌毛和接合传递功能（类似F质粒）；\n   - **耐药决定子（r-determinant）**：编码多种针对不同抗生素的特异性灭活酶或外排泵。\n2. **临床危害**：R质粒能介导细菌间频繁发生**接合转移**，不仅在同种菌之间传播，还能跨属跨种（如在大肠埃希菌、沙门菌、铜绿假单胞菌间）横向扩散，迅速形成超级多重耐药株。"}]},
            "pointType": "耐药机制",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 5,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【噬菌体分类】毒性噬菌体与温和噬菌体在感染细菌后的结局有何本质不同？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **毒性噬菌体**（Virulent phage）：感染敏感宿主菌后，利用宿主原料迅速复制增殖并合成大量子代病毒，**最终裂解并杀死宿主菌**，在固体平板上裂解细菌形成肉眼可见的透明空斑，称为**噬斑（Plaque，计量单位PFU）**。\n2. **温和噬菌体**（Temperate phage）：感染宿主菌后**不裂解细菌**，其DNA整合到宿主染色体中，成为前噬菌体随细菌染色体同步复制传代，宿主菌正常生长繁殖。"}]},
            "pointType": "噬菌体分类",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 6,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频名词】请解释“前噬菌体”（Prophage）与“溶原性细菌”（Lysogenic bacterium）的概念。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **前噬菌体（Prophage）**：整合到宿主菌染色体上的温和噬菌体基因组DNA。此时噬菌体处于休眠前体状态，不指导合成子代噬菌体颗粒，不引起宿主裂解。\n2. **溶原性细菌（Lysogenic bacterium）**：染色体上整合有前噬菌体基因组的细菌。溶原性细菌对同种噬菌体具有免疫力，但在紫外线或丝裂霉素C诱导下前噬菌体可脱离染色体转入裂解周期。"}]},
            "pointType": "核心名词",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 7,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲黄金考点】什么是溶原性转换（Lysogenic conversion）？请举出白喉棒状杆菌产毒的典型机制。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：当温和噬菌体感染细菌并以前噬菌体形式整合到宿主染色体后，前噬菌体自身携带的基因得到表达，**使宿主菌获得新的生物学性状**的现象。\n2. **白喉棒状杆菌典型机制**：\n   - 无毒的白喉棒状杆菌感染了带有tox基因的**$\\beta$-棒状噬菌体**后，整合成为溶原性细菌；\n   - tox基因在宿主细胞内表达，使无毒菌株转变为能产生剧毒**白喉外毒素**的致病菌株；若前噬菌体丢失，产毒能力随即丧失。"}]},
            "pointType": "黄金考点",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 8,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【基因转移方式】什么是细菌的“转化”（Transformation）？需要具备哪些核心条件？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：供体菌裂解崩解后释放出的**游离裸露DNA片段**，被受体菌直接从周围外环境中摄取，并整合入受体菌基因组实现基因重组的过程。\n2. **必备核心条件**：\n   - **受体菌处于感受态（Competence）**：只有处于生理活性旺盛对数期的受体菌，细胞膜通透性改变、分泌感受态因子时才能摄取外源DNA；\n   - **DNA片段具同源性**：片段大小一般在数千至数万碱基对之间；\n   - 转化过程**完全不需要噬菌体参与，也不需要细菌之间物理直接接触**。"}]},
            "pointType": "基因重组",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 9,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【基因转移方式】什么是细菌的“接合”（Conjugation）？接合传递的物理桥梁与动力是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：供体菌与受体菌通过**直接物理接触**，将质粒或染色体DNA由供体菌单向转移至受体菌的过程。\n2. **物理桥梁**：由供体菌表面生长的**性菌毛（F菌毛）**与受体菌表面受体结合，形成管状接合通道。\n3. **传递动力与过程**：\n   - 供体菌（F+）的质粒DNA双链在复制起点被单链切开，一条链通过接合桥滚环滚入受体菌（F-）；\n   - 供受体双方各自以单链为模板互补合成双链，受体菌（F-）从而转变成具有性菌毛的雄性菌（F+）。"}]},
            "pointType": "基因重组",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 10,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【基因转移方式】什么是细菌的“转导”（Transduction）？其关键介导载体是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：以**噬菌体为载体（媒介）**，将供体菌的DNA片段包裹在噬菌体蛋白质衣壳内，带入受体菌体内并与受体菌染色体进行基因重组的过程。\n2. **关键介导载体**：**噬菌体（Bacteriophage）**。\n3. **核心特征**：转导过程不需要供受体细菌直接物理接触，游离DNA被包裹在噬菌体外壳中能耐受DNA酶（DNase）水解破坏。"}]},
            "pointType": "基因重组",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 11,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【横向对比】普遍性转导（Generalized transduction）与局限性转导（Specialized transduction）有何机制区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "| 比较项目 | 普遍性转导 | 局限性转导 |\n| :--- | :--- | :--- |\n| **转导噬菌体** | 毒性噬菌体或温和噬菌体 | 仅温和噬菌体（溶原性周期） |\n| **发生机制** | 组装时发生“误包”，将切碎的供体染色体DNA误装入头部 | 前噬菌体脱落切离时发生“偏差切离”，带走邻近细菌基因 |\n| **转导的基因** | 供体菌染色体**任意基因片段** | 仅限前噬菌体整合位点**两侧的特定邻近基因**（如大肠杆菌gal或bio基因） |\n| **转导产物** | 完全伪装的假噬菌体（仅含细菌DNA） | 缺陷型重组噬菌体（含噬菌体与宿主杂交DNA） |"}]},
            "pointType": "机制对比",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 12,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【全景总结】请用一张逻辑表横向对比转化、接合、转导、溶原性转换四大基因转移重组机制。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "| 机制类型 | 供体物质形式 | 转移媒介/途径 | 细胞物理接触 | 对DNA酶敏感性 |\n| :--- | :--- | :--- | :--- | :--- |\n| **转化** | 游离裸露DNA片段 | 直接被感受态摄取 | **不需要** | **高度敏感**（被水解） |\n| **接合** | 质粒或染色体DNA | **性菌毛**管道单向转移 | **绝对必需** | 不敏感（管道保护） |\n| **转导** | 供体染色体DNA | **噬菌体衣壳**包裹介导 | **不需要** | 不敏感（衣壳保护） |\n| **溶原性转换** | 前噬菌体自身基因 | 温和噬菌体整合DNA | 不需要 | 不敏感（整合状态） |"}]},
            "pointType": "四大机制总结",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 13,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【跳跃基因】什么是转座子（Transposon，Tn）？与插入序列（IS）有何区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：存在于细菌基因组或质粒上的一段能够从一个基因位点“跳跃、剪切或复制”到另一个新位点的DNA离散片段（转座元件）。\n2. **与插入序列区别**：\n   - **插入序列（IS）**：最小（<2 kb），只编码转座酶和两端反向重复序列（IR），不携带其他表型基因；\n   - **转座子（Tn）**：结构复杂，除转座酶外，还**携带对一种或多种抗生素的耐药基因（如抗氨苄西林、卡那霉素）**，是耐药基因在质粒与染色体间快速转移的关键分子工具。"}]},
            "pointType": "分子结构",
            "starRating": "★★☆",
            "importance": 2
        },
        {
            "c": 14,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【菌落变异】什么是S-R变异（光滑型-粗糙型变异）？在毒力上有何对应变化？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：新分离的野生型致病菌株多为**光滑型（Smooth，S型）菌落**，表面光滑湿润规整；经长期人工体外传代培养后，常丧失表面特异性抗原多糖或外膜O抗原，菌落变为**粗糙型（Rough，R型）**，边缘不整干燥。\n2. **毒力变化**：随着S型向R型变异，细菌丧失了抗吞噬的荚膜或外膜完整LPS，其致病力和**毒力通常显著下降甚至完全丧失**（如肺炎链球菌S型有毒变异为R型无毒）。"}]},
            "pointType": "变异表现",
            "starRating": "★★☆",
            "importance": 2
        },
        {
            "c": 15,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【耐药防控】为什么在临床抗感染治疗中强调必须“足量、足疗程”使用抗菌药物？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **防止筛选自发耐药突变株**：细菌群体中极微小概率（$10^{-6}\\sim 10^{-9}$）存在自发的耐药突变菌；\n2. **避免诱导选择优势**：抗生素并不直接创造耐药突变，而是作为强大的**选择压力**。若药物剂量不足或疗程过短，敏感菌被消灭后，未达致死浓度的突变耐药株得以存活并迅速增殖，取代敏感菌成为优势耐药株，最终导致治疗失败与耐药菌株全院播散。"}]},
            "pointType": "临床用药",
            "starRating": "★★★",
            "importance": 3
        }
    ]
}

QUIZ_04 = {
    "quiz": [
        # --- 单选题 (1~10) ---
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "细菌在抗生素诱导下丢失细胞壁转变为L型细菌，但去除抗生素后又可恢复原细胞壁和毒力。这种变异属于：",
            "options": [
                {"text": "表型变异（饰变）", "isCorrect": True, "rationale": "正确。基因型未发生改变，由环境诱发且可逆，属于表型变异。"},
                {"text": "基因突变", "isCorrect": False, "rationale": "基因突变改变核苷酸序列，具有遗传稳定性。"},
                {"text": "溶原性转换", "isCorrect": False, "rationale": "需要温和噬菌体介导。"},
                {"text": "染色体畸变", "isCorrect": False, "rationale": "不涉及染色体结构不可逆断裂重排。"}
            ],
            "hint": "注意去除诱导因素后能够完全恢复原状且不改变基因型。",
            "rationale": "表型变异受环境影响产生，基因型未变，不具备遗传性，去除环境因素后可恢复原状。"
        },
        {
            "id": 2,
            "type": "multiple_choice",
            "question": "卡介苗（BCG）是预防结核病的常用疫苗，其研制成功利用的是结核分枝杆菌的：",
            "options": [
                {"text": "毒力减毒变异", "isCorrect": True, "rationale": "正确。经胆汁甘油马铃薯培养基传代230代获得稳定减毒株。"},
                {"text": "细菌L型变异", "isCorrect": False, "rationale": "BCG仍保留典型分枝菌酸细胞壁。"},
                {"text": "抗原耐药突变", "isCorrect": False, "rationale": "BCG非抗生素耐药变异。"},
                {"text": "溶原性转换", "isCorrect": False, "rationale": "非噬菌体介导。"}
            ],
            "hint": "丧失了对人类的致病力，但保留了刺激机体产生免疫保护的能力。",
            "rationale": "卡介苗是将牛型结核分枝杆菌在特定培养基上经13年230代人工传代培养获得的毒力变异减毒株。"
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "关于细菌质粒（Plasmid）的生物学特性，下列陈述错误的是：",
            "options": [
                {"text": "是细菌维持基本生命活动必不可少的染色体核心基因", "isCorrect": True, "rationale": "符合题意。质粒非细菌生命所必需，失去质粒细菌仍可存活繁殖！"},
                {"text": "化学本质为共价闭合双链环状DNA分子", "isCorrect": False, "rationale": "叙述正确，质粒为cccDNA。"},
                {"text": "具有独立于宿主染色体的自主复制能力", "isCorrect": False, "rationale": "叙述正确，质粒是独立复制子。"},
                {"text": "可在同种或异种细菌间通过接合等途径发生转移", "isCorrect": False, "rationale": "叙述正确，如R质粒和F质粒的接合传递。"}
            ],
            "hint": "细菌失去了质粒能否正常存活？",
            "rationale": "质粒是染色体外的双链环状DNA，虽然编码耐药性、毒力等附加性状，但绝非细菌维持基本生命活动所必需的基因组结构。"
        },
        {
            "id": 4,
            "type": "multiple_choice",
            "question": "毒性噬菌体感染宿主敏感细菌后，其典型的生活周期表现为：",
            "options": [
                {"text": "迅速复制增殖并裂解杀死宿主菌，释放大量子代噬菌体", "isCorrect": True, "rationale": "正确。毒性噬菌体仅有溶菌周期，最终导致宿主裂解。"},
                {"text": "以噬菌体前体状态整合于染色体长期休眠", "isCorrect": False, "rationale": "这是温和噬菌体的溶原性周期表现。"},
                {"text": "赋予宿主菌合成外毒素的生物学新表型", "isCorrect": False, "rationale": "这是温和噬菌体溶原性转换的特点。"},
                {"text": "与细菌质粒发生重组形成转座子", "isCorrect": False, "rationale": "不属于毒性噬菌体典型结局。"}
            ],
            "hint": "产生透明噬斑、导致细菌细胞膜壁破裂。",
            "rationale": "毒性噬菌体进入菌体后进行复制性增殖，合成大量子代病毒体后裂解细菌释放，在琼脂平板上形成透明噬斑（PFU）。"
        },
        {
            "id": 5,
            "type": "multiple_choice",
            "question": "白喉棒状杆菌只有在感染了携带tox基因的β-棒状噬菌体后，才能产生致命的白喉外毒素。这种遗传变异机制称为：",
            "options": [
                {"text": "溶原性转换（Lysogenic conversion）", "isCorrect": True, "rationale": "正确。温和噬菌体DNA整合使细菌获得产生外毒素新性状，属于经典溶原性转换。"},
                {"text": "转化（Transformation）", "isCorrect": False, "rationale": "转化是受体菌摄取裸露DNA片段。"},
                {"text": "接合（Conjugation）", "isCorrect": False, "rationale": "接合需要性菌毛直接物理接触。"},
                {"text": "转导（Transduction）", "isCorrect": False, "rationale": "转导是噬菌体作为载体搬运供体细菌自身的基因片段。"}
            ],
            "hint": "前噬菌体自身携带的基因表达使细菌获得新致病性状。",
            "rationale": "当温和噬菌体整合到细菌染色体形成前噬菌体后，其自身基因表达导致细菌表型改变（如产生白喉毒素、肉毒毒素），称为溶原性转换。"
        },
        {
            "id": 6,
            "type": "multiple_choice",
            "question": "受体菌直接吸收供体菌裂解释放出的游离裸露DNA片段，并整合入自身基因组的遗传转移方式是：",
            "options": [
                {"text": "转化（Transformation）", "isCorrect": True, "rationale": "正确。吸收裸露外源DNA片段是转化的唯一定义。"},
                {"text": "接合（Conjugation）", "isCorrect": False, "rationale": "接合需要细胞直接接触。"},
                {"text": "转导（Transduction）", "isCorrect": False, "rationale": "转导需要噬菌体衣壳包装。"},
                {"text": "转座（Transposition）", "isCorrect": False, "rationale": "转座是细胞内跳跃移动元件。"}
            ],
            "hint": "直接摄取外界环境中的游离DNA分子。",
            "rationale": "转化（Transformation）是指受体菌在感受态下直接吸收外界环境中供体菌释放的游离DNA分子实现基因重组。"
        },
        {
            "id": 7,
            "type": "multiple_choice",
            "question": "供体菌与受体菌通过性菌毛直接接触传递质粒DNA，如果加入DNA酶（DNase）处理系统，该反应过程：",
            "options": [
                {"text": "完全不受影响，接合传递仍正常进行", "isCorrect": True, "rationale": "正确。接合DNA通过封闭的性菌毛管腔转移，外界DNA酶无法接触降解它。"},
                {"text": "质粒DNA被完全酶解，传递彻底中断", "isCorrect": False, "rationale": "转化过程才会被DNA酶彻底阻断。"},
                {"text": "性菌毛变性脱落", "isCorrect": False, "rationale": "DNA酶不水解蛋白质菌毛。"},
                {"text": "受体菌失去感受态", "isCorrect": False, "rationale": "感受态是转化所需的生理状态，接合不需要感受态。"}
            ],
            "hint": "接合通道是直接物理密封连通的，DNA酶不能穿透。",
            "rationale": "接合依赖性菌毛形成管道传递DNA，不暴露在外界溶液中，因此对DNA酶完全不敏感；而转化中的游离DNA会被DNA酶迅速降解。"
        },
        {
            "id": 8,
            "type": "multiple_choice",
            "question": "噬菌体在装配子代头部时，发生“误包”偶然将供体菌染色体切割下来的任意DNA片段包装入衣壳内，这会导致：",
            "options": [
                {"text": "普遍性转导（Generalized transduction）", "isCorrect": True, "rationale": "正确。误包供体菌任何片段介导的转导为普遍性转导。"},
                {"text": "局限性转导（Specialized transduction）", "isCorrect": False, "rationale": "局限性转导由前噬菌体偏差切离引起，仅转导两侧特定邻近基因。"},
                {"text": "溶原性转换", "isCorrect": False, "rationale": "溶原性转换表达噬菌体自身基因。"},
                {"text": "接合性转位", "isCorrect": False, "rationale": "转位属于转座子功能。"}
            ],
            "hint": "任意基因均可能被错误打包转导。",
            "rationale": "普遍性转导是噬菌体裂解期成熟装配时误将细菌碎裂DNA包装入噬菌体头部形成假噬菌体，能转导供体染色体的任意基因片段。"
        },
        {
            "id": 9,
            "type": "multiple_choice",
            "question": "与普遍性转导不同，局限性转导只能转导前噬菌体整合位点两侧的特定基因，其发生分子机制是：",
            "options": [
                {"text": "前噬菌体从宿主染色体上脱离切离时发生偏差切除（不正常切离）", "isCorrect": True, "rationale": "正确。前噬菌体脱落切离不精确，连带切下两侧邻近基因（如gal或bio）。"},
                {"text": "供体菌在对数期自发发生感受态摄取", "isCorrect": False, "rationale": "感受态为转化机制。"},
                {"text": "性菌毛在转移过程中断裂", "isCorrect": False, "rationale": "属于Hfr接合中断机制。"},
                {"text": "DNA酶选择性水解了非特异性启动子", "isCorrect": False, "rationale": "与限制性核酸内切酶无关。"}
            ],
            "hint": "前噬菌体从宿主染色体上脱落切除时不精确。",
            "rationale": "局限性转导是温和噬菌体在诱导脱离宿主染色体时发生不正常切离，导致前噬菌体一端连接了相邻的宿主基因，故只能转导特定基因。"
        },
        {
            "id": 10,
            "type": "multiple_choice",
            "question": "在遗传结构上，转座子（Transposon，Tn）与插入序列（IS）相比，最核心的区别是转座子携带有：",
            "options": [
                {"text": "与转座酶无关的抗生素耐药基因等其他表型基因", "isCorrect": True, "rationale": "正确。转座子携带有抗生素耐药基因、重金属抗性基因等，IS仅含转座酶基因。"},
                {"text": "编码菌毛蛋白的结构基因", "isCorrect": False, "rationale": "菌毛由质粒或染色体编码。"},
                {"text": "全套完整的衣壳蛋白质基因", "isCorrect": False, "rationale": "衣壳为病毒所有。"},
                {"text": "细胞壁肽聚糖合成酶系", "isCorrect": False, "rationale": "属于常规染色体代谢基因。"}
            ],
            "hint": "转座子携带重要的耐药标记基因。",
            "rationale": "插入序列（IS）仅编码转座酶和反向重复序列；而转座子（Tn）除转座功能外，还携带有与转座无关的抗生素抗性基因等表型标记。"
        },

        # --- 判断题 (11~15) ---
        {
            "id": 11,
            "type": "true_false",
            "question": "质粒不仅能随宿主菌分裂进行复制传代，而且在离开宿主细胞后，依然能独立在培养基中自主复制合成蛋白质。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。质粒离开细菌宿主细胞后就是一段裸露DNA，没有核糖体与酶系，根本无法自主复制！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。质粒依赖宿主细胞的酶系、能量与核糖体才能进行复制和基因表达。"}
            ],
            "hint": "质粒没有细胞结构和代谢系统，离开活细胞能否独立复制？",
            "rationale": "质粒虽然是自主复制子，但必须依赖宿主细胞提供的DNA聚合酶、原料、ATP及核糖体系统才能完成复制和表达。"
        },
        {
            "id": 12,
            "type": "true_false",
            "question": "整合在细菌染色体上的温和噬菌体DNA被称为‘前噬菌体’（Prophage）。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。前噬菌体即整合在染色体上的温和噬菌体基因组。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合前噬菌体的标准定义。"}
            ],
            "hint": "温和噬菌体整合入细菌染色体后的存在状态。",
            "rationale": "前噬菌体是指整合在宿主菌染色体上的温和噬菌体基因组，带有前噬菌体的细菌称为溶原性细菌。"
        },
        {
            "id": 13,
            "type": "true_false",
            "question": "转化作用过程中，受体菌摄取外源游离DNA必须依赖噬菌体的包裹运输保护。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。依赖噬菌体包装的是‘转导’，转化是直接摄取裸露DNA！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。转化不依赖噬菌体，而是受体菌在感受态下直接摄取周围游离DNA。"}
            ],
            "hint": "区分转化（直接摄取裸露DNA）与转导（噬菌体介导）。",
            "rationale": "转化是受体菌直接吸收外界环境中的游离裸露DNA，不需要噬菌体；以噬菌体为介导载体转移基因的方式是转导。"
        },
        {
            "id": 14,
            "type": "true_false",
            "question": "接合作用是通过细菌表面的性菌毛直接物理接触，将质粒由供体菌单向传递给受体菌。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。性菌毛直接物理接触连接是接合传递的标志性特征。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合接合的核心机制。"}
            ],
            "hint": "通过性菌毛直接接触传递DNA。",
            "rationale": "接合（Conjugation）是通过性菌毛使供受体两菌直接接触连接成管道，质粒DNA由此单向传递给受体菌。"
        },
        {
            "id": 15,
            "type": "true_false",
            "question": "抗生素在临床应用中的主要作用是‘诱发’细菌发生特异性的定向耐药突变，而非对抗药菌进行‘选择’。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。抗生素是充当‘环境选择压力’筛选出预先自发存在的耐药突变株！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。基因突变是自发、随机的，抗生素只是定向选择并保留了耐药菌株。"}
            ],
            "hint": "达尔文选择学说：突变是自发的，药物是选择者。",
            "rationale": "现代微生物学证实突变是自发随机产生的，抗生素本身不诱发特异耐药性，而是作为选择压力筛选并扩增了耐药菌。"
        },

        # --- 多选题 (16~19) ---
        {
            "id": 16,
            "type": "multiple_select",
            "question": "下列属于细菌基因间转移与重组的核心机制有：",
            "options": [
                {"text": "转化（Transformation）", "isCorrect": True, "rationale": "摄取游离DNA重组。"},
                {"text": "接合（Conjugation）", "isCorrect": True, "rationale": "性菌毛接触转移质粒。"},
                {"text": "转导（Transduction）", "isCorrect": True, "rationale": "噬菌体为媒介转运基因。"},
                {"text": "溶原性转换（Lysogenic conversion）", "isCorrect": True, "rationale": "温和噬菌体DNA整合表达新性状。"}
            ],
            "hint": "细菌四大基因水平转移与重组途径。",
            "rationale": "细菌基因转移与重组的四种主要方式为：转化、接合、转导和溶原性转换。"
        },
        {
            "id": 17,
            "type": "multiple_select",
            "question": "下列哪些毒素的产生与细菌发生“溶原性转换”密切相关？",
            "options": [
                {"text": "白喉棒状杆菌的白喉外毒素", "isCorrect": True, "rationale": "经典由β-棒状噬菌体介导。"},
                {"text": "肉毒梭菌的肉毒外毒素", "isCorrect": True, "rationale": "肉毒毒素由温和噬菌体溶原性转换控制。"},
                {"text": "A群链球菌的致热外毒素（红疹毒素）", "isCorrect": True, "rationale": "猩红热红疹毒素由前噬菌体编码。"},
                {"text": "大肠埃希菌细胞壁的脂多糖（内毒素）", "isCorrect": False, "rationale": "内毒素是所有G-菌细胞壁固有结构成分，由染色体保守基因合成。"}
            ],
            "hint": "内毒素是染色体编码固有结构，外毒素常由前噬菌体赋予。",
            "rationale": "白喉毒素、肉毒毒素、产气荚膜梭菌毒素及猩红热致热外毒素均由温和前噬菌体携带的毒力基因通过溶原性转换编码合成。"
        },
        {
            "id": 18,
            "type": "multiple_select",
            "question": "耐药质粒（R质粒）在医院感染和细菌耐药扩散中的重要特征包括：",
            "options": [
                {"text": "由耐药传递因子（RTF）和耐药决定子（r-determinant）两部分构成", "isCorrect": True, "rationale": "正确。RTF负责性菌毛接合，r-决定子编码抗药酶。"},
                {"text": "能通过接合作用在同种及异种细菌间高效传播", "isCorrect": True, "rationale": "正确。可在肠道杆菌科等不同属间横向转移。"},
                {"text": "常同时携带针对多种不同类别抗生素的多重耐药基因", "isCorrect": True, "rationale": "正确。导致多重耐药超级细菌产生。"},
                {"text": "质粒DNA与染色体结合后便永远无法人为消除", "isCorrect": False, "rationale": "错误。可用吖啶橙、溴化乙锭等质粒消除剂人工清除。"}
            ],
            "hint": "R质粒的分子结构、接合性及多重耐药特点。",
            "rationale": "R质粒含RTF和r-决定子，常编码多重耐药性，可通过性菌毛在广阔菌群中接合转移，且质粒并非永久结合可被人工消除。"
        },
        {
            "id": 19,
            "type": "multiple_select",
            "question": "下列关于“转化”与“接合”两种机制差异的对比，叙述正确的有：",
            "options": [
                {"text": "转化依赖受体菌处于感受态，接合不需要感受态", "isCorrect": True, "rationale": "正确。感受态是转化的先决条件。"},
                {"text": "转化被外源DNA酶阻断，接合不受DNA酶影响", "isCorrect": True, "rationale": "正确。转化DNA暴露在溶液中，接合DNA在菌毛管道内。"},
                {"text": "接合必须供受体两菌直接物理接触，转化不需要细胞接触", "isCorrect": True, "rationale": "正确。接合需形成性菌毛连接桥。"},
                {"text": "转化只能传递质粒，接合只能传递整个染色体", "isCorrect": False, "rationale": "错误。转化可摄取质粒或染色体片段，接合常传递质粒（如F质粒、R质粒）。"}
            ],
            "hint": "注意两者的媒介、接触要求以及对DNA酶的抵抗情况。",
            "rationale": "转化不需要接触、对DNA酶敏感且需感受态；接合需要性菌毛接触、对DNA酶不敏感且可传递质粒。"
        },

        # --- 填空题 (20~21) ---
        {
            "id": 20,
            "type": "fill_blank",
            "question": "细菌在环境因素影响下发生的暂时、可逆且遗传物质未改变的变异称为（1）____变异；而在特定培养基上传代获得的无毒结核疫苗株卡介苗（BCG）属于（2）____变异。",
            "blankAnswers": [
                "表型",
                "毒力"
            ],
            "hint": "第一空填表型或饰变；第二空填毒力（或基因型）。",
            "rationale": "不可遗传的暂时改变为表型变异（饰变）；卡介苗（BCG）是通过人工长期传代获得的减毒变异株（毒力变异）。"
        },
        {
            "id": 21,
            "type": "fill_blank",
            "question": "整合在宿主菌染色体上的温和噬菌体基因组被称为（1）____；由于其自身基因表达而赋予宿主菌新生物学性状的现象称为（2）____转换。",
            "blankAnswers": [
                "前噬菌体",
                "溶原性"
            ],
            "hint": "Prophage的中文名称；白喉毒素产生的机制名称。",
            "rationale": "整合在宿主染色体上的温和噬菌体称为前噬菌体（Prophage）；其赋予宿主新表型称为溶原性转换（Lysogenic conversion）。"
        }
    ]
}
