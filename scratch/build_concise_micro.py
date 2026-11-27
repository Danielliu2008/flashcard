# -*- coding: utf-8 -*-
"""
Generate concise, short, single-screen readable flashcards for all 8 Microbiology chapters.
"""

import os
import json

DECK_01_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心概念】什么是微生物？其具备哪三大基本特征？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：个体微小、结构简单、肉眼不可见的微小生物。\n• **三大特征**：\n  ① **形微构简**：多为单细胞或非细胞型；\n  ② **种类多、分布广**：土壤、水及体表腔道；\n  ③ **繁殖快、易变异**：环境适应力极强。"}]},
        "pointType": "核心定义", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】按分化程度和结构，微生物分为哪三大类型？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **非细胞型**：最小，无细胞结构，仅一种核酸（DNA或RNA），如**病毒**。\n• **原核细胞型**：仅原始拟核（无核膜核仁），细胞器仅**核糖体**，如**细菌**、支原体。\n• **真核细胞型**：核分化程度高（有核膜核仁），细胞器完备，如**真菌**。"}]},
        "pointType": "大纲掌握", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心性状】非细胞型微生物（病毒）具备哪些关键特异性状？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• 纳米级超微结构，能通过除菌滤器。\n• **单一核酸**：每种病毒仅含 DNA 或 RNA 之一。\n• **严格活细胞内寄生**：以分子自我复制方式增殖。\n• **药敏特性**：对抗生素无效，对**干扰素**敏感。"}]},
        "pointType": "特异性状", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【必背口诀】原核细胞型微生物包含哪六大类群？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "**口诀：支衣立螺放，外加真细菌**\n• **细菌**（狭义细菌）\n• **支原体**（无细胞壁，高度多形）\n• **衣原体**（具独特发育周期）\n• **立克次体**（节肢动物传播）\n• **螺旋体**、**放线菌**"}]},
        "pointType": "经典分类", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【名词解释】什么是病原微生物与机会性致病微生物？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **病原微生物**：能侵犯人体引起感染性疾病的少数微生物（如结核杆菌）。\n• **机会致病菌（条件致病菌）**：正常菌群在机体免疫低下、寄居部位改变或菌群失调时引发的内源感染。"}]},
        "pointType": "概念理解", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频考点】条件致病菌致病的三大核心诱因是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **机体免疫力低下**：放化疗、激素、艾滋病、器官移植。\n② **寄居部位改变（异位寄生）**：肠道大肠杆菌入尿道致尿感。\n③ **菌群失调**：长期滥用广谱抗生素诱发假膜性肠炎等二重感染。"}]},
        "pointType": "机制原理", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲概念】医学微生物学研究的核心范畴“三性两法”指什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **三性**：生物学特性、致病性、免疫性。\n• **两法**：病原学检查诊断方法、特异性防治方法。"}]},
        "pointType": "学科概括", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【生态认知】微生物与人类的关系主要表现在哪些方面？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **绝大多数有益且必需**：参与元素循环；发酵制药；维持人体微生态屏障并合成维生素 K 和 B 族。\n• **极少数有害**：病原微生物引起人类各类感染性疾病。"}]},
        "pointType": "基础认知", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【人物贡献】列文虎克与巴斯德在微生物学史上有何里程碑贡献？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **列文虎克**：自制显微镜首次观察到活微生物形态。\n• **巴斯德（奠基人）**：\n  ① 曲颈瓶实验彻底**否定自然发生说**；\n  ② 发明**巴氏消毒法**；\n  ③ 研制炭疽、**狂犬病减毒活疫苗**。"}]},
        "pointType": "历史人物", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频考点】郭霍的主要贡献与“郭霍法则”的四条准则是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **主要贡献**：创用琼脂固体培养基纯培养，确立细菌学奠基。\n• **郭霍法则四原则**：\n  ① 病人体内常在；\n  ② 体外分离出纯培养；\n  ③ 动物接种复制出相同疾病；\n  ④ 患病动物能再次重分离出该纯培养。"}]},
        "pointType": "奠基伟人", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【医学贡献】琴纳、李斯特与弗莱明分别有哪些划时代贡献？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **琴纳**：发明**牛痘接种法**预防天花（人工主动免疫先河）。\n• **李斯特**：首创**石炭酸无菌手术**（外科防腐消毒灭菌先驱）。\n• **弗莱明**：发现**青霉素**（开启抗生素治疗感染时代）。"}]},
        "pointType": "关键学者", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【历史人物】伊凡诺夫斯基在病毒学发展史上的关键贡献是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• 发现烟草花叶病汁液经**细菌滤器过滤后仍具传染性**。\n• 首次证实存在比细菌更微小、滤过性病原体，发现**烟草花叶病毒**，开创病毒学。"}]},
        "pointType": "病毒先驱", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【横向对比】原核细胞与真核细胞在“细胞核”和“细胞器”上有何本质区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **细胞核**：原核生物仅有**原始拟核**（无核膜、无核仁）；真核生物具有**完整双层核膜与核仁**。\n• **细胞器**：原核生物仅有**核糖体（70S）**；真核生物含完备的线粒体、内质网等。"}]},
        "pointType": "考点对比", "starRating": "★★★", "importance": 3
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【生态屏障】正常菌群对人体宿主具有哪四大不可或缺的生理作用？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **生物拮抗**：竞争受体与营养，排斥外来致病菌。\n② **营养代谢**：肠道菌合成**维生素 K 及 B 族**。\n③ **免疫促进**：刺激宿主黏膜免疫系统发育成熟。\n④ **抗衰抗肿瘤**：清除过氧化物与降解前致癌物。"}]},
        "pointType": "生理作用", "starRating": "★★★", "importance": 3
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药敏对比】细菌与病毒在抗生素和干扰素敏感性上有何截然不同的规律？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **细菌**：对抗生素敏感；对干扰素**不敏感**。\n• **病毒**：对抗生素**天然无效**；对**干扰素敏感**。"}]},
        "pointType": "考点对比", "starRating": "★★★", "importance": 3
    }
]

