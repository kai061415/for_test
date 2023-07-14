# 讀取reviews.txt留言檔
# 測試印出data清單
# 只印出第一筆資料
# 印出讀取檔案的進度(每1000筆印一次)
# 計算留言平均長度
# 篩選出留言小於100字的有幾筆
# 篩選出留言裡有提到good的單字有幾筆

data = []
count = 0
count_line = 0  
count_length = 0
count_good = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data)) 
		count_line = count_line + len(line)
		if len(line) < 100:
			count_length = count_length + 1
		if 'good' in line:
			count_good = count_good + 1	
	print(data[0])	
	print(count_line/len(data))	
	print(count_length)
	print(count_good)

		
