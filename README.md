# Brand Foundation Extension

一个面向 Spec Kit 的品牌策划扩展：从项目已有的 `spec.md` 出发，按四阶段流程完成品牌地基建设，最终产出 `brand.md` 与名称查重报告。

每个阶段结束后都会停下来等待确认，不会自行跳到下一阶段——锚点、名称、Slogan 都由你拍板。

## 前置条件

- 已初始化的 Spec Kit 项目（存在 `.specify/`）
- 已完成 `/speckit-specify`，项目内有 `spec.md`
- Spec Kit `>= 1.4.0`

## 安装

### 方式一：从发布压缩包安装（推荐）

```bash
specify extension add --from https://gitee.com/LeisDevelopment/brand-foundation/raw/main/release/brand-foundation-1.0.0.zip
```

- 当前托管在 Gitee；如果仓库迁移，替换为新的 HTTPS 地址。
- 首次安装会提示 **Untrusted Source**，确认来源可信后输入 `y` 继续。
- 只支持 HTTPS（本机 `localhost` 调试可用 HTTP）。

### 方式二：自建 catalog（可选，适合团队）

```bash
specify extension catalog add https://your-host/catalog.json --name my-brand-catalog --install-allowed
specify extension add brand
```

`--install-allowed` 只应对你自己拥有并审核过的 catalog 开启。添加后可以用 `specify extension search` 在该 catalog 内搜索。

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

在 Claude Code 中（skills 模式）：

```text
/speckit-brand-foundation
```

也可以带可选补充信息：

```text
/speckit-brand-foundation 偏专业感，不做可爱风，可能兼顾 B 端
```

其他集成使用各自的调用语法。

## 四个阶段

| 阶段 | 内容 | 是否需要你确认 |
|---|---|---|
| 1. 定位与锚点 | 提炼人群画像，提出澄清问题；给出 2～3 个文化锚点候选和品牌名草案 | 选定锚点 |
| 2. 名称与查重 | 生成 3～5 个名称候选，逐项查 App Store / 域名 / 公开搜索 / 品牌冲突风险 | 选定名称 |
| 3. Slogan 与全案 | 主推 1 句 + 备选 2 句；按「人群 → 内核 → 视觉 → 语言 → 落地原则」推导 brand.md 草稿 | 选定 Slogan、提修改意见 |
| 4. 固化与交付 | 按意见修改，删除未选备选，检查推导链，写入定稿 | 确认交付 |

## 产出物

```text
docs/brand/
├── name-check.md   # 阶段 2：名称查重报告（含证据、风险等级与免责声明）
└── brand.md        # 阶段 4：唯一确定的品牌方案
```

## 边界

- 只读 `spec.md` 与项目已有文档，不修改 `spec.md`
- 不做视觉执行（logo、VI、物料、投放），只输出品牌方向与原则
- 查重无法联网时逐项标注「需人工核实」，不编造结果
- 查重结果不构成法律意见，正式注册前请咨询专业机构
- 产出物固定在 `docs/brand/` 下

## 发布与版本

### 打包

```bash
python scripts/package.py
```

产出：

```text
dist/brand-foundation-1.0.0.zip
dist/brand-foundation-1.0.0.zip.sha256
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
│   └── brand.md
├── scripts/
│   └── package.py
├── README.md
├── CHANGELOG.md
├── LICENSE
├── release/         # 已提交的发布归档，供 --from 下载
└── dist/            # 本地打包产物，不提交
```

## 卸载

```bash
specify extension remove brand
```

## 许可证

MIT
