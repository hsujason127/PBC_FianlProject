import tkinter as tk
from tkmacosx import Button
from PIL import Image, ImageTk
import google_api
import weather_api


class First_page(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    # 所需元件
    def createWidgets(self):

        # 底圖 # size尺寸！！
        self.im = Image.open('Frame 11.jpg')
        self.resized_img = self.im.resize((1280,720))
        self.img = ImageTk.PhotoImage(self.resized_img)
        self.imLabel = tk.Label(self, image=self.img).pack()

        # 灰色方塊
        self.cube = tk.Frame(self, width = 790, height = 130, bg='#EAEBED')
        self.cube.place(x=450,y=310) 

        # 白色方塊
        self.cube_white = tk.Frame(self, width = 610, height = 60, bg='white')
        self.cube_white.place(x=480, y= 345)

        # 選擇城市
        self.choice = tk.Label(self, text = '選擇目的地縣市', bg = 'white', fg = 'gray', font = ('Roboto', '10'))
        self.choice.place(x=495, y=350)

        # 選擇城市下拉式選單
        self.strvar = tk.StringVar() 
        self.strvar.set('台北市')
        
        self.box = tk.OptionMenu(self, self.strvar, "基隆市",'台北市','新北市','桃園市','新竹市','新竹縣','苗栗縣','台中市','彰化縣','南投縣', '雲林縣', '嘉義市',
                        '嘉義縣', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣','澎湖縣', '金門縣','連江縣')
        self.box.place(x=495, y=373, width = 110, height = 25)
        

        # 選擇日期
        self.choice2 = tk.Label(self, text = '選擇旅行日期', bg = 'white', fg = 'gray', font = ('Roboto', '10'))
        self.choice2.place(x=645, y=350)

        # 日期下拉式選單
        # 月
        self.strvar1 = tk.StringVar() 
        self.strvar1.set('01')
        self.box1 = tk.OptionMenu(self, self.strvar1, '01','02','03','04','05','06','07','08','09','10','11','12')
        self.box1.place(x=645, y=373, width = 45)
        # 日
        self.strvar2 = tk.StringVar() 
        self.strvar2.set('29')
        self.box2 = tk.OptionMenu(self, self.strvar2, '01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19',
                        '20','21','22','23','24','25','26','27','28','29','30','31')
        self.box2.place(x=710, y=373, width = 45)

        self.word_dash = tk.Label(self, text = '-', bg = 'white', fg = 'gray', font = ('Roboto', '12'))
        self.word_dash.place(x=693, y=372)
        
        # 旅程開始時間
        self.choice3 = tk.Label(self, text = '旅程開始時間', bg = 'white', fg = 'gray', font = ('Roboto', '10'))
        self.choice3.place(x=790, y=350)

        self.strvar3 = tk.StringVar() 
        self.strvar3.set('10:00')
        self.box3 = tk.OptionMenu(self, self.strvar3, '06:00','06:30','07:00','07:30', '08:00', '08:30', '09:00', '09:30', '10:00','10:30','11:00','11:30',
                        '12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30',
                        '18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30','24:00')
        self.box3.place(x=790, y=373, width = 110, height = 25)

        # 旅程結束時間
        self.strvar4 = tk.StringVar() 
        self.strvar4.set('22:00')

        self.choice4 = tk.Label(self, text = '旅程結束時間', bg = 'white', fg = 'gray', font = ('Roboto', '10'))
        self.choice4.place(x=940, y=350)
        self.box4 = tk.OptionMenu(self, self.strvar4, '06:00','06:30','07:00','07:30', '08:00', '08:30', '09:00', '09:30', '10:00','10:30','11:00','11:30',
                        '12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30',
                        '18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30','24:00')
        self.box4.place(x=940, y=373, width = 110, height = 25)

        # 開始旅行 # 按下去要跳轉到下一頁！！
        self.button1 = tk.Button(self, text = '開始旅行', bg = '#9E6133', fg = 'black', font = ('Roboto', '14', 'bold'), command=lambda: [self.return_data(), self.button_event()])
        self.button1.place(x=1105, y=345, width = 110 , height = 60)

    # 儲存選單資訊並回傳
    def return_data(self):
        self.info = []
        self.info.append(self.strvar.get()) # 城市資訊
        self.info.append(int(self.strvar1.get())) # 月
        self.info.append(int(self.strvar2.get())) # 日
        # print(self.info)
        return self.info

    # 點擊按鈕後拿到資訊並跳轉
    def button_event(self):
        self.info_back = self.return_data()
        # print(self.info_back)
        # 跳轉函數
        self.destroy()
        Weather(self.info_back)

# 天氣頁面
class Weather(tk.Frame):

    def __init__(self, get_info):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.get_info = get_info.copy()
        print(self.get_info)
        self.call_weather()

    def createWidgets(self):
         # 底圖 
        self.im = Image.open('白底.png')
        self.resized_img = self.im.resize((1300,730))
        self.img = ImageTk.PhotoImage(self.resized_img)
        self.imLabel = tk.Label(self, image=self.img).pack()

        # 未來一週天氣
        self.weather_title = tk.Label(self, text='未來一週天氣', fg='black', font=('Roboto', '45', 'bold'))
        self.weather_title.place(x=60,y=60)

        # button # 繼續旅行 
        self.b1 = Button(self, text='繼續旅行',borderwidth=0, bg='#9E6133', fg='white', font=('Roboto', '16', 'bold'), command=self.clickb1)
        self.b1.place(x=1085, y=60,width = 130, height = 50) 

        # 七個方塊 
        self.space1 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space1.place(x=60, y=190)

        self.space2 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space2.place(x=230, y=190)

        self.space3 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space3.place(x=400, y=190)

        self.space4 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space4.place(x=570, y=190)

        self.space5 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space5.place(x=740, y=190)

        self.space6 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space6.place(x=910, y=190)

        self.space7 = tk.Frame(self, width = 140 , height=450 ,bg = '#EAEBED')
        self.space7.place(x=1080, y=190)

        # 日期title + 天氣項目title 
        self.date1 = tk.Label(self, text = '01/03', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date1.place(x=97, y=220)

        self.date2 = tk.Label(self, text = '01/04', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date2.place(x=267, y=220)

        self.date3 = tk.Label(self, text = '01/05', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date3.place(x=437, y=220)

        self.date4 = tk.Label(self, text = '01/06', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date4.place(x=607, y=220)

        self.date5 = tk.Label(self, text = '01/07', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date5.place(x=777, y=220)

        self.date6 = tk.Label(self, text = '01/08', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date6.place(x=947, y=220)

        self.date7 = tk.Label(self, text = '01/09', fg = 'black', bg = '#EAEBED', font=('Roboto', '18', 'bold'))
        self.date7.place(x=1117, y=220)

        # 各項目title # space1
        self.condition11 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition11.place(x=77, y=280)

        self.highest11 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest11.place(x=77, y=345)

        self.lowest11 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest11.place(x=77, y=410)

        self.comfort11 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort11.place(x=77,y=475)

        self.rain11 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain11.place(x=77,y=540)

        # space2
        self.condition21 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition21.place(x=247, y=280)

        self.highest21 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest21.place(x=247, y=345)

        self.lowest21 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest21.place(x=247, y=410)

        self.comfort21 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort21.place(x=247,y=475)

        self.rain21 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain21.place(x=247,y=540)

        # space3
        self.condition31 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition31.place(x=417, y=280)

        self.highest31 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest31.place(x=417, y=345)

        self.lowest31 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest31.place(x=417, y=410)

        self.comfort31 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort31.place(x=417,y=475)

        self.rain31 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain31.place(x=417,y=540)

        # space4
        self.condition41 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition41.place(x=587, y=280)

        self.highest41 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest41.place(x=587, y=345)

        self.lowest41 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest41.place(x=587, y=410)

        self.comfort41 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort41.place(x=587,y=475)

        self.rain41 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain41.place(x=587,y=540)

        # space5
        self.condition51 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition51.place(x=757, y=280)

        self.highest51 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest51.place(x=757, y=345)

        self.lowest51 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest51.place(x=757, y=410)

        self.comfort51 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort51.place(x=757,y=475)

        self.rain51 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain51.place(x=757,y=540)

        # space6
        self.condition61 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition61.place(x=927, y=280)

        self.highest61 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest61.place(x=927, y=345)

        self.lowest61 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest61.place(x=927, y=410)

        self.comfort61 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort61.place(x=927,y=475)

        self.rain61 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain61.place(x=927,y=540)

        # space7
        self.condition71 = tk.Label(self, text = '天氣狀況', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.condition71.place(x=1097, y=280)

        self.highest71 = tk.Label(self, text = '最高溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.highest71.place(x=1097, y=345)

        self.lowest71 = tk.Label(self, text = '最低溫', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.lowest71.place(x=1097, y=410)

        self.comfort71 = tk.Label(self, text = '舒適度', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.comfort71.place(x=1097,y=475)

        self.rain71 = tk.Label(self, text = '降雨機率', fg = '#534E8F', bg = '#EAEBED', font=('Roboto', '10'))
        self.rain71.place(x=1097,y=540)
    
    def call_weather(self):
        self.get_weather =  weather_api.get_data(self.get_info[0])
        # print(self.get_weather)
        #各天氣項目 會變動ㄉ數據 
        # space1
        self.condition12 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition12['text'] = self.get_weather[0][1] # 根據資料變動
        self.condition12.place(x=77, y=300)

        self.highest12 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest12['text'] = '攝氏' + str(self.get_weather[0][2]) + '度'
        self.highest12.place(x=77,y=365)

        self.lowest12 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest12['text'] = '攝氏' + str(self.get_weather[0][3]) + '度'
        self.lowest12.place(x=77,y=430)

        self.comfort12 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort12['text'] = self.get_weather[0][4]
        self.comfort12.place(x=77,y=495)

        self.rain12 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain12['text'] = self.get_weather[0][5]
        self.rain12.place(x=77,y=560)
    

        # space2
        self.condition22 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition22['text'] = self.get_weather[1][1] # 根據資料變動
        self.condition22.place(x=247, y=300)

        self.highest22 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest22['text'] = '攝氏' + str(self.get_weather[1][2]) + '度'
        self.highest22.place(x=247,y=365)

        self.lowest22 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest22['text'] = '攝氏' + str(self.get_weather[1][3]) + '度'
        self.lowest22.place(x=247,y=430)

        self.comfort22 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort22['text'] = self.get_weather[1][4]
        self.comfort22.place(x=247,y=495)

        self.rain22 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain22['text'] = self.get_weather[1][5]
        self.rain22.place(x=247,y=560)

        # space3
        self.condition32 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition32['text'] = self.get_weather[2][1] # 根據資料變動
        self.condition32.place(x=417, y=300)

        self.highest32 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest32['text'] = '攝氏' + str(self.get_weather[2][2]) + '度'
        self.highest32.place(x=417,y=365)

        self.lowest32 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest32['text'] = '攝氏' + str(self.get_weather[2][3]) + '度'
        self.lowest32.place(x=417,y=430)

        self.comfort32 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort32['text'] = self.get_weather[2][4]
        self.comfort32.place(x=417,y=495)

        self.rain32 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain32['text'] = self.get_weather[2][5]
        self.rain32.place(x=417,y=560)

        # space4
        self.condition42 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition42['text'] = self.get_weather[3][1] # 根據資料變動
        self.condition42.place(x=587, y=300)

        self.highest42 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest42['text'] = '攝氏' + str(self.get_weather[3][2]) + '度'
        self.highest42.place(x=587,y=365)

        self.lowest42 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest42['text'] = '攝氏' + str(self.get_weather[3][3]) + '度'
        self.lowest42.place(x=587,y=430)

        self.comfort42 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort42['text'] = self.get_weather[3][4]
        self.comfort42.place(x=587,y=495)

        self.rain42 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain42['text'] = self.get_weather[3][5]
        self.rain42.place(x=587,y=560)

        # space5
        self.condition52 = tk.Label(self, fg ='black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition52['text'] = self.get_weather[4][1] # 根據資料變動
        self.condition52.place(x=757, y=300)

        self.highest52 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest52['text'] = '攝氏' + str(self.get_weather[4][2]) + '度'
        self.highest52.place(x=757,y=365)

        self.lowest52 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest52['text'] = '攝氏' + str(self.get_weather[4][3]) + '度'
        self.lowest52.place(x=757,y=430)

        self.comfort52 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort52['text'] = self.get_weather[4][4]
        self.comfort52.place(x=757,y=495)

        self.rain52 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain52['text'] = self.get_weather[4][5]
        self.rain52.place(x=757,y=560)

        # space6
        self.condition62 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition62['text'] = self.get_weather[5][1] # 根據資料變動
        self.condition62.place(x=927, y=300)

        self.highest62 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest62['text'] = '攝氏' + str(self.get_weather[5][2]) + '度'
        self.highest62.place(x=927,y=365)

        self.lowest62 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest62['text'] = '攝氏' + str(self.get_weather[5][3]) + '度'
        self.lowest62.place(x=927,y=430)

        self.comfort62 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort62['text'] = self.get_weather[5][4]
        self.comfort62.place(x=927,y=495)

        self.rain62 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain62['text'] = self.get_weather[5][5]
        self.rain62.place(x=927,y=560)

        # space7
        self.condition72 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.condition72['text'] = self.get_weather[6][1] # 根據資料變動
        self.condition72.place(x=1097, y=300)

        self.highest72 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.highest72['text'] = '攝氏' + str(self.get_weather[6][2]) + '度'
        self.highest72.place(x=1097,y=365)

        self.lowest72 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.lowest72['text'] = '攝氏' + str(self.get_weather[6][3]) + '度'
        self.lowest72.place(x=1097,y=430)

        self.comfort72 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.comfort72['text'] = self.get_weather[6][4]
        self.comfort72.place(x=1097,y=495)

        self.rain72 = tk.Label(self, fg = 'black', bg = '#EAEBED', font=('Roboto', '15'))
        self.rain72['text'] = self.get_weather[6][5]
        self.rain72.place(x=1097,y=560)
    

    def clickb1(self):
        info_for_search = self.get_info

        # 跳轉函數
        self.destroy()
        default_item = '酒吧'
        # 右邊item list
        default_list = ['','','','','']
        default_final = []
        Search(info_for_search, default_item, default_list,default_final)

class Search(tk.Frame):

    # 按下 button 後
    def __init__(self, info_for_search, info_item, right_item, final_info):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        # 匯入first page 資訊 (info)
        self.infolist = info_for_search.copy()
        self.item = info_item
        self.right_item = right_item
        self.final_info = final_info
        self.final_recommend()
        self.label_change()
   
    
    def createWidgets(self):
        # 底圖 # size尺寸！！
        self.im = Image.open('白底.png')
        self.resized_img = self.im.resize((1300,730))
        self.img = ImageTk.PhotoImage(self.resized_img)
        self.imLabel = tk.Label(self, image=self.img).pack()

        # 搜尋框
        self.search = tk.Entry(self, borderwidth=0.5)
        self.search.place(x=50, y=60, width = 753, height = 50)
        self.search.config(highlightbackground='#C4C4C4')

        # 標籤 # 已呼叫func
        self.tag1 = Button(self, text='酒吧', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'), command=self.clicktag1)
        self.tag1.place(x=70, y=140, width = 80, height=30)

        self.tag2 = Button(self, text='咖啡', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag2)
        self.tag2.place(x=160, y=140, width = 80, height=30)

        self.tag3 = Button(self, text='公園', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag3)
        self.tag3.place(x=250, y=140, width = 80, height=30)

        self.tag4 = Button(self, text='藝術展覽', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag4)
        self.tag4.place(x=340, y=140, width = 80, height=30)

        self.tag5 = Button(self, text='風景', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag5)
        self.tag5.place(x=430, y=140, width = 80, height=30)

        self.tag6 = Button(self, text='夜生活', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag6)
        self.tag6.place(x=520, y=140, width = 80, height=30)

        self.tag7 = Button(self, text='購物中心', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag7)
        self.tag7.place(x=610, y=140, width = 80, height=30)

        self.tag8 = Button(self, text='博物館', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag8)
        self.tag8.place(x=70, y=180, width = 80, height=30)

        self.tag9 = Button(self, text='圖書館', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag9)
        self.tag9.place(x=160, y=180, width = 80, height=30)

        self.tag10 = Button(self, text='超市', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag10)
        self.tag10.place(x=250, y=180, width = 80, height=30)

        self.tag11 = Button(self, text='飯店', bg='#F0EEF1', fg='gray', font = ('Roboto', '12'),command=self.clicktag11)
        self.tag11.place(x=340, y=180, width = 80, height=30)

        # 提示字
        self.word = tk.Label(self, text='點擊like按鈕以將景點加入「當天想去的景點」（最多可選 5 個景點）', fg='black', font=('Roboto', '10'))
        self.word.place(x=70, y=235)

        # 景點結果！？
        self.block1 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block1.place(x=55,y=265)

        self.block2 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block2.place(x=311,y=265)

        self.block3 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block3.place(x=567,y=265)

        self.block4 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block4.place(x=55,y=400)

        self.block5 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block5.place(x=311,y=400)

        self.block6 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block6.place(x=567,y=400)

        self.block7 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block7.place(x=55,y=535)

        self.block8 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block8.place(x=311,y=535)

        self.block9 = tk.Frame(self, width = 242, height=115, bg = '#F6EDE2')
        self.block9.place(x=567,y=535)

        # 右邊灰色方塊 
        self.space = tk.Frame(self, width = 500 , height=1080 ,bg = '#484C56')
        self.space.place(x=865, y=0)

        self.search_title = tk.Label(self, text='當天想去的景點', bg = '#484C56',fg='white', font=('Roboto', '45', 'bold'))
        self.search_title.place(x=910,y=60)

        # 景點選擇欄位
        self.choice_title = tk.Label(self, text = '已選擇景點', bg = '#484C56', fg = 'gray', font = ('Roboto', '14','bold'))
        self.choice_title.place(x=910, y=150)

        self.choice1 = tk.Frame(self, borderwidth=0)
        self.choice1.place(x=910, y=190, width = 230, height = 50)

        self.choice2 = tk.Frame(self, borderwidth=0)
        self.choice2.place(x=910, y=260, width = 230, height = 50)

        self.choice3 = tk.Frame(self, borderwidth=0)
        self.choice3.place(x=910, y=330, width = 230, height = 50)

        self.choice4 = tk.Frame(self, borderwidth=0)
        self.choice4.place(x=910, y=400, width = 230, height = 50)

        self.choice5 = tk.Frame(self, borderwidth=0)
        self.choice5.place(x=910, y=470, width = 230, height = 50)

        # 停留時間
        self.time_title = tk.Label(self, text = '停留時間/hr', bg = '#484C56', fg = 'gray', font = ('Roboto', '14', 'bold'))
        self.time_title.place(x=1160, y=150)

        self.v1 = tk.StringVar() 
        self.box1 = tk.OptionMenu(self, self.v1, '1','2','3','4','5')
        self.box1.place(x=1170, y=203, width = 70, height = 25)

        self.v2 = tk.StringVar()
        self.box2 = tk.OptionMenu(self, self.v2, '1','2','3','4','5')
        self.box2.place(x=1170, y=273, width = 70, height = 25)

        self.v3 = tk.StringVar()
        self.box3 = tk.OptionMenu(self, self.v3, '1','2','3','4','5')
        self.box3.place(x=1170, y=343, width = 70, height = 25)

        self.v4 = tk.StringVar()
        self.box4 = tk.OptionMenu(self, self.v4, '1','2','3','4','5')
        self.box4.place(x=1170, y=413, width = 70, height = 25)

        self.v5 = tk.StringVar()
        self.box5 = tk.OptionMenu(self, self.v5, '1','2','3','4','5')
        self.box5.place(x=1170, y=483, width = 70, height = 25)

        # 前往規劃最佳路徑 # 呼叫規劃路徑函數?? 
        self.button_route = Button(self, text='前往規劃最佳路徑',borderwidth=0, bg='#9E6133', fg='white', font=('Roboto', '14', 'bold'),command= lambda: self.goto_plan())
        # lambda: [self.return_plandata(), self.goto_plan()]
        self.button_route.place(x=1000, y=590,width = 150, height = 50) 
    
    # 根據選擇景點變換label
    def label_change(self):
        self.choice12 = tk.Label(self, font=('Roboto', '14'), bg = 'white', fg='black')
        self.choice12['text'] = self.right_item[0]
        self.choice12.place(x=920, y=203)

        self.choice22 = tk.Label(self,font=('Roboto', '14'), bg = 'white', fg='black')
        self.choice22['text'] = self.right_item[1]
        self.choice22.place(x=920, y=273)

        self.choice32 = tk.Label(self, font=('Roboto', '14'), bg = 'white', fg='black')
        self.choice32['text'] = self.right_item[2]
        self.choice32.place(x=920, y=343)

        self.choice42 = tk.Label(self, font=('Roboto', '14'), bg = 'white', fg='black')
        self.choice42['text'] = self.right_item[3]
        self.choice42.place(x=920, y=413)

        self.choice52 = tk.Label(self,font=('Roboto', '14'), bg = 'white', fg='black')
        self.choice52['text'] = self.right_item[4]
        self.choice52.place(x=920, y=483)
         

    def final_recommend(self):
        self.final_recommend = google_api.get_recommend_list(self.infolist[0],self.item, self.infolist[1], self.infolist[2])
         # 根據後端資料顯示結果
        print(self.final_recommend)
        self.title1 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
        if len(str(self.final_recommend[0][0])) >= 10:

            self.title1['text'] = self.final_recommend[0][0][:11]
        else:
            self.title1['text'] = self.final_recommend[0][0] # 根據資料變動
        self.title1.place(x=108,y=275)

        self.star1 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
        self.star1['text'] = self.final_recommend[0][1] # 根據資料變動
        self.star1.place(x=108,y=305)

        self.review1 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
        self.review1['text'] = '評論數：' + str(self.final_recommend[0][2]) # 根據資料變動
        self.review1.place(x=133,y=305)

        self.opentime1 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
        self.opentime1['text'] = str(self.final_recommend[0][5]) # 根據資料變動
        self.opentime1.place(x=110,y=325)

        self.like1 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike1)
        self.like1.place(x=111,y=350,width=50)

        # 開啟圖片
        self.im1 = Image.open('map1.png')
        self.resized_img1 = self.im1.resize((40,40))
        self.img1 = ImageTk.PhotoImage(self.resized_img1)
        self.imLabel1 = tk.Label(self, image=self.img1, bg='#F6EDE2')
        self.imLabel1.place(x=60,y=298)

        # x=311 +53
        if len(self.final_recommend) >= 2:
            self.title2 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[1][0])) >= 10:
                self.title2['text'] = self.final_recommend[1][0][:11]
            else:
                self.title2['text'] = self.final_recommend[1][0] # 根據資料變動
    
            self.title2.place(x=364,y=275)

            self.star2 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star2['text'] = self.final_recommend[1][1] # 根據資料變動
            self.star2.place(x=364,y=305)

            self.review2 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review2['text'] = '評論數：' + str(self.final_recommend[1][2]) # 根據資料變動
            self.review2.place(x=389,y=305)

            self.opentime2 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime2['text'] = str(self.final_recommend[1][5]) # 根據資料變動
            self.opentime2.place(x=366,y=325)

            self.like2 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike2)
            self.like2.place(x=367,y=350,width=50)

            # 開啟圖片
            self.imLabel2 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel2.place(x=316,y=298)

        # block3 #x=567+53
        if len(self.final_recommend) >= 3:
            self.title3 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[2][0])) >= 10:

                self.title3['text'] = self.final_recommend[2][0][:11]
            else:
                self.title3['text'] = self.final_recommend[2][0] # 根據資料變動

            self.title3.place(x=620,y=275)

            self.star3 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star3['text'] = self.final_recommend[2][1] # 根據資料變動
            self.star3.place(x=620,y=305)

            self.review3 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review3['text'] = '評論數：' + str(self.final_recommend[2][2]) # 根據資料變動
            self.review3.place(x=645,y=305)

            self.opentime3 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime3['text'] = str(self.final_recommend[2][5]) # 根據資料變動
            self.opentime3.place(x=622,y=325)

            self.like3 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike3)
            self.like3.place(x=623,y=350,width=50)

            # 開啟圖片
            self.imLabel3 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel3.place(x=572,y=298)

        # block4 # y=400+10
        if len(self.final_recommend) >= 4:
            self.title4 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[3][0])) >= 10:

                self.title4['text'] = self.final_recommend[3][0][:11]
            else:
                self.title4['text'] = self.final_recommend[3][0] # 根據資料變動
            self.title4.place(x=108,y=410)

            self.star4 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star4['text'] = self.final_recommend[3][1] # 根據資料變動
            self.star4.place(x=108,y=440)

            self.review4 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review4['text'] = '評論數：' + str(self.final_recommend[3][2]) # 根據資料變動
            self.review4.place(x=133,y=440)

            self.opentime4 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime4['text'] = str(self.final_recommend[3][5]) # 根據資料變動
            self.opentime4.place(x=110,y=460)

            self.like4 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'), command=self.clicklike4)
            self.like4.place(x=111,y=485,width=50)

            self.imLabel4 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel4.place(x=60,y=433)

        # block5
        if len(self.final_recommend) >= 5:
            self.title5 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[4][0])) >= 10:

                self.title5['text'] = self.final_recommend[4][0][:11]
            else:
                self.title5['text'] = self.final_recommend[4][0] # 根據資料變動
            self.title5.place(x=364,y=410)

            self.star5 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star5['text'] = self.final_recommend[4][1] # 根據資料變動
            self.star5.place(x=364,y=440)

            self.review5 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review5['text'] = '評論數：' + str(self.final_recommend[4][2]) # 根據資料變動
            self.review5.place(x=389,y=440)

            self.opentime5 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime5['text'] = str(self.final_recommend[4][5]) # 根據資料變動
            self.opentime5.place(x=366,y=460)

            self.like5 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike5)
            self.like5.place(x=367,y=485,width=50)

            self.imLabel5 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel5.place(x=316,y=433)

        # block6
        if len(self.final_recommend) >= 6:
            self.title6 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[5][0])) >= 10:

                self.title6['text'] = self.final_recommend[5][0][:11]
            else:
                self.title6['text'] = self.final_recommend[5][0] # 根據資料變動
            self.title6.place(x=620,y=410)

            self.star6 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star6['text'] = self.final_recommend[5][1] # 根據資料變動
            self.star6.place(x=620,y=440)

            self.review6 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review6['text'] = '評論數：' + str(self.final_recommend[5][2]) # 根據資料變動
            self.review6.place(x=645,y=440)

            self.opentime6 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime6['text'] = str(self.final_recommend[5][5]) # 根據資料變動
            self.opentime6.place(x=622,y=460)

            self.like6 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike6)
            self.like6.place(x=623,y=485,width=50)

            self.imLabel6 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel6.place(x=572,y=433)

        # block7 # y=535+10
        if len(self.final_recommend) >= 7:
            self.title7 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[6][0])) >= 10:

                self.title7['text'] = self.final_recommend[6][0][:11]
            else:
                self.title7['text'] = self.final_recommend[6][0] # 根據資料變動
            self.title7.place(x=108,y=545)

            self.star7 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star7['text'] = self.final_recommend[6][1] # 根據資料變動
            self.star7.place(x=108,y=575)

            self.review7 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review7['text'] = '評論數：' + str(self.final_recommend[6][2]) # 根據資料變動
            self.review7.place(x=133,y=575)

            self.opentime7 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime7['text'] = str(self.final_recommend[6][5]) # 根據資料變動
            self.opentime7.place(x=110,y=595)

            self.like7 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike7)
            self.like7.place(x=111,y=620,width=50)

            self.imLabel7 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel7.place(x=60,y=568)

        # block8 
        if len(self.final_recommend) >= 8:
            self.title8 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[7][0])) >= 10:

                self.title8['text'] = self.final_recommend[7][0][:11]
            else:
                self.title8['text'] = self.final_recommend[7][0] # 根據資料變動
            self.title8.place(x=364,y=545)

            self.star8 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star8['text'] = self.final_recommend[7][1] # 根據資料變動
            self.star8.place(x=364,y=575)

            self.review8 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review8['text'] = '評論數：' + str(self.final_recommend[7][2]) # 根據資料變動
            self.review8.place(x=389,y=575)

            self.opentime8 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime8['text'] = str(self.final_recommend[7][5]) # 根據資料變動
            self.opentime8.place(x=366,y=595)

            self.like8 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike8)
            self.like8.place(x=367,y=620,width=50)

            self.imLabel8 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel8.place(x=316,y=568)

        # block9
        if len(self.final_recommend) >= 9:
            self.title9 = tk.Label(self, bg = '#F6EDE2', fg='black',font=('Roboto','14','bold'),borderwidth=0)
            if len(str(self.final_recommend[8][0])) >= 10:
                self.title9['text'] = self.final_recommend[8][0][:11]
            else:
                self.title9['text'] = self.final_recommend[8][0] # 根據資料變動
            self.title9.place(x=620,y=545)

            self.star9 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'))
            self.star9['text'] = self.final_recommend[8][1] # 根據資料變動
            self.star9.place(x=620,y=575)

            self.review9 = tk.Label(self, bg = '#F6EDE2', fg='#6E98E9',font=('Roboto','10'))
            self.review9['text'] = '評論數：' + str(self.final_recommend[8][2]) # 根據資料變動
            self.review9.place(x=645,y=575)

            self.opentime9 = tk.Label(self, bg = '#F6EDE2', fg='gray',font=('Roboto','10'),borderwidth=0)
            self.opentime9['text'] = str(self.final_recommend[8][5]) # 根據資料變動
            self.opentime9.place(x=622,y=595)

            self.like9 = tk.Button(self, text='like',bg = 'white', fg='gray',font=('Roboto','10'),command=self.clicklike9)
            self.like9.place(x=623,y=620,width=50)

            self.imLabel9 = tk.Label(self, image=self.img1, bg='#F6EDE2')
            self.imLabel9.place(x=572,y=568)
    
    # 按下標籤後
    def clicktag1(self):
        self.get_tag1 = self.tag1['text']
        # 呼叫function
        self.recommend1 = google_api.get_recommend_list(self.infolist[0], self.get_tag1, self.infolist[1], self.infolist[2])
        # print(self.recommend1) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag1, self.right_item,self.final_info)
    
    # clicktag2以後待補
    def clicktag2(self):
        self.get_tag2 = self.tag2['text']
        # 呼叫function
        self.recommend2 = google_api.get_recommend_list(self.infolist[0], self.get_tag2, self.infolist[1], self.infolist[2])
        # print(self.recommend2) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag2, self.right_item,self.final_info)
    
    def clicktag3(self):
        self.get_tag3 = self.tag3['text']
        # 呼叫function
        self.recommend3 = google_api.get_recommend_list(self.infolist[0], self.get_tag3, self.infolist[1], self.infolist[2])
        # print(self.recommend3) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag3, self.right_item,self.final_info)

    def clicktag4(self):
        self.get_tag4 = self.tag4['text']
        # 呼叫function
        self.recommend4 = google_api.get_recommend_list(self.infolist[0], self.get_tag4, self.infolist[1], self.infolist[2])
        # print(self.recommend4) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag4, self.right_item,self.final_info)
    
    # 風景
    def clicktag5(self):
        self.get_tag5 = self.tag5['text']
        # 呼叫function
        self.recommend5 = google_api.get_recommend_list(self.infolist[0], self.get_tag5, self.infolist[1], self.infolist[2])
        # print(self.recommend5) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag5, self.right_item,self.final_info)
    
    def clicktag6(self):
        self.get_tag6 = self.tag6['text']
        # 呼叫function
        self.recommend6 = google_api.get_recommend_list(self.infolist[0], self.get_tag6, self.infolist[1], self.infolist[2])
        # print(self.recommend6)

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag6, self.right_item,self.final_info)
    
    def clicktag7(self):
        self.get_tag7 = self.tag7['text']
        # 呼叫function
        self.recommend7 = google_api.get_recommend_list(self.infolist[0], self.get_tag7, self.infolist[1], self.infolist[2])
        # print(self.recommend7) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag7, self.right_item,self.final_info)
    
    def clicktag8(self):
        self.get_tag8 = self.tag8['text']
        # 呼叫function
        self.recommend8 = google_api.get_recommend_list(self.infolist[0], self.get_tag8, self.infolist[1], self.infolist[2])
        # print(self.recommend8) 

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag8, self.right_item,self.final_info)
    
    def clicktag9(self):
        self.get_tag9 = self.tag9['text']
        # 呼叫function
        self.recommend9 = google_api.get_recommend_list(self.infolist[0], self.get_tag9, self.infolist[1], self.infolist[2])
        # print(self.recommend9)

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag9, self.right_item,self.final_info)
    
    def clicktag10(self):
        self.get_tag10 = self.tag10['text']
        # 呼叫function
        self.recommend10 = google_api.get_recommend_list(self.infolist[0], self.get_tag10, self.infolist[1], self.infolist[2])
        # print(self.recommend10)

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag10, self.right_item, self.final_info)
    
    def clicktag11(self):
        self.get_tag11 = self.tag11['text']
        # 呼叫function
        self.recommend11 = google_api.get_recommend_list(self.infolist[0], self.get_tag11, self.infolist[1], self.infolist[2])
        # print(self.recommend11)

        # 螢幕更新 # 整個class重跑
        self.destroy()
        Search(self.infolist, self.get_tag11, self.right_item, self.final_info)

    # 按下like按鈕後觸發函數 
    def clicklike1(self):
        self.get_title1 = self.final_recommend[0][0]
        self.get_all1 = self.final_recommend[0]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title1
            self.final_info.append(self.get_all1)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title1
            self.final_info.append(self.get_all1)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title1
            self.final_info.append(self.get_all1)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title1
            self.final_info.append(self.get_all1)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title1
            self.final_info.append(self.get_all1)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item, self.final_info)
    
    def clicklike2(self):
        if len(self.final_recommend[1][0])>15:
            self.get_title2 = self.final_recommend[1][0][0:16]
        else:
            self.get_title2 = self.final_recommend[1][0]
        self.get_all2 = self.final_recommend[1]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title2
            self.final_info.append(self.get_all2)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title2
            self.final_info.append(self.get_all2)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title2
            self.final_info.append(self.get_all2)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title2
            self.final_info.append(self.get_all2)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title2
            self.final_info.append(self.get_all2)
        
        print(self.final_info)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike3(self):
        if len(self.final_recommend[2][0])>15:
            self.get_title3 = self.final_recommend[2][0][0:16]
        else:
            self.get_title3 = self.final_recommend[2][0]
        self.get_all3 = self.final_recommend[2]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title3
            self.final_info.append(self.get_all3)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title3
            self.final_info.append(self.get_all3)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title3
            self.final_info.append(self.get_all3)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title3
            self.final_info.append(self.get_all3)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title3
            self.final_info.append(self.get_all3)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike4(self):
        if len(self.final_recommend[3][0])>15:
            self.get_title4 = self.final_recommend[3][0][0:16]
        else:
            self.get_title4 = self.final_recommend[3][0]
        self.get_all4 = self.final_recommend[3]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title4
            self.final_info.append(self.get_all4)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title4
            self.final_info.append(self.get_all4)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title4
            self.final_info.append(self.get_all4)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title4
            self.final_info.append(self.get_all4)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title4
            self.final_info.append(self.get_all4)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike5(self):
        if len(self.final_recommend[4][0])>15:
            self.get_title5 = self.final_recommend[4][0][0:16]
        else:
            self.get_title5 = self.final_recommend[4][0]
        self.get_all5 = self.final_recommend[4]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title5
            self.final_info.append(self.get_all5)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title5
            self.final_info.append(self.get_all5)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title5
            self.final_info.append(self.get_all5)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title5
            self.final_info.append(self.get_all5)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title5
            self.final_info.append(self.get_all5)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike6(self):
        if len(self.final_recommend[5][0])>15:
            self.get_title6 = self.final_recommend[5][0][0:16]
        else:
            self.get_title6 = self.final_recommend[5][0]
        self.get_all6 = self.final_recommend[5]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title6
            self.final_info.append(self.get_all6)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title6
            self.final_info.append(self.get_all6)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title6
            self.final_info.append(self.get_all6)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title6
            self.final_info.append(self.get_all6)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title6
            self.final_info.append(self.get_all6)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike7(self):
        if len(self.final_recommend[6][0])>15:
            self.get_title7 = self.final_recommend[6][0][0:16]
        else:
            self.get_title7 = self.final_recommend[6][0]
        self.get_all7 = self.final_recommend[6]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title7
            self.final_info.append(self.get_all7)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title7
            self.final_info.append(self.get_all7)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title7
            self.final_info.append(self.get_all7)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title7
            self.final_info.append(self.get_all7)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title7
            self.final_info.append(self.get_all7)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike8(self):
        if len(self.final_recommend[7][0])>15:
            self.get_title8 = self.final_recommend[7][0][0:16]
        else:
            self.get_title8 = self.final_recommend[7][0]
        self.get_all8 = self.final_recommend[7]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title8
            self.final_info.append(self.get_all8)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title8
            self.final_info.append(self.get_all8)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title8
            self.final_info.append(self.get_all8)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title8
            self.final_info.append(self.get_all8)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title8
            self.final_info.append(self.get_all8)

        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    def clicklike9(self):
        if len(self.final_recommend[8][0])>15:
            self.get_title9 = self.final_recommend[8][0][0:16]
        else:
            self.get_title9 = self.final_recommend[8][0]
        self.get_all9 = self.final_recommend[8]

        if self.right_item[0] == '':
            self.right_item[0] = self.get_title9
            self.final_info.append(self.get_all9)
        elif self.right_item[0] != '' and self.right_item[1] == '':
            self.right_item[1] = self.get_title9
            self.final_info.append(self.get_all9)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] == '':
            self.right_item[2] = self.get_title9
            self.final_info.append(self.get_all9)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] == '':
            self.right_item[3] = self.get_title9
            self.final_info.append(self.get_all9)
        elif self.right_item[0] != '' and self.right_item[1] != '' and self.right_item[2] != '' and self.right_item[3] != '' and self.right_item[4] == '' :
            self.right_item[4] = self.get_title9
            self.final_info.append(self.get_all9)
        
        # 頁面刷新
        self.destroy()
        Search(self.infolist, self.item, self.right_item,self.final_info)
    
    # 按下規劃路徑按鈕後觸發函數
    # 儲存選單資訊並回傳給後端計算
    def return_plandata(self):
        self.final_plan1 = []
        self.final_plan2 = []
        self.final_plan1.append(self.final_info[0]) # 第一個行程
        self.final_plan1.append(self.final_info[1]) # 第二個行程
        self.final_plan1.append(self.final_info[2]) # 第三個行程
        self.final_plan2.append(int(self.v1.get())) # 停留時間1
        self.final_plan2.append(int(self.v2.get())) # 停留時間2
        self.final_plan2.append(int(self.v3.get())) # 停留時間3
        # print(self.final_plan1)
        # print(self.final_plan2)
        return self.final_plan1, self.final_plan2
    

    # 點擊按鈕後拿到資訊並跳轉
    def goto_plan(self):
        self.plan_back1, self.plan_back2 = self.return_plandata()
        # print(self.plan_back1)
        # print(self.plan_back2)
        # 跳轉函數 # 行程 # 時間
        self.destroy()
        Result(self.plan_back1, self.plan_back2)

