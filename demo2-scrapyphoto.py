'''
@Function: 爬取壁纸社https://www.toopic.cn/ 精选壁纸
@Author: lxy&&zc
@date:2024/11/17
'''
import requests
from lxml import html
import os
for index in range(1,301): # 遍历每一页
    url = f"https://www.toopic.cn/dnbz/?q=-----.html&px=hot&page={index}"
    response = requests.get(url).text
    # print(response)
    # 解析 HTML 内容
    tree = html.fromstring(response)
    # 使用XPath提取所有class为"lazy"的img标签的src属性
    img_sources = tree.xpath('//img[@class="lazy"]/@data-original')
    # 输出结果
    # print(img_sources)
    '''
    每张图片的url只是一部分，需要为每个url添加前面共有的地址https://www.toopic.cn/
    '''
    urls = [] # 创建一个列表存储真正的url
    for item in img_sources:
        urls.append(f"https://www.toopic.cn/{item}")
    # print(urls)

    # 也可以写成下面这种方式
    '''
        for i in range(len(img_sources)):
        img_sources[i]= "https://www.toopic.cn/" + img_sources[i]
    print(img_sources)
    '''
    '''
    二保存二进制数据--将其存到一个文件夹中-（模板）
    '''
    # 创建一个文件夹（如果不存在）
    folder_path = "壁纸"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 下载每个 URL 并保存为二进制文件
    for i, img_url in enumerate(urls):
        try:
            # 发送 GET 请求获取图片
            img_response = requests.get(img_url)

            # 检查图片是否成功下载
            if img_response.status_code == 200:
                # 获取图片内容
                img_data = img_response.content

                # 保存图片为二进制文件到文件夹中
                img_filename = os.path.join(folder_path, f"page_{index}image_{i + 1}.jpg")
                with open(img_filename, 'wb') as f:
                    f.write(img_data)
                print(f"成功保存 {img_filename}")
            else:
                print(f"无法下载 {img_url}")
        except Exception as e:
            print(f"下载错误 {img_url}: {e}")
'''
summary:
    1、学到了爬取网页图片等二进制文件---将数据保存到文件夹中以二进制方式打开
    2、在张小晨的帮助下，学会了用lxml库提取class标签属性的数据，学会了在最外层添加page循环，修改外层Url,来爬取每一页的数据以及如何添加共有链接头部
    3、多动手 少chat
'''