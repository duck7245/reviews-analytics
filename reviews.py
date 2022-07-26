data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0: # % 餘數
			print(len(data))

print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + Len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言長度小於100的一共有', len(new), '筆')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言提到good的一共有', len(good), '筆')
print(good[0])



# 清單快寫法 list comprehension
# output = [(number-1) for number in reference if number % 2 == 0]
#               運算        變數        清單         篩選條件
good = [d for d in data if 'good' in d]
# good = [d + '123' for d in data if 'good' in d]
# good = [1 for d in data if 'good' in d]
print(len(good))


bad = ['bad' in d for d in data]
print(bad)
# 等同於以下語法
# bad = []
# for d in data:
# 	bad.append('bad' in d)
# print(bad)

