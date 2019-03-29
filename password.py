num = 3 #總共的機會
while num > 0:
	password = input('press your password: ')
	if password == 'a123456': #判斷密碼是否正確
		print('Login Succeessful')
		break
	else:
		num = num - 1
		if num > 0:
			print('password incorrect. you have', num, 'chance')
		else:
			print("you don't have any chance")