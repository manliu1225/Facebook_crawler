import re
import os
f = "./straitstime.log"
F_PATTERN = r'Scraping facebook page https://mbasic.facebook.com/'
POST_P = r'parse_post is '
n = 0
with open(f) as inputf:
	for line in inputf:
		line = line.strip()
		if re.search(F_PATTERN, line):
			file_name = re.search(r"https://mbasic\.facebook\.com/.*?$", line).group().lstrip("https://mbasic\.facebook\.com/")
			# print(file_name)
			n = 0
			output = os.path.join("comments",file_name)
			if not os.path.exists(output):
				os.makedirs(output)
			continue
		if re.search(POST_P, line):
			n += 1
			post_link = re.search(r"https://mbasic.facebook.com/.*?$", line).group()
			print('scrapy crawl comments -a email="gzylalala@163.com" -a password="a199102100014E" -a post="{}" -a date="2020-01-01" -a lang="en" -o comments/{}/{}{}.csv'.format(post_link, file_name, file_name, n))
