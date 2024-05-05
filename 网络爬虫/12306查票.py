import requests
import json
import prettytable as pt
file = open('stations.txt',encoding='utf-8')
content = json.loads(file.read())
# print(content["赣州"])
file.close()

from_city = input('请输入出发城市:')
to_city = input('请输入到达城市:')
table = pt.PrettyTable()
table.field_names = ['序号','车次','出发时间','到达时间','耗时','出发日期','商务座','一等座','二等座']
url = f'https://kyfw.12306.cn/otn/leftTicket/queryE?leftTicketDTO.train_date=2024-03-15&leftTicketDTO.from_station={content[from_city]}&leftTicketDTO.to_station={content[to_city]}&purpose_codes=ADULT'
headers = {'Cookie':'_uab_collina=170713029189605171055685; JSESSIONID=6B7CE180BD8BAA668113F761719EDEE4; BIGipServerpassport=988283146.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1557725450.24610.0000; _jc_save_toDate=2024-02-05; _jc_save_wfdc_flag=dc; speakVolume=100; readStatus=pointRead; batchReadIsOn=false; magnifierIsOn=false; readZoom=1; percentStatus=100; PointReadIsOn=false; fontZoom=1; speakFunctionIsOn=true; textModeStatus=off; speakSpeed=0; wzaIsOn=false; readScreen=false; _jc_save_fromStation=%u5357%u660C%2CNCG; _jc_save_toStation=%u798F%u5DDE%2CFZS; _jc_save_fromDate=2024-02-15',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'}

r = requests.get(url = url,headers = headers)# 发送请求，返回是否返回成功
#print(r.json()['data']['result'])# 获取字典型数据类型
page = 1
for i in r.json()['data']['result']:
    j = i.split('|')

    che_ci = j[3]
    start_time = j[8]
    arrive_time = j[9]
    speed_time = j[10]
    start_data = j[13]
    buiness_seat = j[32]
    first_seat = j[31]
    second_seat = j[30]

    table.add_row([page,che_ci,start_time,arrive_time,speed_time,start_data,buiness_seat,first_seat,second_seat])
    page += 1
print(table)
    #
    # break
    # x = 0
    # for n in j:
    #     print(n,'--->',x)
    #     x += 1

