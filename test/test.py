#вариант 2
print('Задание №1:')
with open ('Ozhegov.txt', encoding = 'utf-8') as f:
	for line in f:
		splited_line = line.split('|')
		if len(splited_line[0]) >= 20:
			print(line)
print('Задание №2:')
cnt = 0
with open ('Ozhegov.txt', encoding = 'utf-8') as f:
	for line in f:
		splited_line = line.split('|')
		if len(splited_line[2]) > 0:
			cnt += 1
	print(cnt)
print('Задание №3:')
with open ('Ozhegov.txt', encoding = 'utf-8') as f:
	list_of_words = []
	list_of_vocabulary = []
	list_of_definitions = []
	word = input('Введите слово(если хотите закончить, введите пустое слово):')
	while len(word) != 0:
		list_of_words.append(word)
		word = input('Введите слово(если хотите закончить, введите пустое слово):')
	for line in f:
		splited_line = line.split('|')
		list_of_vocabulary.append(splited_line[0])
		list_of_definitions.append(splited_line[1] + " — " + splited_line[3])
	for i in range(len(list_of_words)):
		if list_of_words[i] in list_of_vocabulary:
			ind = list_of_vocabulary.index(list_of_words[i])
			print(list_of_vocabulary[ind] + " — " + list_of_definitions[ind])
		else:
			print('Слово не обнаружено' + "\n")