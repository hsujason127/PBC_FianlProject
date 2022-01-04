import googlemaps
import math as m
import time
from itertools import permutations

'''
@author: b08209034
There are two functions in this py.
1. get_recommend_list
2. get_fast_time

I use google maps api to get the information I want.
'''


api_key = 'AIzaSyBcoQ1rwnbTSpNhlKC-mQ7Q7bG41SGMmq4'
gmaps = googlemaps.Client(key=api_key)

def sortList(l):
    length = len(l)
    for i in range(length):
        already_sorted = True
        for j in range(length - i - 1):
            # if l[j]['rating'] < l[j+1]['rating']:
            #     l[j], l[j+1] = l[j+1], l[j]
            #     already_sorted = False
            # elif l[j]['rating'] == l[j+1]['rating']:
            #     if l[j]['user_ratings_total'] < l[j+1]['user_ratings_total']:
            #         l[j], l[j + 1] = l[j + 1], l[j]
            #         already_sorted = False
            if l[j]['rating'] * l[j]['user_ratings_total'] < l[j+1]['rating'] * l[j+1]['user_ratings_total']:
                l[j], l[j+1] = l[j+1], l[j]
                already_sorted = False
        if already_sorted:
            break

    return l

'''
function: get_recommends_list
input:
    string: city >> 城市
    string: item >> 景點項目 ex. 百貨公司
return:
    list: result >> 景點資訊
'''
def get_recommend_list(city, item, month, day):
    ids = []  # 放景點

    google_result = gmaps.geocode(city)
    loc = google_result[0]['geometry']['location']

    # get the data from google maps api
    re1 = gmaps.places_nearby(keyword=item, location=loc, radius=10000)
    for place in re1['results']:
        if 'rating' in place:
            ids.append(place)
    # get the data from next page
    time.sleep(2)
    re2 = gmaps.places_nearby(keyword=item, location=loc, radius=10000, page_token=re1['next_page_token'])
    for place in re2['results']:
        if 'rating' in place:
            ids.append(place)
        if len(ids) == 30:
            break

    # 判斷選定日期當天是星期幾：
    if month == 12:
        if day == 27:
            dateIndex = 0
        elif day == 21 or day == 28:
            dateIndex = 1
        elif day == 22 or day == 29:
            dateIndex = 2
        elif day == 23 or day == 30:
            dateIndex = 3
        elif day == 24 or day == 31:
            dateIndex = 4
        elif day == 25:
            dateIndex = 5
        elif day == 26:
            dateIndex = 6
    elif month == 1:
        if day == 3 or day == 10 or day == 17 or day == 24 or day == 31:
            dateIndex = 0
        elif day == 4 or day == 11 or day == 18 or day == 25:
            dateIndex = 1
        elif day == 5 or day == 12 or day == 19 or day == 26:
            dateIndex = 2
        elif day == 6 or day == 13 or day == 20 or day == 27:
            dateIndex = 3
        elif day == 7 or day == 14 or day == 21 or day == 28:
            dateIndex = 4
        elif day == 1 or day == 8 or day == 15 or day == 22 or day == 29:
            dateIndex = 5
        elif day == 2 or day == 9 or day == 16 or day == 23 or day == 30:
            dateIndex = 6

    # sort the ids by function: sortList
    sortList(ids)
    result = []

    count = 0
    for i in range(len(ids)):
        datalist = gmaps.place(place_id=ids[i]['place_id'])
        # these tags are 24 hours opening
        if item == "公園" or item == "飯店" or item == "風景" or item == "古蹟":
            result.append([])
            # 景點名稱、評分、評論數、icon、類別、當日營業時間
            result[count].append(ids[i]['name'])
            result[count].append(ids[i]['rating'])
            result[count].append(ids[i]['user_ratings_total'])
            result[count].append(ids[i]['icon'])
            result[count].append(ids[i]['types'])
            if dateIndex == 0:
                result[count].append("Monday: 0:00 AM - 12:00 PM")
            elif dateIndex == 1:
                result[count].append("Tuesday: 0:00 AM - 12:00 PM")
            elif dateIndex == 2:
                result[count].append("Wednesday: 0:00 AM - 12:00 PM")
            elif dateIndex == 3:
                result[count].append("Thursday: 0:00 AM - 12:00 PM")
            elif dateIndex == 4:
                result[count].append("Friday: 0:00 AM - 12:00 PM")
            elif dateIndex == 5:
                result[count].append("Saturday: 0:00 AM - 12:00 PM")
            elif dateIndex == 6:
                result[count].append("Sunday: 0:00 AM - 12:00 PM")
            result[count].append(ids[i]['place_id'])
            result[count].append("0000")
            result[count].append("2400")
            count += 1
        elif ('opening_hours' in datalist['result'] and len(datalist['result']['opening_hours']['periods']) == 7):
            result.append([])
            # 景點名稱、評分、評論數、icon、類別、當日營業時間
            result[count].append(ids[i]['name'])
            result[count].append(ids[i]['rating'])
            result[count].append(ids[i]['user_ratings_total'])
            result[count].append(ids[i]['icon'])
            result[count].append(ids[i]['types'])
            result[count].append(datalist['result']['opening_hours']['weekday_text'][dateIndex])
            result[count].append(ids[i]['place_id'])
            result[count].append(datalist['result']['opening_hours']['periods'][dateIndex]['open']["time"])
            if 0 <= int(datalist['result']['opening_hours']['periods'][dateIndex]['close']["time"]) <= 500:
                datalist['result']['opening_hours']['periods'][dateIndex]['close']["time"] = str(int(datalist['result']['opening_hours']['periods'][dateIndex]['close']["time"])+2400)
            result[count].append(datalist['result']['opening_hours']['periods'][dateIndex]['close']["time"])
            count += 1
    return result