DECK_02_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【测量与形态】细菌大小的度量单位是什么？三大基本形态有哪些？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **度量单位**：**微米（μm）**，光学显微镜油镜下观察。\n• **三大形态**：\n  ① **球菌**：双球菌、链球菌、葡萄球菌。\n  ② **杆菌**：长短粗细不一（大肠杆菌、结核杆菌）。\n  ③ **螺形菌**：弧菌（一个弯曲）、螺菌（多个弯曲）。"}]},
        "pointType": "形态基础", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心组成】细菌细胞壁骨架成分肽聚糖由哪三部分构成？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **聚糖骨架**：**N-乙酰葡糖胺（NAG）**与**N-乙酰胞壁酸（NAM）**通过 **β-1,4 糖苷键**交替连接。\n• **四肽侧链**：连于 NAM 上。\n• **五肽交联桥**（或侧链直接肽键连接）。"}]},
        "pointType": "分子结构", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药理机制】溶菌酶与青霉素破坏细菌细胞壁的机制有何不同？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **溶菌酶**：特异性水解聚糖骨架中的 **β-1,4 糖苷键**（静止期、繁殖期细菌均有效）。\n• **青霉素**：竞争性抑制**转肽酶（PBPs）**，阻断肽聚糖交叉联结（**仅对繁殖期细菌有效**）。"}]},
        "pointType": "作用机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】革兰阳性菌（G+）与革兰阴性菌（G-）细胞壁的主要区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **G+ 菌**：厚（20~80nm），肽聚糖致密（多达50层），含特有**磷壁酸**，无外膜。\n• **G- 菌**：薄（10~15nm），肽聚糖仅1~2层，无磷壁酸，外被**外膜（含脂多糖 LPS / 内毒素）**。"}]},
        "pointType": "核心对比", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高危致病】什么是脂多糖（LPS）？其核心毒性中心是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **本质**：G- 菌外膜特有成分，即**内毒素（Endotoxin）**。\n• **三层结构**：**脂质 A（主要毒性成分与活性中心）** + 核心多糖 + O 特异多糖（菌株特异抗原）。"}]},
        "pointType": "高频考点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【临床高频】什么是细菌 L 型？其主要诱因与临床意义是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **概念**：肽聚糖受损缺失的细胞壁缺陷型细菌，仅在**高渗环境**下生存，菌落呈典型**“荷包蛋”状**。\n• **意义**：对青霉素等**天然耐药**；常规培养易漏诊；诱因去除后可恢复壁结构导致感染复发。"}]},
        "pointType": "临床意义", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【特殊结构】什么是细菌荚膜（Capsule）？有何关键功能？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **本质**：多为多糖（炭疽杆菌为多肽）。\n• **四大功能**：\n  ① **抗吞噬**（最核心毒力因素，如肺炎链球菌）；\n  ② 抗体液免疫杀伤；\n  ③ 黏附组织表面；\n  ④ K 抗原分型与制备疫苗。"}]},
        "pointType": "特殊结构", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【特殊结构】什么是细菌鞭毛（Flagellum）？主要功能是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **本质**：由鞭毛蛋白构成的细长波状丝状物。\n• **三大功能**：\n  ① **运动器官**（半固体培养穿刺线呈云雾状扩散）；\n  ② 辅助细菌穿透黏液定植；\n  ③ **H 抗原**（细菌鉴定与血清分型）。"}]},
        "pointType": "特殊结构", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【横向对比】普通菌毛与性菌毛有何本质区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **普通菌毛**：多（数百根），短细，负责**特异性黏附**宿主受体，是重要致病定植因子。\n• **性菌毛（F菌毛）**：极少（1~4根），长粗，仅见于雄性菌，负责**接合传递质粒（传递耐药性）**。"}]},
        "pointType": "考点对比", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【重要考点】什么是细菌芽胞？为什么说芽胞不是繁殖方式？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：部分 G+ 菌在恶劣环境中于胞内形成的圆形致密**休眠体**。\n• **非繁殖方式**：1 个细菌仅产生 1 个芽胞，1 个芽胞萌发也只恢复成 1 个菌，**数量并未增加**，纯属抗逆休眠形式。"}]},
        "pointType": "概念辨析", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【灭菌标准】芽胞耐热的关键物质是什么？在灭菌中有何指标意义？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **耐热机制**：含高浓度特有的**吡啶二羧酸钙（DPA-Ca）**，极低含水率，蛋白质高度耐热。\n• **指标意义**：是生物界抵抗力最强的结构，**以杀灭芽胞作为衡量物理/化学灭菌彻底的黄金指标**。"}]},
        "pointType": "指标意义", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【染色精要】革兰染色法的四步操作流程与各步试剂是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **初染**：结晶紫染 1min（全紫）；\n② **媒染**：碘液染 1min（形成复合物）；\n③ **脱色（最关键）**：**95% 乙醇脱色约 30s**；\n④ **复染**：稀释复红（或沙黄）染 30s。"}]},
        "pointType": "实验原理", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【实验机制】革兰染色脱色步骤的基本原理与结果是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **G+ 菌（显紫色）**：细胞壁厚、肽聚糖致密，乙醇脱水使孔径缩小，紫色复合物不漏出。\n• **G- 菌（显红色）**：细胞壁薄、外膜脂质多，乙醇溶解脂质孔径大，紫色复合物脱失，被复红染成红色。"}]},
        "pointType": "机制原理", "starRating": "★★★", "importance": 3
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【医学应用】革兰染色在医学实践中有哪三大重大意义？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **鉴别分类**：迅速将细菌初分为 G+ 和 G- 两大类。\n② **指导选药**：G+ 选青霉素类/万古霉素；G- 选氨基糖苷类/喹诺酮/三代头孢。\n③ **致病机制**：G+ 多产生外毒素；G- 细胞壁含内毒素。"}]},
        "pointType": "三大意义", "starRating": "★★★", "importance": 3
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【胞质颗粒】什么是异染颗粒？在临床何种细菌诊断中有重要意义？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **本质**：嗜碱性多聚偏磷酸盐颗粒，储藏能量。\n• **临床意义**：在**白喉棒状杆菌**菌体两端极明显，为快速形态学鉴别白喉杆菌的重要特征。"}]},
        "pointType": "颗粒诊断", "starRating": "★★☆", "importance": 2
    }
]

