# Brand Extension

中文 | [English](README.en.md)

**Brand** 是一个 Spec Kit 扩展。它从项目的 `specs/` 出发，把品牌工作串成一条完整链路：品牌手册、名称查重、方向澄清，最后产出一个把视觉板、初版 logo/VI 和界面原型合在一起的页面。品牌是项目级资产，一个项目只产出一份 `brand.md`。

品牌方向由文档承载，具体色值、字体、logo 资产和原型由 `prototype` 阶段落地。名称、Slogan、锚点和视觉方向始终由人拍板；查重无法联网时标注「需人工核实」，不编造结果。

## 前置条件

- 已初始化的 Spec Kit 项目（存在 `.specify/`）
- 已完成 `/speckit-specify`，`specs/` 下至少有 1 份 `spec.md`
- Spec Kit `>= 1.4.0`

## 安装

### 方式一：从发布压缩包安装（推荐）

```bash
# GitHub（主仓库）
specify extension add --from https://github.com/1689393498/speckit-brand-foundation/raw/main/release/brand-foundation-2.1.0.zip

# Gitee（镜像）
specify extension add --from https://gitee.com/LeisDevelopment/speckit-brand-foundation/raw/main/release/brand-foundation-2.1.0.zip
```

- 两个地址内容一致，任选其一。
- 首次安装会提示 **Untrusted Source**，确认来源可信后输入 `y` 继续。
- 只支持 HTTPS（本机 `localhost` 调试可用 HTTP）。

### 方式二：自建 catalog（可选，适合团队）

```bash
specify extension catalog add https://your-host/catalog.json --name my-brand-catalog --install-allowed
specify extension add brand
```

`--install-allowed` 只应对你自己拥有并审核过的 catalog 开启。

### 方式三：本地开发

```bash
specify extension add --dev /path/to/brand-foundation
```

安装后确认：

```bash
specify extension list
specify extension info brand --json
```

## 使用

在 Claude Code 中（skills 模式），默认跑完整流程：

```text
/speckit-brand-run
```

也可以只跑其中一段：

| 命令 | 作用 |
|---|---|
| `/speckit-brand-run` | 全流程，按顺序执行并逐决策点停下 |
| `/speckit-brand-create` | 只生成或重建 `docs/brand/brand.md` |
| `/speckit-brand-name-check` | 只做名称查重，结果写入 `brand.md` |
| `/speckit-brand-clarify` | 只做品牌方向澄清 |
| `/speckit-brand-prototype` | 只做视觉板、初版 logo/VI 和原型合成页 |
| `/speckit-brand-prototype-clarify` | 只做原型行为与状态澄清 |

> Spec Kit 要求命令名为 `speckit.{extension}.{command}` 三段式，因此默认入口是 `/speckit-brand-run`，没有单独的 `/speckit-brand`。

可选补充信息可以直接跟在命令后面：

```text
/speckit-brand-run 偏专业感，不做可爱风，可能兼顾 B 端
```

### 语言

所有提问、阶段汇报和产出文档自动跟随来源 spec 的语言（多份语言不一致时确认一次）；也可以在调用时显式指定：

```text
/speckit-brand-run 请用英文输出
```

命令提示词本身是英文，便于国际用户阅读与贡献，不影响中文交互。

### 多 spec 与来源确认

一个项目通常有多个 `specs/<feature>/spec.md`。品牌是项目级资产，`brand.md` 只有一份：

- 首次运行 `/speckit-brand-create` 或 `/speckit-brand-run` 时，扩展会列出所有 spec（目录、标题、修改时间、是否为当前 feature），请你确认品牌依据哪些 spec。
- 默认纳入整个项目；可以排除内部重构、纯维护类 spec。
- 确认结果写入 `brand.md` 的第 0 节「来源」；后续澄清、查重、原型只读这份清单，不会因为 `feature.json` 切换而漂移。
- 之后新增或删除 spec 时，命令会提示，但不会自动改变来源范围。

## 流程

```text
specs/*/spec.md（确认来源集合）
  │  /speckit-brand-create
  ▼
docs/brand/brand.md                来源、项目背景、人群、定位与锚点、命名、Slogan、方向
  │  /speckit-brand-name-check
  ▼
定名（查重结果写回 brand.md）
  │  /speckit-brand-clarify
  ▼
brand.md 定稿
  │  /speckit-brand-prototype
  ▼
A：视觉板 + 初版 logo/VI
  │
  ▼
B：按 A 设计的界面原型
  │
  ▼
prototype/index.html               上：简介 + A；下：B
  │  一次性人工检查，改 B 的同时改 A
  ▼
/speckit-brand-prototype-clarify   行为与状态澄清，改 B
  │
  ▼
/speckit-plan（原生）              specs/<feature>/plan.md
```

### 各阶段停下确认的点

| 阶段 | 需要你确认 |
|---|---|
| create | 来源范围（多 spec 时）、项目一页纸、人群画像、文化锚点、名称、Slogan |
| name-check | 查重结果与最终名称 |
| clarify | 每轮最多 5 个问题 |
| prototype | 合成页一次性检查：视觉板、logo/VI、原型一起看 |
| prototype-clarify | 每轮最多 5 个问题 |

