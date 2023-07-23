from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

# ws.insert_rows(8) # 8번째 줄에 줄 삽입
# ws.insert_rows(3, 3) # 3번째 줄에 3개의 row 삽입

ws.insert_cols(2, 3) # B번째 줄에 3줄의 col 삽입

wb.save('sample_modify.xlsx')
wb.close()
