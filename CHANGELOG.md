# Changelog

## 2.0.0 - 2026-11-26

破坏性重构，从单一品牌地基命令升级为完整品牌工作流。

- 新增 `/speckit-brand-run` 默认全流程入口，以及 `create`、`name-check`、`clarify`、`prototype`、`prototype-clarify` 五个可独立调用的子命令。
- `brand.md` 结构重组：项目背景、人群画像、定位与锚点、命名（含查重结果）、Slogan 与内核、视觉方向、语言方向、执行原则、决策记录。
- 名称查重改为独立命令，结果写入 `brand.md`；不再产出 `name-check.md`。
- 新增品牌方向澄清命令，参考 `/speckit-clarify`，每轮最多 5 个问题，答案写回 `brand.md`。
- 新增原型命令：先由 `brand.md` 推出视觉板 A，再按 A 设计界面 B，合成一个页面，一次性人工检查，改 B 的同时改 A。
- 新增初版 logo/VI：字标、图形标、变体、App 图标、安全空间与禁用示例、2～3 个应用示例；全部为可编辑 SVG。
- 原型行为与状态澄清并入本扩展，改名 `/speckit-brand-prototype-clarify`，直接修改原型。
- `plan.md` 交给原生 `/speckit-plan`，扩展不再产出。
- 移除 `speckit.brand.foundation` 命令。

## 1.1.0 - 2026-11-25

- 命令提示词改为英文，并支持语言自适应：所有交互与产出文档跟随 `spec.md` 的语言，可在调用时显式指定。
- 扩展与命令描述改为中英双语，便于英文用户发现。
- 发布包包含 `README.en.md`；安装地址更新为 GitHub 主仓库。

## 1.0.0 - 2026-11-25

- 初始版本：四阶段品牌策划工作流（定位与锚点、名称与查重、Slogan 与全案、固化与交付）。
- 产出 `docs/brand/brand.md` 与 `docs/brand/name-check.md`。
- 支持自建/URL 分发，提供 `scripts/package.py` 打包脚本。
