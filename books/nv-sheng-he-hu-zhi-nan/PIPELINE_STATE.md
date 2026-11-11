# 《女生呵护指南》拆书辅助流水线状态

> 用途：为「六层楼先生」人物 Skill 提供本地一手语料，不另做作者角色扮演；最终人物 Skill 位于项目根目录 `SKILL.md`。

- [x] 输入确认：EPUB；六层楼著；2019 年 7 月第 1 版；浙江科学技术出版社
- [x] 试点：本书为本项目第一本试点书
- [x] 文本提取：`SOURCE.txt`、`MANIFEST.json`
- [x] 阶段 0：Adler 整书理解（六章阅读笔记及 `BOOK_OVERVIEW.md` 已完成）
- [x] 用户确认整书骨架（2026-11-10，确认按当前骨架继续）
- [x] 阶段 1：框架/原则/案例/反例/术语五路提取（22/66/30/40/18 条，已落盘）
- [x] 阶段 1.5：三重验证完成（7 个通过单元、4 条降级）；用户于 2026-11-10 确认进入跨书验证
- [ ] 阶段 2：将跨书验证后的方法论并入人物 Skill（RIA++ 证据结构）
- [x] 阶段 3：与另外两本书及网络调研交叉链接（`07-local-corpus-validation.md`）
- [ ] 阶段 4：人物 Skill 压力测试
- [ ] 阶段 5：交付与安装

## 源文件

- 原始 EPUB：`references/sources/books/`（保留原文件）
- 提取文本：`books/nv-sheng-he-hu-zhi-nan/SOURCE.txt`
- 提取元数据：`books/nv-sheng-he-hu-zhi-nan/MANIFEST.json`

## 下一步

汇总六章阅读笔记，生成 `BOOK_OVERVIEW.md`，向用户展示主旨、骨架、术语与作者局限。
