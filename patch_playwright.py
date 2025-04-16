# patch_playwright.py

from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy
from crawl4ai.browser_manager import BrowserManager

async def patched_close(self) -> None:
    # Fecha o browser/context e reseta o singleton
    await self.browser_manager.close()
    BrowserManager._playwright_instance = None

AsyncPlaywrightCrawlerStrategy.close = patched_close

print("✅ Playwright monkey‑patch aplicado")
