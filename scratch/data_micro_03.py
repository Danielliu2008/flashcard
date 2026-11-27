# -*- coding: utf-8 -*-
"""
Microbiology Chapter 3: 细菌的生理
Based strictly on 02-C02细菌学-02细菌的生理(1).pdf page 3 掌握要求
"""

DECK_03 = {
    "id": "micro_03",
    "title": "03 细菌的生理 闪卡",
    "description": "医学微生物学·细菌物理性状、营养与生长繁殖条件、生长曲线四期、代谢产物（热原质/毒素）、人工培养与消毒灭菌法核心考点",
    "topics": {
        "covered": [
            "细菌表面积、带电性（生理pH带负电）与渗透压",
            "细菌营养物质、摄取机制与气体生长类型",
            "细菌二分裂繁殖与生长曲线四大分期特征",
            "对数期（形态典型/药敏最高）与稳定期（产毒素/抗生素/芽胞）",
            "细菌分解产物（IMViC试验）与合成产物（热原质/毒素/色素）",
            "热原质耐热性机制与无热原纯化方法",
            "固体（菌落）、液体与半固体培养基动力学观察",
            "灭菌、消毒、无菌、无菌操作与防腐概念辨析",
            "高压蒸汽灭菌（121℃ 15-20min）、紫外线（TT二聚体）与滤过除菌"
        ],
        "followUp": [
            "细菌耐药质粒在菌群间的接合传递",
            "内毒素与外毒素在宿主体内引起的免疫应答"
        ]
    },
    "flashcards": [
        {
            "c": 1,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【物理性状】在正常生理酸碱度（pH 7.2~7.6）环境下，细菌表面通常带有何种电荷？对染色有何指导意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **带电状态**：细菌的等电点通常在pH 2~5之间。在生理pH（7.2~7.6）的中性或弱碱性溶液中，**细菌解离后表面均带有负电荷**。\n2. **染色意义**：由于表面带负电荷，细菌对解离后带正电荷的**碱性染料（如结晶紫、美蓝、碱性复红）亲和力最强**，故细菌学常规涂片染色均选用碱性染料。"}]},
            "pointType": "物理性状",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 2,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【生长环境】根据对分子氧的需求与耐受能力，细菌可分为哪四种气体类型？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **专性需氧菌**（Obligate aerobe）：必须在有氧环境中生长，含超氧化物歧化酶（SOD）和过氧化氢酶（如结核分枝杆菌）；\n2. **微需氧菌**（Microaerophile）：仅在低氧分压（5%~6% O2）下生长（如幽门螺杆菌、空肠弯曲菌）；\n3. **兼性厌氧菌**（Facultative anaerobe）：有氧或无氧均能良好增殖，大多数医学致病菌属于此类（如大肠埃希菌、金黄色葡萄球菌）；\n4. **专性厌氧菌**（Obligate anaerobe）：只能在无氧环境中生存，缺乏SOD和过氧化氢酶，遇氧易被超氧阴离子毒死（如破伤风梭菌、脆弱拟杆菌）。"}]},
            "pointType": "气体类型",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 3,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】将少量细菌接种至新鲜液体培养基中，其生长曲线分为哪四个主要时期？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "生长曲线按时间顺序分为：\n1. **迟缓期（适应期）**：细菌适应新环境，代谢极其活跃，合成大量酶，菌体增大，但**细菌数量几乎不增加**；\n2. **对数期（指数生长期）**：繁殖速度最快，活菌数呈几何级数增长，**形态、染色性与生理活性最典型，对抗菌药物最敏感**；\n3. **稳定期**：营养减少、代谢产物堆积，活菌数达到最高峰并保持动态平衡，**大量产生外毒素、抗生素、热原质及芽胞**；\n4. **衰亡期**：营养枯竭毒素蓄积，死亡数显著超过活菌数，菌体出现多形畸形或自溶。"}]},
            "pointType": "核心曲线",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 4,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频考点】在进行细菌形态学观察和抗生素药物敏感性试验时，应选用生长曲线哪一时期的细菌？为什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **选用时期**：**对数期（Logarithmic phase）**（通常在接种后8~18小时）。\n2. **核心原因**：\n   - 处于对数期的细菌生理机能最旺盛，代谢状态均一稳定；\n   - 菌体大小、形态最为规整，革兰染色特性最标准、最典型；\n   - 细菌分裂旺盛，对外界环境因子及青霉素等各类抗菌药物的**敏感性最高**，药敏试验结果最准确可靠。"}]},
            "pointType": "实验依据",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 5,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频考点】细菌产生芽胞、外毒素、抗生素等重要生物合成产物主要集中在生长曲线的哪个时期？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **集中时期**：**稳定期（Stationary phase）**。\n2. **生物学背景**：\n   - 稳定期活菌总数达到峰值，环境营养相对受限，初级代谢放缓，促使细菌激活次级代谢合成途径；\n   - 细菌合成产生**外毒素、抗生素、细菌素、热原质、色素**，产芽胞细菌也在此期大量形成耐热**芽胞**。"}]},
            "pointType": "高频考点",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 6,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【鉴别试验】什么是IMViC试验？在肠道杆菌鉴别中有何典型意义？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：由四个生化鉴别试验首字母缩写组成：\n   - **I**：吲哚试验（Indole test）\n   - **M**：甲基红试验（Methyl red test）\n   - **Vi**：V-P试验（Voges-Proskauer test）\n   - **C**：枸橼酸盐利用试验（Citrate utilization test）\n2. **鉴别意义**：\n   - **大肠埃希菌**（典型非致病菌）：结果为 **“+ + - -”**；\n   - **产气肠杆菌**（常见医院感染菌）：结果为 **“- - + +”**。\n   - 是鉴别水质、食品粪便污染及肠道杆菌科菌属的关键生化组合。"}]},
            "pointType": "生化试验",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 7,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【药剂安全】什么是热原质（Pyrogen）？其化学本质是什么？有何物理耐受特性？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：大多数革兰阴性菌在生长代谢过程中产生并释放到菌体外的一种能引起宿主恒温动物体温显著升高的致热物质。\n2. **化学本质**：即革兰阴性菌细胞壁外膜的**脂多糖（LPS/内毒素）**。\n3. **耐热特性**：**耐热性极强**，常规高压蒸汽灭菌（121℃ 20 min）及煮沸消毒完全无法将其破坏分解。通常需经**180℃干烤3~4小时**或**250℃干烤30~45分钟**才能彻底破坏破坏。\n4. **制药防范**：临床注射用水必须采用**重蒸馏法**或微孔活性炭吸附除热原，防止发生严重的输液发热反应。"}]},
            "pointType": "重点概念",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 8,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【人工培养】细菌在液体、固体和半固体培养基中分别表现出哪些典型生长现象？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **液体培养基**：\n   - **均匀浑浊生长**：大多数兼性厌氧菌（大肠埃希菌）；\n   - **沉淀生长**：链状生长细菌在管底形成颗粒状沉淀（化脓性链球菌）；\n   - **菌膜生长**：专性需氧菌在液面形成厚菌膜（结核分枝杆菌、枯草芽胞杆菌）。\n2. **固体培养基（琼脂2%）**：\n   - 单个菌体经分裂繁殖形成肉眼可见的子细胞集团，称为**菌落（Colony）**；连成一片称为菌苔。\n3. **半固体培养基（琼脂0.3%~0.5%）**：\n   - **检测细菌动力**：有鞭毛运动菌在穿刺线周围呈云雾羽毛状浑浊扩散；无动力菌仅沿穿刺线呈清晰细线状生长。"}]},
            "pointType": "生长现象",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 9,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲辨析】请准确区分“灭菌”、“消毒”、“无菌”、“无菌操作”与“防腐”五大术语。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **灭菌**（Sterilization）：杀灭或清除物体上**所有微生物（包括耐热芽胞和繁殖体）**的最高理化标准；\n2. **消毒**（Disinfection）：杀灭物体上的**病原微生物**，不一定能杀灭细菌芽胞或非致病微生物；\n3. **无菌**（Asepsis）：完全不存在任何活的微生物（繁殖体与芽胞均无）；\n4. **无菌操作**（Aseptic technique）：在医疗、手术或微生物实验中，防止微生物进入人体或污染操作环境的规范流程；\n5. **防腐**（Antisepsis）：防止或**抑制微生物生长繁殖**（不一定杀死微生物），去除防腐剂后微生物仍可恢复生长。"}]},
            "pointType": "五大术语",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 10,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【灭菌王牌】简述高压蒸汽灭菌法（Autoclaving）的温度、压力、时间参数及应用范围。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **工作参数**：蒸汽压力为**$103.4\\,\\text{kPa}$（$1.05\\,\\text{kg/cm}^2$）**，温度达到**$121.3^\\circ\\text{C}$**，维持**15~20分钟**。\n2. **核心地位**：湿热灭菌中杀菌穿透力最强、作用最可靠、灭菌最彻底的黄金首选方法，可100%杀灭一切微生物包括细菌芽胞。\n3. **适用范围**：耐高温、耐湿热的物品（手术器械、敷料、生理盐水、普通培养基、橡胶手套等）。*(注：凡遇湿热易变质破坏的血清、抗生素药液不可用)*"}]},
            "pointType": "核心灭菌",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 11,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【物理消毒】紫外线（UV）杀菌的最适波长是多少？其杀菌机制与最大局限性是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **最适波长**：**265~266 nm**（与DNA最大吸收峰260 nm高度吻合）。\n2. **杀菌机制**：紫外线照射破坏细菌DNA结构，促使DNA链中相邻的胸腺嘧啶形成**胸腺嘧啶二聚体（TT二聚体）**，严重干扰DNA复制与转录，导致细菌死亡或突变。\n3. **局限性**：**穿透力极差**，甚至无法穿透普通玻璃、纸张或薄尘，故**仅适用于空气消毒及不耐热平滑物体表面消毒**。"}]},
            "pointType": "物理消毒",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 12,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【物理除菌】滤过除菌法（Filtration）常用的微孔滤膜孔径是多少？主要适用于哪些物品？能除病毒吗？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **常用孔径**：**$0.22\\,\\mu\\text{m}$**（或$0.45\\,\\mu\\text{m}$）。常规细菌大小通常$>0.5\\,\\mu\\text{m}$，故可截留所有细菌。\n2. **适用范围**：不耐高温热敏性溶液的除菌（如人血清、血浆、抗毒素、抗生素药液、维生素溶液及液体培养基原料）。\n3. **能除病毒吗**：**不能！** 病毒体积极小（20~300 nm），能自由通过$0.22\\,\\mu\\text{m}$滤膜；支原体亦有部分可能穿过。"}]},
            "pointType": "滤过除菌",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 13,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【化学消毒】乙醇（酒精）杀菌的最适浓度是多少？为什么100%无水乙醇反而不是最佳杀菌浓度？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **最适浓度**：**70%~75%（常用75%）**。\n2. **为什么不是无水乙醇**：\n   - 95%或100%的高浓度乙醇接触细菌后，因极强脱水性会使细菌表层蛋白质**瞬间极速凝固**，在菌体外围形成一层致密坚固的保护硬膜，反而阻碍乙醇分子进一步深入菌体内层，内部细菌仍可存活；\n   - 75%乙醇能均匀渗透扩散至菌体内部，彻底使细菌全细胞蛋白质变性凝固并溶解细胞膜，杀菌效果最好。"}]},
            "pointType": "消毒机制",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 14,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【培养基类型】什么是选择培养基和鉴别培养基？请各举一例说明。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **选择培养基**：根据某类细菌特殊生长需要或耐药性，在培养基中加入特定抑制剂抑制非目的菌生长，仅允许目标致病菌增殖。\n   - *例*：**SS琼脂（沙门-志贺菌琼脂）**，加入胆盐和煌绿抑制革兰阳性菌和大肠杆菌，利于分离肠道沙门菌和志贺菌。\n2. **鉴别培养基**：在培养基中加入特定底物糖类及酸碱指示剂，利用不同细菌分解底物产酸产气差异呈现不同菌落颜色，用于肉眼鉴别诊断。\n   - *例*：**伊红美蓝培养基（EMB）**，大肠埃希菌分解乳糖产强酸，与染料结合形成典型黑色金属光泽菌落。"}]},
            "pointType": "培养基分类",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 15,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【色素鉴别】铜绿假单胞菌与金黄色葡萄球菌产生的色素在溶解性上有何重要区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **铜绿假单胞菌（绿脓杆菌）**：产生**水溶性色素**（绿脓素pyocyanin与荧光素）。色素能自由弥散渗入周围培养基或宿主敷料创面中，使整个培养基或脓液染成鲜艳蓝绿色。\n2. **金黄色葡萄球菌**：产生**脂溶性色素**。色素不溶于水，仅牢固沉积在菌落本身细胞内，使菌落呈金黄色，而周围培养基颜色保持不变。"}]},
            "pointType": "代谢产物",
            "starRating": "★★☆",
            "importance": 2
        }
    ]
}

