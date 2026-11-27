# -*- coding: utf-8 -*-
"""
Microbiology Chapter 6: 病毒的基本性状
Based strictly on 05-C03病毒学-01病毒的基本性状62.pdf page 6 掌握要求
"""

DECK_06 = {
    "id": "micro_06",
    "title": "06 病毒的基本性状 闪卡",
    "description": "医学微生物学·病毒定义与纳米尺度、核衣壳（核心/衣壳对称型）、包膜与乙醚敏感性、复制周期六阶段、异常增殖与理化抵抗力核心考点",
    "topics": {
        "covered": [
            "病毒定义、纳米级超微结构与单一核酸特征",
            "病毒体（Virion）概念与典型形态",
            "核衣壳结构：核心（DNA/RNA）与衣壳（三大对称型）功能",
            "包膜（Envelope）来源、刺突功能与乙醚敏感试验鉴别",
            "病毒复制周期六阶段（吸附、穿入、脱壳、生物合成、组装、释放）",
            "隐蔽期概念、裂解释放与出芽释放对比",
            "异常增殖现象：顿挫感染、缺陷病毒（丁肝依赖乙肝）与干扰现象",
            "温度（56℃ 30min灭活/耐低温冷冻）与化学消毒剂对病毒的影响"
        ],
        "followUp": [
            "病毒的感染类型（急性感染、慢性感染、潜伏感染、慢发病毒感染）",
            "抗病毒固有免疫（干扰素机制）与中和抗体作用"
        ]
    },
    "flashcards": [
        {
            "c": 1,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心定义】什么是病毒（Virus）？其区别于其他微生物的六大独特性状是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：体积极其微小，无细胞结构，仅含一种类型核酸（DNA或RNA），必须在活细胞内专性寄生，以自我复制方式在分子水平上增殖的非细胞型微生物。\n2. **六大独特性状**：\n   - **超显微纳米尺度**：大小以纳米（nm）计，可通过0.22 μm除菌滤器；\n   - **无细胞结构**：缺乏完整的细胞器与能量代谢系统；\n   - **单一核酸**：每种病毒仅含DNA或RNA，二者绝不同时存在；\n   - **分子水平自我复制**：不进行二分裂，以基因复制和蛋白质装配完成增殖；\n   - **严格活细胞内寄生**：在细胞外仅为无生命活性的化学大分子大分子颗粒；\n   - **药物耐受性**：对常规抗生素天然不敏感，但对**干扰素**敏感。"}]},
            "pointType": "核心定义",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 2,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【度量与病毒体】测量病毒大小的单位是什么？什么是“病毒体”（Virion）？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **度量单位**：**纳米（nm）**。绝大多数病毒大小在$20\\sim 300\\,\\text{nm}$之间（如脊髓灰质炎病毒约27 nm，痘病毒约300 nm），必须借助**电子显微镜**才能观察形态。\n2. **病毒体（Virion）**：成熟的、结构完整的、在宿主细胞外具有感染性的**单个病毒颗粒**。是病毒在宿主细胞间传播转移的实体形态。"}]},
            "pointType": "形态概念",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 3,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【基本结构】什么是病毒的“核衣壳”（Nucleocapsid）？核心与衣壳各具有什么功能？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "所有病毒均具有核衣壳基本结构，由两部分组成：\n1. **核心（Core）**：由病毒**核酸（DNA或RNA）**构成，位于中心。\n   - *功能*：储存全部遗传信息，主导病毒的复制、遗传与变异；某些病毒核酸具有单独感染性（感染性核酸）。\n2. **衣壳（Capsid）**：包绕在核酸外围的蛋白质外壳，由壳粒（Capsomere）对称排列而成。\n   - *功能*：保护脆弱的病毒核酸免受核酸酶水解；介导病毒吸附宿主易感细胞表面受体；具有特异免疫原性，刺激机体产生抗体。"}]},
            "pointType": "基本结构",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 4,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【衣壳对称】根据壳粒在空间中的几何排列方式，病毒衣壳可分为哪三种对称型？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **螺旋对称型（Helical symmetry）**：壳粒沿中心核酸长轴呈规则螺旋盘绕包裹，外观呈杆状或丝状（如狂犬病毒、正黏病毒/流感病毒、副黏病毒）；\n2. **20面体立体对称型（Icosahedral symmetry）**：壳粒排列成由20个等边三角形和12个顶角构成的正20面体球状结构（如脊髓灰质炎病毒、腺病毒、单纯疱疹病毒）；\n3. **复合对称型（Complex symmetry）**：既非纯螺旋又非纯20面体，结构复杂或兼具两者的组合形态（如痘病毒呈砖形、T系噬菌体呈蝌蚪状）。"}]},
            "pointType": "对称类型",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 5,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【包膜与刺突】什么是病毒的包膜（Envelope）与刺突（Spike）？其脂溶剂敏感性有何鉴别意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **包膜与刺突**：\n   - **包膜**：包绕在核衣壳外部的脂质双层膜结构，来源于宿主细胞膜或核膜；\n   - **刺突**：镶嵌在包膜表面的病毒编码糖蛋白突起（如流感病毒HA和NA），负责识别结合宿主受体。\n2. **乙醚敏感试验的鉴别意义**：\n   - **有包膜病毒**（流感、新冠、HBV、HIV）：包膜富含脂质，**对乙醚、氯仿等脂溶剂高度敏感**，处理后包膜溶解丧失感染力；\n   - **无包膜裸露病毒**（脊灰病毒、HAV、轮状病毒）：缺乏脂质，**耐受乙醚**处理；\n   - 临床和实验室利用“乙醚敏感试验”作为判定病毒是否存在包膜的经典鉴别手段。"}]},
            "pointType": "包膜特性",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 6,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【增殖机制】简述病毒在活细胞内进行自我复制增殖的“六大连续阶段”。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "病毒复制周期（Replication cycle）按序分为六个阶段：\n1. **吸附（Adsorption）**：病毒表面刺突或衣壳蛋白与宿主细胞表面特异受体特异性结合；\n2. **穿入（Penetration）**：有包膜病毒通过**膜融合**或受体介导胞饮穿入，裸露病毒通过**直接胞饮**进入；\n3. **脱壳（Uncoating）**：在宿主溶酶体酶等作用下脱去衣壳，释放病毒核酸；\n4. **生物合成（Biosynthesis）**：复制子代核酸，转录翻译早期非结构蛋白酶与晚期结构蛋白（此时细胞内检测不到完整病毒，处于**隐蔽期**）；\n5. **组装（Assembly）**：子代核酸与衣壳蛋白装配成子代核衣壳；\n6. **释放（Release）**：无包膜病毒**裂解细胞**释放；有包膜病毒以**出芽方式**穿过细胞膜带走宿主膜脂质释放。"}]},
            "pointType": "复制周期",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 7,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【生化阶段】什么是病毒复制中的“隐蔽期”（Eclipse period）？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：在病毒进入生物合成阶段后，原有的亲代病毒颗粒已经彻底脱壳裂解，而新的子代病毒体尚未组装成熟；\n2. **生物学状态**：在此阶段，若用物理方法人工粉碎宿主细胞，**用显微镜观察或测定感染性，均无法检测到完整的具有感染性的病毒颗粒**，病毒处于隐蔽状态，故称为隐蔽期。\n3. 本期细胞内部正全速进行病毒mRNA转录、非结构蛋白酶翻译以及病毒核酸的指数级分子复制。"}]},
            "pointType": "生化阶段",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 8,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【横向对比】病毒成熟释放的两种主要方式（裂解释放 vs 出芽释放）有何区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **裂解细胞释放（Lysis）**：\n   - **适用对象**：大多数**无包膜裸露病毒**（如脊髓灰质炎病毒、腺病毒）；\n   - **机制与结局**：子代病毒在胞质或核内大量组装积聚，最终直接破坏宿主细胞膜引起**宿主细胞崩解破裂死亡**，病毒瞬间大批涌入胞外。\n2. **出芽释放（Budding）**：\n   - **适用对象**：大多数**有包膜病毒**（如流感病毒、麻疹病毒、HIV）；\n   - **机制与结局**：核衣壳在宿主细胞膜（或核膜）下方聚集，通过顶推局部修饰有病毒糖蛋白刺突的膜向外凸出“出芽”，获得包膜并脱落释放；**宿主细胞在短时间内不立即破裂死亡**，可持续缓慢释放子代病毒。"}]},
            "pointType": "释放方式",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 9,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【异常增殖】什么是病毒的“顿挫感染”（Abortive infection）与非容许细胞？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **非容许细胞（Non-permissive cell）**：缺乏病毒复制所必需的酶系统、tRNA或特定辅助因子的宿主细胞；\n2. **顿挫感染（流产性感染）**：病毒虽然能够吸附并穿入进入非容许细胞，但由于细胞内部缺乏必要生长条件，**病毒不能完成生物合成或不能组装成熟，最终无法产生具有感染性的子代病毒体**。\n3. *(注：侵入能够完整支持病毒增殖并产生感染性后代的细胞称为容许细胞，其感染过程称为容许性感染)*"}]},
            "pointType": "异常增殖",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 10,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频实例】什么是缺陷病毒（Defective virus）？丁型肝炎病毒（HDV）如何依赖乙型肝炎病毒（HBV）增殖？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **缺陷病毒概念**：因自身基因组存在缺陷，缺乏某些必需复制基因，单独感染细胞时**不能独立完成自我复制增殖**的病毒。\n2. **辅助病毒（Helper virus）**：能补充缺陷病毒缺失产物、协助其完成增殖的另一种活病毒。\n3. **HDV依赖HBV实例**：\n   - 丁型肝炎病毒（HDV）为单链环状RNA缺陷病毒，自身无法合成外壳蛋白；\n   - HDV在人体内必须在**乙型肝炎病毒（HBV）共感染或重叠感染**协助下，**借用HBV编码合成的外膜表面抗原（HBsAg）**作为自己的外壳包膜，才能组装成完整具有传染性的成熟HDV颗粒。"}]},
            "pointType": "经典实例",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 11,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【相互作用】什么是病毒的“干扰现象”（Interference）？其发生机制是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：当两种不同病毒同时或先后感染同一种细胞或宿主时，**先感染的前一种病毒能够显著抑制后一种病毒的复制增殖**的生物学现象。\n2. **发生机制**：\n   - **诱导产生干扰素（IFN）**：第一种病毒刺激细胞产生广谱抗病毒物质干扰素，使周围细胞建立抗病毒状态；\n   - **受体竞争与剥夺**：先入病毒占据或破坏了宿主细胞表面的共同吸附受体；\n   - **竞争代谢元件**：先入病毒霸占了宿主细胞的转录复制酶系、核糖体和能量代谢机制。\n3. **医学意义**：可用于疫苗制备防范，或利用弱毒株阻断强毒株感染。"}]},
            "pointType": "干扰现象",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 12,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【理化耐受】温度对病毒的活性有何影响？常规灭活病毒的标准温度与时间是多少？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **耐冷不耐热**：\n   - 病毒在低温（-70℃、-196℃液氮）下极稳定，核酸与包膜不易受损，冷冻干燥后可长期存活保存数年；\n   - 绝大多数病毒对热敏感，高温使衣壳蛋白和刺突变性凝固，丧失吸附穿入能力。\n2. **常规灭活标准**：**56℃加热30分钟**即可使绝大多数人类致病病毒（如流感病毒、冠状病毒、HIV、麻疹病毒）彻底丧失感染性。\n3. *(例外：乙型肝炎病毒HBV抵抗力较强，100℃煮沸需10分钟以上才能完全灭活)*"}]},
            "pointType": "理化因素",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 13,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【理化耐受】常用化学消毒剂与抗生素对病毒的灭活效果如何？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **化学消毒剂**：\n   - **有效杀灭**：氧化剂（过氧乙酸、84次氯酸钠消毒液、过氧化氢）、卤素类（含氯消毒剂、碘伏）、高浓度乙醇（75%）均能高效破坏病毒衣壳蛋白及核酸；\n   - **耐受剂**：病毒对石炭酸（酚类）、甘油等耐受性较强。\n2. **抗生素**：\n   - **完全无效！** 临床常规抗生素（青霉素、头孢菌素、链霉素、红霉素等）靶向细胞壁、70S核糖体，病毒无细胞结构，故**抗生素对病毒毫无抑制或杀灭作用**。"}]},
            "pointType": "消毒用药",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 14,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【遗传变异】什么是流感病毒的“抗原漂移”（Antigenic drift）与“抗原转变”（Antigenic shift）？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "这是流感病毒表面抗原（HA和NA）两种不同维度的变异方式：\n1. **抗原漂移（Antigenic drift）**：\n   - 编码HA或NA的基因发生点突变引起的**轻度量变**，变异幅度小；\n   - 每年流感季节性小流行多由此引起，需每年根据漂移毒株微调流感疫苗组分。\n2. **抗原转变（Antigenic shift）**：\n   - 不同流感病毒亚型在宿主（如猪、禽类）体内发生**基因片段重组**引起的**剧烈质变**，形成全新HA或NA亚型（如H1N1变为H2N2、H3N2）；\n   - 人群普遍缺乏针对新亚型的保护性免疫力，易酿成**全球性流感大流行**。"}]},
            "pointType": "变异机制",
            "starRating": "★★☆",
            "importance": 2
        },
        {
            "c": 15,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【概念辨析】什么是感染性核酸（Infectious nucleic acid）？哪些病毒具有此特性？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：将病毒的蛋白质衣壳彻底去除后，仅将其纯化的裸露游离核酸直接转染进入易感宿主细胞，仍能独立作为模板指导合成全套病毒蛋白，并复制组装产生完整子代感染性病毒颗粒的核酸。\n2. **具有感染性核酸的病毒**：\n   - 主要是**单正链RNA病毒（+ssRNA）**（如脊髓灰质炎病毒、甲型肝炎病毒HAV、冠状病毒）和部分双链DNA病毒（如单纯疱疹病毒HSV、腺病毒）；\n   - *原理*：+ssRNA其碱基序列本身就具备mRNA功能，能直接结合宿主核糖体翻译出病毒聚合酶蛋白启动复制。"}]},
            "pointType": "深度考点",
            "starRating": "★★☆",
            "importance": 2
        }
    ]
}

