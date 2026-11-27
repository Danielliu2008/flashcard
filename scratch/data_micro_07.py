# -*- coding: utf-8 -*-
"""
Microbiology Chapter 7: 病毒的感染
Based strictly on 06-C03病毒学-02病毒的感染.pdf page 3 掌握要求
"""

DECK_07 = {
    "id": "micro_07",
    "title": "07 病毒的感染 闪卡",
    "description": "医学微生物学·病毒传播途径（水平与垂直传播）、致病机制（CPE/合胞体/内基小体/免疫病理）、持续性感染三大类型、干扰素机制与中和抗体核心考点",
    "topics": {
        "covered": [
            "水平传播与垂直传播（TORCH综合征）概念与病原体",
            "病毒直接损伤细胞机制：CPE、合胞体与包涵体（内基小体）",
            "病毒引起的免疫病理损伤（免疫复合物病与CTL组织破坏）",
            "急性感染与持续性感染三大分类标准",
            "慢性感染（HBV）、潜伏感染（HSV/带状疱疹VZV）与慢发感染（SSPE/朊粒）",
            "干扰素（IFN）分类（I型抗病毒 vs II型免疫调节）",
            "干扰素抗病毒机制（AVP：2-5A合成酶与蛋白激酶PKR）",
            "干扰素四大生物学特性（广谱/高活性/种属特异/间接抗病毒）",
            "特异性体液免疫：中和抗体与局部黏膜sIgA阻断机制"
        ],
        "followUp": [
            "真菌的真核结构、麦角固醇靶点与抗真菌药物机制",
            "条件致病真菌的感染特点与二重感染表现"
        ]
    },
    "flashcards": [
        {
            "c": 1,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【传播途径】什么是水平传播与垂直传播？引起垂直传播的常见病毒有哪些？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **水平传播（Horizontal transmission）**：病毒在人群个体之间横向播散传播（经呼吸道飞沫、消化道粪-口、血液注射、性接触、蚊虫叮咬等途径）。\n2. **垂直传播（Vertical transmission）**：病原体由亲代直接传给子代的垂直途径，主要包括经**胎盘感染**、分娩时经**产道感染**以及产后通过**哺乳**传播。\n3. **引起垂直传播的常见病毒**：\n   - **TORCH综合征病原体**：风疹病毒（Rubella）、巨细胞病毒（CMV）、单纯疱疹病毒（HSV）；\n   - **乙型肝炎病毒（HBV）**（母婴垂直传播主要发生于围产期产道撕裂微量母血暴露）；\n   - **人类免疫缺陷病毒（HIV）**。"}]},
            "pointType": "传播途径",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 2,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【病变效应】什么是细胞病变效应（CPE）？在病毒学体外培养中有何应用价值？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **定义**：溶细胞型病毒在体外培养的宿主单层细胞内增殖时，直接引起的肉眼或低倍光学显微镜下可见的**细胞退化变性形态学改变**，称为细胞病变效应（Cytopathic effect, CPE）。\n2. **典型镜下特征**：正常平铺细胞发生变圆、皱缩、折光性增强、颗粒增多、细胞膜溶解、大面积从培养瓶壁脱落死亡。\n3. **实验应用**：CPE是体外细胞培养中直观判断病毒是否存在、完成病毒定量（如TCID50滴定）以及进行病毒中和试验的经典指标。"}]},
            "pointType": "细胞病变",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 3,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【融合巨细胞】麻疹病毒与呼吸道合胞病毒（RSV）感染如何诱导多核巨细胞（合胞体）形成？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **机制**：有包膜病毒在宿主细胞内增殖时，其合成的**融合蛋白（Fusion protein，F蛋白）**修饰并表达在受染细胞的细胞膜表面；\n2. **合胞体形成**：修饰有F蛋白的感染细胞膜能直接与周围未受染的健康邻近细胞膜发生**直接接触膜融合**；\n3. **病理结果**：大量相邻细胞的细胞质连通融合在一起，形成含有数十个甚至数百个细胞核的大型**多核巨细胞（合胞体）**，使病毒无需暴露在细胞外液即可直接在细胞间快速扩散，有效逃避游离中和抗体的杀伤。"}]},
            "pointType": "合胞体",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 4,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【特征病理】什么是包涵体（Inclusion body）？狂犬病病毒引起的特异性包涵体叫什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：某些病毒感染宿主细胞后，在细胞核内或细胞质内聚集形成的光学显微镜下可见的、具有特异染色性质（嗜酸性或嗜碱性）的圆形或卵圆形斑块状团块。其本质为病毒核衣壳聚集物或细胞应激变性产物。\n2. **狂犬病毒特异性包涵体**：**内基小体（Negri body）**。\n   - 位于狂犬病患者或感染动物脑组织海马回及小脑普肯耶细胞的**细胞质内**，呈鲜红嗜酸性圆形斑块；\n   - 是病理组织学确诊狂犬病的绝对特异性金标准依据。"}]},
            "pointType": "经典病理",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 5,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【免疫损伤】病毒感染如何通过体液免疫和细胞免疫引起机体病理损伤？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **体液免疫病理（III型变态反应）**：\n   - 慢性感染（如HBV）时，病毒游离抗原（如HBsAg）与特异性抗体结合形成中等大小循环免疫复合物；\n   - 复合物沉积在肾小球基底膜或全身中小动脉壁，激活补体引起血管炎、膜性肾小球肾炎与关节炎。\n2. **细胞免疫病理（IV型变态反应）**：\n   - 宿主特异性**CD8+ CTL（细胞毒性T细胞）**识别感染细胞表面的病毒肽-MHC-I类分子复合物；\n   - CTL大量释放穿孔素和颗粒酶特异性裂解靶细胞（如乙肝暴发时，CTL大量杀伤感染的肝细胞导致急性大面积肝坏死，实质是机体自身细胞免疫过度造成的免疫损伤）。"}]},
            "pointType": "免疫病理",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 6,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲重点】病毒持续性感染分为哪三大主要类型？请举出各类的代表病毒。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "持续性感染指病毒在宿主体内长期存在，按病程与排毒特征分为三大类型：\n1. **慢性感染（Chronic infection）**：显性或隐性感染后，病毒长期未被彻底清除，在体内**持续低水平复制并不断向体外排毒**，病程迁延数月甚至数十年（如**乙型肝炎病毒HBV**、丙型肝炎病毒HCV）；\n2. **潜伏感染（Latent infection）**：原发感染后，病毒基因组潜伏于特定神经节或组织内，**间歇潜伏期内不复制也不排毒**；在机体免疫力下降时被激活大量复制引起复发（如**单纯疱疹病毒HSV**、**水痘-带状疱疹病毒VZV**）；\n3. **慢发病毒感染（Slow virus infection）**：潜伏期极长（数年到数十年），无临床症状；一旦发病呈亚急性、慢性进行性加重，最终100%致死（如麻疹病毒引起的**亚急性硬化性全脑炎SSPE**、朊粒引起的克雅病CJD）。"}]},
            "pointType": "三大感染类型",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 7,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【潜伏复发】水痘-带状疱疹病毒（VZV）初次感染与复发时，其临床表现有何截然不同？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "VZV是典型的神经节潜伏感染病毒：\n1. **儿童初次感染**：经呼吸道侵入血流，引起全身泛发性皮疹、水疱和发热，临床表现为**水痘（Chickenpox）**；\n2. **病毒长期潜伏**：水痘痊愈后，少量病毒沿感觉神经纤维逆行潜伏在**脊髓后根神经节或颅神经感觉神经节**中，处于休眠状态；\n3. **成人激活复发**：中年以后或机体免疫力低下（劳累、肿瘤放疗等）时，潜伏的病毒被重新激活，沿感觉神经轴索下行到该神经支配的单侧皮肤节段大量复制，引起剧烈神经痛和沿神经带状分布的集簇水疱，临床表现为**带状疱疹（Shingles/Herpes zoster）**。"}]},
            "pointType": "经典实例",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 8,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【核心分类】干扰素（Interferon, IFN）主要分为哪两大类？各自由什么细胞产生？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **I型干扰素（抗病毒干扰素）**：\n   - **IFN-α（白细胞干扰素）**：主要由被病毒感染的人体**人外周血白细胞（单核-巨噬细胞、B细胞）**产生；\n   - **IFN-β（成纤维细胞干扰素）**：主要由受染的**成纤维细胞及上皮细胞**产生；\n   - *功能*：直接诱导细胞建立强大的广谱抗病毒状态，抑制病毒核酸与蛋白质合成。\n2. **II型干扰素（免疫干扰素）**：\n   - **IFN-γ**：主要由受特异性抗原刺激活化的**T淋巴细胞（Th1细胞、CTL）和NK细胞**合成分泌；\n   - *功能*：主要发挥强效的**免疫调节作用**，强效激活巨噬细胞吞噬杀伤活性，促进MHC分子表达。"}]},
            "pointType": "干扰素分型",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 9,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【大纲黄金大题】干扰素（IFN）发挥广谱抗病毒作用的生化分子机制是什么？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "干扰素**不直接杀灭游离病毒**，而是通过诱导宿主产生**抗病毒蛋白（AVP）**阻断病毒增殖，两大核心生化途径为：\n1. **2'-5'寡腺苷酸合成酶（2-5A合成酶）途径 —— 降解病毒mRNA**：\n   - 干扰素诱导合成无活性的2-5A合成酶，被病毒双链RNA（dsRNA）激活后催化ATP合成2'-5'寡腺苷酸；\n   - 2-5A进而特异性激活宿主细胞内的**核酸内切酶RNase L**，将病毒mRNA广泛切断降解。\n2. **蛋白激酶PKR途径 —— 阻断蛋白质翻译**：\n   - 干扰素诱导合成PKR，被病毒dsRNA激活后发生自身磷酸化，进而催化**真核翻译起始因子-2（eIF-2）发生磷酸化而失活**；\n   - 彻底阻断了病毒核糖体蛋白质多肽链的翻译起始，使病毒无法合成任何衣壳蛋白或酶。"}]},
            "pointType": "分子机制",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 10,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【高频特性】简述干扰素（IFN）的四大生物学特性。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **广谱抗病毒性**：一种干扰素对多种完全不同种属的DNA病毒和RNA病毒均具有显著抑制作用（无病毒特异性）；\n2. **超高生物活性**：极微量纳克级水平即可使靶细胞建立强大的抗病毒防护状态；\n3. **严格的种属特异性**：干扰素必须与同种属生物细胞膜上的特异受体结合才能高效诱导AVP。例如**人干扰素只在人体细胞上表现出最高活性**，对啮齿类或鸡细胞活性极低；\n4. **间接抗病毒性（作用于宿主细胞）**：体外将干扰素与病毒直接混合，并不能灭活或裂解病毒颗粒，必须通过活细胞介导合成AVP才能阻断病毒。"}]},
            "pointType": "四大特性",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 11,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【特异抗体】中和抗体（Neutralizing antibody）在抗病毒免疫中起什么核心作用？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **分子靶点**：中和抗体（主要为血清IgG、部分IgM）特异性结合病毒表面的**衣壳蛋白或包膜刺突受体结合域**；\n2. **作用机制**：\n   - **位阻效应**：空间遮蔽受体结合位点，直接阻止病毒吸附宿主敏感细胞；\n   - **构象破坏**：改变病毒表面构象，阻断病毒穿入与脱壳过程；\n   - **介导吞噬清除**：抗体结合后的免疫复合物被单核-巨噬细胞吞噬清除；\n3. **核心局限**：**仅能清除细胞外游离的病毒体**，对已侵入细胞内的病毒无能为力。"}]},
            "pointType": "中和抗体",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 12,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【局部防线】分泌型IgA（sIgA）在黏膜抗病毒防御中有何不可替代的地位？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **分布部位**：由呼吸道、消化道及生殖道黏膜固有层浆细胞合成，经分泌片（SC）转运至**黏膜表面外分泌液**（唾液、胃肠液、呼吸道黏液、初乳）中；\n2. **核心防御功能**：\n   - 具有双体结构且耐受蛋白酶消化分解；\n   - 能在机体黏膜入口表面直接特异性结合入侵的流感病毒、冠状病毒、轮状病毒等；\n   - **在体外阻断病毒黏附侵入黏膜上皮细胞**，是防御呼吸道和肠道黏膜局部病毒感染的最关键特异性第一道防线。"}]},
            "pointType": "黏膜免疫",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 13,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【免疫抑制】人类免疫缺陷病毒（HIV）是如何导致机体免疫功能全面崩溃的？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **特异性侵入靶细胞**：HIV表面包膜糖蛋白gp120高度特异性结合人辅助性T淋巴细胞表面的**CD4受体**及趋化因子辅助受体（CCR5或CXCR4）；\n2. **大量破坏核心指挥细胞**：HIV在CD4+ T细胞内增殖，通过直接溶细胞、诱导合胞体溶解以及促发细胞凋亡等机制，造成全身**CD4+ T淋巴细胞数量急剧进行性耗竭下降**；\n3. **全身体液与细胞免疫瘫痪**：由于CD4+ Th细胞是免疫应答的核心枢纽，其衰竭导致机体无法抵抗各种机会性病原体感染和肿瘤监视失败，最终发展为获得性免疫缺陷综合征（AIDS）。"}]},
            "pointType": "免疫抑制",
            "starRating": "★★★",
            "importance": 3
        },
        {
            "c": 14,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【病毒致癌】请举出三种已被证实与人类恶性肿瘤发生直接相关的致癌病毒及其所致肿瘤。"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **人乳头瘤病毒（HPV，特别是高危型HPV 16, 18型）**：其E6、E7癌蛋白分别失活抑癌基因p53和pRb，导致宫颈上皮恶性转化，是引发**宫颈癌**的首要病因；\n2. **EB病毒（EBV）**：与人类**鼻咽癌（NPC）**及儿童**伯基特淋巴瘤（Burkitt lymphoma）**的发生密切相关；\n3. **乙型肝炎病毒（HBV） / 丙型肝炎病毒（HCV）**：长期慢性肝炎与肝纤维化硬化，协同HBx反式激活蛋白作用，直接驱动**原发性肝细胞癌（HCC）**的发生。"}]},
            "pointType": "病毒肿瘤",
            "starRating": "★★☆",
            "importance": 2
        },
        {
            "c": 15,
            "f": {"flashcardContentBlock": [{"type": "text", "content": "【慢发感染】什么是慢发病毒感染（Slow virus infection）？与潜伏感染有何根本区别？"}]},
            "b": {"flashcardContentBlock": [{"type": "text", "content": "1. **概念**：病毒侵入机体后潜伏期长达数月、数年甚至十几年，期间无明显症状；一旦发病，呈现慢性、进行性、亚急性恶化，**患者最终呈致死性神经衰竭结局**。\n2. **与潜伏感染的根本区别**：\n   - **潜伏感染**（如单纯疱疹、带状疱疹）：病毒潜伏在神经节，受刺激后急性发作皮疹，间歇期完全缓解恢复正常，**间歇期不排毒，反复发作**；\n   - **慢发病毒感染**（如麻疹后SSPE、朊粒病）：从潜伏期转为发病后**病程持续进行性单向恶化，无任何缓解间歇期**，不可逆直至死亡。"}]},
            "pointType": "概念辨析",
            "starRating": "★★★",
            "importance": 3
        }
    ]
}

