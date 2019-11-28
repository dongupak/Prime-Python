
 #코드 11-10 : 예외의 상속


class UndefinedVehicle(Exception):
    def __str__(self):
        return '정의되지 않은 탈것입니다'


vehicle = input('자전거, 오토바이, 자동차중 하나를 선택하시오: ')
try:
    if vehicle not in ['자전거', '오토바이', '자동차']:
        raise UndefinedVehicle
    
except UndefinedVehicle as e:
    print(e)
