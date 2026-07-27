# Career Prep Coach

一个面向求职准备的独立 Agent Skill，支持 Claude Code、Claude.ai 和 Codex，覆盖三条核心链路：

1. 把零散的实习、工作、项目、创业或校园经历，深挖成可复用的完整经历档案。
2. 从全部经历中推荐职业方向，确认选材策略后生成通用版、方向版或 JD 定制简历。
3. 基于具体 JD 和真实经历，生成面试手册与岗位知识体系。

它不依赖配套网页，也不要求用户单独配置模型 API。安装后直接在支持 Skill 的 Agent 中使用即可。

## 核心能力

### 经历深挖

- 自动识别一段经历中包含的多个项目或工作模块。
- 每轮只追问一个最影响成品质量的问题。
- 根据已有经历提供可选答案，支持单选、多选和自由补充。
- 区分用户确认的事实、模型推断和 AI 建议，不擅自补写成果。
- 多项目经历会逐个覆盖，不会只分析一个项目就提前结束。
- 最终产出：
  - 详细经历底稿
  - 当前单段经历的简历 bullet
  - 800–1200 字完整经历故事
  - 30 秒与 90 秒面试表达
  - 核心亮点
  - 高频追问与应对思路

### 面试准备

- 首次收到 JD 时先完成岗位拆解，不会直接生成一整套泛化内容。
- 用户确认拆解后，再生成完整七章面试手册。
- 面试问题预测包含 15–20 道题，并结合用户真实经历给出回答结构。
- 明确区分：
  - 直接命中
  - 可迁移能力
  - 部分覆盖
  - 真实缺口
- 可单独生成岗位知识体系：
  - Mermaid 思维导图
  - 2–4 个知识模块
  - 核心概念、应用场景、指标与具体例子
  - 应用场景总览

### 方向化简历

- 根据全部经历中的动作、结果和能力证据动态推荐 3–5 个方向，不只照抄历史岗位 title。
- 支持通用版本、AI 推荐方向、自定义方向和具体 JD 定制。
- 生成前先形成结构化选材策略：
  - 主打、保留、弱化或排除哪些经历
  - 每段经历的强调角度
  - 经历分量与 bullet 数量
- 用户确认策略后才生成整份简历。
- 用户手动选择高于 AI 推荐，不会因“方向不够匹配”擅自吞掉经历。
- 通过稳定经历 ID 关联资产、策略和简历，避免标题相似导致误去重。
- 实习中的项目仍保留在实习经历，独立项目才进入项目经历。

### 局部优化

可以只优化某一个成品块，而不覆盖整份内容：

- 单条简历 bullet
- 经历档案中的某个部分
- 面试手册中的某一章
- 知识体系中的某个模块

## 使用流程

### 经历分析

```text
使用 $career-prep-coach 深挖下面这段经历：

[粘贴经历内容]
```

Skill 会先确认经历范围，再通过低负担追问补齐背景、行动、判断、结果证据和个人贡献边界。信息充分后，用户可以选择：

- **精准模式**：只使用已确认事实。
- **增强模式**：允许给出待确认的 AI 建议，并明确标记。

### 面试准备

```text
使用 $career-prep-coach，结合我的经历帮我准备这个岗位的面试：

[粘贴 JD]
[粘贴简历或经历档案]
```

面试准备采用分阶段流程：

```text
JD 拆解
  ↓ 用户确认
七章面试手册
  ↓ 按需继续
知识体系 / 模拟追问 / 局部优化
```

### 生成方向化简历

```text
使用 $career-prep-coach，读取下面全部经历，推荐适合的职业方向并生成简历：

[粘贴全部经历档案]
```

简历采用强制确认链路：

```text
全部经历
  ↓
方向推荐或自定义方向
  ↓
选材策略
  ↓ 用户确认或调整
完整简历
```

通用版同样经过选材策略，只是保持能力覆盖均衡；方向版会改变每段经历的分量和表达重点；JD 定制版会围绕具体岗位重新制定策略。三种版本都不会改变经历事实和一级栏目归属。

