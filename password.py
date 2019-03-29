num = 3
while num > 0:
	password = input('press your password: ')
	if password == 'a123456':
		print('Login Succeessful')
		break
	else:
		num = num - 1
		if num > 0:
			print('password incorrect. you have', num, 'chance')