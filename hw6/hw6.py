import random

def imperative(filename):
	with open(filename, encoding ='utf-8') as f:
		imperatives = f.read()
		imperatives = imperatives.split()
	random_imperative = random.choice(imperatives)
	return random_imperative

def noun_nom(filename):
	with open(filename, encoding ='utf-8') as f:
		nouns_nom = f.read()
		nouns_nom = nouns_nom.split()
	random_noun_nom = random.choice(nouns_nom)
	return random_noun_nom

def noun_acc(filename):
	with open(filename, encoding ='utf-8') as f:
		nouns_acc = f.read()
		nouns_acc = nouns_acc.split()
	random_noun_acc = random.choice(nouns_acc)
	return random_noun_acc

def name(filename):
	with open(filename, encoding ='utf-8') as f:
		names = f.read()
		names = names.split()
	random_name = random.choice(names)
	return random_name

def indicative(filename):
	with open(filename, encoding ='utf-8') as f:
		indicatives = f.read()
		indicatives = indicatives.split()
	random_indicative = random.choice(indicatives)
	return random_indicative

def affirmative_sent():
	type_aff = random.choice([0, 1])
	if type_aff == 0:
		sent = name('names.txt') + ' ' + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt')
	else:
		sent = noun_nom('nouns_nom.txt') + ' ' + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt')
	return sent.capitalize()

def neg_for_cond():
	neg = random.choice([0, 1])
	if neg == 0:
		return 'не ' 
	else:
		return ''

def aff_for_cond_sent():
	type_aff = random.choice([0, 1])
	if type_aff == 0:
		sent = name('names.txt') + ' ' + neg_for_cond() + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt')
	else:
		sent = noun_nom('nouns_nom.txt') + ' ' + neg_for_cond() + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt')
	return sent

def interrogative_sent():
	type_int = random.choice([0, 1])
	if type_int == 0:
		sent = name('names.txt') + ' ' + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt') + '?'
	else:
		sent = noun_nom('nouns_nom.txt') + ' ' + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt') + '?'
	return sent.capitalize()

def negative_sent():
	type_neg = random.choice([0, 1])
	if type_neg == 0:
		sent = name('names.txt') + ' ' + 'не' + ' ' + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt')
	else:
		sent = noun_nom('nouns_nom.txt') + ' ' + 'не' + ' ' + indicative('indicatives.txt') + ' ' + noun_acc('nouns_acc.txt')
	return sent.capitalize()

def imperative_sent():
	type_imp = random.choice([0, 1])
	if type_imp == 0:
		sent = name('names.txt') + ',' + ' ' + imperative('imperatives.txt') + ' ' + noun_acc('nouns_acc.txt') + '!'
	else:
		sent = noun_nom('nouns_nom.txt') + ',' + ' ' + imperative('imperatives.txt') + ' ' + noun_acc('nouns_acc.txt') + '!'
	return sent.capitalize()

def conditional_sent():
	sent = 'Если' + ' ' + aff_for_cond_sent() + ',' + ' ' + 'то' + ' ' + aff_for_cond_sent()
	return sent

def make_text():
	select = [1, 2, 3, 4, 5]
	random.shuffle(select)
	for i in range(len(select)):
		if select[i] == 1:
			print(affirmative_sent() + '.' + '\n')
		elif select[i] == 2:
			print(interrogative_sent() + '\n')
		elif select[i] == 3:
			print(negative_sent() + '.' + '\n')
		elif select[i] == 4:
			print(imperative_sent() + '\n')
		else:
			print(conditional_sent() + '.' + '\n')

make_text()