from pytrends.request import TrendReq
import json
import time
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
curYear = int(date.strftime("%Y"))
curMonth = int(date.strftime("%m"))
curDay = int(date.strftime("%d"))

# Google Trends Key Words
kw_list = ["bitcoin"]

pytrends = TrendReq(hl='en-US', tz=360) 

# main process to call the TrendReq to get the result
get_historical_interest = pytrends.get_historical_interest(kw_list, year_start=2015, month_start=1, day_start=1, hour_start=0, year_end=curYear, month_end=curMonth, day_end=curDay, hour_end=0, cat=0, sleep=0, frequency='daily')

result = get_historical_interest.to_json(orient="split")
jsonContent = json.loads(result)

keyWord = jsonContent['columns'][0]
result_data = jsonContent['index']

resultDataByDay = []
resultDataByWeek = {}

# filter data 
for i in range(len(result_data)):
    now = int(result_data[i]/1000)
    
    YearMonthDay= time.strftime("%Y-%m-%d", time.localtime(now))
    dayData = {}
    dayData[YearMonthDay] = jsonContent['data'][i][0]
    resultDataByDay.append(dayData)
    
    YearWeek = time.strftime("%Y-%W", time.localtime(now))
    WeekData = {}
    WeekData[YearWeek] = jsonContent['data'][i][0]
    resultDataByWeek[YearWeek] = WeekData

# write day json to file

with open("dayData.txt","w") as file:
    file.write(json.dumps(resultDataByDay))

# write week json to file
resultDataByWeekText = []
for weekValue in resultDataByWeek.values():
    resultDataByWeekText.append(weekValue)
with open("weekData.txt","w") as file:
    file.write(json.dumps(resultDataByWeekText))