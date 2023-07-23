from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

# ws.delete_rows(7) # 7번째 row 삭제
ws.delete_rows(7, 3) # 7번째 줄 부터 3개의 row 삭제

# ws.delete_cols(2) # B열 삭제
ws.delete_cols(2, 2) # B열로 부터 2개의 cols 삭제

wb.save('sample_modify.xlsx')
wb.close()
