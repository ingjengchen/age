driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有唷')
	raise SystemExit

age = input('請問你的年齡?: ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恩恩 可以開車')
	else:
		print('奇怪 你怎麼可以開車?!')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照唷')
	else:
		print('等你滿18歲就可以考囉')
