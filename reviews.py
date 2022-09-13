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





# 文字計數
wc = {}
for d in data:
	words = d.split(' ') # split() 的預設值是空白鍵，但不會切出空白字元
	for word in words:
		if word in wc: # if word not in wc
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key進wc字典

count = 1
for word in wc:
	if wc[word] > 1000000:
		print(count, word, ':', wc[word])
		count += 1

while True:
	word = input('請問你想找什麼字?')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word],'次')
	else:
		print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')


print(wc['Neo'])

# print(len(wc))
# print(wc)
# print(wc['they'])