DECK_03_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【物理性状】在生理酸碱度（pH 7.2~7.6）环境下，细菌表面带何种电荷？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **带电状态**：细菌等电点在 pH 2~5，在生理 pH（7.2~7.6）环境中**解离带负电荷**。\n• **染色意义**：易与带正电荷的**碱性染料（如结晶紫、美蓝）**紧密结合上色。"}]},
        "pointType": "物理性状", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【生长环境】根据对分子氧的需求与耐受能力，细菌分为哪四种气体类型？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **专性需氧**：必须有氧（结核杆菌）。\n• **微需氧**：低氧 5%~6%（幽门螺杆菌）。\n• **兼性厌氧**：有氧无氧均可（大多数致病菌，如大肠杆菌、金葡菌）。\n• **专性厌氧**：只能无氧，缺乏 SOD 与过氧化氢酶（破伤风梭菌）。"}]},
        "pointType": "气体类型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【生长曲线】液体培养基中细菌生长曲线分为哪四个主要时期？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **迟缓期（适应期）**：体积增大、代谢旺盛，菌数不增。\n② **对数期**：指数繁殖，**形态典型，药敏最高**。\n③ **稳定期**：增殖与死亡平衡，**产外毒素、抗生素、芽胞、热原质**。\n④ **衰亡期**：死亡超过活菌，形态多形自溶。"}]},
        "pointType": "核心曲线", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频考点】细菌形态学检查和抗生素药敏试验应选用哪一时期的细菌？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **选用时期**：**对数期（指数生长期）**。\n• **原因**：细菌生理活性最旺盛、形态染色最规整标准、对外界抗感染药物**敏感性最高**，结果最准确。"}]},
        "pointType": "实验依据", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频考点】细菌产生外毒素、抗生素和形成芽胞主要在哪个时期？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **集中时期**：**稳定期**。\n• **原因**：活菌总数达峰值，次级代谢活跃，大量合成外毒素、抗生素、细菌素、热原质，产芽胞菌形成耐热芽胞。"}]},
        "pointType": "高频考点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【鉴别试验】什么是 IMViC 试验？大肠埃希菌的反应特征是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **包含试验**：吲哚(I)、甲基红(M)、VP(Vi)、枸橼酸盐利用(C)。\n• **典型特征**：\n  • **大肠埃希菌**：**“+ + - -”**\n  • **产气肠杆菌**：**“- - + +”**"}]},
        "pointType": "生化试验", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药剂安全】什么是热原质（Pyrogen）？其耐热特性与去除方法是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **本质**：G- 菌细胞壁的**脂多糖（LPS/内毒素）**。\n• **耐热特性**：**极耐高热**，高压蒸汽灭菌（121℃）不能破坏；需 **180℃ 干烤 3~4h** 才能破坏。\n• **制药防范**：注射用水必须用**蒸馏法**制备无热原纯水。"}]},
        "pointType": "重点概念", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【人工培养】细菌在液体、固体和半固体培养基中有何典型生长现象？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **液体**：均匀浑浊、沉淀（链球菌）、菌膜（结核杆菌）。\n• **固体**：单个细菌分裂形成的肉眼可见子细胞集团称为**菌落（Colony）**。\n• **半固体（0.3%~0.5%琼脂）**：**检查动力**，有动力呈云雾状扩散，无动力仅限穿刺线。"}]},
        "pointType": "生长现象", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲辨析】准确区分“灭菌”、“消毒”、“无菌”与“防腐”。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **灭菌**：杀灭或清除物体上**一切活微生物（包括芽胞）**。\n• **消毒**：仅杀灭物体上的**病原微生物**（不一定杀灭芽胞）。\n• **无菌**：完全不含任何活微生物。\n• **防腐**：**抑制微生物生长繁殖**（不一定杀死）。"}]},
        "pointType": "五大术语", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【灭菌王牌】高压蒸汽灭菌法的标准参数是什么？地位如何？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **标准参数**：压力 103.4 kPa，温度 **121.3℃**，维持 **15~20 min**。\n• **核心地位**：湿热灭菌中杀菌最强、最彻底可靠的黄金方法，可彻底杀灭包括**芽胞**在内的一切微生物。"}]},
        "pointType": "核心灭菌", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【物理消毒】紫外线杀菌的最适波长、机制与最大局限是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **最适波长**：**265~266 nm**。\n• **杀菌机制**：诱导 DNA 相邻碱基形成**胸腺嘧啶二聚体（TT二聚体）**干扰复制。\n• **最大局限**：**穿透力极差**（薄纸/玻璃即能阻挡），仅用于空气与物体表面消毒。"}]},
        "pointType": "物理消毒", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【物理除菌】滤过除菌法的常用孔径是多少？能除病毒吗？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **常用孔径**：**0.22 μm**，用于热敏性液体（血清、抗生素、毒素）除菌。\n• **能除病毒吗**：**不能！** 病毒纳米级超微结构，能自由穿过滤膜；支原体亦可能穿过。"}]},
        "pointType": "滤过除菌", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【化学消毒】乙醇（酒精）杀菌的最适浓度是多少？为什么不是纯酒精？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **最适浓度**：**70%~75%**。\n• **原理**：75% 酒精能渗入菌体深层使蛋白均匀变性；纯酒精使菌体表层蛋白瞬间硬化凝固成壳，反而阻挡药物渗透，深层细菌仍存活。"}]},
        "pointType": "消毒机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【培养基类型】什么是选择培养基与鉴别培养基？请各举一例。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **选择培养基**：加入抑制剂抑制非目的菌，仅允许目标致病菌生长（如 **SS 琼脂**分离肠道沙门/志贺菌）。\n• **鉴别培养基**：加入特定底物和指示剂利用显色鉴别（如 **伊红美蓝 EMB 培养基**鉴别大肠杆菌深紫金属光泽菌落）。"}]},
        "pointType": "培养基分类", "starRating": "★★★", "importance": 3
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【色素鉴别】水溶性色素与脂溶性色素在表现上有何区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **水溶性色素**：溶于水，扩散染绿培养基或创面脓液（如**铜绿假单胞菌绿脓素**）。\n• **脂溶性色素**：不溶于水，仅沉积局限于菌落本身（如**金葡菌金黄色菌落**，培养基不变色）。"}]},
        "pointType": "代谢产物", "starRating": "★★☆", "importance": 2
    }
]

