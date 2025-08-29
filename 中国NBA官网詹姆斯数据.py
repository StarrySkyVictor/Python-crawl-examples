from playwright.sync_api import sync_playwright
import pandas as pd


def get_cell_text(page, row, col):
    """根据行号和列号提取单元格文本"""
    locator = f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{row}]/td[{col}]/span'
    return page.locator(locator).inner_text()


with sync_playwright() as p:
    all_games_data = []

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://china.nba.cn/player/2544/stats')

    page.get_by_role("button", name="赛季数据").click()
    page.get_by_role("combobox").select_option("2024_2")# 以24年常规赛为例
    page.wait_for_timeout(1000)

    rows = page.locator("table.left-table2 tr[data-v-756fc229]")
    count = rows.count()
    print("元素数量:", count)

    for i in range(1, count + 1):
        game_data = {
            '球队': get_cell_text(page, i, 1),
            '出场时间': get_cell_text(page, i, 2),
            '得分': get_cell_text(page, i, 3),
            '篮板': get_cell_text(page, i, 4),
            '助攻': get_cell_text(page, i, 5),
            '抢断': get_cell_text(page, i, 6),
            '盖帽': get_cell_text(page, i, 7),
            '投篮命中': get_cell_text(page, i, 8),
            '投篮出手': get_cell_text(page, i, 9),
            '三分命中率': get_cell_text(page, i, 13),
            '罚球命中率': get_cell_text(page, i, 14),
            '进攻篮板': get_cell_text(page, i, 15),
            '防守篮板': get_cell_text(page, i, 16),
            '失误': get_cell_text(page, i, 17),
            '犯规': get_cell_text(page, i, 18),
        }
        all_games_data.append(game_data)

    browser.close()

df = pd.DataFrame(all_games_data)
print(df)
# df.to_excel('詹姆斯.xlsx', index=False) 可选择是否保存为csv或excel
