# import requests
#
# response = requests.get("https://serpapi.com/search?engine=google_trends")
# # r = requests.post('https://httpbin.org/post', data={'key': 'value'})
#
# print(response.json())

# from pytrends.request import TrendReq
#
# # pytrend = TrendReq(hl='en-US', tz=360)
# pytrend = TrendReq()


# keywords = ['Python programming', 'Data Science', 'Machine Learning']
#
# pytrend.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')


#
# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())
#
# # Interest by Region
# interest_by_region_df = pytrend.interest_by_region()
# print(interest_by_region_df.head())
#
# # Related Queries, returns a dictionary of dataframes
# related_queries_dict = pytrend.related_queries()
# print(related_queries_dict)
#
# # Get Google Hot Trends data
# trending_searches_df = pytrend.trending_searches()
# print(trending_searches_df.head())
#
# # Get Google Hot Trends data
# today_searches_df = pytrend.today_searches()
# print(today_searches_df.head())
#
# # Get Google Top Charts
# top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
# print(top_charts_df.head())
#
# # Get Google Keyword Suggestions
# suggestions_dict = pytrend.suggestions(keyword='pizza')
# print(suggestions_dict)
#
# # Get Google Realtime Search Trends
# realtime_searches = pytrend.realtime_trending_searches(pn='IN')
# print(realtime_searches.head())
#
# # Recreate payload with multiple timeframes
# pytrend.build_payload(kw_list=['pizza', 'bagel'], timeframe=['2022-09-04 2022-09-10', '2022-09-18 2022-09-24'])
#
# # Multirange Interest Over Time
# multirange_interest_over_time_df = pytrend.multirange_interest_over_time()
# print(multirange_interest_over_time_df.head())