DECK_04_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心对比】表型变异（饰变）与基因型变异有何本质区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **表型变异**：基因型未变，外界诱导引起的暂时形态改变，**不可遗传，可逆**（如抗生素诱导 L 型）。\n• **基因型变异**：基因结构改变，**可稳定遗传**，不可逆（如耐药突变）。"}]},
        "pointType": "概念辨析", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【毒力变异】卡介苗（BCG）是如何研制成功的？属于何种变异？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **研制历程**：牛型结核杆菌在胆汁、甘油、马铃薯培养基上历经 13 年、传代 230 代获得。\n• **变异类型**：属于细菌的**毒力减毒变异（基因型变异）**，用于人工主动免疫预防结核。"}]},
        "pointType": "经典疫苗", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】什么是质粒（Plasmid）？具备哪些关键特性？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：染色体外的双链共价闭合环状 DNA。\n• **四大特性**：\n  ① **自主复制**；\n  ② **非生命必需**；\n  ③ 编码特定表型（耐药 R、性菌毛 F、毒力 Vi）；\n  ④ 可接合转移，可被溴化乙锭等人工消除。"}]},
        "pointType": "物质基础", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【耐药扩散】什么是耐药质粒（R质粒）？其结构与危害是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **结构**：耐药传递因子（RTF，编码性菌毛）+ 耐药决定子（编码抗药酶）。\n• **危害**：通过**接合作用**在同种及异种细菌间高效水平转移，导致临床多重耐药超级细菌扩散。"}]},
        "pointType": "耐药机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【噬菌体分类】毒性噬菌体与温和噬菌体的结局有何不同？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **毒性噬菌体**：仅有溶菌周期，迅速增殖并**裂解细菌**，平板上形成透明**噬斑（PFU）**。\n• **温和噬菌体**：侵入后**不裂解细菌**，DNA 整合于宿主染色体，随细菌分裂同步传代。"}]},
        "pointType": "噬菌体分类", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心名词】什么是前噬菌体与溶原性细菌？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **前噬菌体（Prophage）**：整合到宿主菌染色体上的温和噬菌体基因组 DNA。\n• **溶原性细菌**：染色体上带有前噬菌体的细菌。"}]},
        "pointType": "核心名词", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【黄金考点】什么是溶原性转换？白喉杆菌产毒机制是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **溶原性转换**：前噬菌体自身基因表达，使宿主菌获得新的生物学性状。\n• **经典实例**：无毒白喉棒状杆菌受 **$\beta$-棒状噬菌体** 感染整合后，表达 tox 基因产生致命的**白喉外毒素**。"}]},
        "pointType": "黄金考点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【基因转移方式】什么是细菌的“转化”（Transformation）？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：受体菌在**感受态**下直接摄取外源供体菌释放的**游离裸露 DNA** 片段实现重组。\n• **特征**：**不需要细胞接触**，不需要噬菌体，**能被 DNA 酶阻断水解**。"}]},
        "pointType": "基因重组", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【基因转移方式】什么是细菌的“接合”（Conjugation）？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：供受体细菌通过**性菌毛直接物理接触**，单向传递质粒 DNA 的过程。\n• **特征**：**必须直接物理接触**，DNA 在密封管道转移，**不受 DNA 酶影响**。"}]},
        "pointType": "基因重组", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【基因转移方式】什么是细菌的“转导”（Transduction）？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：以**噬菌体为媒介载体**，将供体菌 DNA 片段包裹并转入受体菌中实现基因重组。\n• **特征**：不需细胞接触，DNA 被衣壳保护，不受 DNA 酶破坏。"}]},
        "pointType": "基因重组", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【机制对比】普遍性转导与局限性转导有何本质区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **普遍性转导**：子代装配时发生“误包”，可转导供体染色体的**任意基因片段**。\n• **局限性转导**：温和噬菌体不正常切离，仅能转导整合位点**两侧特定邻近基因**（如 gal/bio）。"}]},
        "pointType": "机制对比", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【全景总结】四大基因转移重组机制横向对比速查。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **转化**：游离裸露 DNA + 感受态（被 DNA 酶水解）。\n• **接合**：性菌毛直接接触传递质粒（不受 DNA 酶影响）。\n• **转导**：噬菌体做载体包装转运供体基因。\n• **溶原性转换**：前噬菌体 DNA 整合表达自身基因（产毒素）。"}]},
        "pointType": "四大机制总结", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【跳跃基因】什么是转座子（Tn）？与插入序列（IS）有何区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **插入序列（IS）**：仅编码转座酶和反向重复序列。\n• **转座子（Tn）**：除转座酶外，还**携带有抗生素耐药基因**等表型基因，可在染色体与质粒间跳跃转移耐药性。"}]},
        "pointType": "分子结构", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【菌落变异】什么是 S-R 变异？毒力有何对应变化？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **S-R 变异**：光滑型菌落（S型）变异为粗糙型（R型）。\n• **毒力变化**：常伴随表面特异抗原（荚膜或外膜 LPS）缺失，致病力与**毒力显著减弱甚至消失**。"}]},
        "pointType": "变异表现", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【耐药防控】抗生素与细菌耐药性筛选是什么关系？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• 抗生素**不直接诱导定向突变**，耐药突变是自发随机产生的。\n• 抗生素充当**环境选择压力**，杀死敏感菌并定向筛选保留耐药突变株，导致耐药菌成为优势群。"}]},
        "pointType": "临床用药", "starRating": "★★★", "importance": 3
    }
]

