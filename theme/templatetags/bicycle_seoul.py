import requests

url = "http://openapi.seoul.go.kr:8088/515261424a696d743732716e434c62/json/bikeList/1/1000/"
res = requests.get(url)
data = res.json()
# print(data)
RealTime = data['rentBikeStatus']['row']
# print(RealTime)
for i in RealTime:
    print(i['stationName'])
    print('거치대개수:', i['rackTotCnt'],'개,', '자전거주차총건수:', i['parkingBikeTotCnt'], '개,', '거치율:', i['shared'], '%')
    print("위도: ", i['stationLatitude'] , ',', "경도: ", i['stationLongitude'])
    print()
