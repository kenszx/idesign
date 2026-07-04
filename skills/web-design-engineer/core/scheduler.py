"""
Pipeline Scheduler — idesign v2 编译管道主调度器
协调 Planner → Executor → Critic → Compiler 流程。
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional


class PipelineScheduler:
    """idesign v2 Pipeline — 主调度器"""

    def __init__(self, config_path: str = "config.yaml"):
        import yaml
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        self.workspace = Path(self.config["paths"]["workspace"])
        self.max_retries = self.config["pipeline"]["max_retries"]
        self.themes_dir = Path(self.config["paths"]["themes"])

    # ── Logging ──

    def log(self, stage: str, message: str):
        """追加写入迭代日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        log_file = self.workspace / "iteration_log.md"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{stage}] - {message}\n")
        print(f"[{stage}] {message}")

    # ── Pipeline Steps ──

    def load_design_json(self) -> dict:
        """从 workspace 加载 Planner 产出的设计蓝图"""
        schema_path = self.workspace / "current_design.json"
        if not schema_path.exists():
            raise FileNotFoundError(f"Design blueprint not found: {schema_path}")
        return json.loads(schema_path.read_text(encoding="utf-8"))

    def load_theme_tokens(self, style: str) -> Optional[str]:
        """根据风格名加载对应的 tokens.css"""
        # 1. 先查 style-recipes tokens
        recipe_path = Path(
            f"../web-design-engineer/references/style-recipes/tokens/{style}.css"
        )
        if recipe_path.exists():
            return recipe_path.read_text(encoding="utf-8")

        # 2. 再查 video themes tokens
        theme_path = self.themes_dir / f"{style}.css"
        if theme_path.exists():
            return theme_path.read_text(encoding="utf-8")

        # 3. 查找 video themes 目录下的 tokens.css
        for theme_dir in self.themes_dir.glob("*/"):
            tokens_file = theme_dir / "tokens.css"
            if tokens_file.exists() and style.lower() in theme_dir.name.lower():
                return tokens_file.read_text(encoding="utf-8")

        print(f"[Scheduler] Warning: No tokens.css found for style '{style}'")
        return None

    def generate_marp_theme(self, tokens_css: str) -> str:
        """将 tokens.css 转换为 Marp 可用的 CSS 主题"""
        # Marp 需要 section {} 包裹样式，直接注入 tokens 变量
        return f"""/* @theme idesign */
{tokens_css}
section {{
  background: var(--surface, #ffffff);
  color: var(--text, #1a1a1a);
  font-family: var(--font-body);
  padding: var(--stage-pad-y, 60px) var(--stage-pad-x, 80px);
}}
h1 {{ color: var(--accent, #000); font-family: var(--font-display-en, sans-serif); }}
h2 {{ font-family: var(--font-display-en, sans-serif); }}
h3 {{ color: var(--text-2); }}
"""

    def run(
        self,
        style: str = "linear",
        target_format: str = "pptx",
    ) -> str:
        """
        运行完整 Pipeline

        Args:
            style: 风格名称（匹配 tokens.css）
            target_format: 输出格式 (pptx / pdf / both)

        Returns:
            最终交付物路径
        """
        self.log("PIPELINE", f"启动 - 风格: {style}, 格式: {target_format}")

        # 1. 加载设计蓝图
        schema = self.load_design_json()
        self.log("SCHEDULER", f"加载蓝图: {schema['meta']['total_slides']} 页")

        # 2. 加载主题 tokens
        tokens = self.load_theme_tokens(style)
        if tokens:
            self.log("SCHEDULER", f"加载主题: {style}")
        else:
            self.log("SCHEDULER", f"主题 {style} 未找到，使用默认")

        # 3. 生成 Marp 主题 CSS
        marp_theme = self.generate_marp_theme(tokens or "")
        theme_path = self.workspace / "current_theme.css"
        theme_path.write_text(marp_theme, encoding="utf-8")
        self.log("SCHEDULER", "Marp 主题已生成")

        # 4. Executor 输出文件应在 workspace/output.md
        # 5. Critic 审查结果应在 workspace/review_result.json
        # 6. Compiler 编译
        output = self.compile(target_format)
        self.log("PIPELINE", f"完成 - {output}")
        return output

    def compile(self, target_format: str) -> str:
        """编译最终输出"""
        md_path = self.workspace / "output.md"
        theme_path = self.workspace / "current_theme.css"

        if target_format in ("pptx", "both"):
            from tools.compiler_marp import MarpCompiler
            compiler = MarpCompiler({
                "workspace": str(self.workspace),
                "marp_cli": self.config["tools"]["marp_cli"],
            })
            output = compiler.to_pptx(
                str(md_path),
                str(self.workspace / "final_output.pptx"),
                str(theme_path) if theme_path.exists() else None,
            )
            return output

        if target_format in ("pdf",):
            from tools.renderer_playwright import PlaywrightRenderer
            renderer = PlaywrightRenderer({
                "workspace": str(self.workspace),
                "slide_width": self.config["defaults"]["slide_width"],
                "slide_height": self.config["defaults"]["slide_height"],
            })
            html_path = self.workspace / "output.html"
            return renderer.to_pdf(str(html_path), str(self.workspace / "final_output.pdf"))

        raise ValueError(f"Unknown format: {target_format}")


if __name__ == "__main__":
    scheduler = PipelineScheduler("config.yaml")
    scheduler.run(style="linear", target_format="pptx")