QUIZ_03 = {
    "quiz": [
        # --- 单选题 (1~10) ---
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "在正常生理酸碱度（pH 7.2~7.6）环境中，细菌菌体表面解离后通常带有何种电荷？",
            "options": [
                {"text": "负电荷", "isCorrect": True, "rationale": "正确。细菌等电点在pH 2~5之间，在生理pH中均解离带负电荷。"},
                {"text": "正电荷", "isCorrect": False, "rationale": "在极强酸性环境（低于等电点）下才可能带正电荷。"},
                {"text": "电中性", "isCorrect": False, "rationale": "等电点时才呈电中性。"},
                {"text": "随细菌种类随机呈正或负", "isCorrect": False, "rationale": "所有常见细菌在生理pH下均稳定带负电荷。"}
            ],
            "hint": "细菌等电点（pH 2~5）远低于生理pH环境。",
            "rationale": "细菌由大量两性电解质蛋白质构成，等电点为pH 2~5。在生理pH（7.2~7.6）溶液中，细菌解离带负电荷，因此易与带正电荷的碱性染料结合。"
        },
        {
            "id": 2,
            "type": "multiple_choice",
            "question": "破伤风梭菌必须在完全无游离分子氧的厌氧环境中才能生长，其主要原因是因为该菌体内缺乏：",
            "options": [
                {"text": "超氧化物歧化酶（SOD）与过氧化氢酶", "isCorrect": True, "rationale": "正确。专性厌氧菌缺乏清除氧毒性自由基的SOD和过氧化氢酶，接触氧气会导致自身被氧化毒死。"},
                {"text": "肽聚糖合成酶系", "isCorrect": False, "rationale": "破伤风梭菌是G+菌，具有完整的肽聚糖合成酶。"},
                {"text": "三羧酸循环（TCA）所需的所有还原糖", "isCorrect": False, "rationale": "无氧发酵途径与糖类来源丰富度无关。"},
                {"text": "细胞膜上的电子传递链载体", "isCorrect": False, "rationale": "厌氧发酵同样具备底物水平磷酸化或无氧呼吸链。"}
            ],
            "hint": "清除超氧阴离子（O2-）和过氧化氢所必需的抗氧化防御酶。",
            "rationale": "专性厌氧菌体内缺乏超氧化物歧化酶（SOD）和过氧化氢酶，不能清除氧代谢过程中产生的具有强毒性的超氧化物阴离子，因而无法在有氧条件下生存。"
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "在医学微生物学实验中，进行细菌形态学染色镜检和抗生素药物敏感性试验，最佳采集时期是生长曲线的：",
            "options": [
                {"text": "对数期（指数生长期）", "isCorrect": True, "rationale": "正确。对数期细菌形态最标准、染色特征最典型、对抗菌药物最敏感。"},
                {"text": "迟缓期（适应期）", "isCorrect": False, "rationale": "迟缓期细菌尚未开始分裂，数量极少。"},
                {"text": "稳定期", "isCorrect": False, "rationale": "稳定期代谢产物蓄积，且开始产生芽胞或变异。"},
                {"text": "衰亡期", "isCorrect": False, "rationale": "衰亡期细菌出现多形退化与自溶裂解。"}
            ],
            "hint": "细菌繁殖最旺盛、形态染色最规整的一期。",
            "rationale": "对数期细菌增殖迅速，生理性状极其均一，形态典型且对药物最敏感，是进行形态检查与药敏试验的标准黄金时期。"
        },
        {
            "id": 4,
            "type": "multiple_choice",
            "question": "细菌产生外毒素、抗生素以及产芽胞菌形成耐热芽胞，主要集中发生在生长曲线的：",
            "options": [
                {"text": "稳定期", "isCorrect": True, "rationale": "正确。在稳定期细菌活菌数达到最大，次级代谢极为活跃，大量产生外毒素、抗生素及芽胞。"},
                {"text": "迟缓期", "isCorrect": False, "rationale": "迟缓期为适应环境期，仅合成酶类。"},
                {"text": "对数期", "isCorrect": False, "rationale": "对数期以菌体大量细胞结构快速复制为主。"},
                {"text": "衰亡期", "isCorrect": False, "rationale": "衰亡期代谢停滞，大量死菌崩解。"}
            ],
            "hint": "菌落活菌数达到峰值、次级代谢产物合成最旺盛的时期。",
            "rationale": "稳定期营养逐渐消耗，代谢产物堆积，细菌由初级代谢转向次级代谢，大量合成外毒素、抗生素、细菌素、热原质，并形成芽胞。"
        },
        {
            "id": 5,
            "type": "multiple_choice",
            "question": "大肠埃希菌在IMViC生化鉴别试验中的典型结果特征为：",
            "options": [
                {"text": "+ + - -", "isCorrect": True, "rationale": "正确。大肠埃希菌吲哚试验（+）、甲基红试验（+）、VP试验（-）、枸橼酸盐利用（-）。"},
                {"text": "- - + +", "isCorrect": False, "rationale": "这是产气肠杆菌的典型生化特征。"},
                {"text": "+ - + -", "isCorrect": False, "rationale": "不符合大肠埃希菌经典生化反应。"},
                {"text": "- + - +", "isCorrect": False, "rationale": "不符合大肠埃希菌经典生化反应。"}
            ],
            "hint": "大肠埃希菌与产气肠杆菌刚好相反，前两项为阳性。",
            "rationale": "大肠埃希菌的IMViC反应为“+ + - -”，而产气肠杆菌为“- - + +”，这是临床鉴别两者的经典生化试验。"
        },
        {
            "id": 6,
            "type": "multiple_choice",
            "question": "静脉注射大输液若被微量热原质污染可导致致命性高热反应。关于热原质的理化特性，下列说法正确的是：",
            "options": [
                {"text": "耐热性极强，常规121℃高压蒸汽灭菌20分钟无法将其破坏", "isCorrect": True, "rationale": "正确。热原质（内毒素LPS）极其耐热，常规高压蒸汽灭菌不能分解破坏。"},
                {"text": "化学本质是革兰阳性菌分泌的热敏性蛋白质", "isCorrect": False, "rationale": "化学本质是革兰阴性菌细胞壁的脂多糖（LPS）。"},
                {"text": "在100℃煮沸5分钟即可彻底失去致热活性", "isCorrect": False, "rationale": "煮沸完全不能破坏热原质。"},
                {"text": "可通过普通滤纸或0.22μm滤膜彻底过滤清除", "isCorrect": False, "rationale": "热原质可溶解于水并通过除菌滤膜。"}
            ],
            "hint": "热原质耐热，需180℃ 3~4h干烤或重蒸馏法制备纯水。",
            "rationale": "热原质就是革兰阴性菌的内毒素（脂多糖成分），极耐热，高压灭菌不能破坏，需180℃干烤3~4小时或采用蒸馏法制备无热原注射用水。"
        },
        {
            "id": 7,
            "type": "multiple_choice",
            "question": "在含有0.3%~0.5%低浓度琼脂的半固体培养基中进行穿刺接种，其主要目的是：",
            "options": [
                {"text": "观察细菌是否具备运动鞭毛和动力", "isCorrect": True, "rationale": "正确。有鞭毛有动力的细菌穿刺线周围呈云雾扩散浑浊，无动力细菌仅局限在穿刺线清晰生长。"},
                {"text": "测定细菌对糖类的发酵产气能力", "isCorrect": False, "rationale": "糖发酵管通常倒置杜氏小管测产气。"},
                {"text": "分离单个纯培养菌落", "isCorrect": False, "rationale": "分离单个菌落需用2%固体琼脂平板划线。"},
                {"text": "观察细菌是否产生外毒素", "isCorrect": False, "rationale": "外毒素测定需毒力试验或血清学试验。"}
            ],
            "hint": "低浓度琼脂允许活泼有鞭毛的细菌自由游动扩散。",
            "rationale": "半固体培养基常用于检查细菌动力，有鞭毛细菌在穿刺线周围羽毛状或浑浊扩散生长，无鞭毛细菌仅沿穿刺线生长。"
        },
        {
            "id": 8,
            "type": "multiple_choice",
            "question": "医学上要求最彻底、杀灭或清除物体上一切活的微生物（包括抵抗力极强的细菌芽胞）的处理方法被称为：",
            "options": [
                {"text": "灭菌（Sterilization）", "isCorrect": True, "rationale": "正确。灭菌指杀灭所有微生物包括芽胞的绝对标准。"},
                {"text": "消毒（Disinfection）", "isCorrect": False, "rationale": "消毒仅指杀灭病原微生物，不保证杀灭芽胞。"},
                {"text": "防腐（Antisepsis）", "isCorrect": False, "rationale": "防腐仅抑制细菌繁殖，不一定杀灭细菌。"},
                {"text": "清洁（Cleaning）", "isCorrect": False, "rationale": "清洁仅为去除表面肉眼污垢。"}
            ],
            "hint": "注意五个术语的区别，最高级别杀灭所有包括芽胞。",
            "rationale": "灭菌是指杀灭或清除物体上所有的微生物，包括抵抗力最强的细菌芽胞；而消毒通常只能杀灭病原菌繁殖体。"
        },
        {
            "id": 9,
            "type": "multiple_choice",
            "question": "目前临床医院对耐热、耐湿手术金属器械、手术敷料等物品进行灭菌的最优、最常用湿热灭菌方法是：",
            "options": [
                {"text": "高压蒸汽灭菌法（121℃，15~20 min）", "isCorrect": True, "rationale": "正确。高压蒸汽灭菌穿透力最强、最彻底、最可靠。"},
                {"text": "巴氏消毒法（62℃，30 min）", "isCorrect": False, "rationale": "巴氏法仅用于牛奶啤酒等食品低温消毒。"},
                {"text": "紫外线照射灭菌法（波长265 nm）", "isCorrect": False, "rationale": "紫外线穿透力极差，不能穿透器械内部或布类。"},
                {"text": "滤过除菌法（0.22 μm）", "isCorrect": False, "rationale": "滤过法仅用于热敏性液体除菌。"}
            ],
            "hint": "121℃、103.4 kPa饱和蒸汽压。",
            "rationale": "高压蒸汽灭菌利用饱和水蒸汽潜热大、穿透力强的优势，能高效杀灭包括芽胞在内的一切微生物，是耐高温高湿物品的黄金灭菌手段。"
        },
        {
            "id": 10,
            "type": "multiple_choice",
            "question": "紫外线（UV）杀菌力最强的波长约为265~266 nm，其导致细菌死亡的核心分子机制是：",
            "options": [
                {"text": "促使细菌DNA链中相邻的胸腺嘧啶形成二聚体（TT二聚体）", "isCorrect": True, "rationale": "正确。TT二聚体阻碍DNA复制与转录，导致致死性突变。"},
                {"text": "水解细胞壁肽聚糖骨架上的β-1,4糖苷键", "isCorrect": False, "rationale": "这是溶菌酶的作用机制。"},
                {"text": "氧化细菌外膜上的脂多糖成分", "isCorrect": False, "rationale": "属于强氧化性化学消毒剂机制。"},
                {"text": "直接使细菌细胞膜表面活性降解穿孔", "isCorrect": False, "rationale": "属于表面活性剂机制。"}
            ],
            "hint": "形成TT二聚体，阻碍DNA复制。",
            "rationale": "波长265~266 nm的紫外线照射使细菌DNA链上的相邻胸腺嘧啶共价连接形成胸腺嘧啶二聚体，干扰DNA正常复制转录导致菌体死亡。"
        },

        # --- 判断题 (11~15) ---
        {
            "id": 11,
            "type": "true_false",
            "question": "因为无水乙醇（100%纯酒精）浓度最高、脱水能力最强，所以临床常用100%纯酒精进行皮肤和穿刺部位消毒。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。100%酒精使菌体表层蛋白瞬间硬化结壳，阻碍渗透，杀菌效果极差！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。临床最适杀菌浓度为70%~75%乙醇，能充分渗透入菌体深层彻底变性蛋白。"}
            ],
            "hint": "过高浓度瞬间凝固表层形成保护硬膜，反而保护了深层细菌。",
            "rationale": "100%纯乙醇导致菌体表面蛋白质迅速凝固成保护膜，阻止乙醇渗透；而70%~75%乙醇兼顾穿透力与脱水变性能力，杀菌效果最好。"
        },
        {
            "id": 12,
            "type": "true_false",
            "question": "由于滤过除菌法使用的滤膜孔径通常为0.22微米，因此经过滤除菌后的血清或培养液可以完全排除病毒的污染。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。病毒直径多在20~300 nm之间，能自由通过0.22微米滤膜！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。病毒体微小，能穿透除菌滤膜，滤过除菌法只能去除细菌和真菌，不能除病毒。"}
            ],
            "hint": "病毒纳米级，能通过细菌滤器。",
            "rationale": "病毒属于非细胞型微生物，体积极其微小，可通过0.22 μm常规孔径细菌滤器，故滤过除菌法无法滤除病毒。"
        },
        {
            "id": 13,
            "type": "true_false",
            "question": "单个细菌在固体琼脂培养基表面经过分裂繁殖后，最终形成的肉眼可见的子细胞群体被称为‘菌落’（Colony）。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。菌落即由单个细菌或少数几个相同细菌细胞繁殖而成的肉眼可见集团。"},
                {"text": "错误", "isCorrect": False, "rationale": "菌落是微生物纯培养分离的核心概念。"}
            ],
            "hint": "单个细菌在固体培养基上繁殖形成的肉眼可见集合体。",
            "rationale": "菌落（Colony）是由单个细菌繁殖形成的肉眼可见子细胞群落，在固体培养基上观察菌落形态是病原菌鉴定的基础。"
        },
        {
            "id": 14,
            "type": "true_false",
            "question": "紫外线不仅杀菌力强，而且具有极强的物体穿透力，能穿透普通厚玻璃和病房门窗对房间内部深层彻底灭菌。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。紫外线最大弱点就是穿透力极差，连普通薄玻璃或一张纸都穿不透！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。紫外线穿透力极弱，只能用于空气消毒及暴露的物体表面消毒。"}
            ],
            "hint": "紫外线能否穿透普通玻璃？",
            "rationale": "紫外线能量低、穿透力极弱，普通玻璃、薄纸甚至尘埃均能阻挡紫外线，因此仅适用于空气和物体平滑表面消毒。"
        },
        {
            "id": 15,
            "type": "true_false",
            "question": "防腐是指防止或抑制体外微生物生长繁殖，但防腐剂去除或浓度下降后，被抑制的微生物仍可能恢复生长。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。防腐主要表现为抑菌作用而非永久性杀灭。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合防腐的医学定义。"}
            ],
            "hint": "防腐以抑制生长为特征，与杀灭一切的灭菌有本质区别。",
            "rationale": "防腐（Antisepsis）主要通过抑制微生物的新陈代谢阻止其繁殖，一般并不杀死微生物，条件改善后细菌可重新恢复繁殖。"
        },

        # --- 多选题 (16~19) ---
        {
            "id": 16,
            "type": "multiple_select",
            "question": "在细菌生长曲线中，关于“对数生长期”的特征描述正确的有：",
            "options": [
                {"text": "细菌体内形态、染色性和生理生化反应最为典型", "isCorrect": True, "rationale": "正确。处于最标准状态。"},
                {"text": "细菌对各类抗菌药物及外界环境因子的敏感性最高", "isCorrect": True, "rationale": "正确。旺盛分裂期对药物最为敏感。"},
                {"text": "活菌总数呈几何级数（指数方式）迅速上升", "isCorrect": True, "rationale": "正确。对数期增殖特征。"},
                {"text": "是临床常规进行药物敏感试验和形态镜检的标准时期", "isCorrect": True, "rationale": "正确。标准采菌时期。"}
            ],
            "hint": "对数期是细菌生命活动最为旺盛和特征最纯正的黄金时期。",
            "rationale": "四个选项均准确概括了对数期细菌的典型生理特征与实验应用价值。"
        },
        {
            "id": 17,
            "type": "multiple_select",
            "question": "下列属于细菌代谢合成的生物活性产物包括哪些？",
            "options": [
                {"text": "热原质（内毒素脂多糖成分）", "isCorrect": True, "rationale": "合成产物，致体温升高。"},
                {"text": "外毒素与侵袭性酶（如血浆凝固酶）", "isCorrect": True, "rationale": "合成毒力因子。"},
                {"text": "抗生素与细菌素", "isCorrect": True, "rationale": "次级代谢合成产物。"},
                {"text": "维生素（如维生素K和B族）", "isCorrect": True, "rationale": "合成营养成分。"}
            ],
            "hint": "细菌合成代谢产物丰富，涵盖致病性、抗微生物以及营养合成物质。",
            "rationale": "细菌合成代谢产物包括热原质、毒素和侵袭性酶、色素、抗生素、细菌素和维生素等。"
        },
        {
            "id": 18,
            "type": "multiple_select",
            "question": "下列灭菌或消毒方法中，属于利用“湿热法”进行处理的有：",
            "options": [
                {"text": "高压蒸汽灭菌法（121℃）", "isCorrect": True, "rationale": "经典湿热灭菌法。"},
                {"text": "巴氏消毒法（61~63℃）", "isCorrect": True, "rationale": "利用热水进行低温湿热消毒。"},
                {"text": "干烤灭菌法（160~170℃）", "isCorrect": False, "rationale": "干烤属于干热灭菌法。"},
                {"text": "煮沸消毒法（100℃）", "isCorrect": True, "rationale": "在水沸腾中进行的湿热消毒。"}
            ],
            "hint": "区分湿热法（有水或饱和蒸汽介质）与干热法。",
            "rationale": "湿热消毒灭菌法包括巴氏消毒法、煮沸法、流通蒸汽灭菌法、间歇灭菌法和高压蒸汽灭菌法；干烤和焚烧属于干热法。"
        },
        {
            "id": 19,
            "type": "multiple_select",
            "question": "滤过除菌法是临床制药与实验室除菌的重要手段，主要适用于下列哪些物品？",
            "options": [
                {"text": "含有血清蛋白的热敏性细胞培养液", "isCorrect": True, "rationale": "正确。蛋白质受热易变性凝固，只能滤过除菌。"},
                {"text": "易受高温破坏的抗毒素与疫苗原液", "isCorrect": True, "rationale": "正确。抗毒素蛋白不能高压灭菌。"},
                {"text": "用于静脉滴注的抗生素溶液", "isCorrect": True, "rationale": "正确。抗生素药液遇热多易降解失效。"},
                {"text": "手术室使用的棉纱敷料与金属止血钳", "isCorrect": False, "rationale": "手术敷料与金属器械耐热，首选高压蒸汽灭菌。"}
            ],
            "hint": "凡是受热易变质、降解或变性的液体物质均适用滤过除菌。",
            "rationale": "滤过除菌法主要用于不耐高温的热敏性液体，如血清、抗生素、维生素、毒素、培养液等；固体器材耐高温应首选高压灭菌。"
        },

        # --- 填空题 (20~21) ---
        {
            "id": 20,
            "type": "fill_blank",
            "question": "高压蒸汽灭菌法的标准灭菌工作参数为：蒸汽压力达到103.4 kPa（1.05 kg/cm²），温度达到（1）____℃，维持时间为（2）____分钟，可彻底杀灭一切微生物与芽胞。",
            "blankAnswers": [
                "121",
                "15~20"
            ],
            "hint": "温度约121度，时间在15到20分钟之间。",
            "rationale": "高压蒸汽灭菌法标准参数为121.3℃维持15~20分钟（或填121）。"
        },
        {
            "id": 21,
            "type": "fill_blank",
            "question": "波长在（1）____nm范围内的紫外线杀菌效果最强，其分子杀菌机制主要是诱导细菌DNA相邻碱基形成（2）____二聚体，阻碍DNA复制与转录。",
            "blankAnswers": [
                "265~266",
                "胸腺嘧啶"
            ],
            "hint": "波长265左右；TT二聚体全称。",
            "rationale": "紫外线杀菌最敏感波长为265~266 nm，机制是诱导胸腺嘧啶二聚体（TT二聚体）形成。"
        }
    ]
}
