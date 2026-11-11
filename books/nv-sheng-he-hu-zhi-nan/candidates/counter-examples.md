# 《女生呵护指南》反例候选（仓颉阶段1）

> 提取器：counter-example-extractor | 完整性：全书六章已通读 | 所有 source_quote 均核对 SOURCE.txt 行号

## 一、作者明确警告的失败模式 / 错误做法（外部反例）

```yaml
- id: ce01
  title: 用洗液冲洗阴道，"洗洗更健康"
  type: counter-example
  source_chapter: 第一章 私处怎么洗（SOURCE.txt:302–314）
  source_quote: |
    "刚开始用时，情况立马得到了改善……就长期用起来，结果时间一长，却发现情况
    越来越严重了，还出现了之前没有的症状。"（另："使用阴道洗液的女性患盆腔感染
    的概率比不使用阴道洗液的女性多73%"，行314）
  failure_mode: 把正常分泌物当脏东西，用妆字号/消字号洗液冲洗阴道，短期缓解掩盖长期破坏。
  mechanism: 阴道靠乳酸杆菌维持酸性自净环境；洗液无差别杀菌，"把守家护土的士兵全部清除出境"（行1015），菌群失衡后外来病原体更易定植，形成"越洗越炎、越炎越洗"的循环。
  warning_signs: [依赖洗液后停用即复发, 症状初期"立马改善"的错觉, 广告话术把正常分泌描述为"不洁"]
  bound_to: ["自净/微生态保护原则", "干预前先问'这个干预会破坏什么'"]
  tags: [counter-example, over-treatment, marketing-trap, microbiome]

- id: ce02
  title: 拿教科书单一标准对照自己，"白带不是透明就有问题"
  type: counter-example
  source_chapter: 第一章 什么样的白带是正常的（SOURCE.txt:189–196）
  source_quote: |
    "这会让很多女性陷入误区。她们会认为自己的白带只要不是上面说的那种状态就是有问题，
    还有一部分人会错误地认为只要白带不是透明的就是有问题。"
  failure_mode: 用"量少、白色、无异味"的单一模板对照动态身体，把周期性正常波动当病。
  mechanism: 正常范围是随激素周期、饮食、环境变化的动态区间；单点读数脱离基线和伴随症状就下结论，必然产生大量假阳性焦虑，反复无效检查。
  warning_signs: [检查结果正常仍不放心, 每天对照内裤/色卡焦虑, 一次波动就上网检索到崩溃]
  bound_to: ["动态基线判断框架", "正常是区间不是点"]
  tags: [counter-example, health-anxiety, misdiagnosis]

- id: ce03
  title: 清洁度Ⅲ度就被开一大堆药：指标异常≠需要治疗
  type: counter-example
  source_chapter: 第一章 白带常规·清洁度（SOURCE.txt:236–244）
  source_quote: |
    "医生认为她有炎症，需要治疗，结果给她开了一大堆药……现实生活中我们常常会遇到正常人的
    白带清洁度是Ⅲ度……如果其他项目都是正常的，只有白带清洁度为Ⅲ度，且没有任何症状的话，则无需治疗。"
  failure_mode: 医方按生硬分级机械开药；患方把"报告与当初一样"当"没治好"，陷入无限治疗。
  mechanism: 教科书分级未纳入环境、情绪、月经周期等真实变量；"当初就不用治疗"（行229）——治疗一个不需要治疗的"病"，制造了新的病人身份和持续用药依赖。
  warning_signs: [无任何症状仅凭报告异常被开药, 以"复查指标"而非症状作为治愈标准]
  bound_to: ["症状+整体检查+指征三重把关", "过度治疗/延误治疗双风险评估"]
  tags: [counter-example, over-treatment, iatrogenic]

- id: ce04
  title: 见白细胞加号就治疗，有人花了上万元
  type: counter-example
  source_chapter: 第一章 白带常规·白细胞（SOURCE.txt:252–256）
  source_quote: |
    "有的人光是因为白细胞那几个加号就花了上万元，结果到头来还是有白细胞，因为她们认为
    有白细胞就一定有炎症，需要治疗。"（另："我要帮帮忙！用点儿药，搞一搞冲洗！这就完蛋了"）
  failure_mode: 把免疫反应当敌人，用药物和冲洗"帮忙"，反而瓦解防御。
  mechanism: 白细胞是"军队"在作战的信号；外部干预相当于在自家战场盲目开火（作者以德军远离本土供给不足为喻，行255），消灭的不是敌人而是自己的战斗力。
  warning_signs: [报告有加号就要求开药, 无症状却反复用药复查]
  bound_to: ["无症状不干预原则", "区分指标与疾病"]
  tags: [counter-example, over-treatment, health-anxiety]

- id: ce05
  title: 豆腐渣样白带自己买药治
  type: counter-example
  source_chapter: 第一章 豆腐渣样白带（SOURCE.txt:219）
  source_quote: |
    "这个时候千万不要自己去买药进行治疗，而应该去医院检查白带常规，并且在医生的指导下用药，不然情况只会越来越糟糕。"
  failure_mode: 凭外观"自诊"（还可能认错豆腐渣），跳过白带常规直接用药。
  mechanism: 相似性状对应不同病原；不检测病原体就用药，"往往会掩盖病情，影响诊断，延误治疗"（行1001），且自行用药破坏菌群后更难根治。
  warning_signs: [网购/药店自购抗真菌药, 症状反复就换药加量]
  bound_to: ["先检查后用药", "就医转介红线"]
  tags: [counter-example, self-medication]

- id: ce06
  title: 就诊前先用洗液清洗，"掩耳盗铃"
  type: counter-example
  source_chapter: 第一章 私处怎么洗（SOURCE.txt:313）
  source_quote: |
    "有些患者在去医院检查之前事先用洗液清洗，这种掩耳盗铃的做法，着实不推荐，不然检查结果不准确，到头来受罪的还是患者。"
  failure_mode: 因羞耻感想"收拾干净再去"，洗掉病原体导致假阴性。
  mechanism: 羞耻驱动的事前修饰破坏了诊断样本；信息被自己清除，医生只能按不完整信息决策。
  warning_signs: [就诊当天刻意冲洗、用药, 隐瞒症状或病史（呼应行885"如实沟通"）]
  bound_to: ["就诊信息完整性原则", "去羞耻化沟通"]
  tags: [counter-example, shame-driven, diagnostic-error]

- id: ce07
  title: "内裤挑战"式自我监测成瘾
  type: counter-example
  source_chapter: 第一章 内裤上总是有东西（SOURCE.txt:323–331）
  source_quote: |
    "国外有过一场叫'内裤挑战'的活动，鼓励大家晒出内裤来证明自己健康。其实，这是在误导大家。
    可能会挑战大家认知的事实是正常情况下内裤上就是会有东西的。"
  failure_mode: 把高频自检当健康行为，实际制造持续焦虑；会员病例每天看照片"总觉得自己哪里不对劲"。
  mechanism: 监测频率越高，捕获到正常波动的概率越高；没有基线知识的观察只会生产假信号——注意力本身成为症状来源（行202"你要是过分关注，那就是个事儿"）。
  warning_signs: [每日多遍检查记录, 为无症状的"异常"拍照求证]
  bound_to: ["观察须伴随判断框架", "转移注意力作为干预"]
  tags: [counter-example, health-anxiety, monitoring-trap]

- id: ce08
  title: "月经排毒"叙事与经量焦虑
  type: counter-example
  source_chapter: 第二章 月经是子宫寂寞的眼泪 / 如果你月经量过少（SOURCE.txt:397, 710, 723）
  source_quote: |
    "请不要相信无良商家那些言之凿凿的宣传语，说什么月经可以排毒之类的话，那些基本上都是胡扯，不要硬给月经赋予什么崇高的使命。"
  failure_mode: 把月经当排毒通道，经量减少→恐惧毒素淤积→服中药保健品"调经"。
  mechanism: "月经只是一个现象，月经量的多少并不重要"（行723）——伪机制（排毒）催生伪需求，商家从健康焦虑中获利（行177"白带排毒骗局"同构）。
  warning_signs: [用"排毒""养颜"解释月经变化, 长期服用调经保健品]
  bound_to: ["利益相关方审计", "机制解释优先于标签"]
  tags: [counter-example, pseudo-science, marketing-trap]

- id: ce09
  title: 影视剧"黑血=毒血"的认知模板迁移
  type: counter-example
  source_chapter: 第二章 月经应该是什么颜色（SOURCE.txt:423–427）
  source_quote: |
    "通过这些影视作品，我们了解到，黑血相当于有毒的血……出现黑血就表示一定是有问题的。
    ……错！……处在现代社会的你们还继续犯这个错误就不应该了。"
  failure_mode: 把武侠剧"疗伤吐黑血"的叙事框架直接套用到月经黑色血块上。
  mechanism: 叙事模板先于科学解释占位；血离开人体凝固变深是物理过程（行429–433），颜色深浅与"毒性"无关。类比一旦先入为主，机制解释很难翻转直觉。
  warning_signs: [用"排毒""淤堵"描述经血, 见黑色血块即恐慌]
  bound_to: ["直觉类比只是入口不是证据", "机制解释去恐惧化"]
  tags: [counter-example, cognitive-bias, narrative-template]

- id: ce10
  title: 想当然的经期禁忌（芒果/梨/巧克力/冰激凌等）
  type: counter-example
  source_chapter: 第二章 经期禁忌真的存在吗（SOURCE.txt:476–499）
  source_quote: |
    "人们想当然地认为经期不能吃芒果，因为会止血。但是实际上……经血还是照样流出来，可见其势不可当，更不要说吃几个芒果了。"（另：山楂禁忌"居然是个乌龙"，行490）
  failure_mode: 从单一成分性质（"促进血凝""性凉"）跳跃到系统级结论（经期禁食）。
  mechanism: 忽略剂量、人体代偿和整体生理——血小板凝血能力远强于食物影响；禁忌靠"一提到X就想到过度"的联想链生成（行482），未经对照验证。
  warning_signs: ["听说经期不能吃X"但说不出机制, 禁忌清单随口口相传不断加长]
  bound_to: ["证据分级审查", "剂量与整体视角"]
  tags: [counter-example, folk-belief, causal-fallacy]

- id: ce11
  title: "六颗红枣代替营养支持治疗"：食疗替代医疗
  type: counter-example
  source_chapter: 第二章 红枣能不能吃（SOURCE.txt:494）
  source_quote: |
    "患者术后最需要的就是营养支持治疗，结果有一位患者就是不配合治疗……她妈妈说那些营养支持治疗都不管用，最管用的是每天吃六颗红枣。她说得头头是道，六层楼竟然无言以对。"
  failure_mode: 用低成本、低风险的食疗替代有循证支持的规范治疗。
  mechanism: "人们选择相信，只是因为成本少"（行2891）——食用无害被偷换为"治疗有效"，放弃正规治疗的隐性代价未计入决策。
  warning_signs: ["食补代替药补""是药三分毒", 依从家属经验多于医嘱]
  bound_to: ["证据优先于经验", "方案比较须含'不处理/替代方案'的代价"]
  tags: [counter-example, food-therapy, non-compliance]

- id: ce12
  title: "经期吃再多也不会胖"的促销式错觉
  type: counter-example
  source_chapter: 第二章 能不能多吃（SOURCE.txt:526–530）
  source_quote: |
    "经期女性的新陈代谢会比平时快30%左右，但是仅仅这30%就可以让人吃什么都不会变胖吗？……你们看到的体重下降是——错——觉！"
  failure_mode: 拿单条研究数据（代谢+30%）支撑"随便吃"的授权。
  mechanism: 经前水钠潴留抬高了基线体重，经期回落被误读为"吃不胖"；作者用"先提价再打折"作喻（行529）。片段化数据脱离完整机制就会被用来许可放纵。
  warning_signs: [引用单一百分比正当化行为, 固定时间外的体重对比]
  bound_to: ["数据须放回完整机制", "基线与测量条件控制"]
  tags: [counter-example, motivated-reasoning, data-misuse]

- id: ce13
  title: "经期同房=完美避孕"的小九九
  type: counter-example
  source_chapter: 第二章 能不能同房（SOURCE.txt:554–557）
  source_quote: |
    "绝对有很多人认为经期同房可以避孕，尤其是男性。如果再懂点所谓的'理论'，那帮小兔崽子们哄骗女友经期同房简直一骗一个准！……我在临床上遇到过……她的排卵期是在经期的第三天。"
  failure_mode: 用"安全期"逻辑在经期裸奔；排卵期因个体和情绪波动根本不固定。
  mechanism: 排卵期漂移使任何基于日历的避孕都不可靠；一个反例（经期第三天排卵）即可粉碎普遍规则。
  warning_signs: [以"省安全套"为动机的"理论", 男性主动提出经期无需防护]
  bound_to: ["补救措施不能当常规方案", "拒绝的权利与固定伴侣+安全套"]
  tags: [counter-example, contraception-failure, coercion-risk]

- id: ce14
  title: 止痛药当"最后救命稻草"：痛到受不了才吃
  type: counter-example
  source_chapter: 第二章 原发性痛经·A方案（SOURCE.txt:763–764）
  source_quote: |
    "如果前列腺素已经生成了……这个时候吃再多此类药物已无济于事……我知道很多人把吃止痛药作为最后的救命稻草，只有在痛得实在受不了的时候才会选择，但结果往往是依然没有效果。"
  failure_mode: 因恐惧成瘾而最晚用药，恰好用出最差效果，反过来"验证"了药物无效。
  mechanism: 解热镇痛药抑制前列腺素生成而非对抗已生成者——时机决定疗效；恐惧偏差导致使用方式错误，错误体验又强化恐惧，形成自证循环。
  warning_signs: [疼到极限才服药且嫌无效, 混淆阿片类与解热镇痛类（行760）]
  bound_to: ["了解机制再使用工具", "副作用要与收益和不干预风险并列比较"]
  tags: [counter-example, fear-of-medicine, timing-error, time-sensitive-evidence]

- id: ce15
  title: 短效避孕药治痛经被家属怒斥退药
  type: counter-example
  source_chapter: 第二章 原发性痛经·B方案（SOURCE.txt:771–773）
  source_quote: |
    "家属怒问：'你到底会不会看病，我女儿只是个高中生，你怎么能开这种药？'解释无果，患者和家属要求退药。"
  failure_mode: 把"避孕药"名称等同于"性许可"，用道德联想否决适应证用药。
  mechanism: 药物名称触发价值判断而非药理评估；外行以道德标准推翻专业决策，最终受损的是患者本人。
  warning_signs: ["XX药=XX行为"式联想, 拒绝听机制解释坚持退药]
  bound_to: ["按适应证而非名称评价方案", "知情选择需要机制科普托底"]
  tags: [counter-example, moral-bias, non-compliance]

- id: ce16
  title: 症状一消失就停药：56%的VVC患者不完成疗程
  type: counter-example
  source_chapter: 第三章 霉菌性阴道炎·规范化治疗（SOURCE.txt:983–984, 1026–1027）
  source_quote: |
    "有56%的患者没有按照医嘱坚持用药一个疗程；有51%的患者受古语'是药三分毒'的影响，在用药三四天后因症状得到缓解而停止用药。"
  failure_mode: 以症状消除为治愈标准，自行停药或自行延长疗程（两个方向都错）。
  mechanism: 症状清除≠病原清除（行2134"病原体可能处于被抑制状态"）；停药留下耐药/残余菌群，加上习惯未改，复发→再用药→更难治。"每个人都认为自己可以当自己的医生"（行1027）。
  warning_signs: ["好了就不用吃了", 自行把7天疗程延长成一个月]
  bound_to: ["规范、足量、足疗程", "区分症状缓解与病原学治愈"]
  tags: [counter-example, non-compliance, recurrence]

- id: ce17
  title: 治疗欲望与"不开药就是不负责任"的过度医疗合谋
  type: counter-example
  source_chapter: 第三章 宫颈炎（SOURCE.txt:1073, 1091）
  source_quote: |
    "大家只要有点儿小毛病就要治疗的欲望实在太强烈，以至于很多人都希望医生给自己开药，甚至认为如果不开药，就是不负责任。过度医疗就是这样产生的，有时候，医生也挺委屈的。"
  failure_mode: 患方主动索取治疗，医方顺从供给——过度医疗是双方合谋的产物，不只是医生的问题。
  mechanism: 焦虑把"被重视感"与"被开药"绑定；医患期望偏差（前言行70）下，开药成为最省力的安抚手段，双向风险（过度治疗伤害身体与钱包）被忽略。
  warning_signs: [没病也想"开点什么", 用药物支出衡量医生态度]
  bound_to: ["让无需治疗的患者保护好身体和钱包", "知情选择而非权威依赖"]
  tags: [counter-example, over-treatment, doctor-patient]

- id: ce18
  title: "宫颈糜烂"骗局闭环：恐吓→道德绑架→钱包收割
  type: counter-example
  source_chapter: 第三章 宫颈糜烂样改变（SOURCE.txt:1133–1181）
  source_quote: |
    "有多少人在治疗之前对这个词的理解是正确的呢？几乎是零！……在读大学的时候有个外号叫'糜糜'，只因为同学看到了她的检查结果。这导致她大学期间异常痛苦，一度想轻生。"（另，无良医院话术，行1163）
  failure_mode: 过时诊断名+性道德污名+恐吓式话术，把生理现象做成庞大治疗产业链。
  mechanism: 三条通路（柱状上皮外移/宫颈炎/HPV癌变）本无关联（行1178–1181），骗局靠混淆三者成立；恐惧来自未知（行1168"一切恐惧都源于无知"），正规门诊"这不是病，走吧"的冷处理反而把患者推回无良医院（行1166）。
  warning_signs: [被告知"会变成宫颈癌/影响生育", 治疗前从未做过TCT/HPV, 医院靠该项目创收]
  bound_to: ["利益相关方审计", "机制解释+去羞耻化", "只去正规医院"]
  tags: [counter-example, predatory-medicine, stigma, misinformation]

- id: ce19
  title: 搜索"乳腺肿块"→100%是乳腺癌：关键词式自我诊断
  type: counter-example
  source_chapter: 第四章 乳腺纤维腺瘤（SOURCE.txt:1713）；同房出血（SOURCE.txt:2057）
  source_quote: |
    "发现之后立马到网上查看相关信息，结果吓得就差尿床了……用这两个关键词搜到的结果100%是乳腺癌，搁谁都受不了。"
  failure_mode: 用最吓人的关键词检索，把罕见严重结局当成默认解释。
  mechanism: 搜索结果按流量与恐慌价值排序，不按贝叶斯概率排序；绝大多数乳房肿物是纤维腺瘤或增生（行1714）。恐惧检索制造"查前正常、查后哪儿都疼"的心因性症状（行1499）。
  warning_signs: [检索词直接用最坏疾病名, 查完立刻对号入座出现"症状"]
  bound_to: ["先验概率意识", "信息源可信度分级"]
  tags: [counter-example, cyberchondria, survivorship]

- id: ce20
  title: 对号入座式"诊断"：外阴白斑与卵巢多囊样改变
  type: counter-example
  source_chapter: 第四章 外阴白斑（SOURCE.txt:1230）；多囊卵巢综合征（SOURCE.txt:1639, 1644–1646）
  source_quote: |
    "并不是因为她们确实有这种病，而是因为她们听说过这个词，并且从网上了解了一些信息，然后通过观察开始对号入座。"（另："将近四分之一的人有卵巢多囊样改变，而这些多囊样改变的人中又有超过一半的人是正常人。"）
  failure_mode: 听说过病名→找身体相似处→自我确诊；把影像学改变当疾病本身。
  mechanism: 疾病有严格诊断标准（痤疮须持续3个月以上、闭经须停经超6个月，行1639）；单一影像/表象与疾病之间隔着症状组合、持续时间和排除诊断。
  warning_signs: ["我听说X病，我好像就是", 用单项检查结果自称患病]
  bound_to: ["诊断标准意识", "检出/存在不等于疾病（伴生状态）"]
  tags: [counter-example, self-diagnosis, misdiagnosis]

- id: ce21
  title: 紧急避孕药被循环使用："越吃越紊乱，越紊乱越吃"
  type: counter-example
  source_chapter: 第五章 紧急避孕药（SOURCE.txt:1890, 1916）
  source_quote: |
    "我说过多少次了，紧急避孕药不能作为常规避孕手段，可还是有人不顾劝阻、铤而走险……于是又得吃，结果就是月经越紊乱越需要吃，越吃越紊乱。"
  failure_mode: 把85%成功率的补救措施当常规方案；月经被扰乱后排卵更不可测，进一步依赖补救。
  mechanism: 补救措施本身制造新的不确定性，形成依赖回路；"摇摆不定的排卵期岂不是更容易被你撞上"（行1916）。
  warning_signs: [一年内多次服用, 不与常规避孕措施并用]
  bound_to: ["预防/常规/补救分层", "长效可逆措施（皮埋等）"]
  tags: [counter-example, remedy-as-routine, contraception, time-sensitive-evidence]

- id: ce22
  title: "今天做人流，明天就上班"：无痛人流广告的三重话术
  type: counter-example
  source_chapter: 第五章 意外怀孕·人流手术（SOURCE.txt:1999–2004, 2011）
  source_quote: |
    "广告里写着'无痛人流''超导可视无痛人流'……其实在我们看来，它们在手术操作上没什么区别！……这种'看上去更高级一些的技术'真的可以蒙骗很多小女生和刚刚从朋友那里借来钱的小男生。"
  failure_mode: 把"感受无痛"偷换为"身体无损伤"，用科技名词抬高价格。
  mechanism: 麻醉只改变主观感受，手术创面与风险不变；麻醉状态下患者无法及时反馈异常反而隐藏并发症（行2011）；"弱化手术本身对身体造成的影响"（行2003）降低了对避孕的重视。
  warning_signs: [以"无痛/可视"为选择依据, 术后当天即恢复日常]
  bound_to: ["人流只是补救措施", "感受与实质分离的识别"]
  tags: [counter-example, advertising-trap, minimization-of-harm]

- id: ce23
  title: 自己在家药流与"把人流当避孕方式"
  type: counter-example
  source_chapter: 第五章 药物流产 / 数据（SOURCE.txt:2038–2040, 1990, 2022）
  source_quote: |
    "每年都有自己在家药流的患者，因为大出血没有得到及时的救治而去世。"（另：超过60%的人"发生性行为前不考虑怀孕问题……甚至有人会把人流或药流当作避孕方式"，行1990）
  failure_mode: 无禁忌评估、无B超确认、无抢救条件的自行用药；或根本不避孕、以流产兜底。
  mechanism: 药流有明确禁忌证和留院观察要求（行2046）；补救链条每一环都依赖正规医疗兜底，跳过兜底则低概率事件（大出血）对个体就是100%（行2008）。
  warning_signs: [网购流产药, "反正怀了就打掉"]
  bound_to: ["预防优先于补救", "风险概率对个体无意义原则"]
  tags: [counter-example, self-medication, fatal-risk]

- id: ce24
  title: "我就蹭蹭不进去"：侥幸心理与性病规避失败
  type: counter-example
  source_chapter: 第五章 尖锐湿疣（SOURCE.txt:2146, 2145）
  source_quote: |
    "如果听到他说'我就蹭蹭不进去，没事的'，别犹豫，直接将他踹下床！……对所有不洁的性接触来说，感染尖锐湿疣的风险都很大，仅仅一次摩擦就足够为HPV'搭桥过河'了。"
  failure_mode: 以行为"不完全"推断风险"接近零"；一次无保护接触即可能感染。
  mechanism: 感染只需要病原-黏膜接触这一个充分条件，不需要"完整行为"；HPV潜伏期3周–8个月（行2153），感染时点与症状出现脱钩，进一步喂养侥幸。
  warning_signs: ["就一次""没进去", 依赖对方口头保证健康状况]
  bound_to: ["安全套规避80%感染", "高危接触后及时检查"]
  tags: [counter-example, risk-miscalibration, STI]

- id: ce25
  title: 尖锐湿疣偏方、小药丸与自行开方治梅毒
  type: counter-example
  source_chapter: 第五章 尖锐湿疣 / 梅毒（SOURCE.txt:2162, 2182）
  source_quote: |
    "那些谎称可以治疗尖锐湿疣的偏方、小药丸根本没用，只会拉低你们的智商。""有些人会因为自己给自己开药方，在相信网络的这条路上越走越远，很有可能错过最佳的治疗时机。"
  failure_mode: 因羞耻走"地下渠道"，用无效偏方替代可治愈的规范治疗（梅毒早期治愈率高达90%）。
  mechanism: 羞耻让患者宁愿相信"不用见人"的方案；可治愈疾病的延误恰恰发生在最不该延误的人群。
  warning_signs: [网上寻"良方"、买三无产品, 症状好转即中断治疗]
  bound_to: ["去羞耻化的正规就诊", "足量足疗程"]
  tags: [counter-example, shame-driven, folk-remedy]

- id: ce26
  title: 私处美白/乳晕漂白/嫩红素：为不存在的"标准色"付费
  type: counter-example
  source_chapter: 第六章 私处的颜色 / 乳晕应该是什么颜色（SOURCE.txt:2286–2317）
  source_quote: |
    "嫩红素其实是一类漂剂……因为长期受到酸碱的刺激，皮肤会出现损伤，进而导致色素沉积，反而得不偿失。"（另："很多都没有获得国家相关部门的审批认证，甚至不少是三无产品或者走私产品。"）
  failure_mode: 为审美制造的伪需求购买漂白/涂色产品，短期变浅、长期损伤加深色沉。
  mechanism: 颜色由基因和性激素决定（"要私处颜色变浅除非有某种产品可以改变基因或者扰乱我们的激素分泌"，行2317）；产品用"量变不够"话术让用户无限复购（行2314）；审美绑架正常生理即"畸形的审美"（行2277）。
  warning_signs: [私处颜色被用作道德评判, 产品要求"长期涂抹才见效"]
  bound_to: ["谁在制造这个问题", "健康比白更重要"]
  tags: [counter-example, manufactured-need, beauty-industry]

- id: ce27
  title: 美容院阴道紧缩术失败案例与不严谨的手术指征
  type: counter-example
  source_chapter: 第六章 阴道松弛 / 太紧了是怎么回事（SOURCE.txt:2503–2509, 2556）
  source_quote: |
    "曾有一位患者，她为了留住丈夫的心，掷重金去美容院做阴道紧缩术。但是美容院不正规，手术做得也过于草率……手术失败了……导致丈夫的心没留住，还总是把丈夫拒之'门'外。"
  failure_mode: 为心理/关系问题购买手术解法；同一术式换个名字（阴道紧缩术）就放宽了指征。
  mechanism: "手术只能解决确实存在的阴道松弛问题，并不能解决心理或其他原因造成的性生活问题"（行2509）；瘢痕、阴道狭窄、粘连是真实反向风险——矫枉过正制造新病。
  warning_signs: [动机是"留住对方"而非症状, 美容机构而非医院开展手术]
  bound_to: ["手术须有明确指征", "身体手段不解决关系问题"]
  tags: [counter-example, unnecessary-surgery, relationship-projection]

- id: ce28
  title: 卖卵换钱：黑诊所取卵的完整风险链
  type: counter-example
  source_chapter: 第六章 卖卵换钱值得吗（SOURCE.txt:2657–2694）
  source_quote: |
    "黑中介把卖卵说成是简单安全的赚钱捷径，对取卵的风险却避而不谈……黑诊所还可能给供卵者注射过量的促排卵药物——这就很可怕了，卖卵者的生命健康根本得不到一点点保障。"
  failure_mode: 在无监控、无菌、无抢救条件下促排卵+穿刺取卵，换取几万元。
  mechanism: OHSS（卵巢过度刺激综合征）可致腹水、血栓、呼吸衰竭、休克、死亡（行2667）；正规流程靠密集复查调药控风险——黑诊所没有这个环节，且环境污染可致不孕（后患无穷）。
  warning_signs: ["简单安全的赚钱捷径"式话术, 出租屋操作、不给麻醉]
  bound_to: ["高风险操作的监控前提", "短期金钱与长期健康不可比价"]
  tags: [counter-example, predatory, irreversible-harm]

- id: ce29
  title: "卵巢保养"：摸不到的器官成了按摩项目
  type: counter-example
  source_chapter: 第六章 卵巢需要保养吗（SOURCE.txt:2695–2736）
  source_quote: |
    "正常大小的卵巢几乎是摸不到的，就算临床上的常规妇科查体也很难触碰到，更不要说从肚皮把药物按摩到卵巢上去了。就是按摩吐了，也没戏！"
  failure_mode: 用"20岁姑娘50岁的卵巢"恐吓新闻引流，卖精油按摩与掺杂激素的保健品。
  mechanism: 解剖上不可能经腹壁给药；掺杂激素类药物"对部分卵巢肿瘤、子宫内膜癌、乳腺癌等有一定的促进作用"（行2733）——伪需求产品不仅无效还有致癌风险；真实可做的是生活方式管理（行2742）。
  warning_signs: [恐吓标题+保养产品组合出现, "保养"承诺逆转不可逆过程]
  bound_to: ["可逆性判断", "恐吓营销识别"]
  tags: [counter-example, fear-marketing, hormone-risk]

- id: ce30
  title: 处女膜修复手术：为舆论赋予的价值买单
  type: counter-example
  source_chapter: 第六章 如何看待处女膜修复（SOURCE.txt:2646–2656）
  source_quote: |
    "真正做这种手术的人大多数是从事性交易的女性……处女膜有着一定的附加价值。这是舆论赋予这层膜的价值，如同钻石的骗局一样。"
  failure_mode: 把社会符号当身体功能去修复；术后瘢痕"有可能非常坚韧，导致同房困难"（行2650）。
  mechanism: "需要处女膜才能保护的感情，会像这层膜一样脆弱"（行2656）——修复解决不了符号系统本身，且引入真实的手术并发症。
  warning_signs: [动机是"给对方交代", 将膜等同于贞操与价值]
  bound_to: ["区分生理问题与社会建构", "手术指征审查"]
  tags: [counter-example, social-construct, unnecessary-surgery]

- id: ce31
  title: 洗内裤12步流程：过度清洁的仪式化
  type: counter-example
  source_chapter: 第六章 内裤怎么洗（SOURCE.txt:2320–2357）
  source_quote: |
    "微波炉加热3～5分钟作预处理……滑炒后小火慢炖……浇上消毒剂，开大火收汁……阴天则选择给内裤直流通电。"（作者评：健康人群"流动水+清洗剂就已经足够……洗个内裤而已，又不是做手术"）
  failure_mode: 追求绝对无菌的过度清洁仪式；"没必要刻意追求绝对的无菌、无害"（行2357）。
  mechanism: 皮肤与阴道菌群本身就是屏障；高温蒸煮反而损坏材质（行2340）；过度消毒与过度冲洗阴道（ce01）同构——把"干净"推到极限会摧毁保护系统。
  warning_signs: [多步消毒流程成为执念, 因"不够干净"反复重洗]
  bound_to: ["够用即可的清洁标准", "天然屏障保护"]
  tags: [counter-example, over-cleaning, anxiety-ritual]

- id: ce32
  title: 张悟本绿豆食疗与放血疗法：错误证据的两种死法
  type: counter-example
  source_chapter: 第六章 如何"变聪明"（SOURCE.txt:2890–2897）
  source_quote: |
    "张大师……'三大法宝'——白萝卜、绿豆和长茄子，并声称多次以此治好了肺癌、糖尿病……就连我父母也难以幸免，家里现在还有几麻袋绿豆。"（放血疗法：366名士兵对照实验，放血组死亡35人 vs 不放血组2人和4人）
  failure_mode: ①低成本伪疗法因"试试无妨"扩散并挤占正规治疗；②流传数百年的权威疗法从未被对照检验。
  mechanism: 采纳成本越低，伪疗法越易传播（"就算没用我也不亏"）；个人经验、权威资历（"医生越老越可靠"，行2898）在对照实验面前不堪一击——证据分级是唯一的防线。
  warning_signs: ["吃点又没坏处", "祖传""大师""有效个案"]
  bound_to: ["相信证据而非权威/经验", "随机对照意识"]
  tags: [counter-example, pseudo-science, evidence-hierarchy]

- id: ce33
  title: 相关≠因果的两个信息陷阱（40岁生育活百岁 / 每周3次性生活年轻10岁）
  type: counter-example
  source_chapter: 第六章 如何"变聪明"（SOURCE.txt:2886–2894）
  source_quote: |
    "如果一个女性在40岁以后自然怀孕并且生出孩子，那么她比普通女性活到百岁的可能性高出4倍……并不是40岁生孩子这件事让她们活到百岁，恰恰是因为她们身体本来就挺好，所以还能在40岁生孩子。"
  failure_mode: 把筛选效应读成因果效应；把不可验证的相关性当行动指南。
  mechanism: 前者是反向因果/健康者偏差（能40岁生育是健康的结果而非长寿的原因）；后者无法做对照实验、不具普适性——"但凡遇到不能做实验、不具有普适性的信息时，我们就要提高警惕"（行2894）。
  warning_signs: [标题式"X让Y提升N倍", 无对照、无机制的统计关联]
  bound_to: ["相关不等于因果", "可验证性与普适性审查"]
  tags: [counter-example, causal-fallacy, media-literacy]
```

