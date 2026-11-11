# 《女生呵护指南》术语提取候选报告（阶段1 · glossary lane）

> 提取人：glossary extractor。共 18 条候选。全部为作者反复使用、明确定义、用法与常识不同或核心论点组成词。一般妇科疾病名词（子宫肌瘤、畸胎瘤等）未收录。本阶段不筛选，主代理负责落盘与阶段1.5验证。

```yaml
- id: g01
  term: 正常范围（动态正常）
  type: term
  source_chapter: 第一章"什么样的白带是正常的"（SOURCE.txt:188-202）；第二章"什么样的月经是正常的"（SOURCE.txt:399-421）
  author_definition: |
    "白带并不只有一种固定的状态……白带会随着女性在月经周期内所处的阶段不同而变化"
    "白带的正常范畴还是挺宽泛的"；月经周期波动1周以内均属正常。
  key_distinction: |
    ≠ 教科书上的单一标准形态（"量少、白色、无异味"/"28～30天来一次"）
    = 随周期阶段、年龄、妊娠、饮食、情绪、环境变化的动态区间；单点读数偏离标准不等于异常
  why_it_matters: |
    全书判断框架的起点。若沿用"固定标准"义，skill 会教用户拿单一指标自我诊断；
    正确用法是"先定位所处阶段，再看是否落在动态区间内"。
  tags: [term, core-concept, judgment-framework]

- id: g02
  term: 自身基线
  type: term
  source_chapter: 第二章（SOURCE.txt:405-409, 419-420）
  author_definition: |
    "作为医生，我们更加在意的是月经周期的规律性……如果你的月经周期本身是规律的，
    不管时间间隔是一个月，还是两个月，甚至三个月到半年，那都可以理解为正常。"
    判断月经量也要与"原来"比较（比原来增减1/2）。
  key_distinction: |
    ≠ 与"28天模板"或他人比较；≠ 单次波动即异常
    = 与个人既往周期/表现比较，且需持续超过三个月经周期才考虑就诊
  why_it_matters: |
    是所有"异常判断"类回答的前置步骤：skill 必须先问"你之前是什么样的"，
    否则会把个人正常基线误判为疾病，制造恐慌。
  tags: [term, core-concept, judgment-framework]

- id: g03
  term: 处理方法
  type: term
  source_chapter: 第一章"内裤上总是有东西"（SOURCE.txt:334-362，10种情况每条末尾固定出现）
  author_definition: |
    每种分泌物/出血情况末尾给定的边界动作，如"处理方法：注意清洗外阴及更换内裤"
    "处理方法：密切观察，及时就诊""处理方法：检查白带常规，规范用药"。
  key_distinction: |
    ≠ 让读者照书自行诊断和用药；≠ 治疗方案
    = 分层的行动边界：观察/清洁/记录/就诊，"这里的重视可不是让你自己去药店买药自己治疗"（SOURCE.txt:209）
  why_it_matters: |
    是作者科普的安全绳设计：只交付到"下一步该做什么"为止，不越界到诊断开药。
    人物 skill 输出健康建议时必须保持这个层级，否则越界变成伪诊疗。
  tags: [term, output-structure, safety-boundary]

- id: g04
  term: 自净功能／菌群平衡（微生态）
  type: term
  source_chapter: 第一章（SOURCE.txt:183, 294-301）；第三章"如何预防阴道炎复发"（SOURCE.txt:1012-1015）
  author_definition: |
    "这个内环境具有一定的自净功能，同时还可以抵御外来病原体的侵入"；阴道有30余种常驻菌群，
    乳酸杆菌是"警察"，维持pH 3.8～4.4的微妙平衡；"菌群失衡"是阴道炎的核心机制。
  key_distinction: |
    ≠ "越洗越干净"；干预（洗液、冲洗、滥用抗生素）本身会破坏平衡
    = 平衡是保护机制，维护平衡比清除细菌更重要
  why_it_matters: |
    作者反对洗液、反对冲洗阴道、慎用抗生素的全部论证都建立在这个词上。
    若按常识理解为"卫生=灭菌"，skill 会输出完全相反的建议。
  tags: [term, core-concept, mechanism]

- id: g05
  term: 三道天然防护屏障
  type: term
  source_chapter: 第一章"私处怎么洗"（SOURCE.txt:294-301）
  author_definition: |
    "第一道：两扇大门——大小阴唇；第二道：自净工厂——阴道菌群；第三道：自我封闭——宫颈黏液栓。"
  key_distinction: |
    ≠ 需要外用产品额外保护的"脆弱部位"
    = 人体自带的结构性防御系统；市售护理品的"保护"叙事与生理事实相反
  why_it_matters: |
    作者用来拆解"洗洗更健康"类营销话术的核心论据；人物 skill 评价任何
    私处护理产品时应先对照这三道屏障是否被干预破坏。
  tags: [term, mechanism, anti-marketing]

- id: g06
  term: 妆字号／消字号／药准字号（洗液三分类）
  type: term
  source_chapter: 第一章"私处怎么洗"（SOURCE.txt:305-312）
  author_definition: |
    妆字号：无治疗成分，"作用还不如清水"；消字号：杀菌抑菌针对所有菌群，"长时间使用肯定会
    破坏阴道内的菌群平衡"；药准字号：用于治疗阴道炎，"需要在医生指导下使用，不能擅自买来用"。
  key_distinction: |
    ≠ 广告里统一包装成的"私处护理必需品"
    = 按批准文号划分的三类产品，作者结论分别是"不要用/不要用/遵医嘱用"
  why_it_matters: |
    作者特定用法，字典和常识均无此区分意识。skill 涉及洗液/护理品话题时
    若不按此分类讨论，会误把消字号产品当成日常清洁推荐。
  tags: [term, author-specific, anti-marketing]

- id: g07
  term: 月经史
  type: term
  source_chapter: 第二章"一定要牢记自己的月经史"（SOURCE.txt:867-885）
  author_definition: |
    "它包括初次月经年龄、月经周期时长、经期时长、末次月经时间、月经量多少、月经颜色、
    是否伴有痛经或者其他症状等。"
  key_distinction: |
    ≠ 单纯"上次月经是什么时候"
    = 一组结构化的个人健康数据，影响妇科检查时机、治疗方案选择和手术风险（出血风险）
  why_it_matters: |
    是作者强调读者应主动掌握并向医生如实提供的核心信息包；skill 引导用户
    就医准备时应按这七项组织信息，而不是笼统说"记录月经情况"。
  tags: [term, practical-tool]

- id: g08
  term: 原发性痛经／继发性痛经
  type: term
  source_chapter: 第二章（SOURCE.txt:743-752, 791-803）
  author_definition: |
    "痛经分为两种……前者是与生俱来的，很多人从第一次来月经开始就会有痛经的情况；
    后者显然是由某些因素导致的痛经"——继发性痛经由子宫内膜异位症、子宫腺肌病等疾病导致。
  key_distinction: |
    ≠ 所有痛经一概"忍忍就好"或"喝热水"
    = 原发性：机制是前列腺素，可用解热镇痛药/短效避孕药，需在痛前1～2天服药；
      继发性：止痛药无效是典型信号，提示必须检查原发病
  why_it_matters: |
    这个区分直接决定行动分支：原发性→正确用药；"用了止痛药都无效"→就医排查。
    混淆两者会导致 skill 要么轻视疾病信号，要么制造不必要恐慌。
  tags: [term, core-concept, triage]

- id: g09
  term: 经血逆流
  type: term
  source_chapter: 第二章"经血会逆流吗"（SOURCE.txt:559-581）
  author_definition: |
    "几乎你们每个人都出现过经血逆流，只是你们自己不知道而已"；"90%的女性都有经血逆流的情况，
    而子宫内膜异位症的发生率却很低"。
  key_distinction: |
    ≠ 经血逆流＝子宫内膜异位症＝不孕（民间恐惧链条）
    = 普遍生理现象；只有少数"随遇而安型"内膜+其他因素才可能发展为疾病；
      因此"经期倒立/同房致病"的说法站不住脚
  why_it_matters: |
    作者示范"用机制拆解恐惧"的标志性案例；skill 涉及经期禁忌类问题时的标准推理模板。
  tags: [term, mechanism, myth-busting]

- id: g10
  term: 生理性／病理性（检出≠疾病）
  type: term
  source_chapter: 第三章"盆腔积液"（SOURCE.txt:1182-1189）；另见宫颈囊肿（SOURCE.txt:1250-1257）、宫颈糜烂样改变（SOURCE.txt:1133-1145）
  author_definition: |
    "盆腔积液的深度小于3厘米，且身体没有其他不适的症状，那么通常是不需要处理的……
    生理性盆腔积液，无需治疗"；宫颈囊肿"只是一种生理现象形成的良性改变"。
  key_distinction: |
    ≠ 检查报告出现名词＝患病＝需要治疗
    = "存在异常指标"与"需要治疗"之间隔着症状、整体检查和医学指征
  why_it_matters: |
    贯穿第三章的主导判断模式：作者反复用同一框架拆解盆腔积液、宫颈囊肿、
    "宫颈糜烂"。skill 必须保留这个"先分类生理性/病理性，再看症状指征"的两步判断。
  tags: [term, core-concept, judgment-framework]

- id: g11
  term: 宫颈糜烂样改变
  type: term
  source_chapter: 第三章（SOURCE.txt:1133-1181）
  author_definition: |
    ""宫颈糜烂"这个词早已经在2008年从《妇产科学》第7版教材上取消了……现在称之为
    宫颈糜烂样改变，说到底它只是一种改变，而不是疾病"，本质是宫颈柱状上皮异位的生理现象。
  key_distinction: |
    ≠ 疾病；≠ 与性生活不检点相关（道德绑架）；≠ 会发展成宫颈癌
    = 雌激素驱动的正常生理改变；与宫颈炎、宫颈病变、宫颈癌是三条互不关联的通路（SOURCE.txt:1178-1181）
  why_it_matters: |
    是全书"被商业和羞耻制造成的伪疾病"的最典型案例，也是作者科普生涯的标志性议题。
    人物 skill 谈此类话题时若沿用旧词旧义，即失去作者立场的根基。
  tags: [term, core-concept, myth-busting, anti-marketing]

- id: g12
  term: 治疗欲望
  type: term
  source_chapter: 第三章"宫颈炎"（SOURCE.txt:1073, 1091, 1107）
  author_definition: |
    "所谓的治疗欲望，指的是患者一旦发现自己有这种病，就会产生的一种想尽一切办法治愈它的欲望。"
  key_distinction: |
    ≠ 患者真实 medically 需要的治疗
    = 被恐惧、羞耻和无良医院话术点燃的心理需求，常导致过度医疗；
      "很多人希望医生给自己开药，甚至认为如果不开药，就是不负责任"
  why_it_matters: |
    作者对"过度医疗"心理机制的命名。人物 skill 识别用户"非治不可"的焦虑时，
    应先处理治疗欲望本身，而不是顺着欲望给方案。
  tags: [term, author-specific, psychology]

- id: g13
  term: 补救措施
  type: term
  source_chapter: 第五章"紧急避孕药"（SOURCE.txt:1887-1918）、"意外怀孕"（SOURCE.txt:2022）
  author_definition: |
    "服用紧急避孕药只能作为常规避孕措施失败后亡羊补牢的手段"；"人工流产只是避孕失败后的
    补救措施，绝对不是一种避孕方式"。
  key_distinction: |
    ≠ 常规避孕手段；≠ 低代价可重复选项
    = 分层中的最末层：常规预防失败后降低损害的手段，本身成功率仅85%左右且有明确代价
  why_it_matters: |
    "预防→常规→补救"三层划分是作者避孕论述的骨架。若不保留分层，
    skill 可能把紧急避孕药/人流描述成与常规避孕并列的选项，严重失真。
  tags: [term, core-concept, layered-decision]

- id: g14
  term: 长效可逆避孕措施（LARC）
  type: term
  source_chapter: 第五章"长期避孕"（SOURCE.txt:1927-1950）
  author_definition: |
    "皮埋和宫内节育器、避孕针剂避孕法一样，都属于长效可逆避孕措施"；短效措施使用者
    "意外怀孕率要高22倍"；皮埋避孕成功率超过99%，可持续3～5年，取出后立刻恢复生育能力。
  key_distinction: |
    ≠ "上环=老一辈落后选择"的民间印象
    = 国际权威机构联合推广、作者明确推崇但国内认知不足的一线方案
  why_it_matters: |
    作者在此与国内主流认知相反、立场明确。skill 需要保留这个"反常识推崇"，
    否则会复刻民间对皮埋/新式宫内节育器的偏见。
  tags: [term, author-specific, recommendation]

- id: g15
  term: 不是问题的问题
  type: term
  source_chapter: 第六章章名及全章（SOURCE.txt:145, 2213-2742）；典型如假性湿疣（SOURCE.txt:2370-2405）、阴道松弛（SOURCE.txt:2462-2509）、乳晕颜色（SOURCE.txt:2260-2291）
  author_definition: |
    被羞耻、审美或商业话术制造成"疾病"的正常现象：假性湿疣"它的确不是病"；
    "阴道松弛并不是真正意义上的病，之所以被重视主要是因为主观因素"；
    "如果审美开始绑架正常的生理现象……那么再主流的审美也是畸形的审美"。
  key_distinction: |
    ≠ "这个问题不存在"——困扰是真实的（羞耻、焦虑、关系压力）
    ≠ 需要医学处理的问题——不存在医学指征
    = 困扰真实存在，但解决方案是去羞耻化和认知纠正，而非治疗
  why_it_matters: |
    全书书名级的核心概念。人物 skill 区分"要给医学信息的问题"与"要给情感支持
    和去羞耻回应的问题"时，必须依赖这个范畴，否则会把伪需求当疾病处理。
  tags: [term, core-concept, de-stigmatization]

- id: g16
  term: 证据／相信证据
  type: term
  source_chapter: 第六章"如何'变聪明'"（SOURCE.txt:2880-2899）
  author_definition: |
    ""变聪明"的关键——相信证据"；证据按"质量和可靠程度分高级和低级"，
    随机对照研究优于个人经验；"凡是遇到不能做实验、不具有普适性的信息时，我们就要提高警惕"。
  key_distinction: |
    ≠ "专家说了""隔壁大妈好了""网上都这么说"
    = 可核查的研究与论证；个案、幸存者偏差、广告话术、相关≠因果都需单独审查
  why_it_matters: |
    全书方法论收束点，也是人物 skill 的根本立场。作者自己的经验法（"六层楼的经验"）
    在此框架内属于低级别证据——skill 表述时需保留这一自我设限。
  tags: [term, core-concept, epistemology]

- id: g17
  term: 条件致病菌（条件致病性真菌）
  type: term
  source_chapter: 第五章"性传播疾病·病原体"（SOURCE.txt:2122-2123）
  author_definition: |
    "就是要到一定条件，这种真菌才有可能引起疾病，如果条件不合适，即使存在这种真菌
    也不会引起疾病，自然也就不用治疗。这就是六层楼经常跟你们说如果没有症状可以不处理的原因。"
  key_distinction: |
    ≠ 检出病原体＝感染＝必须清除
    = 病原体存在与否不决定行动，症状与条件才决定；"根治一定是骗人的"（SOURCE.txt:1001）
  why_it_matters: |
    支撑作者"无症状不处理"的一系列建议。若按常识"有菌即治"，skill 会输出
    与作者立场相反的过度治疗建议。
  tags: [term, mechanism, judgment-framework]

- id: g18
  term: 微创手术（≠腹腔镜手术）
  type: term
  source_chapter: 第六章"妇科手术有哪些"（SOURCE.txt:2743-2778）
  author_definition: |
    "所谓的微创只是一种观念和思路，是指依靠现有的科技和医生的技巧，尽可能地缩小手术创伤……
    凡是满足这一条件的手术都可以称为微创手术"；"人们嘴里说得最多的微创手术绝大多数是指
    腹腔镜手术。虽然腹腔镜手术更好地贯彻了微创手术的理念，但是这两者之间不能画等号"。
  key_distinction: |
    ≠ 腹腔镜手术的同义词；≠ 营销话术中的"高科技、恢复快、不伤身"
    = 一种原则；阴式手术反而是"真正的微创"却最不被市场提及；手术方式应个体化选择而非点名"微创"
  why_it_matters: |
    作者对营销概念偷换的警惕示范。skill 讨论手术选择时应复现"原则≠术式、
    反对按广告点菜"的立场，避免把"微创"当成可指定购买的商品。
  tags: [term, author-specific, anti-marketing]
```

