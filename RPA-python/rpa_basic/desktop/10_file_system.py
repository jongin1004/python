import os
# print(os.getcwd()) # 현재 작업 공간 (current working directory)
# os.chdir('rpa_basic')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# os.chdir('/Users/') # 절대경로
# print(os.getcwd())

# 파일 경로 (절대경로 생성)
# file_path = os.path.join(os.getcwd(), 'my_file.txt')

# 파일 경로에서 폴더 정보 가져오기 
# file_path = os.path.dirname('/Users/jongin/project/python/RPA-python/files/quiz.xlsx')

# 파일 정보 가져오기
import time
import datetime

filePath = '/Users/jongin/project/python/RPA-python/files/quiz.xlsx'
# 파일 생성 날짜 (사람이 알기 쉬운 포맷으로 바꿈)
ctime = os.path.getctime(filePath)
ctime = datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S')

# 파일 수정 날짜 
mtime = os.path.getmtime(filePath)
mtime = datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d %H:%M:%S')

# 파일 접근 날짜 
atime = os.path.getatime(filePath)
atime = datetime.datetime.fromtimestamp(atime).strftime('%Y%m%d %H:%M:%S')

# 파일 크기 
size = os.path.getsize(filePath) #바이트 단위로 가져옴