'''
function: get_fast_time
input:
    list: alist >> 景點資訊
    list: blist >> 停留時間
:return
    list: result_timePoint >> 最佳行程時間表
    list: result_schedule >> 最佳行程表
'''
def get_fast_time(alist, blist):
    length = len(alist)

    clist = []
    for i in range(length):
        clist.append([])
        clist[i].append(alist[i])
        clist[i].append(blist[i])
    # 窮舉所有排列可能：
    prob_lists = list(permutations(clist, length))

    # 計算此組合下的總時長與抵達各點的時間
    tmp = get_time(list(prob_lists[0]))
    totalTime_min = 10000000
    timePoint_min = tmp[1].copy()

    best_schedule = list(prob_lists[0]).copy()
    c = m.factorial(length)

    for i in range(1, c):
        tmp = get_time(list(prob_lists[i]))
        totalTime = tmp[0]
        timePoint = tmp[1].copy()

        # 先確定這個順序下每個景點都在營業時間內
        inTime = True
        for j in range(length):
            if int(prob_lists[i][j][0][7]) <= int(timePoint[2*j]) <= int(prob_lists[i][j][0][8]):
                continue
            else:
                inTime = False
                break

        if inTime:
            if totalTime < totalTime_min:
                totalTime_min = totalTime
                timePoint_min = timePoint
                best_schedule = list(prob_lists[i]).copy()

    # 處理時間格式
    for i in range(len(timePoint_min)):
        if len(timePoint_min[i]) == 3:
            timePoint_min[i] = timePoint_min[i][:1] + ':' + timePoint_min[i][1:]
        else:
            timePoint_min[i] = timePoint_min[i][:2] + ':' + timePoint_min[i][2:]

    # 整理時間表
    result_timePoint = []
    for i in range(len(timePoint_min)-1):
        result_timePoint.append(timePoint_min[i] + ' - ' + timePoint_min[i+1])

    # 把交通時間加進行程表中
    result_schedule = []
    result_schedule.append(best_schedule[0][0][0])
    for i in range(1, length):
        result_schedule.append("交通時間")
        result_schedule.append(best_schedule[i][0][0])

    return result_timePoint, result_schedule

def sec2time(sec):
    ''' Convert seconds to '#D days#, HH:MM' '''
    if hasattr(sec,'__len__'):
        return [sec2time(s) for s in sec]
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    pattern = r'%02d%02d'
    return pattern % (h, m)

# be used in get_fast_time
def get_time(clist):
    # 以秒為單位
    result = 0
    timeNow = 11 * 60 * 60
    time = ['1100']
    for i in range(len(clist)-1):
        tmp = gmaps.distance_matrix(clist[i][0][0], clist[i+1][0][0])['rows'][0]['elements'][0]
        if tmp['status'] != 'ZERO_RESULTS':
            a = tmp['duration']["value"]
        else:
            a = 30 * 60
        result += a + clist[i][1] * 60 * 60
        timeNow += clist[i][1] * 60 * 60
        time.append(sec2time(timeNow))
        timeNow += a
        time.append(sec2time(timeNow))
    timeNow += clist[-1][1] * 60 * 60
    result += clist[-1][1] * 60 * 60
    time.append(sec2time(timeNow))
    return result, time

