import asyncio
import time  # 导入 time 模块
from playwright.async_api import async_playwright
import pandas as pd

async def run():
    all_games_data = []

    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 访问网页
        await page.goto("https://china.nba.cn/player/2544/stats?tab=2")

        # 等待表格加载完成
        await page.wait_for_selector('table')

        # 获取表格中的数据
        for i in range(1, 26):
            try:
                game_data = {} 
                # 提取比赛信息//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[1]/td[1]/span
                game_data['姓名'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[1]/span').inner_text()
                game_data['出场时间'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[2]/span').inner_text()
                game_data['得分'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[3]/span').inner_text()
                game_data['篮板'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[4]/span').inner_text()
                game_data['助攻'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[5]/span').inner_text()
                game_data['抢断'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[6]/span').inner_text()
                game_data['盖帽'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[7]/span').inner_text()
                game_data['投篮命中'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[8]/span').inner_text()
                game_data['投篮出手'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[9]/span').inner_text()
                game_data['三分命中率'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[13]/span').inner_text()
                game_data['罚球命中率'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[14]/span').inner_text()
                game_data['进攻篮板'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[15]/span').inner_text()
                game_data['防守篮板'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[16]/span').inner_text()
                game_data['失误'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[17]/span').inner_text()
                game_data['犯规'] = await page.locator(f'//*[@id="app"]/div[2]/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/table/tr[{i}]/td[18]/span').inner_text()

                all_games_data.append(game_data)

            except Exception as e:
                print(f"Error retrieving data for row {i}: {e}")
                break  # 可以选择在出现错误时跳过当前数据行

    for game in all_games_data:
        print(game)
    print('保存完成！')

    # 关闭浏览器
    await browser.close()

# 记录开始时间
start_time = time.time()

# 运行异步任务
asyncio.run(run())

# 记录结束时间
end_time = time.time()

# 计算并打印运行时间
execution_time = end_time - start_time
print(f"运行时间: {execution_time:.2f} 秒")