## 二、作者自身的论证 / 表达风险（以下均为【读者分析】，非作者原话）

```yaml
- id: ce34
  title: 【读者分析】"多数没事"的安抚基调可能压低风险感知
  type: counter-example
  source_chapter: 全书整体结构；对照第一章血性白带（SOURCE.txt:217）、第二章鲜红色出血（SOURCE.txt:352）
  source_quote: |
    "（读者分析）作者反复使用'放宽心——但有这些红线要就医'的双段结构；若读者只记住前半段的安抚，可能把危险信号也归入'正常波动'。"
  failure_mode: 先安抚后给红线的结构，红线信息在情绪上被前文稀释；血性白带、鲜红出血、绝经后出血这类"必须立即检查"的信号可能被延迟处理。
  mechanism: 读者按最省力的策略（"多数没事"）泛化，而危险信号恰恰依赖例外识别；作者虽多处强调"重视可不是让你自己买药"（行209），但整体情绪曲线以消除焦虑为主。
  warning_signs: [读者引用本书论证"不用去医院", 出血类症状按"观察"处理超过一个周期]
  bound_to: ["就医红线清单必须独立于安抚语", "安抚与红线不可互相稀释"]
  tags: [reader-analysis, risk-communication, boundary]

- id: ce35
  title: 【读者分析】玩笑化类比（酸奶味/小蝌蚪跑道/城管军队）的记忆点与失真风险
  type: counter-example
  source_chapter: 全书，如第一章（SOURCE.txt:201, 246–255, 271）
  source_quote: |
    "（读者分析）'要我说，是酸奶味''乳酸杆菌是城管、白细胞是军队'——类比建立直觉的同时，也把机制简化成了人格化剧本。"
  failure_mode: 读者可能记住类比而丢掉机制边界：把"城管"理解为需要"补充编制"（补乳酸杆菌制剂），或把"酸奶味"当成健康标准去对照。
  mechanism: 类比是启发式而非证据（BOOK_OVERVIEW已指出"类比负责建立直觉，不能单独充当医学证据"）；拟人化会导致过度干预（给"军队"增援即ce04）。
  warning_signs: [用类比的字面逻辑推进行动, 以"标准气味/颜色"自我对照]
  bound_to: ["类比仅作入口，行动依据回到机制"]
  tags: [reader-analysis, analogy-risk, expression]

- id: ce36
  title: 【读者分析】性别刻板表述复制其反羞耻目标
  type: counter-example
  source_chapter: 第二章开篇（SOURCE.txt:372–374, 450）；第一章开篇（SOURCE.txt:171）；行472
  source_quote: |
    "（读者分析）'女性是敏感的生物，天生就有一种对健康的焦虑''处于经期的女人更是如同变身了一般，充满杀气''争取做一个安静美好的姑娘'——作者在为女性去羞耻的同时，使用了强化性别刻板印象的表达。"
  failure_mode: 把健康焦虑、情绪波动描述为女性"天生"属性，可能被读者接受为本质论断而非观察描述。
  mechanism: 作者自己的证据（原因三"心理暗示"，行458）恰恰说明焦虑部分是文化建构——论证与修辞存在张力；此类表述若进入人物 Skill 会复制其试图反对的框架。
  warning_signs: [用"女性天生……"作解释, 将经期情绪整体污名化]
  bound_to: ["区分生理机制与社会建构（作者本人原则应用于其自身表达）"]
  tags: [reader-analysis, stereotype, expression]

- id: ce37
  title: 【读者分析】大量比例与"经验法"无出处，证据标准不均质
  type: counter-example
  source_chapter: 例：洗液盆腔感染+73%（SOURCE.txt:314）；VVC 56%/51%/60%（SOURCE.txt:984）；混合感染26.05%（SOURCE.txt:993）；"某研究表明每天运动30–40分钟降低乳腺癌37%"（SOURCE.txt:1780）
  source_quote: |
    "（读者分析）多数'研究表明/数据显示'未给出研究名称、样本、年份；部分（如导师生发茵素三联1:1:1方案，行1240）为个人经验方案。"
  failure_mode: 修辞上强调"相信证据"，但正文证据分级不一致；读者无法区分随机对照结论与临床经验。
  mechanism: 权威口吻统一呈现不等可靠度的信息；第六章的证据分级原则（行2899）未被全书执行。
  warning_signs: [引用本书数字时无法溯源, 个人经验方案被当通用方案]
  bound_to: ["证据分级标注", "时效核查（2019年成书，数据可能已更新）"]
  tags: [reader-analysis, evidence-consistency, timeliness]

- id: ce38
  title: 【读者分析】对中医的调侃式处理可能造成读者立场混乱
  type: counter-example
  source_chapter: 第二章黑色血块（SOURCE.txt:434）；山楂/梨/红枣条目（SOURCE.txt:480, 490, 494）
  source_quote: |
    "（读者分析）'中医认为这是由气血两虚、气滞血瘀、肾虚等原因引起的……中医的原理我也讲不清楚，所以我就讲到这里，也不评价其对与错'——同一章内中医说法既被当禁忌来源批评（梨'性凉'），又被借来支持山楂活血（行490）。"
  failure_mode: 读者难以形成稳定规则：中医框架何时可参考、何时应忽略？可能导致全盘否定或随机采纳。
  mechanism: 作者以西医证据标准评判中医条目，但未给出统一的使用边界；否定禁忌时引机制，肯定山楂时引"活血化瘀"的功能表述——标准漂移。
  warning_signs: [按结论合意与否选择性采用中医概念]
  bound_to: ["明确证据框架边界后再讨论替代体系"]
  tags: [reader-analysis, epistemic-consistency]

- id: ce39
  title: 【读者分析】男性第一人称经验充当论据的边界
  type: counter-example
  source_chapter: 第一章气味（SOURCE.txt:277）；月经杯体验（SOURCE.txt:649–651）；乳腺增生（SOURCE.txt:1664）
  source_quote: |
    "（读者分析）'根据几十年来我对尿液的观察（你们知道的，男人不得不观察）'、作者试用卫生巾一日推断经期体验——以男性身体经验推断女性长期体验，样本为1且存在生理差异。"
  failure_mode: 一日体验、男性观察被用作对女性长期、身体性经验的论据；妻子个案（经期、乳腺）亦为n=1。
  mechanism: 共情式代入不等于第一人称知识；角色 Skill 若继承此类论证，需标注其性质为类比而非经验。
  warning_signs: ["我体验过一天所以理解", 用单一亲属/患者案例推广]
  bound_to: ["经验类论据须标注来源与样本量"]
  tags: [reader-analysis, standpoint-limitation, argument]

- id: ce40
  title: 【读者分析】"囊肿/息肉可能自行消失"类表述被过度泛化
  type: counter-example
  source_chapter: 第四章 子宫内膜息肉（SOURCE.txt:1330）；LSIL一年复查（SOURCE.txt:1287）
  source_quote: |
    "（读者分析）'有可能到经期随着内膜一起脱落了……真是来去匆匆，只带走一片内膜'——观察等待是有条件、有随访的方案，娱乐化表达可能让读者忽略'观察'本身也是医疗决策。"
  failure_mode: 把"可以不管"理解为"不用管"，跳过确认性质（病理）与随访节点。
  mechanism: 观察策略的前提是已完成恶性排除（息肉恶性率2‰–4‰仍需病理，行1322）；观察是积极决策而非不作为。
  warning_signs: [拒绝活检/复查, 以"听说会自己好"为依据长期不就诊]
  bound_to: ["观察也是方案，需指征+随访"]
  tags: [reader-analysis, watchful-waiting, boundary]
```

## 自检结果
- [x] 每条均有 failure_mode 与 mechanism（机制含因果链，非"这是错的"）
- [x] 每条有 warning_signs
- [x] 每条有 bound_to（指向阶段2 B段）
- [x] 每条有原文引用 + SOURCE 行号
- [x] ce34–ce40 明确标注【读者分析】，未冒充作者原话
- [x] 未收纯情绪化吐槽（如对洗液广告的抱怨均已落到机制层）；未筛选，候选共 40 条

**给主代理的提示**：ce01/ce03/ce18/ce32/ce33 与 BOOK_OVERVIEW 优先级 1–2（利益审计、双风险判断）对应最紧密，阶段1.5验证时可优先核对；ce37/ce38 的行号引用跨多处，落盘时建议保留全部行号以便回查。
