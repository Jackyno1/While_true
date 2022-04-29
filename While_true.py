#重複輸入名字, 輸入q則離開
while True:
	name = input('請問你的名字:')
	if name == 'q':
		print('再見')
		break
	else:
		print(name, '你好!')
