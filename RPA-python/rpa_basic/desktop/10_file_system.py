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

# 파일 목록 가져오기
# print(os.listdir()) # 현재 작업공간의 모든 폴더, 파일목록 가져오기
# print(os.listdir('rpa_basic')) # 해당 경로 밑에 있는 디렉도리 정보 가져오기

# 파일 목록 가져오기 (하위 폴더/파일 모두 포함)
result = os.walk('rpa_basic') # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기 

# root: 디렉토리 경로, dirs: 디렉토리 리스트, files: 파일 리스트
# for root, dirs, files in result:
#     print(root, dirs, files)

# 폴더 내에서 특정 파일들을 찾으려면?
name = '10_file_system.py'
result = []
for root, dirs, files in os.walk(os.getcwd()):
    if name in files:
        result.append(os.path.join(root, name))

# *.xlsx, *.txt 등 특정 포멧이나 정규식등을 사용하여 파일을 찾는 경우 
import fnmatch # 파일이름 일치하는지 체크

pattern = '*.xlsx' 
result  = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if fnmatch.fnmatch(file, pattern): # file이 pattern에 일치하면 
            result.append(os.path.join(root, file))

# 주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir('rpa_basic'))
# print(os.path.isfile('rpa_basic'))

# print(os.path.isdir('mylogfile_230723220700.log'))
# print(os.path.isfile('mylogfile_230723220700.log'))

# 주어진 경로가 존재하는지 확인
# path = 'rpa_basic'
# if os.path.exists(path):
#     print(f'[{path}]는 존재함')
# else :
#     print(f'[{path}]는 존재하지 않음')

# print(result)

