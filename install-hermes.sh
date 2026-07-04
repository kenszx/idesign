#!/bin/bash
# Idesign → Hermes Agent 安装脚本
# 将 idesign 技能套件安装到 ~/.hermes/skills/design/

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HERMES_SKILLS="$HOME/.hermes/skills/design"

echo "=== Idesign → Hermes 安装 ==="
echo "目标: $HERMES_SKILLS"
echo ""

# 创建分类目录
mkdir -p "$HERMES_SKILLS"

# 安装 idesign 调度器
echo "[1/6] 安装 idesign 调度器..."
mkdir -p "$HERMES_SKILLS/idesign"
cp "$SCRIPT_DIR/idesign.md" "$HERMES_SKILLS/idesign/SKILL.md"

# 安装 5 个子技能
echo "[2/6] 安装子技能..."
for skill in web-design-engineer web-video-presentation gpt-image-2 beautiful-article kb-retriever; do
  if [ -d "$SCRIPT_DIR/skills/$skill" ]; then
    rm -rf "$HERMES_SKILLS/$skill"
    cp -r "$SCRIPT_DIR/skills/$skill" "$HERMES_SKILLS/$skill"
    echo "  ✓ $skill"
  else
    echo "  ✗ $skill (未找到)"
  fi
done

# 安装共享资源
echo "[3/6] 安装共享资源..."
rm -rf "$HERMES_SKILLS/idesign/shared"
cp -r "$SCRIPT_DIR/shared" "$HERMES_SKILLS/idesign/shared"
echo "  ✓ shared/ (参考文档 + 资产 + SFX + BGM)"

# 安装脚本工具
echo "[4/6] 安装脚本工具..."
rm -rf "$HERMES_SKILLS/idesign/scripts"
cp -r "$SCRIPT_DIR/scripts" "$HERMES_SKILLS/idesign/scripts"
echo "  ✓ scripts/ (15 个工具)"

# 安装展示案例
echo "[5/6] 安装展示案例..."
rm -rf "$HERMES_SKILLS/idesign/showcases"
cp -r "$SCRIPT_DIR/showcases" "$HERMES_SKILLS/idesign/showcases"
echo "  ✓ showcases/ (24 个案例)"

# 安装 Demo
echo "[6/6] 安装 Demo..."
if [ -d "$SCRIPT_DIR/demos" ]; then
  rm -rf "$HERMES_SKILLS/idesign/demos"
  cp -r "$SCRIPT_DIR/demos" "$HERMES_SKILLS/idesign/demos"
  echo "  ✓ demos/ (21 个示例)"
fi

echo ""
echo "=== 安装完成 ==="
echo ""
echo "安装位置: $HERMES_SKILLS"
echo ""
echo "在 Hermes 中使用:"
echo "  hermes skills list | grep design"
echo ""
echo "对话示例:"
echo "  \"用 idesign 设计一个 SaaS 产品官网首页\""
