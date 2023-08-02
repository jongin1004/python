import zipfile
from config import *

def get_file_list(directory_path):
    # 디렉토리 내의 파일과 디렉토리 리스트 가져오기
    file_list = os.listdir(directory_path)
    
    # 파일 리스트만 필터링하여 반환
    files = [file for file in file_list if os.path.isfile(os.path.join(directory_path, file))]
    
    return files

def removeFileWithoutCsv():

    files = get_file_list(DOWNLOAD_PATH)

    for file in files:
        if not file.endswith('.csv'):
            os.remove(os.path.join(DOWNLOAD_PATH, file))

def unzip(fileName):
    zip_file_path = DOWNLOAD_PATH + fileName  # 압축 해제할 zip 파일 경로

    # zip 파일 압축 해제
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(DOWNLOAD_PATH)

# unzip('diff_20230731.zip')
removeFileWithoutCsv()