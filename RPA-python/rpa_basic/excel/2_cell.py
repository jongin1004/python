from openpyxl import Workbook
wb = Workbook() # 워크북 생성

ws = wb.active # 현재 활성화된 sheet 획득
ws.title = 'jonginSheet' # sheet이름 변경

wb.save('sample.xlsx') # 파일 저장
wb.close() # 파일 종료 
