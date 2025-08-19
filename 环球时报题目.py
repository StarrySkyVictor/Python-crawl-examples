from DrissionPage import ChromiumPage  
import time  

page = ChromiumPage()  
page.listen.start('https://api.bilibili.com/x/space/wbi/arc/search?')  
 
page.get('https://space.bilibili.com/10303206/upload/video')   

time.sleep(1) 

 
responses = []  
for _ in range(10): 
    packet = page.listen.wait()  
    page.stop_loading()  
    response_body = packet.response.body  
    responses.append(response_body)
    page.ele('@text()=下一页').click()  
    time.sleep(1)

time.sleep(0.5)
# 处理和打印捕获到的所有响应  
total_comments = 0  
titles = []
for response in responses:  
    try:    
            datas = response['data']['list']['vlist']
            total_comments += len(datas)  
            for data in datas:   
                print(data['title'])  
                print()
                titles.append(data['title'])
    except KeyError as e:  
        print(f"处理响应时出现错误: {e}")  
    print(f"共捕获到 {total_comments} 条标题")
page.close()  # 关闭浏览器