class Result(tk.Frame):

    def __init__(self,  get_final_plan1, get_final_plan2):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        self.get_final_plan1 = get_final_plan1  # 行程
        self.get_final_plan2 = get_final_plan2 # 時間
        self.cal_bestplan()
    
    # 所需元件
    def createWidgets(self):
        # 底圖！！
        self.im = Image.open('result_page.jpg')
        self.resized_img = self.im.resize((1300,730))
        self.img = ImageTk.PhotoImage(self.resized_img)
        self.imLabel = tk.Label(self, image=self.img).pack()

        # if 三個景點內 # 用entry還是Label???

        self.time_title = tk.Label(self, text = '時間', bg = '#DEDEDB', fg = 'gray', font = ('Roboto', '14','bold'))
        self.time_title.place(x=480, y=195)

        self.time_result11 = tk.Frame(self, width = 140, height = 50, bg='white', bd=0)
        self.time_result11.place(x=430, y= 235)

        self.time_result21 = tk.Frame(self, width = 140, height = 50, bg='white', bd=0)
        self.time_result21.place(x=430, y= 310)

        self.time_result31 = tk.Frame(self, width = 140, height = 50, bg='white', bd=0)
        self.time_result31.place(x=430, y= 385)

        self.time_result41 = tk.Frame(self, width = 140, height = 50, bg='white', bd=0)
        self.time_result41.place(x=430, y= 460)

        self.time_result51 = tk.Frame(self, width = 140, height = 50, bg='white', bd=0)
        self.time_result51.place(x=430, y= 535)

        self.travel_title = tk.Label(self, text = '行程內容', bg = '#E1E2E2', fg = 'gray', font = ('Roboto', '14','bold'))
        self.travel_title.place(x=730, y=195)

        self.travel_result11 = tk.Frame(self, width = 230, height = 50, bg='white', bd=0)
        self.travel_result11.place(x=650, y= 235)

        self.travel_result21 = tk.Frame(self, width = 230, height = 50, bg='white', bd=0)
        self.travel_result21.place(x=650, y= 310)

        self.travel_result31 = tk.Frame(self, width = 230, height = 50, bg='white', bd=0)
        self.travel_result31.place(x=650, y= 385)

        self.travel_result41 = tk.Frame(self, width = 230, height = 50, bg='white', bd=0)
        self.travel_result41.place(x=650, y= 460)

        self.travel_result51 = tk.Frame(self, width = 230, height = 50, bg='white', bd=0)
        self.travel_result51.place(x=650, y= 535)

    def cal_bestplan(self): #計算最佳路徑函數
        tmp = google_api.get_fast_time(self.get_final_plan1, self.get_final_plan2)
        # print(tmp)
        self.bestplan1, self.bestplan2 = tmp[0], tmp[1]
        # self.bestplan1 = self.tmp[0]
        # self.bestplan2 = self.tmp[1]
        # 時間變動
        self.time_result12 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.time_result12['text'] = self.bestplan1[0] # 根據資料變動
        self.time_result12.place(x=445, y= 248)

        self.time_result22 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.time_result22['text'] = self.bestplan1[1]# 根據資料變動
        self.time_result22.place(x=445, y= 323)

        self.time_result32 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.time_result32['text'] = self.bestplan1[2] # 根據資料變動
        self.time_result32.place(x=445, y= 398)

        self.time_result42 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.time_result42['text'] = self.bestplan1[3]  # 根據資料變動
        self.time_result42.place(x=445, y= 473)

        self.time_result52 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.time_result52['text'] = self.bestplan1[4]  # 根據資料變動
        self.time_result52.place(x=445, y= 548)

        # 行程變動
        self.travel_result12 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.travel_result12['text'] = self.bestplan2[0] # 根據資料變動
        self.travel_result12.place(x=668, y= 248)

        self.travel_result22 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.travel_result22['text'] = self.bestplan2[1] # 根據資料變動
        self.travel_result22.place(x=668, y= 323)

        self.travel_result32 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.travel_result32['text'] = self.bestplan2[2] # 根據資料變動
        self.travel_result32.place(x=668, y= 398)

        self.travel_result42 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.travel_result42['text'] = self.bestplan2[3] # 根據資料變動
        self.travel_result42.place(x=668, y= 473)

        self.travel_result52 = tk.Label(self, bg='white', font=('Roboto', '15'))
        self.travel_result52['text'] = self.bestplan2[4] # 根據資料變動
        self.travel_result52.place(x=668, y=548)

plan = First_page()
plan.master.title("旅遊規劃小幫手")
plan.master.geometry('1920x1080')
plan.mainloop()