`/speckit-brand-run` 的「默认全流程」指顺序执行，不是替你拍板。每个决策点都会停下。

## 产出物

```text
docs/brand/
├── brand.md                  # 唯一品牌文字源（来源清单、查重结果与决策记录都在里面）
├── tokens.css                # 色值、字体、字号、间距、圆角，开发直接引用
└── assets/
    ├── logo/
    │   ├── logo-horizontal.svg
    │   ├── logo-stacked.svg
    │   ├── mark.svg
    │   ├── logo-mono.svg
    │   └── logo-inverse.svg
    └── app-icon.svg

prototype/
├── index.html                # 上：项目简介 + 视觉板；下：界面原型
├── styles.css                # 引用 ../docs/brand/tokens.css
├── app.js
└── README.md
```

- 不再产出单独的 `name-check.md`；查重结论、证据、风险等级并入 `brand.md` 的「命名」一节。
- 不产出 `plan.md`；下一步使用原生 `/speckit-plan`。

## 初版 logo 与 VI

`prototype` 阶段会从 `brand.md` 推出视觉板，并默认附带一版 logo 和基础 VI：

- 字标（横版、竖版）、一个简单图形标、单色与反白变体、App 图标
- 安全空间、最小尺寸、背景限制、禁用示例
- 按产品类型选 2～3 个应用示例
- 全部为可编辑 SVG；字体只用开源可嵌入字体

边界：

- 只给一个推荐方向，不做多方案比稿
- 不做商标图形近似检索；初版 logo 不构成法律意见，正式使用前请专业检索
- 不用 AI 生成的位图 logo
- 不做印刷交付（CMYK、出血、刀版），不做完整品牌手册 PDF
- 不做独立 VI 手册；视觉板是初版，不是已交付的完整视觉系统

如果项目里已有 logo，命令会先检测 `docs/brand/assets/logo/`，沿用现有资产并补规则，不重造。

## 边界

- 只读已确认的 spec 与项目已有文档，不修改任何 `spec.md`
- 名称、Slogan、锚点、视觉方向由人决定
- 查重无法联网时逐项标注「需人工核实」，不编造结果
- `brand.md` 只写方向，不写色值、字号；具体取值落在 `tokens.css`
- 产出只在 `docs/brand/` 和 `prototype/`
- 品牌工作止于原型与视觉板；工程计划交给原生 `/speckit-plan`

## 发布与版本

### 打包

```bash
python scripts/package.py
```

产出：

```text
dist/brand-foundation-2.1.0.zip
dist/brand-foundation-2.1.0.zip.sha256
```

把 zip 上传到任意 HTTPS 地址即可分发；SHA-256 可用于自建 catalog 或用户校验。

### 版本升级

1. 修改 `extension.yml` 中的 `extension.version`
2. 在 `CHANGELOG.md` 记录变更
3. 重新执行 `python scripts/package.py`

## 目录结构

```text
brand-foundation/
├── extension.yml
├── commands/
│   ├── brand-run.md                  # speckit.brand.run
│   ├── brand-create.md               # speckit.brand.create
│   ├── brand-name-check.md           # speckit.brand.name-check
│   ├── brand-clarify.md              # speckit.brand.clarify
│   ├── brand-prototype.md            # speckit.brand.prototype
│   └── brand-prototype-clarify.md    # speckit.brand.prototype-clarify
├── scripts/
│   └── package.py
├── README.md        # 中文
├── README.en.md     # English
├── CHANGELOG.md
├── LICENSE
├── release/         # 已提交的发布归档，供 --from 下载
└── dist/            # 本地打包产物，不提交
```

## 从 1.x 升级

2.0.0 是破坏性重构：

- `speckit.brand.foundation` 移除，改用 `/speckit-brand-run` 及其子命令
- `docs/brand/name-check.md` 并入 `brand.md`，可删除
- 独立安装的 `speckit-prototype-clarify` 由本扩展的 `/speckit-brand-prototype-clarify` 取代
- 已有 `prototype/` 会被检测；命令会询问「沿用 / 重建」，不会静默覆盖

### 从 2.0.0 升级

2.1.0 不破坏兼容，已有 `brand.md` 可继续使用。首次运行任一命令时，若缺少第 0 节「来源」，会回退一次旧的 spec 定位方式并提示补写；确认后写入来源清单。

## 仓库与同步

| 仓库 | SSH 地址 | 远端名 |
|---|---|---|
| GitHub（主仓库） | `git@github.com:1689393498/speckit-brand-foundation.git` | `github` |
| Gitee（镜像） | `git@gitee.com:LeisDevelopment/speckit-brand-foundation.git` | `origin` |

```bash
git push origin main   # Gitee
git push github main   # GitHub
```

GitHub 使用 SSH 连接；首次使用需把本机公钥添加到 GitHub 账号。

## 卸载

```bash
specify extension remove brand
```

## 许可证

MIT