---

## 与 BOOK_OVERVIEW.md 关键术语表的交叉说明

阶段0表格中的 9 条术语（正常范围、自身基线、处理方法、自净/微生态、伴生状态、补救措施、不是问题的问题、证据、知情选择）全部被本报告覆盖或对应（g01-g05, g13, g15, g16）。其中两点差异供阶段1.5验证注意：

1. **"伴生状态"**：在 SOURCE.txt 全文中未检索到该词作为术语反复出现（宫颈炎一节用的是"伴随终身"的表述，SOURCE.txt:1078），疑似阶段0的概括词而非作者原词，故本次未单列；其语义已由 g10（检出≠疾病）和 g17（条件致病菌）承载。
2. **"知情选择"**：作为名词短语在原文中未成定义，但作者的用法特征明确——"权衡利弊，选择利大于弊的方案，而不是一心盯着副作用"（SOURCE.txt:1905）、"具体的……由患者说了算"（SOURCE.txt:2807）、"这个选择权还是交给你们自己"（SOURCE.txt:680）。若阶段1.5要求收录，建议以"权衡利弊式知情选择"命名并引用上述三处原文，本次因"未明确定义"暂未单列（可在筛选阶段决定是否补入）。

## 自检

- [x] author_definition 全部使用书中原文片段（含 SOURCE 行号）
- [x] 每条均满足四条件之一：反复出现（≥3次）或明确定义或用法异于常识或核心论点组成词
- [x] 未收录一般妇科疾病名词（子宫肌瘤、畸胎瘤、HPV 疫苗细节等）
- [x] 18 条，在 5-20 区间内
