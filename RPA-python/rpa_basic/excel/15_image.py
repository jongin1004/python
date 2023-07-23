import datetime
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image('img.png')
ws.add_image(img, 'C2')

wb.save('sample_modify.xlsx')
wb.close()