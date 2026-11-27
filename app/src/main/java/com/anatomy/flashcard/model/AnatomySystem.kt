package com.anatomy.flashcard.model

data class StudyUnit(
    val id: String,
    val subjectId: String,
    val title: String,
    val subtitle: String = "",
    val description: String = "",
    val filename: String = id
) {
    companion object {
        val OVERVIEW = StudyUnit(
            id = "overview",
            subjectId = "anatomy",
            title = "01 概论与组织皮肤",
            subtitle = "Overview, Tissues & Skin",
            description = "解剖学姿势、方位术语、上皮/结缔/肌/神经四大人体基本组织及皮肤结构与屏障功能。",
            filename = "overview_system"
        )
        val SKELETAL = StudyUnit(
            id = "skeletal",
            subjectId = "anatomy",
            title = "02 骨骼系统",
            subtitle = "Skeletal System",
            description = "涵盖骨学总论、中轴骨（颅骨、椎骨、胸骨）、附肢骨（上肢骨、下肢骨）、关节学构造与足弓功能。",
            filename = "skeletal_system"
        )
        val MUSCULAR = StudyUnit(
            id = "muscular",
            subjectId = "anatomy",
            title = "03 肌肉系统",
            subtitle = "Muscular System",
            description = "涵盖骨骼肌微细结构、肌节、肌丝滑动学说、头颈躯干及四肢肌群分布与运动学效应。",
            filename = "muscular_system"
        )
        val NERVOUS = StudyUnit(
            id = "nervous",
            subjectId = "anatomy",
            title = "04 神经系统",
            subtitle = "Nervous System",
            description = "涵盖中枢神经系统（脑、脊髓）、周围神经系统（脑神经、脊神经）、传导通路与自主神经系统。",
            filename = "nervous_system"
        )
        val ENDOCRINE = StudyUnit(
            id = "endocrine",
            subjectId = "anatomy",
            title = "05 内分泌系统",
            subtitle = "Endocrine System",
            description = "涵盖甲状腺、甲状旁腺、肾上腺、垂体、松果体等内分泌腺及内分泌细胞群的功能与构造。",
            filename = "endocrine_system"
        )
        val SENSORY = StudyUnit(
            id = "sensory",
            subjectId = "anatomy",
            title = "06 感觉器官",
            subtitle = "Sensory Organs",
            description = "涵盖视器（眼球结构、折光系统、屈光不正）、前庭蜗器（外耳、中耳、内耳平衡与听觉受器）及皮感觉构造。",
            filename = "sensory_system"
        )
        val CIRCULATORY = StudyUnit(
            id = "circulatory",
            subjectId = "anatomy",
            title = "07 循环系统",
            subtitle = "Circulatory System",
            description = "心脏大体与瓣膜构造、心肌细胞电生理、心传导系统、心动周期、大循环与微循环动脉静脉血压调控。",
            filename = "circulatory_system"
        )
        val BLOOD = StudyUnit(
            id = "blood",
            subjectId = "anatomy",
            title = "08 血液与淋巴",
            subtitle = "Blood & Lymphatic System",
            description = "血细胞三大类、血浆晶体与胶体渗透压、生理性止血、凝血三大阶段、抗凝与纤溶系统、淋巴器官。",
            filename = "blood_system"
        )
        val RESPIRATORY = StudyUnit(
            id = "respiratory",
            subjectId = "anatomy",
            title = "09 呼吸系统",
            subtitle = "Respiratory System",
            description = "呼吸道与肺脏结构、胸膜腔负压、肺泡表面活性物质、通气阻力、通气/血流比值与血气运输及呼吸中枢调控。",
            filename = "respiratory_system"
        )
        val DIGESTIVE = StudyUnit(
            id = "digestive",
            subjectId = "anatomy",
            title = "10 消化系统",
            subtitle = "Digestive System",
            description = "消化管壁组织构造、胃黏膜屏障、小肠绒毛微绒毛、胰腺内外分泌、肝小叶与门静脉、胆汁排泄与三大营养素吸收。",
            filename = "digestive_system"
        )
        val URINARY = StudyUnit(
            id = "urinary",
            subjectId = "anatomy",
            title = "11 泌尿系统",
            subtitle = "Urinary System",
            description = "肾单位、滤过膜三层屏障、有效滤过压、近端小管重吸收、髓袢逆流倍增、RAAS系统、ADH水重吸收及排尿反射。",
            filename = "urinary_system"
        )
        val REPRODUCTIVE = StudyUnit(
            id = "reproductive",
            subjectId = "anatomy",
            title = "12 生殖系统",
            subtitle = "Reproductive System",
            description = "睾丸与精子发生、血睾屏障、雄激素；卵巢与卵泡发育、排卵黄体、子宫内膜周期性变化、受精与着床机制。",
            filename = "reproductive_system"
        )
        val METABOLISM = StudyUnit(
            id = "metabolism",
            subjectId = "anatomy",
            title = "13 体温与能量代谢",
            subtitle = "Temperature & Metabolism",
            description = "三大产能营养素代谢、BMR测定、深部体温、产热器官（内脏/骨骼肌）、辐射传导对流蒸发四大散热、体温调定点与发热病理。",
            filename = "metabolism_system"
        )

        val ANATOMY_UNITS = listOf(
            OVERVIEW, SKELETAL, MUSCULAR, NERVOUS, ENDOCRINE, SENSORY,
            CIRCULATORY, BLOOD, RESPIRATORY, DIGESTIVE, URINARY, REPRODUCTIVE, METABOLISM
        )

        val MICROBIOLOGY_UNITS = listOf(
            StudyUnit("micro_01", "microbiology", "01 绪论", "Introduction", "微生物基本概念、三大类型划分与医学微生物学范畴", "micro_01"),
            StudyUnit("micro_02", "microbiology", "02 细菌形态与结构", "Bacterial Morphology", "细菌基本形态、细胞壁、肽聚糖与特殊结构（荚膜、鞭毛、芽胞）", "micro_02"),
            StudyUnit("micro_03", "microbiology", "03 细菌的生理", "Bacterial Physiology", "细菌营养摄取、代谢产物、生长繁殖与人工培养条件", "micro_03"),
            StudyUnit("micro_04", "microbiology", "04 细菌的遗传与变异", "Genetics & Variation", "质粒、噬菌体、基因重组机制（转化、转导、接合）与变异效应", "micro_04"),
            StudyUnit("micro_05", "microbiology", "05 细菌的感染与免疫", "Infection & Immunity", "细菌毒力机制（内毒素、外毒素）、侵袭力与宿主抗感染免疫", "micro_05"),
            StudyUnit("micro_06", "microbiology", "06 病毒的基本性状", "Viral Characteristics", "病毒核酸/衣壳构造、复制增殖周期与理化抵抗力", "micro_06"),
            StudyUnit("micro_07", "microbiology", "07 病毒的感染", "Viral Infection", "病毒感染类型、致病机制（细胞病变、免疫病理）与持续感染", "micro_07"),
            StudyUnit("micro_08", "microbiology", "08 真菌学总论", "Mycology Overview", "真菌形态、孢子繁殖、菌落形态与致病分类", "micro_08")
        )

        val IMMUNOLOGY_UNITS = listOf(
            StudyUnit("immu_01", "immunology", "01 绪论与免疫系统", "Immune System Overview", "免疫三大功能、中枢与外周免疫器官及免疫细胞分布", "immu_01"),
            StudyUnit("immu_02", "immunology", "02 固有免疫", "Innate Immunity", "组织屏仗、吞噬细胞、NK细胞及体液固有免疫分子效应", "immu_02"),
            StudyUnit("immu_03", "immunology", "03 抗原", "Antigens", "抗原表位、异物性、特异性及佐剂与超抗原", "immu_03"),
            StudyUnit("immu_04", "immunology", "04 抗原提呈与MHC", "Antigen Presentation & MHC", "MHC分子结构、多态性与内源性/外源性抗原加工提呈途径", "immu_04"),
            StudyUnit("immu_05", "immunology", "05 T淋巴细胞与免疫分子", "T Lymphocytes", "T细胞表面标志（TCR、CD3、CD4/CD8）、亚群分化与细胞因子", "immu_05"),
            StudyUnit("immu_06", "immunology", "06 B淋巴细胞和抗体", "B Cells & Antibodies", "BCR复合物、免疫球蛋白IgG/IgM/IgA结构及功能特性", "immu_06"),
            StudyUnit("immu_07", "immunology", "07 免疫应答", "Immune Response", "体液与细胞免疫应答的时相、激活信号与效应清除机制", "immu_07"),
            StudyUnit("immu_08", "immunology", "08 免疫学应用", "Immunological Applications", "人工被动/主动免疫、抗体应用及免疫治疗原则", "immu_08")
        )

        val ALL_UNITS = ANATOMY_UNITS + MICROBIOLOGY_UNITS + IMMUNOLOGY_UNITS

        fun fromId(id: String): StudyUnit {
            return ALL_UNITS.find { it.id == id } ?: SKELETAL
        }
    }
}

typealias AnatomySystemType = StudyUnit
