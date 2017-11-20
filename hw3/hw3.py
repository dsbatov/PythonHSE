#вариант 3

word = input("Введите слово:")

word = list(word)

for i in range(len(word)):

	print(*(word[i:] + word[:i]), sep="")