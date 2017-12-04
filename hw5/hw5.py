#вариант 3
with open('output.txt', 'a', encoding='utf-8') as f:
	word = 'Надо же с чего-то начать'
	cnt = 1
	while word != '':
		word = input('Введите слово(если хотите закончить, введите пустое слово):')
		f.write(word[cnt:]+"\n")
		cnt += 1