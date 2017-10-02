word = input("Пожалуйста, введите слово:")
for i in range(len(word)-1, -1, -1):
	if word[i] != "з" and word[i] != "я" and word[i] != "З" and word[i] != "Я":
		print(word[i])	
