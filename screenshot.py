import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser in headless mode (no window)
        browser = await p.chromium.launch()
        # Set viewport to exactly 1080p to fix the Insignia scaling
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Replace the URL below with your actual Streamlit App URL
        # Adding ?embed=true helps remove the Streamlit sidebar
        target_url = "https://dollarsbooked-ja4j8cf2scjgkkckuglpsz.streamlit.app/?embed=true"
        
        print(f"Navigating to {target_url}...")
        await page.goto(target_url, wait_until="networkidle")
        
        # IMPORTANT: Streamlit takes time to fetch data from your .ttx file.
        # We wait 10 seconds to ensure the charts/tables are fully rendered.
        print("Waiting 10 seconds for data to load...")
        await asyncio.sleep(10)
        
        # Take the shot. 'full_page=False' ensures we only get the 1080p area.
        await page.screenshot(path='dashboard.png', full_page=False)
        print("Screenshot saved as dashboard.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
