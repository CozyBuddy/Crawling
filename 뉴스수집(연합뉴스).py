import asyncio
from playwright.async_api import async_playwright
from openpyxl import Workbook
import re
from datetime import datetime

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[
                "--disable-gpu",
                "--disable-blink-features=AutomationControlled",
                "--disable-extensions",
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ]
        )

        context = await browser.new_context(
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/119.0.6045.200 Safari/537.36"),
            permissions=[]
        )

        page = await context.new_page()
        num = 1

        await page.goto('https://www.yna.co.kr/sitemap/index')
        await page.wait_for_selector('div.link-field01 ul.link-zone01 a')
        href_list = await page.eval_on_selector_all(
                        'div.link-field01 ul.link-zone01 a',
                        'els => els.map(e => e.href)')

        for a_url in href_list:
            wb2 = Workbook()
            ws2 = wb2.active
            excelnum2 = 1

            await page.goto(a_url)
            await page.wait_for_timeout(1500)

            level2_links = await page.eval_on_selector_all(
                'div.link-zone02 a' ,
                'els => els.map(e => e.href)'
            )
            # level2 = await page.query_selector_all('div.link-zone02 a')
            # level2_links = [await el.get_attribute('href') for el in level2]

            for link2 in level2_links:
                await page.goto(link2)
                await page.wait_for_timeout(1500)
                # level3 = await page.query_selector_all('div.link-zone03 a')
                # level3_links = [await el.get_attribute('href') for el in level3]
                level3_links = await page.eval_on_selector_all('div.link-zone03 a' , 'els => els.map(item => item.href)')
                for link3 in level3_links:
                    try:
                        await page.goto(link3)
                        await page.wait_for_selector('div.story-news.article')
                        article = await page.inner_text('div.story-news.article')
                        splitresult = [s.strip() for s in article.split('.') if s.strip()]

                        for s in splitresult:
                               # if re.fullmatch(r"[가-힣.,!=?\"'()\ ]+", s):
                                ws2[f"A{excelnum2+1}"] = s
                                excelnum2 += 1
                    except Exception:
                        continue

            wb2.save(f'뉴스기사수집(연합뉴스){num}_{datetime.now().date()}.xlsx')
            num += 1

        await browser.close()

asyncio.run(main())
