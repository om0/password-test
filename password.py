password = 'a123456'
i = 3 #剩餘次數
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登入成功')
		break
	elif i > 0:
		print('密碼錯誤！ 還有', i, '次機會')
	else:
		print('密碼輸入超過次數! bye!')