### 局部改写

```text
使用 $career-prep-coach，只优化下面这条 bullet，让个人判断和方法更具体：

[粘贴 bullet]
```

Skill 只返回原文和 2–3 个替换候选，不会重写整份档案。

## 安装

### 在 Claude Code 中直接安装

在 Claude Code 对话中依次输入：

```text
/plugin marketplace add hirclelili/career-prep-coach
/plugin install career-prep-coach@career-prep-coach
/reload-plugins
```

安装后，直接说“帮我深挖这段经历”或“结合我的经历拆解这个 JD”即可触发。

### 在 Claude.ai 中安装

1. 下载 [`dist/career-prep-coach.zip`](dist/career-prep-coach.zip)
2. 打开 Claude 的 `Customize → Skills`
3. 点击 `+ → Create skill → Upload a skill`
4. 上传 ZIP 并启用

不要直接上传 GitHub 自动生成的 Source code ZIP；它的外层目录带有分支后缀，不符合 Claude 自定义 Skill 的目录规则。

### 在 Codex 中安装

在 Codex 中直接发送：

```text
请使用 skill-installer 安装这个 Skill：
https://github.com/hirclelili/career-prep-coach
```

安装完成后，在下一条消息中使用 `$career-prep-coach`。

### 使用安装脚本

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo hirclelili/career-prep-coach \
  --path skills/career-prep-coach \
  --name career-prep-coach \
  --method git
```

默认安装到：

```text
~/.codex/skills/career-prep-coach
```

如果目标目录已经存在，请先更新现有安装或选择新的安装目录，不要直接覆盖未知文件。

## 事实安全

这个 Skill 把内容分为三类：

| 类型 | 含义 | 使用方式 |
|---|---|---|
| `confirmed` | 用户原文或明确确认的信息 | 可以写入正式成品 |
| `inferred` | 根据行业或岗位作出的合理推断 | 只能作为追问选项 |
| `suggested` | 为补全方法或流程提供的 AI 建议 | 必须标记并等待确认 |

不会自动虚构：

- 数据结果
- 上线效果
- 用户反馈
- 公司内部事实
- 奖项与评价
- 个人贡献边界
- 未实际使用过的 RAG、Agent 或其他技术方案

## 搜索能力

如果宿主 Agent 已经提供网页搜索工具，Skill 可以在具体 JD 的简历定制或面试准备时按需查询公司官网、业务介绍和同类岗位信息。

搜索只用于补充公司、业务和岗位语境，不会被用来补写用户的个人经历。通用方向推荐不会搜索。没有搜索工具时，Skill 仍可仅根据 JD 和用户材料正常工作。

## 不包含的功能

- 不负责网页中的经历库、岗位库、草稿缓存和按钮状态。
- 不提供简历 Word、PDF 或图片导出。
- 不依赖原网页项目的岗位库、经历库或浏览器缓存。
- 不自动把草稿视为已保存档案。

Skill 会生成完整的 Markdown 简历内容；文档模板和 Word、PDF、PNG 导出仍由网页或宿主文档工具负责。

## 项目结构

```text
career-prep-coach/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── dist/
│   └── career-prep-coach.zip
└── skills/
    └── career-prep-coach/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        └── scripts/
            └── validate_artifact.py
```

## 产物校验

保存 Markdown 产物后，可以运行：

```bash
python3 skills/career-prep-coach/scripts/validate_artifact.py experience <经历档案路径>
python3 skills/career-prep-coach/scripts/validate_artifact.py resume <简历路径>
python3 skills/career-prep-coach/scripts/validate_artifact.py manual <面试手册路径>
python3 skills/career-prep-coach/scripts/validate_artifact.py knowledge <知识体系路径>
```

校验器会检查必需章节、问题数量、思维导图、禁止标记和常见结构错误。

## License

当前项目尚未添加开源许可证。在添加许可证前，代码默认保留全部权利。
