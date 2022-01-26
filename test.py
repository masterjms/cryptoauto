from os import access
import pyupbit

access = "1r8rKX4hWTyNcDKU80vc6GIlirzXF9pVLvNxKkiD"          # 본인 값으로 변경
secret = "o7D9ZXBtqtBHw5Sz6MCk8TwsooK0fXrERjuCwvFe"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회