DECK_05_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心名词】什么是隐性感染、显性感染与带菌者？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **隐性感染**：无明显症状，但获得特异性免疫（多数传染病最常见结局）。\n• **显性感染**：出现特异临床症状体征。\n• **带菌者**：体内长期带菌并向外排毒但无明显症状，是隐匿危险的传染源（如伤寒带菌者）。"}]},
        "pointType": "感染类型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【极高频考点】毒血症、菌血症、败血症与脓毒血症全分辨。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **毒血症**：菌不入血，仅**外毒素入血**致全身症状（白喉、破伤风）。\n• **菌血症**：菌**一过性入血**，不在血中繁殖（伤寒早期）。\n• **败血症**：菌侵入血流并**大量生长繁殖产毒**，高热皮疹中毒深。\n• **脓毒血症**：化脓菌败血症伴随**全身多发转移性化脓病灶**（金葡菌脓肿）。"}]},
        "pointType": "四大感染类型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【生态屏障】正常菌群对宿主具有哪四大有益生理作用？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **生物拮抗**：排斥外来致病菌定植。\n② **营养代谢**：肠道菌合成**维生素 K 及 B 族**。\n③ **免疫促进**：刺激黏膜免疫系统发育成熟。\n④ **抗衰抗肿瘤**：清除过氧化物与降解前致癌物。"}]},
        "pointType": "生理作用", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【临床高发】什么是二重感染？其诱发机制是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **概念**：长期滥用广谱抗生素杀灭敏感正常菌群，使不敏感耐药菌（难辨梭菌、白念珠菌）乘机剧烈增殖导致的继发新感染。\n• **典型疾病**：**假膜性肠炎**（难辨梭菌引起）。"}]},
        "pointType": "二重感染", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【致病要素】细菌毒力由哪两大核心要素构成？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **侵袭力**：定植黏附（菌毛）、抗吞噬（荚膜/SPA）、侵袭性酶（血浆凝固酶/透明质酸酶）。\n• **毒素**：**外毒素**（蛋白质）与**内毒素**（脂多糖）。"}]},
        "pointType": "毒力构成", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【侵袭酶类】血浆凝固酶与透明质酸酶致病作用有何区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **血浆凝固酶**（金葡菌）：使纤维蛋白沉积包裹菌体抗吞噬，使**感染病灶局限化**。\n• **透明质酸酶（扩散因子）**（链球菌）：分解细胞间质透明质酸，使**感染弥漫性扩散**（蜂窝织炎）。"}]},
        "pointType": "侵袭性酶", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲黄金大题】外毒素与内毒素全维度对比速查。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **外毒素**：大多 G+ 菌；分泌至胞外；**蛋白质**；**不耐热**；**毒性极强**（微克致死）；特异靶器官；**强抗原性可制类毒素**。\n• **内毒素**：几乎所有 G- 菌；细胞壁裂解释放；**脂多糖（LPS/脂质A）**；**极耐热**；毒性较弱；发热休克DIC；**抗原性弱不能制类毒素**。"}]},
        "pointType": "核心大题", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【毒素结构】外毒素经典的 A-B 亚基模型是如何协同致病的？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **B 亚基**：结合亚基，无毒，特异结合靶细胞膜受体，介导 A 亚基穿入。\n• **A 亚基**：毒性活性催化亚基，进入胞质水解破坏核心靶标（如白喉毒素抑制蛋白质合成）。"}]},
        "pointType": "分子机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【免疫制剂】类毒素与抗毒素有何本质不同？各用于何种免疫？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **类毒素（Toxoid）**：外毒素经甲醛脱毒制成，丧失毒性但保留免疫原性，用于**主动免疫预防接种**（如破伤风类毒素）。\n• **抗毒素（Antitoxin）**：含特异中和抗体的免疫血清，用于**被动免疫紧急救治**（如破伤风抗毒素 TAT）。"}]},
        "pointType": "生物制品", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【内毒素效应】革兰阴性菌内毒素（LPS）入血诱发哪三大病理反应？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **发热反应**：促使单核细胞释放 IL-1、TNF-α 致热。\n② **感染性休克**：微血管广泛扩张、通透性暴增致低血压休克。\n③ **弥散性血管内凝血（DIC）**：激活凝血因子形成广泛微血栓伴大出血。"}]},
        "pointType": "病理机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【宿主防线】宿主抗感染固有免疫包含哪三大生理屏障体系？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **皮肤黏膜屏障**：机械阻挡、分泌物化学杀菌、正常菌群拮抗。\n② **血脑屏障**：保护脑脊髓中枢神经系统免受感染。\n③ **胎盘屏障**：阻止母体血液病原体侵入胎儿。"}]},
        "pointType": "机体屏障", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【特异免疫】抗胞外寄生菌与抗胞内寄生菌在免疫形式上有何根本区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **抗胞外菌**：**以体液免疫为主**（IgG/IgM 中和毒素、调理吞噬、溶菌；sIgA 黏膜阻断）。\n• **抗胞内菌**：**以细胞免疫为主**（抗体进不去细胞，依赖 Th1 活化巨噬细胞、CTL 裂解靶细胞）。"}]},
        "pointType": "免疫机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【免疫逃逸】葡萄球菌 A 蛋白（SPA）是如何逃避吞噬杀伤的？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **机制**：SPA 非特异性结合人 **IgG 的 Fc 段**。\n• **后果**：遮蔽 Fc 受体结合位点，彻底**阻断 IgG 的生理调理吞噬作用**。"}]},
        "pointType": "逃逸机制", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【外毒素分类】外毒素三大临床分类及其代表是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **神经毒素**：破伤风毒素（强直痉挛）；肉毒毒素（弛缓性麻痹）。\n• **细胞毒素**：白喉毒素（失活 EF-2 抑制蛋白质翻译）。\n• **肠毒素**：霍乱肠毒素（cAMP 暴增致剧烈水样米泔水腹泻）。"}]},
        "pointType": "毒素分类", "starRating": "★★★", "importance": 3
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【易感感染】机会致病菌“异位寄生”典型疾病举例。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **尿路感染**：肠道大肠埃希菌逆行侵入尿道引起膀胱炎与肾盂肾炎。\n• **急性腹膜炎**：阑尾穿孔后肠道菌群大量进入腹膜腔引发弥漫化脓性腹膜炎。"}]},
        "pointType": "异位寄生", "starRating": "★★★", "importance": 3
    }
]

