from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://www.rottentomatoes.com/m/ne_zha_ii/reviews?type=user",# 以哪吒2为例，可自由更改
        wait_until="domcontentloaded"
    )
    for _ in range(5):  # 共爬取五页内容
        load_more = page.get_by_text("Load More")
        if load_more.is_visible():
            load_more.click()
            page.wait_for_timeout(2000)
        else:
            break

    reviews = page.locator("p.audience-reviews__review.js-review-text[data-qa='review-text']")
    count = reviews.count()

    for i in range(count):
        text = reviews.nth(i).inner_text().strip()
        print(f"{i+1}. {text}")

    print("评论总数：", count)
    browser.close() 



