import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser in headless mode
        browser = await p.chromium.launch()
        
        # Set viewport to 1080p
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        target_url = "https://dollarsbooked-ja4j8cf2scjgkkckuglpsz.streamlit.app/?embed=true"
        
        print(f"Navigating to {target_url}...")
        
        # --- FIXED INDENTATION BELOW ---
        await page.goto(target_url, wait_until="domcontentloaded", timeout=90000)
        await page.wait_for_timeout(10000)
        # -------------------------------
        
        print("Waiting 10 seconds for data to load...")
        await asyncio.sleep(10)
        
        # Take the shot
        await page.screenshot(path='dashboard.png', full_page=False)
        print("Screenshot saved as dashboard.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
