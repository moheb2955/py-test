import requests

title = input('''موضوع
(پیش فرض ندارد)
: ''') or ""
count = input('''تعداد 
(پیش فرض حداکثر)
: ''')
geo = input('''کشور
(https://serpapi.com/google-trends-locations) از این سایت برای به دست آورد کد مناطق استفاده کنید 
(پیش فرض US)
: ''') or "US"
date = input('''
now 1-H - 1 ساعت پیش
now 4-H - 4 ساعت پیش
now 1-d - 1 روز
now 7-d - 7 روز
today 1-m - 1 ماه
today 3-m - 3 ماه
today 12-m - 1 سال
today 5-y - 5 سال
all - از 2004 تا کنون yyyy-mm-dd تاریخ میلادی را وارد کنید
: ''') or "today 3-m"

gprop = input('''Web Search, YouTube Search, News Search, Image Search
(پیش فرض Web Search)
: ''') or ''

url = "https://serpapi.com/search?engine=google_trends"

params = {
  "q": title,
  "api_key": "dc0a5c7c4813fa80909e0c45623cffd5dab1cee47d4ced79fe74c997c11bc6b1",
  "hl": "fa",
  "geo": geo,
  "gprop": gprop,
  "date": date,
  # "csv": "true",
  "output": "json",  # can also get "html"
  "data_type": "RELATED_TOPICS",
}

req = requests.get(url, params=params)
res = req.json()['related_topics']['top']
print(res)

if count != '':
  del res[int(count):]


for i in res:
  trends = f'title: {i["topic"]["title"]}, type: {i["topic"]["type"]}'
  print(trends)


# todo for google_trends_autocomplete engine (it's not recommended)
# res = req.json()['suggestions']
#
# for i in res:
#   trends = f'title: {i["title"]}, type: {i["type"]}'
#   print(trends)
# print(req.json())