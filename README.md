# VCI 可视计算与交互复习笔记

从 Lab 1 的二维绘制出发，解释颜色、显示、图像处理、光栅化、插值、曲线和采样，并整理真题参考解析、独立自测与补充问答。

> **持续更新中｜课程尚未结束**
> 
> 内容更新至：2026-10-13 · 本次发布整理：2026-10-13

## 当前范围

当前为第一阶段讲解版，覆盖已提供的 01–07 课件及 Lab 1 相关原理，15 章沿用讲义编号。课程尚未结束，也未据此宣称老师确认的完整考试范围。

第 13 章包含整套真题参考解析；第 14 章自测答案默认折叠。搜索排除练习答案和真题解析。

## 开始阅读

- [在线 HTML 阅读](https://by-lastime.github.io/vci-study-notes/)：无需安装。
- [下载完整仓库 ZIP](https://github.com/by-lastime/vci-study-notes/archive/refs/heads/main.zip)：解压后打开 `site/index.html`，保留同目录的资源文件。
- [Markdown 源稿](content/)：用于查看原文与追溯修订。

## 内容目录

- [阅读路线与范围](https://by-lastime.github.io/vci-study-notes/#doc=overview)
- [1 引言：可视计算与交互在研究什么](https://by-lastime.github.io/vci-study-notes/#doc=d1)
- [2 颜色：光、数字和感知](https://by-lastime.github.io/vci-study-notes/#doc=d2)
- [3 图像表示与显示](https://by-lastime.github.io/vci-study-notes/#doc=d3)
- [4 图像滤波：从核到手算](https://by-lastime.github.io/vci-study-notes/#doc=d4)
- [5 修复、融合与抠图](https://by-lastime.github.io/vci-study-notes/#doc=d5)
- [6 光栅化：直线、圆与增量算法](https://by-lastime.github.io/vci-study-notes/#doc=d6)
- [7 多边形、三角形与插值](https://by-lastime.github.io/vci-study-notes/#doc=d7)
- [8 贝塞尔曲线：构造、性质与真题证明](https://by-lastime.github.io/vci-study-notes/#doc=d8)
- [9 样条：低次分段和局部控制](https://by-lastime.github.io/vci-study-notes/#doc=d9)
- [10 抖动与误差扩散](https://by-lastime.github.io/vci-study-notes/#doc=d10)
- [11 采样、反走样与超采样](https://by-lastime.github.io/vci-study-notes/#doc=d11)
- [12 Lab 1 对照：从做出效果到说清原理](https://by-lastime.github.io/vci-study-notes/#doc=d12)
- [14 自测变式与答案](https://by-lastime.github.io/vci-study-notes/#doc=d14)
- [15 公式速查、使用约定与来源](https://by-lastime.github.io/vci-study-notes/#doc=d15)
- [补充问答 · Q001–Q017](https://by-lastime.github.io/vci-study-notes/#doc=supplements)

## 答案入口

建议先独立尝试，再展开或打开答案。
- [第13章：去年真题逐题参考解析](https://by-lastime.github.io/vci-study-notes/#doc=d13)
- [第14章：16道自测与逐题折叠答案](https://by-lastime.github.io/vci-study-notes/#doc=d14)

## 使用方式

### 在线与离线 HTML

左侧切换讲次或章节，右上「目录」定位小节，「Aa」调整字号与深浅色。Q 编号链接在当前页面弹窗展示补充解答，关闭后返回阅读位置。公式、字体、代码样式和图表资源随阅读器提供，离线阅读无需联网。

下载 ZIP 后须完整解压，再双击 `site/index.html`。直接双击模式读取已生成内容；源稿修改后需要重新构建并刷新。阅读位置与外观保存在当前浏览器，不代表学习进度。

### PDF 与打印

正文与练习包含补充问答；第 13 章真题解析及第 14 章自测答案放入独立答案册。PDF 保留网页章号，所以正文从第 12 章跳至第 14 章。

- [第一阶段复习讲义](https://by-lastime.github.io/vci-study-notes/downloads/%E7%AC%AC%E4%B8%80%E9%98%B6%E6%AE%B5%E5%A4%8D%E4%B9%A0%E8%AE%B2%E4%B9%89.pdf)
- [第一阶段复习讲义-答案册](https://by-lastime.github.io/vci-study-notes/downloads/%E7%AC%AC%E4%B8%80%E9%98%B6%E6%AE%B5%E5%A4%8D%E4%B9%A0%E8%AE%B2%E4%B9%89-%E7%AD%94%E6%A1%88%E5%86%8C.pdf)

## 来源与使用约定

参考本学期课件、Lab 1、署名 Sparkle 的《Quiz_Review_01》笔记及 2025 年第一次小测。署名、原资料定位与核对来源保留。真题材料未提供官方答案，解答属于参考推导。

本仓库发布整理后的复习笔记、教学问答、必要插图和对应阅读器。原始教材、课件、扫描试卷、实验工程和个人学习记录未随仓库分发；来源名称、章节及页码保留供核对。原内容署名与权利按来源保留。阅读器依赖说明见 [ORIGIN.md](ORIGIN.md)。

## 更新与维护

Markdown 是内容源稿。补充、更正先改 `content/`，随后构建 HTML；需要更新打印版时再导出 PDF。生成的 `site/content.js` 不单独维护。

```sh
npm ci
npm run build
npm start
```

本地 HTTP 阅读入口为 `http://127.0.0.1:8765`；也可直接打开 `site/index.html`。

导出 PDF 需要 Pandoc、XeLaTeX 及脚本指定的中文字体：

```sh
npm run pdf
```

推送 `main` 后，GitHub Actions 构建并更新 HTML 阅读网站。PDF 为已核对的发布副本；网页构建不会自动重排 PDF。后续新增课程范围与修订记录会在此更新。

## 发布记录

- 2026-10-13：整理当前阶段笔记，建立独立仓库，提供在线与离线 HTML、PDF 和补充问答入口；标记持续更新。
