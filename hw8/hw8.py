import random

def make_dict(filename):
	dic = {}
	with open(filename, encoding = 'utf-8') as f:
		for line in f:
			line = line.strip()
			sp_line = line.split(';')
			dic[sp_line[0]] = sp_line[1]
	return dic

dic = make_dict('hw8.csv')
words = list(dic.keys())
word = random.choice(words)
attempts = len(dic[word])
while attempts > 0:	
	print('Подсказка: ' + word + ' ..., попыток осталось: ' + str(attempts))
	att = input('Введите ответ: ')
	if att == dic[word]:
		print('Верно!')
		break
	else:
		print('Неверно. Попыток осталось: ' + str(attempts - 1))
		attempts -= 1
		if attempts == 0:
			print('К сожалению, вы не угадали. Правильный ответ: ' + dic[word] + '. Спасибо за игру!')