"""
 爬取csdn 文章标题、链接
 https://www.cnblogs.com/rossiXYZ
 
 //div[@class="postTitle"]/a
 
"""

import requests
from bs4 import BeautifulSoup

def crawl_cnblogs_pages(start_page, end_page, save_file):
    nums = 0 
    with open(save_file, 'w', encoding='utf-8') as f_:
        for page_num in range(start_page, end_page + 1):
            url = f"https://www.cnblogs.com/rossiXYZ?page={page_num}"
            response = requests.get(url)

            if response.status_code == 200:
                # 使用BeautifulSoup解析页面内容
                soup = BeautifulSoup(response.text, 'html.parser')
                # print(f'soup: {soup}')
                # 这里可以根据页面结构提取你需要的信息
                # 比如找到文章的标题、链接等等
                articles = soup.find_all('div', class_='postTitle')
                # print(f'articles: {articles}  ?????')
                for article in articles:
                    print(f'='*20)
                    # print(f'article : {article}, {type(article)}')
                    a_tag = article.find('a', class_='postTitle2')
                    if a_tag:
                        nums +=1 
                        link = a_tag['href']
                        title = a_tag.text.strip().replace('\n','')
                        print(f"p{nums}---{title},  {link}")

                        # 写入标题和链接到文件中
                        f_.write(f"p{nums}---{title},  {link}\n")

            else:
                print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")

if __name__ == "__main__":
    start_page = 1
    end_page = 31 # 31
    
    save_file = './tmp/tmp.json'
    
    crawl_cnblogs_pages(start_page, end_page, save_file)
