import json
import requests

'''
@author: b08209034
There are a function in this py.
1. get_data

I use weather api to get the information I want.
'''

'''
weather api 使用方法：
input: 輸入想去的城市（Ex. 臺北市、新北市、台中市）
output: 
資料型態：list[][] -> len(list) = 7; len(list[i]) = 6
list[i][0]為日期
list[i][1]為天氣狀況
list[i][2]為最高溫
list[i][3]為最低溫
list[i][4]為舒適度
list[i][5]為降雨機率
正常：使用此function當天往後7天的天氣資料
錯誤：輸入錯誤的城市名稱
'''
def get_data(city):
    # 判斷用戶要選哪個縣市
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091"
    params = {
        "Authorization": "CWB-B174379B-EB15-44F0-BA1A-B42A2237164A",
    }

    #
    if city == "台北市":
        city = "臺北市"
    elif city == "台中市":
        city = "臺中市"
    elif city == "台南市":
        city = "臺南市"
    elif city == "台東市":
        city = "臺東市"
    try:
        response = requests.get(url, params=params)
        result = []
        if response.status_code == 200:
            data = json.loads(response.text)
            cityIndex = 0
            # 找尋district的index
            for i in range(len(data["records"]["locations"][0]['location'])):
                if city in data["records"]["locations"][0]['location'][i]['locationName']:
                    cityIndex = i
            else:
                weather_elements = data["records"]["locations"][0]['location'][cityIndex]["weatherElement"]
                index = 0
                for i in range(len(weather_elements[10]["time"])-14, len(weather_elements[10]["time"]), 2):
                    result.append([])
                    day = weather_elements[10]["time"][i]["startTime"][:10]
                    prob_precipitation = weather_elements[0]["time"][i]["elementValue"][0]["value"]
                    if prob_precipitation == ' ':
                        prob_precipitation = 'unknown'
                    else:
                        prob_precipitation += ' %'
                    comfort_index = weather_elements[3]["time"][i]["elementValue"][1]["value"]
                    max_temp = weather_elements[12]["time"][i]["elementValue"][0]["value"]
                    min_temp = weather_elements[8]["time"][i]["elementValue"][0]["value"]
                    weather_state = weather_elements[6]["time"][i]["elementValue"][0]["value"]
                    result[index].append(day)
                    result[index].append(weather_state)
                    result[index].append(max_temp)
                    result[index].append(min_temp)
                    result[index].append(comfort_index)
                    result[index].append(prob_precipitation)
                    index += 1
            return result
        else:
            print("Can't get data!")
    except:
        print('請輸入正確縣市名稱')
