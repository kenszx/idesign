# Idesign

面向 AI 编程代理的统一设计技能集合。通过自然语言对话即可构建交互原型、演示文稿、动画、品牌系统、图片生成等。

**兼容**: Claude Code · Hermes Agent · Cursor · Codex

---

## 技能列表

| 技能 | 说明 | 加载路径 |
|---|---|---|
| **web-design-engineer** | 网页/落地页/UI 原型设计 | `skills/web-design-engineer/SKILL.md` |
| **web-video-presentation** | 脚本 → 交互式 16:9 视频演示 | `skills/web-video-presentation/SKILL.md` |
| **gpt-image-2** | 图片生成（79 个提示词模板） | `skills/gpt-image-2/SKILL.md` |
| **beautiful-article** | URL/PDF/DOCX → 精美文章 | `skills/beautiful-article/SKILL.md` |
| **kb-retriever** | 本地知识库检索 | `skills/kb-retriever/SKILL.md` |
| **design-prototyping** | iOS/Android/桌面交互原型 | `skills/design-prototyping/SKILL.md` |
| **design-slides** | 幻灯片 → PPTX/PDF 导出 | `skills/design-slides/SKILL.md` |
| **design-animation** | 动效设计 → MP4/GIF 导出 | `skills/design-animation/SKILL.md` |
| **design-critique** | 5 维专家设计评审 | `skills/design-critique/SKILL.md` |
| **design-direction-advisor** | 需求模糊时的风格探索 | `skills/design-direction-advisor/SKILL.md` |
| **design-brand-system** | 品牌资产提取与应用 | `skills/design-brand-system/SKILL.md` |

## 安装

```bash
# npx skills（通用）
npx skills add kenszx/idesign

# 或直接克隆
git clone https://github.com/kenszx/idesign.git
```

## 使用方式

主调度器会自动将你的需求路由到对应的子技能。每个技能都采用**交互式工作流**：

1. **方向选择** — AI 出 2-3 个方向，你选
2. **骨架预览** — 看结构草稿，确认后开始
3. **逐步构建** — 每完成一个模块等你确认
4. **精调导出** — 最后润色，交付

> **核心理念**: 用户参与全流程，不是 AI 全自动生成后一次性验收。