DECK_06_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心定义】什么是病毒？其独特性状有哪些？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：体积微小、无细胞结构、单一核酸、严格活细胞内寄生的非细胞型微生物。\n• **独特性状**：纳米尺度；单一核酸（DNA或RNA）；分子水平自我复制；抗生素无效，**干扰素敏感**。"}]},
        "pointType": "核心定义", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【度量与病毒体】测量病毒大小的单位是什么？什么是“病毒体”？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **度量单位**：**纳米（nm）**，通常在 20~300 nm 之间，电镜观察。\n• **病毒体（Virion）**：成熟的、结构完整的、在细胞外具备感染性的**单个病毒颗粒**。"}]},
        "pointType": "形态概念", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【基本结构】什么是病毒的“核衣壳”？核心与衣壳功能是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **核心**：病毒核酸（DNA 或 RNA），主导复制、遗传与变异。\n• **衣壳**：蛋白质外壳，功能：① 保护核酸；② 介导吸附宿主受体；③ 特异免疫原性。"}]},
        "pointType": "基本结构", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【衣壳对称】根据壳粒空间排列，病毒衣壳分为哪三种对称型？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **螺旋对称**：壳粒螺旋盘绕核酸，呈杆状/弹状（狂犬病毒、流感病毒）。\n• **20面体立体对称**：呈正 20 面体球形（脊灰病毒、腺病毒、HSV）。\n• **复合对称**：兼具两者或复杂结构（痘病毒、蝌蚪状噬菌体）。"}]},
        "pointType": "对称类型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【包膜与刺突】包膜有何功能？乙醚敏感试验有何鉴别意义？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **包膜与刺突**：宿主膜脂双层镶嵌病毒糖蛋白刺突，负责受体结合吸附。\n• **乙醚敏感试验**：\n  • **有包膜病毒**（流感、新冠、HBV）：对乙醚等脂溶剂**高度敏感**。\n  • **无包膜裸露病毒**（脊灰、HAV）：对乙醚**耐受**。"}]},
        "pointType": "包膜特性", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【增殖机制】简述病毒在活细胞内自我复制增殖的六大连续阶段。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **吸附**：刺突/衣壳结合特异受体。\n② **穿入**：膜融合或吞饮入胞。\n③ **脱壳**：脱去衣壳释放核酸。\n④ **生物合成**：复制核酸并合成结构/非结构蛋白（隐蔽期）。\n⑤ **组装**：装配成子代核衣壳。\n⑥ **释放**：裂解释放或出芽释放。"}]},
        "pointType": "复制周期", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【生化阶段】什么是病毒复制中的“隐蔽期”（Eclipse period）？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **概念**：生物合成期母代病毒已脱壳，子代病毒尚未装配成熟。\n• **特征**：此时在细胞内**无法检测出具有感染性的完整病毒颗粒**。"}]},
        "pointType": "生化阶段", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【释放方式】裂解释放与出芽释放有何本质区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **裂解释放**：多数**无包膜病毒**（如脊灰病毒），病毒大批积聚致细胞破裂死亡。\n• **出芽释放**：多数**有包膜病毒**（如流感、HIV），借由宿主细胞膜出芽包裹，细胞暂不破裂。"}]},
        "pointType": "释放方式", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【异常增殖】什么是病毒的“顿挫感染”与非容许细胞？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **非容许细胞**：不能提供病毒完整复制所需条件的宿主细胞。\n• **顿挫感染**：病毒侵入非容许细胞后，因缺乏必要因子**不能产生感染性子代病毒**的现象。"}]},
        "pointType": "异常增殖", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频实例】什么是缺陷病毒？丁肝（HDV）如何依赖乙肝（HBV）？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **缺陷病毒**：基因组不完整，必须在辅助病毒协助下才能增殖。\n• **HDV 实例**：丁型肝炎病毒缺乏包膜蛋白基因，必须在 **乙型肝炎病毒（HBV）** 提供 HBsAg 协助下才能组装成成熟病毒颗粒。"}]},
        "pointType": "经典实例", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【相互作用】什么是病毒的“干扰现象”？其发生机制是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **定义**：前一种病毒感染显著抑制后一种病毒的复制增殖。\n• **机制**：\n  ① 刺激宿主细胞产生**干扰素（IFN）**；\n  ② 竞争受体结合位点；\n  ③ 抢占宿主核糖体与转录酶系。"}]},
        "pointType": "干扰现象", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【理化耐受】温度对病毒活性有何影响？常规灭活标准是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **特性**：耐冷不耐热，-70℃ 或液氮可长年保存。\n• **常规灭活**：**56℃ 加热 30 min** 使绝大多数病毒衣壳/刺突变性灭活。*(注：HBV较耐热需煮沸10min以上)*"}]},
        "pointType": "理化因素", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【理化耐受】化学消毒剂与抗生素对病毒的灭活效果如何？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **消毒剂有效**：过氧乙酸、84次氯酸钠、碘伏、75%乙醇能高效破坏衣壳与核酸灭活病毒。\n• **抗生素无效**：常规抗生素靶向细胞壁与细菌核糖体，对病毒**完全无效**。"}]},
        "pointType": "消毒用药", "starRating": "★★★", "importance": 3
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【遗传变异】抗原漂移与抗原转变（流感病毒）有何区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **抗原漂移**：基因点突变引起轻度量变，引起每年**季节性小流行**。\n• **抗原转变**：基因片段重组引起剧烈质变，产生全新 HA/NA 亚型，易酿成**全球大流行**。"}]},
        "pointType": "变异机制", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【概念辨析】什么是感染性核酸？哪些病毒具有此特性？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **概念**：脱去衣壳的纯化裸露病毒核酸，直接转染细胞仍能独立复制出完整子代病毒。\n• **代表**：主要是**单正链 RNA（+ssRNA）病毒**（如脊灰病毒、HAV、冠状病毒）。"}]},
        "pointType": "深度考点", "starRating": "★★☆", "importance": 2
    }
]

