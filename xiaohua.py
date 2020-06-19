import requests
from bs4 import BeautifulSoup
#import 和form xx import xx 都表示的导入相关的模块，让Python使用相关功能，这段代码不能少
#需要先分别安装requests、bs4库才可以运行
#打开cmd输入：pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple  回车
#打开cmd输入pip install bs4 lxml -i https://pypi.tuna.tsinghua.edu.cn/simple  回车
#如果你是mac系统就打开终端，将pip改成pip3，其他不变同样输入代码回车分别安装。

#爬取笑话内容

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
#访问网页#

for i in range(5):
	html = requests.get('http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i+1),headers = headers)
	soup = BeautifulSoup(html.text,'lxml')
	print(soup.text)
	for joke in soup.select('li.article-summary'):
		title = joke.select('.article-title')[0].text
		content = joke.select('.summary-text')[0].text
		print(title)
		print('---------------------------------------------------')
		print(content)