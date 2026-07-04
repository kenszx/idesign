"""
Playwright Renderer — HTML → Screenshot / PDF
用于 Critic 视觉审查和最终 PDF 导出。
"""

import asyncio
import base64
from pathlib import Path
from typing import Optional


class PlaywrightRenderer:
    """无头浏览器渲染：截图 + PDF 导出"""

    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
        self.browser_type = self.config.get("playwright_browser", "chromium")
        self.viewport = {
            "width": self.config.get("slide_width", 1280),
            "height": self.config.get("slide_height", 720),
        }
        self.workspace = Path(self.config.get("workspace", "./workspace"))

    async def _get_page(self, html_path: str):
        """获取渲染后的 Playwright page 对象"""
        from playwright.async_api import async_playwright

        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(viewport=self.viewport)

        # 用 data URI 加载 HTML（避免本地文件 CORS 问题）
        html_content = Path(html_path).read_text(encoding="utf-8")
        data_uri = "data:text/html;charset=utf-8," + self._encode_uri(html_content)
        await page.goto(data_uri, wait_until="networkidle")

        # 等待字体和图片加载
        await page.wait_for_timeout(1000)

        return page, browser, playwright

    def _encode_uri(self, html: str) -> str:
        """将 HTML 编码为 data URI"""
        import urllib.parse
        return urllib.parse.quote(html, safe="")

    def screenshot(
        self,
        html_path: str,
        output_png: str,
        full_page: bool = False,
    ) -> str:
        """对 HTML 页面截图（同步封装）"""
        return asyncio.run(self._screenshot_async(html_path, output_png, full_page))

    async def _screenshot_async(
        self,
        html_path: str,
        output_png: str,
        full_page: bool = False,
    ) -> str:
        page, browser, playwright = await self._get_page(html_path)

        output_path = Path(output_png)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        await page.screenshot(
            path=str(output_path),
            full_page=full_page,
            type="png",
        )

        await browser.close()
        await playwright.stop()

        print(f"[Renderer] Screenshot saved: {output_path} ({output_path.stat().st_size} bytes)")
        return str(output_path)

    def to_pdf(
        self,
        html_path: str,
        output_pdf: str,
        print_background: bool = True,
    ) -> str:
        """将 HTML 导出为高清 PDF（同步封装）"""
        return asyncio.run(self._to_pdf_async(html_path, output_pdf, print_background))

    async def _to_pdf_async(
        self,
        html_path: str,
        output_pdf: str,
        print_background: bool = True,
    ) -> str:
        page, browser, playwright = await self._get_page(html_path)

        output_path = Path(output_pdf)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        await page.pdf(
            path=str(output_path),
            print_background=print_background,
            width=f"{self.viewport['width']}px",
            height=f"{self.viewport['height']}px",
            prefer_css_page_size=False,
        )

        await browser.close()
        await playwright.stop()

        print(f"[Renderer] PDF generated: {output_path} ({output_path.stat().st_size} bytes)")
        return str(output_path)


if __name__ == "__main__":
    # 快速测试
    renderer = PlaywrightRenderer()
    renderer.screenshot("workspace/output.html", "workspace/screenshot.png")
