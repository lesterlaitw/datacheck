from pathlib import Path# 引入 pathlib 模組
my_file = Path('X:\IDC資產清單')#檔案或目錄路徑
if my_file.exists():# 檢查路徑是否存在
  print('檢查當前路經',my_file, '，正常！' )
else:
  print('路徑不存在，請檢查確認。', my_file)

#import glob#查詢特定檔案
#targetPattern = r"D:\*.txt"
#asd = glob.glob(targetPattern)
#print(asd)

import os
path = my_file              # 設定路徑
dirs = os.listdir(path)          # 獲取指定路徑下的檔案
rightdatalist = []
notrightdatalist = []
for i in dirs:               # 迴圈讀取路徑下的檔案並篩選輸出
	if os.path.splitext(i)[1] == '.xlsx':  # 篩選指定名稱的檔案
		rightdatalist.append(i)
		print(i)              # 輸出所有的csv檔案
	else :
		print('有非.bak的檔案，請到', my_file, '資料匣中檢查一下')
print('資料匣中總共有：', len(dirs), '個檔案。')
print('備份檔.bak共有：', len(rightdatalist), '個檔案。')
print('異常檔案共有：', len(dirs) - len(rightdatalist), '個檔案。')


#import time 
#for r in os.listdir(path): 
#	if r.endswith(".txt"): 
#		t=os.stat(r) 
#		print("建立時間?",time.localtime(t.st_ctime)) 