DECK_07_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【传播途径】什么是水平传播与垂直传播？垂直传播常见病毒有哪些？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **水平传播**：个体之间横向播散（呼吸道、消化道、血行、性接触、蚊虫）。\n• **垂直传播**：母体经胎盘、产道、哺乳传给子代（TORCH病原体：风疹、巨细胞、HSV，以及 HBV、HIV）。"}]},
        "pointType": "传播途径", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【病变效应】什么是细胞病变效应（CPE）？有何实验价值？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **概念**：溶细胞型病毒在体外培养细胞内增殖引起的细胞退行性变性。\n• **特征**：细胞变圆、皱缩、脱落、溶解死亡（用于病毒定量测定与中和试验）。"}]},
        "pointType": "细胞病变", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【融合巨细胞】麻疹病毒与 RSV 如何诱导多核巨细胞（合胞体）？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **机制**：病毒编码融合蛋白（F蛋白）表达于细胞膜，介导受染细胞与邻近细胞发生**直接膜融合**形成多核巨细胞，利于病毒逃避游离中和抗体直接扩散。"}]},
        "pointType": "合胞体", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【特征病理】什么是包涵体？狂犬病毒特异包涵体叫什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **概念**：病毒在受染细胞核内或胞质内聚集形成的特征性斑块结构。\n• **内基小体（Negri body）**：**狂犬病毒**在脑神经细胞胞质内形成的嗜酸性包涵体，为确诊狂犬病金标准。"}]},
        "pointType": "经典病理", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【免疫损伤】病毒感染如何通过体液和细胞免疫引起机体损伤？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **体液损伤（III型）**：游离抗原与抗体形成循环免疫复合物沉积于血管和肾脏，引起血管炎与肾炎（如乙肝肾炎）。\n• **细胞损伤（IV型）**：特异性 **CD8+ CTL** 杀伤清除感染靶细胞的同时，造成组织大面积坏死（如乙肝重症肝坏死）。"}]},
        "pointType": "免疫病理", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】病毒持续性感染分为哪三大主要类型？各举一例。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **慢性感染**：病毒长期存在且**持续低水平排毒**（HBV、HCV）。\n• **潜伏感染**：病毒潜伏在神经节，**间歇期不排毒**，免疫下降时激活复发（HSV、带状疱疹 VZV）。\n• **慢发病毒感染**：潜伏期数年，发病后进行性加重致死（麻疹 SSPE、朊粒）。"}]},
        "pointType": "三大感染类型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【潜伏复发】水痘-带状疱疹病毒初次感染与复发有何不同？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **初次感染（儿童）**：经呼吸道侵入血流引起全身水疱疹，即**水痘**。\n• **激活复发（成人）**：潜伏于**脊髓后根神经节**的病毒受刺激复发，沿单侧神经节段引起皮疹伴剧痛，即**带状疱疹**。"}]},
        "pointType": "经典实例", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心分类】干扰素（IFN）主要分为哪两大类？各由什么细胞产生？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **I 型（抗病毒）**：**IFN-α**（白细胞产生）、**IFN-β**（成纤维细胞产生）。\n• **II 型（免疫调节）**：**IFN-γ**（活化 T 细胞和 NK 细胞产生，强效激活巨噬细胞）。"}]},
        "pointType": "干扰素分型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【黄金大题】干扰素抗病毒的生化分子机制（AVP）是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "干扰素不直接杀灭游离病毒，结合受体诱导**抗病毒蛋白（AVP）**：\n① **2-5A合成酶途径**：激活 RNase L **降解病毒 mRNA**。\n② **蛋白激酶 PKR 途径**：磷酸化失活 eIF-2，**阻断蛋白质翻译起始**。"}]},
        "pointType": "分子机制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频特性】简述干扰素（IFN）的四大生物学特性。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "① **广谱抗病毒**：对多种不同 DNA/RNA 病毒均有效。\n② **高活性**：极微量即可建立保护状态。\n③ **种属特异性**：人干扰素主要在人细胞上发挥最高活性。\n④ **间接抗病毒**：通过活细胞诱导 AVP 起效，体外直接接触不杀灭病毒。"}]},
        "pointType": "四大特性", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【特异抗体】中和抗体在抗病毒免疫中起什么核心作用？局限是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **核心作用**：特异结合病毒表面刺突或衣壳，**阻断病毒吸附与穿入**，介导巨噬细胞吞噬清除。\n• **核心局限**：**仅能清除细胞外游离病毒**，对细胞内病毒无效。"}]},
        "pointType": "中和抗体", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【局部防线】分泌型 IgA（sIgA）在黏膜抗病毒防御中有何地位？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **分布**：呼吸道、消化道黏膜表面外分泌液中。\n• **功能**：阻断病毒在黏膜表面上皮细胞的定植黏附，是黏膜抗感染的第一道特异防线。"}]},
        "pointType": "黏膜免疫", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【免疫抑制】HIV 是如何导致机体免疫功能全面崩溃的？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **靶细胞**：gp120 特异性结合人辅助性 T 细胞的 **CD4 受体**及辅助受体。\n• **后果**：直接破坏耗竭全身 **CD4+ T 淋巴细胞**，致使体液与细胞免疫调节中枢瘫痪（艾滋病）。"}]},
        "pointType": "免疫抑制", "starRating": "★★★", "importance": 3
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【病毒致癌】举出三种常见致癌病毒及其诱发的恶性肿瘤。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **高危型 HPV（16, 18型）**：诱发**宫颈癌**。\n• **EB 病毒（EBV）**：诱发**鼻咽癌**和伯基特淋巴瘤。\n• **HBV / HCV**：诱发**原发性肝细胞癌（HCC）**。"}]},
        "pointType": "病毒肿瘤", "starRating": "★★☆", "importance": 2
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【慢发感染】慢发病毒感染与潜伏感染有何根本区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **潜伏感染**：间歇期不排毒，反复发作并有完全缓解期（如单纯疱疹）。\n• **慢发病毒感染**：潜伏期数年，发病后呈持续不可逆单向恶化致死，无缓解期（如 SSPE）。"}]},
        "pointType": "概念辨析", "starRating": "★★★", "importance": 3
    }
]

