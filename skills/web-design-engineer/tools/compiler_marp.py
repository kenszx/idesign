"""
Marp CLI Compiler — Markdown → PPTX / PDF
封装 Marp CLI 调用，将 Executor 产出的 Markdown 编译为标准 PPTX 或 PDF。
"""

import subprocess
import os
import shutil
from pathlib import Path
from typing import Optional


class MarpCompiler:
    """将 Marp Markdown 编译为 PPTX 或 PDF"""

    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
        self.marp_cmd = self.config.get("marp_cli", "npx @marp-team/marp-cli")
        self.workspace = Path(self.config.get("workspace", "./workspace"))

    def _find_marp(self) -> str:
        """查找 Marp CLI 可执行路径"""
        # 优先用 npx
        if shutil.which("npx"):
            return "npx @marp-team/marp-cli"
        # 其次找全局安装
        if shutil.which("marp"):
            return "marp"
        raise RuntimeError(
            "Marp CLI not found. Install with: npm install -g @marp-team/marp-cli"
        )

    def to_pptx(
        self,
        input_md: str,
        output_pptx: str,
        theme_css: Optional[str] = None,
        allow_local_files: bool = True,
    ) -> str:
        """
        将 Marp Markdown 编译为 PPTX

        Args:
            input_md: 输入 .md 文件路径
            output_pptx: 输出 .pptx 文件路径
            theme_css: 自定义 CSS 主题文件路径（可选）
            allow_local_files: 是否允许本地文件（True 用于本地图片）

        Returns:
            输出文件路径
        """
        input_path = Path(input_md)
        output_path = Path(output_pptx)

        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_md}")

        cmd = [*self.marp_cmd.split(), str(input_path), "--pptx", "-o", str(output_path)]

        if theme_css and Path(theme_css).exists():
            cmd.extend(["--theme", theme_css])
        if allow_local_files:
            cmd.append("--allow-local-files")

        print(f"[Compiler] Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode != 0:
            raise RuntimeError(f"Marp compilation failed:\n{result.stderr}")

        print(f"[Compiler] PPTX generated: {output_path} ({output_path.stat().st_size} bytes)")
        return str(output_path)

    def to_pdf(
        self,
        input_md: str,
        output_pdf: str,
        theme_css: Optional[str] = None,
    ) -> str:
        """将 Marp Markdown 编译为 PDF"""
        input_path = Path(input_md)
        output_path = Path(output_pdf)

        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_md}")

        cmd = [*self.marp_cmd.split(), str(input_path), "--pdf", "-o", str(output_path)]

        if theme_css and Path(theme_css).exists():
            cmd.extend(["--theme", theme_css])
        cmd.append("--allow-local-files")

        print(f"[Compiler] Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode != 0:
            raise RuntimeError(f"Marp PDF compilation failed:\n{result.stderr}")

        print(f"[Compiler] PDF generated: {output_path} ({output_path.stat().st_size} bytes)")
        return str(output_path)

    def validate_markdown(self, md_path: str) -> dict:
        """验证 Markdown 是否包含有效的 Marp 结构"""
        content = Path(md_path).read_text(encoding="utf-8")
        issues = []

        if "---" not in content:
            issues.append("No Marp frontmatter found (missing --- separator)")
        if content.count("---") < 2:
            issues.append("Less than 2 slides (need at least 2 --- separators)")
        if "marp: true" not in content[:500]:
            issues.append("Missing 'marp: true' in frontmatter")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
            "slide_count": content.count("---") - 1,  # frontmatter不算页
        }


if __name__ == "__main__":
    # 快速测试
    compiler = MarpCompiler()
    validation = compiler.validate_markdown("workspace/output.md")
    print(f"Validation: {validation}")
