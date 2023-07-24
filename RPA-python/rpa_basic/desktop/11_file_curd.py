import os

# 파일 생성
# open('create_file.txt', 'a').close() # 빈 파일 생성

# 파일명 변경
# os.rename('create_file.txt', 'rename_file.txt')

# 파일 삭제
# os.remove('rename_file.txt')

# 폴더 생성
# os.mkdir('create_dir')

# 중첩 폴더 생성
# os.makedirs('dir/dir1/dir2/dir3')

# 폴더명 변경
# os.rename('create_dir', 'rename_dir')

# 폴더 삭제
# os.rmdir ('rename_dir') # 폴더안이 비어있을 경우 

import shutil # shell utilities 
# shutil.rmtree('dir') # 폴더안이 비어있지 않더라도, 모두 삭제 (rm -rf)

# 파일복사하기
# 1) 파일을 폴더 안으로 복사
# os.mkdir('copy')
# open('copy.txt', 'a').close()
# shutil.copy('copy.txt', 'copy')
# shutil.copy('copy.txt', 'copy/rename.txt') # 파일명을 변경하여 복사
# shutil.copyfile('copy.txt', 'copy/rename.txt') # 폴더명만 적으면 안되고, 파일 명까지 명시해야함
# copy, copyfile: 메타정보 복사 x, copy2: 메타정보까지 복사
# shutil.copy2('copy.txt', 'copy/copy2.txt') 

# 폴더 복사
# shutil.copytree('copy', 'copytree')

# 폴더 이동
# shutil.move('copytree', 'copy') # copytree 폴더를 copy 폴더로 이동
# shutil.move('copy.txt', 'copy')