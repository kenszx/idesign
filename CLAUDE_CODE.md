# 在 Claude Code 中安装 Idesign

Idesign 专为 Claude Code 设计，安装后全局可用。

---

## 方式一：自动安装（推荐）

```bash
git clone https://github.com/kenszx/idesign.git /tmp/idesign
cp -r /tmp/idesign/* ~/.claude/skills/
cp /tmp/idesign/idesign.md ~/.claude/skills/
rm -rf /tmp/idesign
```

### Windows (PowerShell)

```powershell
git clone https://github.com/kenszx/idesign.git $env:TEMP\idesign
Copy-Item -Recurse -Force "$env:TEMP\idesign\*" "$env:USERPROFILE\.claude\skills\"
Remove-Item -Recurse -Force "$env:TEMP\idesign"
```

---

## 方式二：手动安装

```bash
# 1. 创建技能目录
mkdir -p ~/.claude/skills

# 2. 下载并复制
git clone https://github.com/kenszx/idesign.git
cp -r idesign/* ~/.claude/skills/

# 3. 清理
rm -rf idesign
```

---

## 目录结构

安装后的 `~/.claude/skills/` 目录：

```
~/.claude/skills/
├── idesign.md                    # 主调度器（入口）
├── idesign_SKILL.md              # 调度器副本
├── HERMES.md                     # Hermes 安装指引
├── install-hermes.sh             # Hermes Linux/macOS 安装脚本
├── install-hermes.ps1            # Hermes Windows 安装脚本
├── skills/
│   ├── web-design-engineer/      # Web UI / PPT / 原型 / 动画
│   ├── web-video-presentation/   # 16:9 演示 + 口播
│   ├── gpt-image-2/              # 图像生成 / 编辑
│   ├── beautiful-article/        # 网页文章排版
│   └── kb-retriever/             # 知识库检索
├── shared/
│   ├── anti-slop-rules.md        # 反 AI 味道规则
│   ├── references/               # 30 篇参考文档
│   └── assets/                   # 37 SFX + 6 BGM + 设备框架
├── scripts/                      # 15 个工具脚本
├── showcases/                    # 24 个展示案例
└── demos-huashu/                 # 21 个交互 demo
```

---

## 安装后验证

在 Claude Code 对话中输入：

```
加载 idesign
```

如果调度器正确加载，会进入 Phase 0 需求澄清流程。

---

## 使用流程

| 阶段 | 做什么 |
|------|------|
| Phase 0 | 说"加载 idesign"，回答 1 个需求问题 |
| Phase 1 | 从 2-3 个风格方向中选择 |
| Phase 2 | 查看骨架布局，确认后进入构建 |
| Phase 3 | 逐模块构建，每步确认 |
| Phase 4 | 最终精调 + 导出入库 |

---

## 更新技能

```bash
cd /tmp && git clone https://github.com/kenszx/idesign.git
cp -r idesign/* ~/.claude/skills/
rm -rf idesign
```

---

## 可用子技能

| 技能 | Claude Code Skill 工具名 | 用途 |
|------|------|------|
| Web Design Engineer | `web-design-engineer` | Web UI / PPT / 原型 / 仪表盘 / 动画 / 数据可视化 |
| Web Video Presentation | `web-video-presentation` | 16:9 点击驱动演示 + TTS 口播合成 |
| GPT Image 2 | `gpt-image-2` | 图像生成 / 编辑，18 大类 93 模板 |
| Beautiful Article | `beautiful-article` | URL/PDF/DOCX → 单文件 HTML 网页文章 |
| KB Retriever | `kb-retriever` | 本地知识库 PDF/Excel 渐进式检索 |

在 Claude Code 中可直接用 Skill 工具调用这些子技能名称。
