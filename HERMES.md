# 在 Hermes Agent 中安装 Idesign

Idesign 兼容 [Hermes Agent](https://github.com/NousResearch/hermes-agent)，可通过以下两种方式安装。

---

## 方式一：自动安装脚本

### Linux / macOS

```bash
git clone https://github.com/kenszx/idesign.git /tmp/idesign
bash /tmp/idesign/install-hermes.sh
```

### Windows (PowerShell)

```powershell
git clone https://github.com/kenszx/idesign.git $env:TEMP\idesign
powershell -File $env:TEMP\idesign\install-hermes.ps1
```

---

## 方式二：手动安装

Hermes 技能按分类目录组织：`~/.hermes/skills/<分类>/<技能名>/`

```bash
# 1. 创建分类目录
mkdir -p ~/.hermes/skills/design

# 2. 安装 idesign 调度器
cp idesign.md ~/.hermes/skills/design/idesign/SKILL.md

# 3. 安装 5 个子技能
cp -r skills/web-design-engineer ~/.hermes/skills/design/web-design-engineer
cp -r skills/web-video-presentation ~/.hermes/skills/design/web-video-presentation
cp -r skills/gpt-image-2 ~/.hermes/skills/design/gpt-image-2
cp -r skills/beautiful-article ~/.hermes/skills/design/beautiful-article
cp -r skills/kb-retriever ~/.hermes/skills/design/kb-retriever

# 4. 安装共享资源
mkdir -p ~/.hermes/skills/design/idesign
cp -r shared ~/.hermes/skills/design/idesign/shared
cp -r scripts ~/.hermes/skills/design/idesign/scripts
cp -r showcases ~/.hermes/skills/design/idesign/showcases
cp -r demos ~/.hermes/skills/design/idesign/demos
```

---

## 安装后验证

```bash
# 检查技能是否在 Hermes 中可见
hermes skills list | grep -E "idesign|web-design|web-video|gpt-image|beautiful-article|kb-retriever"
```

---

## 在 Hermes 中使用

安装后，在 Hermes 对话中：

```
用 idesign 设计一个美妆品牌的客户提案 PPT
```

Hermes 会加载 idesign 调度器，按 Phase 0-4 交互式设计流程执行。

### Hermes 中的技能组织

| Hermes 路径 | 说明 |
|------|------|
| `~/.hermes/skills/design/idesign/SKILL.md` | 主调度器 |
| `~/.hermes/skills/design/web-design-engineer/SKILL.md` | Web UI / PPT / 原型 |
| `~/.hermes/skills/design/web-video-presentation/SKILL.md` | 16:9 演示 + 口播 |
| `~/.hermes/skills/design/gpt-image-2/SKILL.md` | 图像生成 |
| `~/.hermes/skills/design/beautiful-article/SKILL.md` | 文章排版 |
| `~/.hermes/skills/design/kb-retriever/SKILL.md` | 知识库检索 |
| `~/.hermes/skills/design/idesign/shared/` | 共享参考文档/资产 |
| `~/.hermes/skills/design/idesign/scripts/` | 工具脚本 |
| `~/.hermes/skills/design/idesign/showcases/` | 展示案例 |

---

## 更新技能

```bash
cd /tmp/idesign && git pull
bash install-hermes.sh   # 重新执行安装脚本覆盖更新
```
