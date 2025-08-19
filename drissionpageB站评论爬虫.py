from DrissionPage import ChromiumPage  #  pip install DrissionPage  
import time  
 
URL = input("请输入B站视频链接:")  
num = int(input("请输入要爬取的页面次数:"))
 
page = ChromiumPage()  
page.set.load_mode.none()  
 
# 监听特定的网络流  
page.listen.start('https://api.bilibili.com/x/v2/reply/wbi/main?')  
 
# 访问B站页面  
page.get(f'{URL}')  

time.sleep(5)
 
for _ in range(num+1):
    page.scroll.to_bottom()
    time.sleep(2)
 
 
# 用于存储所有捕获的响应数据  
responses = []  
 
try:  
    # 循环监听直到达到所需数量或超时  
    for _ in range(num):  
        # 等待网络请求包到达  
        packet = page.listen.wait()  
        
        # 停止加载页面（这步可以根据需求调整）  
        page.stop_loading()  
 
        # 接收 HTTP 响应内容  
        response_body = packet.response.body  
 
        # 将响应内容存储到列表中  
        responses.append(response_body)  
 
        time.sleep(1)  
 
except Exception as e:  
    print(f"解析出现错误: {e}")  
 
# 处理和打印捕获到的所有响应  
total_comments = 0  
 
for response in responses:  
    try:  
        if 'data' in response:  
            datas = response['data']['replies']  
            total_comments += len(datas)  
            for data in datas:   
                comments = data['content']['message']
                uname = data['member']['uname']  
                sex = data['member']['sex']  
                IP = data['reply_control']['location']  
                print(f"评论内容: {comments}\n用户名: {uname}\n性别: {sex}\nIP地址: {IP}\n")  
 
    except KeyError as e:  
        print(f"处理响应时出现错误: {e}")  
 
page.close()  
 
# 最后打印总评论数量  
print(f"总评论数量: {total_comments}")
 