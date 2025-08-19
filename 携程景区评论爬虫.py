from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://you.ctrip.com/sight/feixi2619/20464.html") # 爬取的页面地址

    for j in range(4): # 爬取4页
        comments = page.locator('div.commentDetail')
        count = comments.count()

        for i in range(count):
            text = comments.nth(i).inner_text().strip()
            print(f"{20 * j + i + 1}.{text}\n")

        page.get_by_text("下一页").click()
        page.wait_for_selector("div.commentDetail")

    browser.close()