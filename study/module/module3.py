# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_mornig(4)
# theater_module.price_soldier(5)

# import theater_module as mv  # theater_module가 이름이 너무 기니까 mv라고 지정해주는 것
# mv.price(3)
# mv.price_mornig(4)
# mv.price_soldier(5)

# # theater_module을 붙히지 않고 그 안에 모든 라이브러리를 사용하겠다.
# from theater_module import *
# price(3)
# price_mornig(4)
# price_soldier(5)

# #원하는 함수만 쓰도록 지정해줄 수 있다.
# from theater_module import price, price_mornig
# price(3)
# price_mornig(4)
# # price_soldier(5)

# 가져올 함수를 또 as로 이름을 지정해줄 수 도 있다.
from theater_module import price_soldier as price
price(3)  # 여기서 prcie 는 theater_module에 있는 price가 아닌 price_soldier다
