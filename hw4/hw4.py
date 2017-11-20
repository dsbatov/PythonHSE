#вариант 3
with open("input.txt", encoding="utf-8") as f:
	cnt3 = 0
	cnt1 = 0
	checked = False
	for line in f:
		line = line.strip().split()
		for word in line:
			if checked and len(word) == 1:
				cnt1 += 1
			elif checked and len(word) == 3:
				cnt3 += 1
			elif not checked and len(word) == 2 and word.startswith("\ufeff"):
				cnt1 += 1
				checked = True
			elif not checked and len(word) == 4 and word.startswith("\ufeff"):
				cnt3 += 1
				checked = True
if cnt1 == 0:
	print("В тексте нет слов длины 1")
else:
	print(cnt3 / cnt1)