QUIZ_07 = {
    "quiz": [
        # --- 单选题 (1~10) ---
        {
            "id": 1,
            "type": "multiple_choice",
            "question": "病原体由母亲经由胎盘、产道或哺乳途径直接传给胎儿或新生儿的传播方式称为：",
            "options": [
                {"text": "垂直传播（Vertical transmission）", "isCorrect": True, "rationale": "正确。由母体直接传给后代的方式即为垂直传播。"},
                {"text": "水平传播（Horizontal transmission）", "isCorrect": False, "rationale": "水平传播是人群个体之间的横向传播。"},
                {"text": "虫媒传播", "isCorrect": False, "rationale": "属于水平传播的节肢动物媒介途径。"},
                {"text": "医源性传播", "isCorrect": False, "rationale": "属于医疗操作引起的传播。"}
            ],
            "hint": "从母体到胎儿或婴儿的垂直传递。",
            "rationale": "垂直传播是指病原体从母体直接传递给子代的传播途径，包括经胎盘、经产道和哺乳三种方式。"
        },
        {
            "id": 2,
            "type": "multiple_choice",
            "question": "狂犬病毒感染患者或感染动物后，在小脑普肯耶细胞及大脑海马回胞质内形成的特异性嗜酸性包涵体称为：",
            "options": [
                {"text": "内基小体（Negri body）", "isCorrect": True, "rationale": "正确。狂犬病毒在神经细胞质内形成的嗜酸性包涵体称为内基小体，是狂犬病病理确诊依据。"},
                {"text": "高尔基小体", "isCorrect": False, "rationale": "高尔基体是正常细胞器。"},
                {"text": "网状小体", "isCorrect": False, "rationale": "衣原体细胞内繁殖形式。"},
                {"text": "原体", "isCorrect": False, "rationale": "衣原体细胞外感染形式。"}
            ],
            "hint": "狂犬病神经元特异性嗜酸性包涵体名称。",
            "rationale": "内基小体（Negri body）是狂犬病毒在脑神经细胞质内形成的特异性包涵体，对狂犬病的组织病理学确诊具有绝对诊断意义。"
        },
        {
            "id": 3,
            "type": "multiple_choice",
            "question": "单纯疱疹病毒（HSV）在原发感染控制后，病毒基因组可长期潜伏于宿主特定组织内，在间歇期内不复制也不排毒。这种感染类型属于：",
            "options": [
                {"text": "潜伏感染（Latent infection）", "isCorrect": True, "rationale": "正确。间歇期不排毒、免疫下降时复发，是潜伏感染的典型特征。"},
                {"text": "慢性感染（Chronic infection）", "isCorrect": False, "rationale": "慢性感染在整个病程中持续低水平排毒（如HBV）。"},
                {"text": "慢发病毒感染（Slow virus infection）", "isCorrect": False, "rationale": "慢发感染呈进行性不可逆致死性单向恶化。"},
                {"text": "急性感染", "isCorrect": False, "rationale": "急性感染病程短并彻底清除。"}
            ],
            "hint": "病毒潜伏在神经节，不复制不排毒，劳累发热后复发。",
            "rationale": "潜伏感染是指原发感染后病毒未被完全清除，潜伏于神经节等特定组织内，间歇期不排毒，机体抵抗力下降时可反复被激活发病。"
        },
        {
            "id": 4,
            "type": "multiple_choice",
            "question": "麻疹病毒感染儿童数年甚至十几年后，偶可引起一种亚急性进行性神经系统退化并最终致死的严重中枢神经疾病（SSPE）。这种感染属于：",
            "options": [
                {"text": "慢发病毒感染（Slow virus infection）", "isCorrect": True, "rationale": "正确。潜伏期数年，发病后呈亚急性进行性致死恶化，属于慢发病毒感染。"},
                {"text": "隐性感染", "isCorrect": False, "rationale": "SSPE有极严重的神经系统致死症状。"},
                {"text": "顿挫感染", "isCorrect": False, "rationale": "顿挫感染不产生病毒体，无致死性神经损伤。"},
                {"text": "带菌状态", "isCorrect": False, "rationale": "病毒感染不叫带菌。"}
            ],
            "hint": "潜伏期极长（数年），发病后进行性致死。",
            "rationale": "亚急性硬化性全脑炎（SSPE）是慢发病毒感染的典型代表，麻疹病毒在体内长期潜伏变异，多年后发病引起进行性脑退行性致死损害。"
        },
        {
            "id": 5,
            "type": "multiple_choice",
            "question": "干扰素（IFN）具有强大的抗病毒活性，关于其直接发挥抗病毒作用的机制，下列说法正确的是：",
            "options": [
                {"text": "与宿主细胞受体结合，诱导细胞合成2-5A合成酶和蛋白激酶PKR等抗病毒蛋白（AVP）", "isCorrect": True, "rationale": "正确。干扰素不直接杀灭病毒，而是通过活化AVP降解病毒mRNA并阻断翻译。"},
                {"text": "在宿主细胞外直接与病毒衣壳蛋白结合，促使病毒颗粒在血清中崩解沉淀", "isCorrect": False, "rationale": "干扰素在细胞外不与游离病毒直接作用。"},
                {"text": "直接激活补体经典途径对病毒包膜进行打孔溶解", "isCorrect": False, "rationale": "这是特异性抗体的功能，非干扰素功能。"},
                {"text": "特异性抑制病毒DNA反转录酶的活性", "isCorrect": False, "rationale": "这是逆转录酶抑制剂药物机制。"}
            ],
            "hint": "诱导宿主细胞产生抗病毒蛋白（AVP）。",
            "rationale": "干扰素不直接作用于病毒体，而是结合宿主细胞受体诱导产生抗病毒蛋白（2-5A合成酶与PKR），降解病毒mRNA并抑制蛋白质合成。"
        },
        {
            "id": 6,
            "type": "multiple_choice",
            "question": "干扰素的一大重要生物学特性是“种属特异性”，其具体含义是：",
            "options": [
                {"text": "某一种属生物细胞产生的干扰素，通常只在该种属的细胞上发挥最高抗病毒活性", "isCorrect": True, "rationale": "正确。如人干扰素在人体细胞上活性最高，对其他动物细胞活性极低。"},
                {"text": "一种干扰素只对某单一特定属的病毒具有抗病毒效果", "isCorrect": False, "rationale": "干扰素是广谱抗病毒的，对多种病毒均有效。"},
                {"text": "只能由特定一种白细胞产生", "isCorrect": False, "rationale": "白细胞、成纤维细胞、T细胞等均可产生不同类型干扰素。"},
                {"text": "只对具有包膜的病毒有效，对无包膜病毒无效", "isCorrect": False, "rationale": "对有无包膜病毒均有效。"}
            ],
            "hint": "注意区分‘抗病毒的广谱性’与‘作用细胞宿主的种属特异性’。",
            "rationale": "干扰素抗病毒作用是广谱的，但具有严格的宿主细胞种属特异性，人细胞合成的干扰素主要在人或灵长类细胞上发挥保护活性。"
        },
        {
            "id": 7,
            "type": "multiple_choice",
            "question": "主要由活化的T淋巴细胞（Th1细胞）和NK细胞产生，主要发挥免疫调节作用而非直接抗病毒作用的干扰素类型是：",
            "options": [
                {"text": "II型干扰素（IFN-γ / 免疫干扰素）", "isCorrect": True, "rationale": "正确。IFN-γ属于II型干扰素，主要调节巨噬细胞和特异性细胞免疫。"},
                {"text": "IFN-α（白细胞干扰素）", "isCorrect": False, "rationale": "属于I型干扰素，主要抗病毒。"},
                {"text": "IFN-β（成纤维细胞干扰素）", "isCorrect": False, "rationale": "属于I型干扰素，主要抗病毒。"},
                {"text": "肿瘤坏死因子TNF-α", "isCorrect": False, "rationale": "TNF属于促炎细胞因子，非干扰素。"}
            ],
            "hint": "由致敏T细胞产生的免疫干扰素（γ-干扰素）。",
            "rationale": "I型干扰素（IFN-α/β）主要行使广谱抗病毒功能；II型干扰素（IFN-γ）主要由T细胞和NK细胞产生，发挥强效巨噬细胞活化与免疫调节功能。"
        },
        {
            "id": 8,
            "type": "multiple_choice",
            "question": "特异性中和抗体能够有效清除细胞外的游离病毒体，其阻止病毒感染易感细胞的核心机制是：",
            "options": [
                {"text": "与病毒表面吸附蛋白/刺突特异性结合，位阻性阻断病毒与宿主细胞表面受体的结合吸附", "isCorrect": True, "rationale": "正确。空间阻断受体识别是中和抗体的核心功能。"},
                {"text": "进入宿主细胞内部特异性水解病毒单链RNA核酸", "isCorrect": False, "rationale": "抗体是大分子免疫球蛋白，无法进入活细胞内部水解核酸。"},
                {"text": "直接氧化破坏病毒衣壳的肽聚糖骨架", "isCorrect": False, "rationale": "病毒根本没有肽聚糖结构。"},
                {"text": "抑制宿主细胞核糖体的60S大亚基活性", "isCorrect": False, "rationale": "中和抗体不抑制宿主核糖体。"}
            ],
            "hint": "阻止病毒结合靶细胞膜受体。",
            "rationale": "中和抗体结合在病毒体表面抗原决定簇上，封闭了病毒与细胞表面受体的结合部位，阻碍病毒吸附穿入，并介导吞噬清除。"
        },
        {
            "id": 9,
            "type": "multiple_choice",
            "question": "人类免疫缺陷病毒（HIV）主要特异性侵犯并破坏下列哪种关键免疫细胞，导致宿主细胞免疫与体液免疫功能全面衰竭？",
            "options": [
                {"text": "CD4+ T淋巴细胞（辅助性T细胞）", "isCorrect": True, "rationale": "正确。HIV的gp120高度亲和CD4受体，造成CD4+ T细胞大量死亡耗竭。"},
                {"text": "CD8+ 细胞毒性T淋巴细胞（CTL）", "isCorrect": False, "rationale": "HIV主要侵犯CD4+细胞，导致CD4/CD8比值严重倒置。"},
                {"text": "中性粒细胞", "isCorrect": False, "rationale": "非HIV特异侵犯靶细胞。"},
                {"text": "嗜酸性粒细胞", "isCorrect": False, "rationale": "非HIV受体表达靶细胞。"}
            ],
            "hint": "艾滋病患者血检指标中哪类细胞计数严重降低？",
            "rationale": "HIV表面包膜糖蛋白gp120特异性结合CD4+ T细胞表面的CD4分子及辅助受体，大量杀伤破坏CD4+ T细胞，导致整个免疫系统瘫痪。"
        },
        {
            "id": 10,
            "type": "multiple_choice",
            "question": "经证实，高危型人乳头瘤病毒（HPV 16, 18型）持续感染与下列哪种人类恶性肿瘤的发生具有直接因果关联？",
            "options": [
                {"text": "宫颈癌", "isCorrect": True, "rationale": "正确。HPV 16和18型高危型感染是诱发宫颈癌的最主要病因。"},
                {"text": "原发性肝癌", "isCorrect": False, "rationale": "原发性肝癌与HBV/HCV相关。"},
                {"text": "伯基特淋巴瘤", "isCorrect": False, "rationale": "伯基特淋巴瘤与EBV相关。"},
                {"text": "卡波西肉瘤", "isCorrect": False, "rationale": "卡波西肉瘤与HHV-8相关。"}
            ],
            "hint": "HPV疫苗针对预防的最核心妇科恶性肿瘤。",
            "rationale": "高危型HPV（特别是16和18型）编码的E6和E7癌蛋白降解p53并失活pRb，是导致女性宫颈上皮恶变和宫颈癌发生的直接病因。"
        },

        # --- 判断题 (11~15) ---
        {
            "id": 11,
            "type": "true_false",
            "question": "在体外细胞培养瓶中，如果将干扰素与游离的病毒颗粒直接在试管中混合，干扰素便会像抗生素一样迅速裂解并灭活所有病毒颗粒。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。干扰素在体外不直接杀灭游离病毒，必须作用于活细胞诱导AVP后才能发挥抗病毒作用！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。干扰素的作用机制是间接的，作用于靶细胞而非游离病毒。"}
            ],
            "hint": "干扰素具有间接抗病毒性，体外直接接触无法灭活病毒。",
            "rationale": "干扰素不能直接中和或杀灭病毒颗粒，必须与活细胞表面的特异受体结合，通过信号转导诱导产生抗病毒蛋白（AVP）后才能阻断病毒复制。"
        },
        {
            "id": 12,
            "type": "true_false",
            "question": "水痘-带状疱疹病毒（VZV）在儿童期引起水痘痊愈后，少量病毒可长期潜伏于脊髓后根神经节，在成人免疫力下降时复发引起带状疱疹。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。这是VZV典型的潜伏-激活复发过程。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合VZV的致病特点与潜伏部位。"}
            ],
            "hint": "水痘与带状疱疹是由同一种病毒在不同时期引起的两种截然不同表现。",
            "rationale": "VZV初次感染引起儿童水痘，愈后病毒潜伏于脊髓后根感觉神经节中，在机体抵抗力低下时被激活引起带状分布的带状疱疹。"
        },
        {
            "id": 13,
            "type": "true_false",
            "question": "中和抗体主要清除已侵入宿主细胞内部、正处于生物合成旺盛期的细胞内病毒。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。大分子抗体无法跨膜进入活细胞内，中和抗体只能清除细胞外游离的病毒颗粒！"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。抗体仅对细胞外游离病毒发挥中和阻断作用，清除细胞内病毒必须依赖CTL等细胞免疫。"}
            ],
            "hint": "抗体分子能否自由跨过宿主活细胞膜清除胞质内的病毒？",
            "rationale": "中和抗体作为大分子免疫球蛋白，仅能特异性结合细胞外游离的病毒体，阻断其再感染健康细胞；细胞内病毒主要靠细胞毒性T细胞（CTL）清除。"
        },
        {
            "id": 14,
            "type": "true_false",
            "question": "慢性感染是指显性或隐性感染后，病毒长期潜伏在神经节内，在整个潜伏间歇期内完全不复制也不排出病毒。",
            "options": [
                {"text": "正确", "isCorrect": False, "rationale": "判断错误。这是‘潜伏感染’的定义！慢性感染在整个病程中是持续复制排毒的（如HBV）。"},
                {"text": "错误", "isCorrect": True, "rationale": "判断正确。慢性感染长期持续排毒；间歇期不排毒的属于潜伏感染。"}
            ],
            "hint": "区分慢性感染（持续复制排毒）与潜伏感染（间歇期不排毒）。",
            "rationale": "慢性感染病程迁延，病毒在机体内持续低水平复制并不断排毒；而潜伏期不复制、不排毒、仅在复发时排毒的为潜伏感染。"
        },
        {
            "id": 15,
            "type": "true_false",
            "question": "分泌型IgA（sIgA）主要存在于呼吸道、胃肠道及生殖道外分泌液中，是机体阻断外来病毒定植黏附的最重要黏膜免疫防线。",
            "options": [
                {"text": "正确", "isCorrect": True, "rationale": "判断正确。sIgA耐消化酶，是黏膜表面第一道特异性体液免疫屏障。"},
                {"text": "错误", "isCorrect": False, "rationale": "符合sIgA的黏膜防御功能。"}
            ],
            "hint": "呼吸道和肠道黏膜分泌液中的主力抗体。",
            "rationale": "外分泌型sIgA存在于唾液、泪液、呼吸道和消化道黏液中，能有效阻止病毒在黏膜表面的吸附与侵入，是局部抗感染的核心抗体。"
        },

        # --- 多选题 (16~19) ---
        {
            "id": 16,
            "type": "multiple_select",
            "question": "下列病毒中，能够通过胎盘或产道发生母婴“垂直传播”的常见病毒有：",
            "options": [
                {"text": "风疹病毒（Rubella virus）", "isCorrect": True, "rationale": "引起严重先天性畸形（先天性风疹综合征）。"},
                {"text": "巨细胞病毒（CMV）", "isCorrect": True, "rationale": "常见宫内感染病原体。"},
                {"text": "乙型肝炎病毒（HBV）", "isCorrect": True, "rationale": "经典母婴垂直传播病毒。"},
                {"text": "人类免疫缺陷病毒（HIV）", "isCorrect": True, "rationale": "可通过胎盘、产道及乳汁垂直传染。"}
            ],
            "hint": "TORCH综合征核心病原体及肝炎、艾滋病毒。",
            "rationale": "风疹病毒、巨细胞病毒、单纯疱疹病毒、乙肝病毒及HIV均属于可导致严重宫内感染或母婴垂直传播的典型病毒。"
        },
        {
            "id": 17,
            "type": "multiple_select",
            "question": "关于干扰素（IFN）发挥广谱抗病毒作用的特性，描述正确的有：",
            "options": [
                {"text": "抗病毒范围极广，对多种不同科属的DNA和RNA病毒均有效", "isCorrect": True, "rationale": "正确。广谱抗病毒。"},
                {"text": "具有严格的宿主细胞种属特异性（人干扰素在人细胞上活性最高）", "isCorrect": True, "rationale": "正确。受体结合具有种属限制。"},
                {"text": "通过诱导合成2-5A合成酶激活RNase L降解病毒mRNA", "isCorrect": True, "rationale": "正确。经典抗病毒生化途径之一。"},
                {"text": "通过诱导蛋白激酶PKR磷酸化失活eIF-2阻断蛋白质翻译", "isCorrect": True, "rationale": "正确。经典抗病毒翻译抑制途径。"}
            ],
            "hint": "干扰素的广谱性、种属特异性以及两大AVP生化机制。",
            "rationale": "四个选项均准确概括了干扰素的生物学特性及其细胞内介导的AVP分子作用机制。"
        },
        {
            "id": 18,
            "type": "multiple_select",
            "question": "下列属于病毒感染机体引起的典型“免疫病理损伤”的有：",
            "options": [
                {"text": "乙型肝炎患者体内形成大量抗原-抗体循环免疫复合物沉积引起肾小球肾炎", "isCorrect": True, "rationale": "正确。III型超敏反应免疫复合物病。"},
                {"text": "CD8+ 细胞毒性T细胞（CTL）在清除受染细胞时过度杀伤大量正常肝组织", "isCorrect": True, "rationale": "正确。IV型迟发性细胞免疫损伤。"},
                {"text": "HIV特异性耗竭CD4+ T淋巴细胞引起严重的全身免疫功能缺陷", "isCorrect": True, "rationale": "正确。病毒引起的继发性免疫抑制。"},
                {"text": "细菌质粒通过性菌毛接合转移扩散广谱抗生素耐药性", "isCorrect": False, "rationale": "错误。这是细菌耐药机制，不属于病毒免疫病理。"}
            ],
            "hint": "病毒引起的免疫复合物沉积、CTL组织损伤以及免疫抑制。",
            "rationale": "病毒引起的免疫病理涵盖免疫复合物病（III型）、CTL杀伤靶细胞引起的组织坏死（IV型）以及免疫细胞耗竭抑制（如HIV）。"
        },
        {
            "id": 19,
            "type": "multiple_select",
            "question": "下列关于“潜伏感染”与“慢发病毒感染”的鉴别点，表述正确的有：",
            "options": [
                {"text": "潜伏感染在间歇期内病毒不复制、不向体外排毒", "isCorrect": True, "rationale": "正确。潜伏期完全隐蔽。"},
                {"text": "单纯疱疹病毒（HSV）和水痘-带状疱疹病毒（VZV）是潜伏感染的代表", "isCorrect": True, "rationale": "正确。典型神经节潜伏病毒。"},
                {"text": "慢发病毒感染发病后病程持续进行性单向恶化，最终导致死亡", "isCorrect": True, "rationale": "正确。如SSPE或朊粒病。"},
                {"text": "慢发病毒感染在发病前通常经历长达数月乃至数年的极长潜伏期", "isCorrect": True, "rationale": "正确。潜伏期超长是慢发感染的标志。"}
            ],
            "hint": "潜伏感染有间歇不排毒与多次复发；慢发感染潜伏期极长且发病后不可逆致死。",
            "rationale": "四个选项均准确表达了潜伏感染与慢发病毒感染的定义、病程特点与代表病原体。"
        },

        # --- 填空题 (20~21) ---
        {
            "id": 20,
            "type": "fill_blank",
            "question": "干扰素主要分为两类：由白细胞和成纤维细胞产生的（1）____型干扰素主要行使抗病毒作用；由活化T细胞和NK细胞产生的（2）____型干扰素（IFN-γ）主要行使免疫调节作用。",
            "blankAnswers": [
                "I",
                "II"
            ],
            "hint": "填写罗马数字I和II（或一和二）。",
            "rationale": "I型干扰素（IFN-α/β）主要抗病毒；II型干扰素（IFN-γ）主要进行免疫调节。"
        },
        {
            "id": 21,
            "type": "fill_blank",
            "question": "在体外细胞培养中，溶细胞型病毒增殖直接引起的细胞变圆脱落死亡现象称为（1）____效应（CPE）；而水痘-带状疱疹病毒在原发感染水痘痊愈后，其基因组可长期潜伏于人体的（2）____神经节中，成年后复发表现为带状疱疹。",
            "blankAnswers": [
                "细胞病变",
                "脊髓后根"
            ],
            "hint": "第一空填CPE的中文全称；第二空填VZV潜伏的神经节名称。",
            "rationale": "CPE全称为细胞病变效应（Cytopathic effect）；VZV潜伏于脊髓后根感觉神经节或颅神经感觉神经节中。"
        }
    ]
}
