#вариант 3
import collections

def read_text(filename):
	with open(filename, encoding='utf-8') as f:
		text = f.read()
	return text

def find_words(text):
	wordlist = []
	text.replace(',', '')
	text.replace('.', '')
	text.replace('-', '')
	text.replace('?', '')
	text.replace('!', '')
	text.replace(';', '')
	text.replace(':', '')
	text.replace('+', '')
	text.replace('=', '')
	text.replace('@', '')
	text.replace('#', '')
	text.replace('^', '')
	text.replace('*', '')
	text.replace('<', '')
	text.replace('>', '')
	text.replace('/', '')
	words = text.split()
	for word in words:
		if word.endswith('hood'):
			wordlist.append(word)
	return wordlist

def find_freq(wordlist):
	freq = {}
	for word in wordlist:
		if word in freq: 
			freq[word] += 1 / len(wordlist)
		else:
			freq[word] = 1 / len(wordlist)
	return freq

def min_freq(freq):
	values = list(freq.values())
	return min(values)

def print_stems(wordlist):
	for word in wordlist:
		if word[:-4].endswith('i'):
			print(word[:-5] + 'y')
		else:
			print(word[:-4])

text = read_text(input('Введите название файла: '))
wordlist = find_words(text)
if len(wordlist) != 0:
	freq = find_freq(wordlist)
	min_freq = min_freq(freq)

if len(wordlist) != 0:
	print(len(wordlist))
	print(min_freq)
	print_stems(wordlist)
else:
	print('В тексте нет существительных с суффиксом hood')