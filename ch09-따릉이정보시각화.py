import requests
import json
api_key='725752507a6b776f3732706d4f6141'
start_num =1

end_num =5
url = f'http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{start_num}/{end_num}/'

data = requests.get(url)
#print(data.text)
result = json.loads(data.text)
#print(json.dumps(result, indent=4, ensure_ascii=False))

# for row in result['rentBikeStatus']['row']:
#     print(f"대여소 이름: {row['stationName']}")
#     print(f"현재 주차 대수: {row['parkingBikeTotCnt']}")
#     print(f"거치율: {row['shared']}")
#     print(f"위도/경도 좌푯값: {row['stationLatitude']} / {row['stationLongitude']}")

#     print('-'*100)

# num = 0
# while True:
#     start_num = 1 + 1000 * num
#     end_num = 1000 + 1000*num

#     url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{start_num}/{end_num}/"

#     data = requests.get(url)

#     data_dict = json.loads(data.text)

#     if 'MESSAGE' in data_dict.keys():
#         if data_dict['MESSAGE'] == '해당하는 데이터가 없습니다.':
#             break 

#     for row in data_dict['rentBikeStatus']['row']:
#         print(f"대여소 이름 : {row['stationName']}")
#         print(f"현재 주차 대수 : {row['parkingBikeTotCnt']}")
#         print(f"거치율 : {row['shared']} %")
#         print(f"위도/경도 좌푯값 : {row['stationLatitude']}/{row['stationLongitude']} %")

#         print('-'*100)
    
#     num += 1

import pandas as pd
import pydeck as pdk
    

bike_dict = { 'rackTotCnt' : [] , 'stationName' : [] , 'parkingBikeTotCnt' : [] , 'shared' : [] , 'latitude' :[] , 'longitude' : []}
num = 0
while True :

    start_num = 1 + 1000 * num
    end_num = 1000 + 1000*num

    url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{start_num}/{end_num}/"

    data = requests.get(url)

    data_dict = json.loads(data.text)

    if 'MESSAGE' in data_dict.keys():
        if data_dict['MESSAGE'] == '해당하는 데이터가 없습니다.':
            break 

    for row in data_dict['rentBikeStatus']['row']:
        bike_dict['rackTotCnt'].append(int(row['rackTotCnt']))
        bike_dict['stationName'].append(row['stationName'])
        bike_dict['parkingBikeTotCnt'].append(int(row['parkingBikeTotCnt']))
        bike_dict['shared'].append(int(row['shared']))
        bike_dict['latitude'].append(float(row['stationLatitude']))
        bike_dict['longitude'].append(float(row['stationLongitude']))

    num+=1

df = pd.DataFrame(bike_dict)

print(df.to_string())

import os
import platform
import webbrowser

layer = pdk.Layer('ScatterplotLayer' , df ,get_position = ['longitude' , 'latitude'] , get_fill_color = ['255-shared','255-shared','255'] , get_radius='(60 * parkingBikeTotCnt ) / 10' , pickable = True)

lat_center = df['latitude'].mean()
lon_center = df['longitude'].mean()

initial_view = pdk.ViewState(latitude=lat_center , longitude=lon_center , zoom=10)
map = pdk.Deck(layers=[layer] , initial_view_state=initial_view , tooltip={'text' : "대여소 : {stationName}\n 현재 주차 대수 : {parkingBikeTotCnt}"})

map.to_html("./seoul_bike.html")

ap = os.path.abspath('./seoul_bike.html')

if platform.system() == 'Windows':
    webbrowser.open('file:///' + ap.replace('\\','/'))
