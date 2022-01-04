# 漫步在雲端- 行程規劃小幫手
## function: front.py

### 內容 
前端＋main function

### Class:
1. First_Page（首頁）


    功能：讓使用者輸入想去的城市以及選擇日期


2. Weather （天氣預報頁面）


    功能：顯示使用者使用此程式後7天的天氣資料

    後端：呼叫weather_api.py中的get_data

3. Search（景點選取頁面）


    功能：
        a. 標籤預設為酒吧，使用者可自行選擇想要的景點類型
        b. 按下like即可加進行程中，並顯示在右方
        c. 行程都選完後，再選取在該地點的停留時間
    
    後端：呼叫googlemaps_api.py中的get_recommend_list

4. Result（結果頁面）


    功能：顯示最佳行程規劃之時間表與行程表

    後端：呼叫google_api.py中的get_fast_time

## weather_api
### 內容
透過中央氣象局的api抓取各縣市一週的天氣資料

### function:
1. get_data(city)


    功能：抓取各縣市一週的天氣資料

    input: 輸入想去的城市（Ex. 臺北市、新北市、台中市）

    return: 
    資料型態：list
    result[][] -> len(result) = 7; len(result[i]) = 6
    result[i][0]為日期
    result[i][1]為天氣狀況
    result[i][2]為最高溫
    result[i][3]為最低溫
    result[i][4]為舒適度
    result[i][5]為降雨機率

## google_api.py
### 內容
透過google maps的api抓取資料

### function:
1. get_recommend_list(city, item, month, day)


    功能：給定城市與地點項目，回傳30筆景點資料

    input:
    string: city >> 城市
    string: item >> 景點項目 ex. 百貨公司

    return:
    資料型態：list
    result[][] -> len(result) = 30; len(result[i]) = 9
    result[i][0]為景點名稱
    result[i][1]為評價
    result[i][2]為評論數
    result[i][3]為icon
    result[i][4]為地點標籤
    result[i][5]為當天營業時間
    result[i][6]為place_id
    result[i][7]為開始營業時間
    result[i][8]為結束營業時間

2. sortList(alist)
    

    功能：依評價乘上評論數，由大到小排序alist
    
    演算法：bubble sort

    複雜度：O(n^2)

3. get_fast_time(alist, blist)


    功能：排出總交通時長最短的行程並確定個行程都在營業時間內
    
    複雜度：O(n!)，為了窮舉所有情況

    input:
    list: alist >> 景點資訊
    list: blist >> 停留時間

    return:
    資料型態：list
    result_timePoint >> 最佳行程時間表
    result_schedule >> 最佳行程表

4. get_time(clist)


    功能：計算總時間及各行程對應之時間點

    複雜度：O(n)

    input:
    list: clist >> list(景點資訊,停留時間)
    
    return:
    資料型態：list
    result >> 總時長
    time >> 各行程對應之時間點

5. sec2time(sec)

    
    功能：轉換時間格式

    input:
    int: sec >> 時間（秒數）

    return:
    資料型態：string
    pattern >> 時間 （HH:MM）# PBC_FianlProject