DECK_08_CARDS = [
    {
        "c": 1,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心属性】真菌属于哪类微生物？细胞壁与细菌有何区别？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **类别**：**真核细胞型微生物**（有完整核膜、核仁、细胞器完备）。\n• **细胞壁**：主要由**几丁质、葡聚糖、甘露聚糖**构成，**完全不含肽聚糖**（青霉素类抗生素对其天然无效）。"}]},
        "pointType": "细胞结构", "starRating": "★★★", "importance": 3
    },
    {
        "c": 2,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药物靶分子】真菌细胞膜特有的固醇成分是什么？有何意义？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **特有成分**：**麦角固醇（Ergosterol）**（动物细胞膜为胆固醇）。\n• **意义**：是两性霉素 B、唑类等抗真菌药物高度选择性打击的关键分子靶点。"}]},
        "pointType": "分子靶点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 3,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【形态分类】酵母型真菌与类酵母型真菌有何区别？代表菌是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **酵母型真菌**：单细胞出芽，无菌丝，如**新生隐球菌**（具宽厚**多糖荚膜**，用墨汁负染镜检）。\n• **类酵母型真菌**：出芽延长形成**假菌丝（Pseudohypha）**，如**白假丝酵母菌（白念珠菌）**。"}]},
        "pointType": "单细胞真菌", "starRating": "★★★", "importance": 3
    },
    {
        "c": 4,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【多细胞结构】丝状真菌（霉菌）的菌丝和孢子各具什么特征？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **菌丝**：管状丝状物，分为**有隔菌丝**（曲霉、青霉）与**无隔菌丝**（毛霉）；按功能分**营养菌丝**与**气生菌丝**。\n• **孢子**：真菌的繁殖器官，耐热性弱（60℃ 1h 灭活），与细菌休眠芽胞截然不同。"}]},
        "pointType": "多细胞结构", "starRating": "★★★", "importance": 3
    },
    {
        "c": 5,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【培养特性】真菌培养基是什么？生长环境（pH/温度）有何特点？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **培养基**：**沙氏葡萄糖琼脂（SDA）**。\n• **环境特点**：**嗜弱酸性（pH 4.0~6.0）**；最适生长温度 **22~28℃**（深部菌 37℃）；生长缓慢（需数天至数周）。"}]},
        "pointType": "培养特性", "starRating": "★★★", "importance": 3
    },
    {
        "c": 6,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【菌落表型】简述固体培养基上真菌形成的三大典型菌落特征。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **酵母型菌落**：湿润、光滑、黏稠似细菌菌落（隐球菌）。\n• **类酵母型菌落**：似酵母菌落但假菌丝向琼脂深层扎根（白念珠菌）。\n• **丝状菌落**：绒毛状、絮状或粉末状，常带鲜艳色素（曲霉、青霉）。"}]},
        "pointType": "菌落类型", "starRating": "★★★", "importance": 3
    },
    {
        "c": 7,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【抵抗力与药敏】真菌对理化因素的抵抗力与药敏有何特点？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **抵抗力**：对干燥、紫外线抵抗力强；**对热敏感（60℃ 1小时杀灭）**。\n• **药敏**：抗细菌抗生素天然耐受；对抗真菌药（两性霉素B、氟康唑、卡泊芬净）敏感。"}]},
        "pointType": "理化特性", "starRating": "★★★", "importance": 3
    },
    {
        "c": 8,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【临床高危】常见的四大条件致病真菌有哪些？三大诱因是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **四大菌**：**白假丝酵母菌（白念珠菌）、新生隐球菌、曲霉、毛霉**。\n• **三大诱因**：① 长期滥用广谱抗生素（二重感染）；② 激素/免疫抑制剂/放化疗；③ 艾滋病（AIDS）。"}]},
        "pointType": "条件致病", "starRating": "★★★", "importance": 3
    },
    {
        "c": 9,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【毒素致癌】黄曲霉毒素主要污染何种食品？有何严重危害？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **来源**：黄曲霉污染发霉的**花生、玉米、粮油**产生的剧毒代谢物。\n• **危害**：强肝脏毒性，世界卫生组织 I 类强致癌物，特异诱发**原发性肝细胞癌（HCC）**。"}]},
        "pointType": "真菌毒素", "starRating": "★★★", "importance": 3
    },
    {
        "c": 10,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药物机制】多烯类抗真菌药（两性霉素B）的分子机制是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **靶点**：直接结合细胞膜上的**麦角固醇**。\n• **机制**：在膜上形成跨膜微孔，导致胞内 **K+ 钾离子大量外漏**，真菌崩解死亡。"}]},
        "pointType": "药物靶点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 11,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药物机制】唑类抗真菌药（氟康唑、伏立康唑）的分子机制是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **靶点**：抑制**羊毛甾醇 14α-脱甲基酶（CYP51）**。\n• **机制**：阻断羊毛甾醇向麦角固醇转化，导致麦角固醇匮乏破坏膜完整性。"}]},
        "pointType": "药物靶点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 12,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【药物机制】棘白菌素类抗真菌药（卡泊芬净）的作用靶点和机制是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **靶点**：真菌细胞壁 **β-1,3-葡聚糖合成酶**。\n• **机制**：阻断细胞壁核心多糖骨架合成，使细胞壁完整性丧失渗透裂解（人体无细胞壁，毒性低）。"}]},
        "pointType": "药物靶点", "starRating": "★★★", "importance": 3
    },
    {
        "c": 13,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【靶点总结】常用抗真菌药物的三大作用靶点速查。"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **细胞膜结合打孔**：多烯类（两性霉素B、制霉菌素）。\n• **抑制膜固醇合成**：唑类（氟康唑、伊曲康唑）。\n• **抑制细胞壁合成**：棘白菌素类（卡泊芬净）。"}]},
        "pointType": "靶点总结", "starRating": "★★★", "importance": 3
    },
    {
        "c": 14,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【染色诊断】脑脊液中检查新生隐球菌的经典染色方法与特征是什么？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **方法**：**墨汁负染色法**。\n• **镜下特征**：黑色视野背景中，可见圆形单细胞外围环绕一圈**宽厚清晰透亮的透明晕**，可确诊隐球菌脑膜炎。"}]},
        "pointType": "经典诊断", "starRating": "★★★", "importance": 3
    },
    {
        "c": 15,
        "f": {"flashcardContentBlock": [{"type": "text", "content": "【临床假丝】白假丝酵母菌引起人体浅表黏膜感染的两种典型病症？"}]},
        "b": {"flashcardContentBlock": [{"type": "text", "content": "• **鹅口疮**：儿童或免疫低下者颊、舌黏膜表面附着**凝乳状白色假膜**。\n• **霉菌性阴道炎**：女性剧烈外阴瘙痒伴**豆腐渣样/凝乳块状白色阴道分泌物**。"}]},
        "pointType": "临床病症", "starRating": "★★★", "importance": 3
    }
]

ALL_DECKS = [
    (1, "01 绪论", DECK_01_CARDS),
    (2, "02 细菌形态与结构", DECK_02_CARDS),
    (3, "03 细菌的生理", DECK_03_CARDS),
    (4, "04 细菌的遗传与变异", DECK_04_CARDS),
    (5, "05 细菌的感染与免疫", DECK_05_CARDS),
    (6, "06 病毒的基本性状", DECK_06_CARDS),
    (7, "07 病毒的感染", DECK_07_CARDS),
    (8, "08 真菌学总论", DECK_08_CARDS),
]

def main():
    base_assets = r"d:\Code\Android\flashcard\app\src\main\assets\subjects\microbiology"
    decks_dir = os.path.join(base_assets, "decks")
    
    for ch_num, ch_title, cards in ALL_DECKS:
        uid = f"micro_0{ch_num}"
        p1 = os.path.join(decks_dir, f"{uid}.json")
        p2 = os.path.join(decks_dir, f"{ch_title} 闪卡.json")
        
        # Read existing deck metadata if present
        meta_title = f"{ch_title} 闪卡"
        meta_desc = "医学微生物学核心考点"
        covered = []
        followUp = []
        if os.path.exists(p1):
            with open(p1, "r", encoding="utf-8") as f:
                old_d = json.load(f)
                meta_title = old_d.get("title", meta_title)
                meta_desc = old_d.get("description", meta_desc)
                topics = old_d.get("topics", {})
                covered = topics.get("covered", [])
                followUp = topics.get("followUp", [])
                
        new_deck = {
            "id": uid,
            "title": meta_title,
            "description": meta_desc,
            "topics": {
                "covered": covered,
                "followUp": followUp
            },
            "flashcards": cards
        }
        
        content = json.dumps(new_deck, ensure_ascii=False, indent=2)
        with open(p1, "w", encoding="utf-8") as f:
            f.write(content)
        with open(p2, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {uid} with {len(cards)} concise cards.")

if __name__ == "__main__":
    main()
