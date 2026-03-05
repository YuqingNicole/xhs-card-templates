# 小红书精美图文模版 Skill

## 这是什么

帮你生成设计感强的小红书图文卡片（PNG 高清图），5 种风格可选，支持封面 + 要点清单 + 段落正文 + 金句结语 4 种卡片类型。

## 风格一览

| 代号 | 风格名 | 色调 | 适合内容 |
|------|--------|------|---------|
| `warm` | 暖奶油 WARM SOFT BLUR | 米白/暖棕/柔焦光晕 | 生活分享、日常干货 |
| `dark` | 暗系高级感 | 深墨绿/金色 | 深度内容、品牌感强的账号 |
| `bw` | 极简包豪斯 | 纯白/黑 | 设计、学习、知识型内容 |
| `blue` | 清冷蓝灰 | 雾霾蓝/灰白 | 文艺、思考型内容 |
| `pink` | 奶油粉嫩 | 草莓拿铁/粉橙 | 生活方式、种草类内容 |

## 卡片类型（warm 风格完整套装）

- **cover** — 封面：大标题 + 副标题
- **card_list** — 要点清单：编号列表，适合"X个方法/工具"类内容
- **card_text** — 段落正文：分节正文，适合对比/详解类内容
- **card_quote** — 金句结语：大引言 + 呼吁互动

## 使用方式

### 当用户说"帮我出一篇小红书"时

1. 询问主题（如果没有，自己选一个合适的）
2. 询问风格偏好（展示5种选项），或直接推荐 `warm`
3. 撰写文案（标题、副标题、正文要点、金句）
4. 用 render.py 渲染成图片
5. 通过 message 工具发送给用户

### 渲染命令

```bash
# 渲染某一风格所有卡片
python3 /root/.openclaw/skills/xhs-card-templates/scripts/render.py \
  --style warm \
  --output /tmp/xhs_output

# 渲染所有风格的封面（预览用）
python3 /root/.openclaw/skills/xhs-card-templates/scripts/render.py \
  --style all \
  --output /tmp/xhs_preview

# 直接渲染指定 HTML 文件
python3 /root/.openclaw/skills/xhs-card-templates/scripts/render.py \
  --html /path/to/custom.html \
  --output /tmp/output.png
```

### 填充内容的标准流程

1. 复制对应风格的 HTML 模版到 `/tmp/xhs_work/`
2. 用 Python/sed 替换占位文字（标题、副标题、正文等）
3. 调用 render.py 渲染
4. 用 message 工具发图给用户

### 快速替换占位符（Python 示例）

```python
import re

def fill_template(html_path: str, replacements: dict, output_path: str):
    with open(html_path, 'r') as f:
        content = f.read()
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    with open(output_path, 'w') as f:
        f.write(content)
```

## 模版文件位置

```
/root/.openclaw/skills/xhs-card-templates/assets/templates/
├── warm/
│   ├── cover.html       # 封面
│   ├── card_list.html   # 要点清单
│   ├── card_text.html   # 段落正文
│   └── card_quote.html  # 金句结语
├── dark/
│   └── cover.html
├── bw/
│   └── cover.html
├── blue/
│   └── cover.html
└── pink/
    └── cover.html
```

## 占位符说明（warm/cover 封面）

| 占位符 | 说明 |
|--------|------|
| `效率干货` | 顶部标签 |
| `标题放<br>这里` | 主标题（可换行） |
| `副标题 · 一句话说清楚这篇讲什么` | 副标题 |
| `@你的账号` | 作者名 |

## 注意事项

- 图片尺寸固定 1080×1440px（小红书标准竖版）
- 字体依赖 Google Fonts（Noto Serif SC + Noto Sans SC），需要网络
- 离线时可替换为本地字体路径
- 渲染依赖 playwright + chromium（已安装）

## 扩展建议

- 给 dark/bw/blue/pink 各补充完整 4 张卡片
- 增加"横版"模版（1080×1080）用于封面
- 增加自动发布到小红书功能（配合 Auto-Redbook-Skills）