QUIZ_06 = {
    "quiz": [
        # --- 单选题 (1~10) ---
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "测量病毒体大小最通用的物理计量单位是：",
            "options": [
                {"text": "纳米（nm）", "isCorrect": True, "rationale": "正确。病毒体极微小，测量单位为纳米（nm）。"},
                {"text": "微米（μm）", "isCorrect": False, "rationale": "微米为细菌度量单位。"},
                {"text": "毫米（mm）", "isCorrect": False, "rationale": "毫米用于宏观结构。"},
                {"text": "飞米（fm）", "isCorrect": False, "rationale": "飞米用于亚原子尺度。"}
            ],
            "hint": "1微米等于1000纳米。",
            "rationale": "病毒属于超微结构微生物，绝大多数病毒体大小在20~300 nm之间，度量单位为纳米（nm）。"
        },
        {
            "id": 2,
            "type": "multiple_choice",
            "question": "成熟完备、结构完整、在细胞外具备感染性的单个病毒颗粒称为：",
            "options": [
                {"text": "病毒体（Virion）", "isCorrect": True, "rationale": "正确。病毒体是指结构完整且具备感染性的单个成熟病毒颗粒。"},
                {"text": "前噬菌体（Prophage）", "isCorrect": False, "rationale": "前噬菌体是整合入染色体的温和噬菌体DNA。"},
                {"text": "包涵体（Inclusion body）", "isCorrect": False, "rationale": "包涵体是病毒感染细胞内部形成的嗜酸/嗜碱性斑块。"},
                {"text": "拟核（Nucleoid）", "isCorrect": False, "rationale": "拟核是细菌的原始核结构。"}
            ],
            "hint": "Virion的标准中文译名。",
            "rationale": "病毒体（Virion）特指一个结构完整并具有感染性的成熟病毒颗粒，是病毒在细胞外存在的实体形式。"
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "所有病毒均具备的基本结构核心组件是：",
            "options": [
                {"text": "核衣壳（核心 + 衣壳）", "isCorrect": True, "rationale": "正确。核衣壳由内部核酸核心与外围蛋白质衣壳组成，是所有病毒共有的基本结构。"},
                {"text": "包膜与刺突", "isCorrect": False, "rationale": "包膜仅存在于有包膜病毒中，无包膜病毒（裸露病毒）缺乏包膜。"},
                {"text": "70S核糖体", "isCorrect": False, "rationale": "病毒无细胞器，不含核糖体。"},
                {"text": "拟核与质粒", "isCorrect": False, "rationale": "属于细菌原核细胞结构。"}
            ],
            "hint": "由核酸与包绕其外的蛋白质外壳组合而成。",
            "rationale": "病毒的基本结构是核衣壳，由核心（核酸）和衣壳（蛋白质）组成；包膜属于辅助结构，并非所有病毒均具备。"
        },
        {
            "id": 4,
            "type": "multiple_choice",
            "question": "狂犬病毒外形呈弹状，其衣壳壳粒沿中心核酸长轴呈规则螺旋盘旋包裹，这种衣壳对称类型称为：",
            "options": [
                {"text": "螺旋对称型", "isCorrect": True, "rationale": "正确。呈螺旋管状排列包裹核酸属于螺旋对称。"},
                {"text": "20面体立体对称型", "isCorrect": False, "rationale": "20面体呈正多面球形结构。"},
                {"text": "复合对称型", "isCorrect": False, "rationale": "复合对称见于痘病毒或蝌蚪状噬菌体。"},
                {"text": "无规则多形对称型", "isCorrect": False, "rationale": "病毒衣壳排列高度规则，无此分类。"}
            ],
            "hint": "沿长轴像弹簧一样螺旋盘绕。",
            "rationale": "螺旋对称型是指壳粒紧贴核酸呈螺旋盘旋排列，整体呈长圆柱状或弹状，狂犬病毒、正黏病毒等属于此类。"
        },
        {
            "id": 5,
            "type": "multiple_choice",
            "question": "临床微生物实验室中，用于快速鉴别某种未知病毒表面是否覆盖有“包膜”的经典实验方法是：",
            "options": [
                {"text": "乙醚敏感试验", "isCorrect": True, "rationale": "正确。乙醚为脂溶剂，能迅速溶解包膜使有包膜病毒失去感染力，无包膜病毒耐受乙醚。"},
                {"text": "革兰染色法", "isCorrect": False, "rationale": "革兰染色用于鉴别细菌细胞壁。"},
                {"text": "甘露糖敏感性血凝试验", "isCorrect": False, "rationale": "用于鉴别细菌菌毛类型。"},
                {"text": "抗酸染色法", "isCorrect": False, "rationale": "用于分枝杆菌鉴定。"}
            ],
            "hint": "利用脂溶剂溶解包膜中的脂双层成分。",
            "rationale": "包膜主要成分是脂双层，对乙醚等脂溶剂极敏感；经乙醚处理后感染性丧失者为有包膜病毒，保持感染性者为无包膜病毒。"
        },
        {
            "id": 6,
            "type": "multiple_choice",
            "question": "在病毒的自我复制周期中，下列哪一阶段在受染宿主细胞内用显微镜或常规检测手段均无法查见具有感染性的成熟病毒颗粒？",
            "options": [
                {"text": "生物合成期（隐蔽期）", "isCorrect": True, "rationale": "正确。此时母代病毒脱壳裂解，子代尚未组装成熟，处于隐蔽期。"},
                {"text": "吸附期", "isCorrect": False, "rationale": "吸附期母代完整病毒体清晰附着于细胞膜表面。"},
                {"text": "穿入期", "isCorrect": False, "rationale": "穿入期完整病毒颗粒正通过膜融合或吞饮进入胞质。"},
                {"text": "释放期", "isCorrect": False, "rationale": "释放期有大量具有完全感染力的子代病毒颗粒涌出。"}
            ],
            "hint": "脱壳后、组装前，病毒以核酸和游离蛋白质分子形式分散在细胞内。",
            "rationale": "脱壳后病毒进入生物合成阶段，此期细胞内不存在完整的病毒颗粒，检测不到感染性，称为隐蔽期（Eclipse period）。"
        },
        {
            "id": 7,
            "type": "multiple_choice",
            "question": "关于大多数有包膜病毒（如流感病毒、HIV）成熟释放的典型方式，下列叙述正确的是：",
            "options": [
                {"text": "以“出芽”方式穿过宿主修饰膜释放，宿主细胞可在一定时期内保持存活", "isCorrect": True, "rationale": "正确。有包膜病毒主要通过出芽释放获得包膜，对宿主破坏缓慢。"},
                {"text": "瞬间强力裂解破裂宿主细胞，导致宿主细胞迅速自溶死亡", "isCorrect": False, "rationale": "这是无包膜裸露病毒（如脊灰病毒）的释放方式。"},
                {"text": "通过性菌毛管道单向传递至相邻易感细胞", "isCorrect": False, "rationale": "这是细菌接合机制。"},
                {"text": "仅在宿主细胞发生凋亡后才被巨噬细胞被动释放", "isCorrect": False, "rationale": "出芽是病毒的主动释放过程。"}
            ],
            "hint": "包膜通常是在穿过宿主细胞膜向外突出包裹时获得的。",
            "rationale": "有包膜病毒多通过出芽（Budding）方式成熟释放，出芽时带走宿主细胞膜脂质并镶嵌病毒糖蛋白刺突，宿主细胞常不立即裂解。"
        },
        {
            "id": 8,
            "type": "multiple_choice",
            "question": "丁型肝炎病毒（HDV）自身无法独立合成外壳包膜蛋白，必须在下列哪种病毒的辅助协助下才能组装成完整具有传染性的病毒体？",
            "options": [
                {"text": "乙型肝炎病毒（HBV）", "isCorrect": True, "rationale": "正确。HDV是缺陷病毒，依赖HBV提供的HBsAg包装其核衣壳。"},
                {"text": "甲型肝炎病毒（HAV）", "isCorrect": False, "rationale": "HAV为无包膜肠道微小RNA病毒。"},
                {"text": "丙型肝炎病毒（HCV）", "isCorrect": False, "rationale": "HCV与HDV无装配辅助关系。"},
                {"text": "单纯疱疹病毒（HSV）", "isCorrect": False, "rationale": "非嗜肝辅助病毒。"}
            ],
            "hint": "HDV必须借用哪种肝炎病毒的表面抗原（HBsAg）？",
            "rationale": "HDV属于缺陷病毒，其基因组仅编码内层核心抗原，必须借用乙型肝炎病毒（HBV）合成的外膜表面抗原（HBsAg）才能完成组装成熟。"
        },
        {
            "id": 9,
            "type": "multiple_choice",
            "question": "两种不同病毒同时或先后感染同一细胞时，常发生先感染病毒抑制后感染病毒复制的“干扰现象”，其主要机制不包括：",
            "options": [
                {"text": "第一种病毒刺激宿主细胞合成分泌具有广谱抗病毒作用的干扰素（IFN）", "isCorrect": False, "rationale": "这是干扰现象的主要内源性机制。"},
                {"text": "第一种病毒占据或破坏了宿主细胞表面的共同吸附受体", "isCorrect": False, "rationale": "这是受体竞争机制。"},
                {"text": "第一种病毒在细胞内竞争性霸占了宿主的转录核糖体与能量系统", "isCorrect": False, "rationale": "这是代谢原料抢夺机制。"},
                {"text": "第一种病毒在细胞质内合成分泌高效青霉素水解了后入病毒的细胞壁", "isCorrect": True, "rationale": "符合题意。病毒根本没有细胞壁，更不会产生青霉素！"}
            ],
            "hint": "注意病毒无细胞壁，抗生素相关机制纯属荒谬选项。",
            "rationale": "干扰现象机制包括产生干扰素、占据受体位点、竞争复制酶系与核糖体等；病毒不含细胞壁，不产生抗生素。"
        },
        {
            "id": 10,
            "type": "multiple_choice",
            "question": "绝大多数人类致病性病毒对高温较为敏感，在实验室和临床血清样本前处理中，灭活大多数普通病毒的标准加热条件通常为：",
            "options": [
                {"text": "56℃ 加热 30 分钟", "isCorrect": True, "rationale": "正确。56℃ 30 min是临床和实验室灭活病毒的标准水浴条件。"},
                {"text": "37℃ 孵育 1 小时", "isCorrect": False, "rationale": "37℃是病毒最适生长温度，不能灭活。"},
                {"text": "100℃ 煮沸 2 小时", "isCorrect": False, "rationale": "破坏过度会使血清蛋白质严重变性凝块。"},
                {"text": "0℃ 冰浴 24 小时", "isCorrect": False, "rationale": "低温不仅不灭活，反而完美保存病毒。"}
            ],
            "hint": "56度半小时，经典灭活参数。",
            "rationale": "绝大多数病毒耐冷不耐热，56℃加热30分钟能使病毒衣壳或包膜刺突蛋白变性，使其丧失感染力，是常规灭活参数。"
        },

        # --- 判断题 (11~15) ---
        {
            "id": 11,
            "type": "true_false",
            "question": "病毒体内同时含有DNA和RNA两种核酸分子，通过二分裂方式独立进行能量代谢和增殖。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。病毒仅含DNA或RNA一种核酸，且以自我复制方式在宿主细胞内增殖！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。病毒只有单一核酸，无二分裂繁殖，无独立能量代谢。"}
            ],
            "hint": "病毒是一类单一核酸、严格活细胞内自我复制的微生物。",
            "rationale": "病毒体内绝不兼有DNA和RNA，每种病毒仅含一种核酸，增殖方式为在分子水平上的自我复制组装，不进行二分裂。"
        },
        {
            "id": 12,
            "type": "true_false",
            "question": "由于无包膜的裸露病毒缺乏脆弱的脂质双层外壳，因此这类病毒通常比有包膜病毒对乙醚、酸性胃液及干燥环境更具抵抗力。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。裸露病毒耐乙醚、耐酸耐干燥（如肠道病毒耐胃酸与胆汁经粪-口传播）。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合裸露病毒的高物理化学抵抗力规律。"}
            ],
            "hint": "无包膜裸露病毒（如HAV、脊灰病毒）能否经受胃酸穿过消化道？",
            "rationale": "无包膜病毒衣壳由紧密蛋白质构成，对脂溶剂、干燥和酸碱抵抗力显著强于有包膜病毒，因此多数能耐受胃酸通过消化道传播。"
        },
        {
            "id": 13,
            "type": "true_false",
            "question": "在病毒自我复制的隐蔽期，如果将受染宿主细胞人工强行裂解研碎，提取物中依然可以检测到大量具有完全感染力的子代病毒体。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。隐蔽期亲代已脱壳，子代未组装，完全检测不到具有感染力的完整病毒颗粒！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。隐蔽期细胞内只有游离核酸和蛋白质原料，无完整感染性病毒体。"}
            ],
            "hint": "隐蔽期之所以叫‘隐蔽’，正是因为测不出成熟病毒颗粒。",
            "rationale": "隐蔽期亲代病毒衣壳已脱去，子代病毒尚在生物合成游离核酸和多肽阶段，尚未装配成核衣壳，故无法检测到感染性病毒颗粒。"
        },
        {
            "id": 14,
            "type": "true_false",
            "question": "病毒在零下70℃超低温或液氮中极度稳定，其感染性可长期保存数年而不丧失。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。病毒耐冷不耐热，超低温是长期保存毒株的标准手段。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合病毒冷冻保存的物理特性。"}
            ],
            "hint": "实验室保存毒株通常放在-80℃超低温冰箱或液氮罐中。",
            "rationale": "病毒对低温抵抗力极强，在-70℃甚至-196℃液氮环境中，蛋白质与核酸分子活动处于休眠凝固状态，可长年保持感染活力。"
        },
        {
            "id": 15,
            "type": "true_false",
            "question": "青霉素和头孢菌素等抗生素能够强效水解病毒表面的蛋白质衣壳，因此可作为治疗急性普通病毒感染的首选用药。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。抗生素靶向细菌细胞壁或核糖体，对病毒完全无效！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。抗生素对病毒毫无抑制或破坏作用，滥用抗生素治疗病毒性感冒是错误的医疗行为。"}
            ],
            "hint": "抗生素能否杀灭病毒？",
            "rationale": "常规抗生素只作用于细胞壁肽聚糖合成、70S核糖体蛋白质翻译等细胞特有靶点，病毒缺乏这些结构，因此抗生素对病毒完全无效。"
        },

        # --- 多选题 (16~19) ---
        {
            "id": 16,
            "type": "multiple_select",
            "question": "关于病毒核衣壳中“衣壳”的生物学功能，描述正确的有：",
            "options": [
                {"text": "保护包裹在内部的病毒核酸免遭环境中核酸酶的水解破坏", "isCorrect": True, "rationale": "正确。物理化学保护屏障。"},
                {"text": "无包膜病毒的衣壳表面蛋白介导识别与吸附易感宿主细胞受体", "isCorrect": True, "rationale": "正确。负责介导感染启动。"},
                {"text": "具有特异免疫原性，能刺激机体免疫系统产生中和抗体", "isCorrect": True, "rationale": "正确。衣壳蛋白是主要抗原成分。"},
                {"text": "为病毒在细胞外的独立存活提供ATP能量代谢合成途径", "isCorrect": False, "rationale": "错误。衣壳无能量代谢酶系。"}
            ],
            "hint": "衣壳的三大功能：保护核酸、介导吸附、免疫原性。",
            "rationale": "衣壳具有保护核酸、介导特异性吸附受体以及作为特异性抗原刺激机体产生体液免疫的三大关键功能。"
        },
        {
            "id": 17,
            "type": "multiple_select",
            "question": "下列关于病毒增殖过程的描述，正确的有：",
            "options": [
                {"text": "增殖方式为在分子水平上进行的自我复制，不进行无性二分裂", "isCorrect": True, "rationale": "正确。自我复制是病毒增殖标志。"},
                {"text": "吸附阶段病毒表面蛋白与易感细胞表面受体发生特异性结合", "isCorrect": True, "rationale": "正确。决定组织亲嗜性。"},
                {"text": "脱壳是指在宿主细胞溶酶体等酶类作用下脱除蛋白质外壳", "isCorrect": True, "rationale": "正确。释放核酸启动合成。"},
                {"text": "生物合成期包括子代核酸复制与结构蛋白、非结构蛋白合成", "isCorrect": True, "rationale": "正确。全套组件在胞内分别合成。"}
            ],
            "hint": "病毒自我复制六阶段的基本生理步骤。",
            "rationale": "四个选项准确概括了病毒以核酸复制为核心、经过吸附穿入脱壳合成组装释放的自我增殖规律。"
        },
        {
            "id": 18,
            "type": "multiple_select",
            "question": "下列属于病毒异常增殖或特殊相互作用现象的有：",
            "options": [
                {"text": "顿挫感染（侵入非容许细胞导致不能产生成熟子代病毒）", "isCorrect": True, "rationale": "正确。流产性感染。"},
                {"text": "缺陷病毒（基因组不完整，需辅助病毒协助增殖）", "isCorrect": True, "rationale": "正确。如丁型肝炎病毒HDV。"},
                {"text": "干扰现象（先入病毒抑制后入病毒的增殖）", "isCorrect": True, "rationale": "正确。通过干扰素或受体竞争等途径发生。"},
                {"text": "芽胞休眠（病毒在恶劣环境中形成耐热性芽胞颗粒）", "isCorrect": False, "rationale": "错误。芽胞是革兰阳性细菌特有的结构，病毒根本不形成芽胞！"}
            ],
            "hint": "芽胞是细菌的结构，绝对不属于病毒。",
            "rationale": "顿挫感染、缺陷病毒和干扰现象是病毒学三大经典异常增殖与相互作用形式；芽胞属于特定细菌的休眠体。"
        },
        {
            "id": 19,
            "type": "multiple_select",
            "question": "下列理化因素中，能够有效灭活大多数普通人类致病病毒的有：",
            "options": [
                {"text": "56℃ 加热处理 30 分钟", "isCorrect": True, "rationale": "正确。标准灭活温度。"},
                {"text": "含氯消毒剂（如次氯酸钠/84消毒液）", "isCorrect": True, "rationale": "正确。强氧化作用破坏核酸与蛋白。"},
                {"text": "体外照射波长 265 nm 的紫外线", "isCorrect": True, "rationale": "正确。破坏病毒核酸形成二聚体。"},
                {"text": "高浓度广谱青霉素与链霉素混合液", "isCorrect": False, "rationale": "错误。抗生素对病毒毫无灭活效果！"}
            ],
            "hint": "区分物理化学消毒法与对病毒无效的抗细菌抗生素。",
            "rationale": "高温热力、次氯酸钠强氧化剂及紫外线照射能破坏病毒蛋白衣壳与核酸从而有效灭活病毒；抗生素对病毒无效。"
        },

        # --- 填空题 (20~21) ---
        {
            "id": 20,
            "type": "fill_blank",
            "question": "所有病毒都必须具备的基本结构是（1）____，它由内部的核心核酸与外周由蛋白质构成的（2）____紧密组合而成。",
            "blankAnswers": [
                "核衣壳",
                "衣壳"
            ],
            "hint": "第一空填写基本结构统称；第二空填写外周蛋白质外壳。",
            "rationale": "病毒的基本结构是核衣壳（Nucleocapsid），由核心（Core，核酸）与包绕在外的衣壳（Capsid，蛋白质）组成。"
        },
        {
            "id": 21,
            "type": "fill_blank",
            "question": "有包膜病毒对乙醚等脂溶剂高度（1）____，而无包膜的裸露病毒对乙醚则表现为（2）____；丁型肝炎病毒（HDV）由于自身缺乏外壳基因，必须依赖（3）____型肝炎病毒协助提供包膜表面抗原才能组装成熟。",
            "blankAnswers": [
                "敏感",
                "耐受",
                "乙"
            ],
            "hint": "第一空填敏感；第二空填耐受（或耐药/抵抗）；第三空填乙（HBV）。",
            "rationale": "有包膜病毒对脂溶剂敏感，无包膜裸露病毒耐受乙醚；丁型肝炎病毒为缺陷病毒，必须在乙型肝炎病毒（HBV）协助下增殖。"
        }
    ]
}
