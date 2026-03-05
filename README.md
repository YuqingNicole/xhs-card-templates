# 小红书精美图文模版

> 设计感强的小红书图文卡片生成工具，5种风格，4种卡片类型，一键渲染高清 PNG

## 风格预览

- 🌿 **暖奶油** (warm) — WARM SOFT BLUR，柔焦光晕，米白暖棕
- 🖤 **暗系高级** (dark) — 深墨绿底，金色文字，杂志质感
- ◼️ **极简包豪斯** (bw) — 纯白黑，线条构成，设计师风
- 🩶 **清冷蓝灰** (blue) — 雾霾蓝，冷淡文艺
- 🌸 **奶油粉嫩** (pink) — 草莓拿铁，少女感不俗气

## 快速开始

```bash
python3 scripts/render.py --style warm --output /tmp/output
```

## 文件结构

```
xhs-card-templates/
├── SKILL.md          # AI 调用指南
├── README.md         # 本文件
├── manifest.json
├── package.json
├── scripts/
│   └── render.py     # 渲染脚本
└── assets/
    └── templates/    # HTML 模版文件
        ├── warm/     # 完整4张套装
        ├── dark/
        ├── bw/
        ├── blue/
        └── pink/
```

Made with ❤️ by Nicole & 小天才
