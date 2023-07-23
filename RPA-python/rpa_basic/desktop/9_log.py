import pyautogui
import logging
from datetime import datetime

# level: 해당 레벨을 포함한 상위의 에러만 출력함
# logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s [%(levelname)s] %(message)s") 

# debug < info < warning < error < critical
# logging.debug('문제 발생')
# logging.info('자동화 수행 준비')
# logging.warning('스크립트의 호환성의 문제성이 존재합니다.')
# logging.error('[code: 999] 에러발생')
# logging.critical('심각한 문제 발생')

# 터미널과 파일에 함께 로그 남기기 
# 시간 [로그레벨] 메세지 형태로 로그 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 

logger = logging.getLogger()
# 로그레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)에 로그 
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일에 로그
filename = datetime.now().strftime('mylogfile_%y%m%d%H%M%S.log')
fileHandler = logging.FileHandler(filename, encoding='utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logging.debug('문제 발생')
logging.info('자동화 수행 준비')
logging.warning('스크립트의 호환성의 문제성이 존재합니다.')
logging.error('[code: 999] 에러발생')
logging.critical('심각한 문제 발생')
