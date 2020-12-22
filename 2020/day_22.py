import numpy as np

def points(deck):
	score = 0
	deck = deck[::-1]
	for i in range(len(deck)):
		score += (i+1)*deck[i]
	return score

def cardsToString(p1, p2):
	s1 = [str(c) for c in p1]
	s2 = [str(c) for c in p2]
	return '-'.join(s1)+'+'+'-'.join(s2)

def combat(p1, p2):
	while len(p1) > 0 and len(p2) > 0:
		card_p1 = p1.pop(0)
		card_p2 = p2.pop(0)
		if card_p1 > card_p2:
			p1.append(card_p1)
			p1.append(card_p2)
		else:
			p2.append(card_p2)
			p2.append(card_p1)
	return p1, p2

def recursiveCombat(p1, p2):
	seen = list()
	seen.append(cardsToString(p1, p2))
	while len(p1) > 0 and len(p2) > 0:
		card_p1 = p1.pop(0)
		card_p2 = p2.pop(0)
		if len(p1) >= card_p1 and len(p2) >= card_p2:
			p1_, p2_, forced = recursiveCombat(p1[:card_p1].copy(), p2[:card_p2].copy())
			if forced or len(p2_) == 0:
				p1.append(card_p1)
				p1.append(card_p2)
			else:
				p2.append(card_p2)
				p2.append(card_p1)
		elif card_p1 > card_p2:
			p1.append(card_p1)
			p1.append(card_p2)
		else:
			p2.append(card_p2)
			p2.append(card_p1)
		s = cardsToString(p1, p2)
		if s in seen:
			return p1, p2, True
		else:
			seen.append(s)
	return p1, p2, False

def task1(p1, p2):
	p1, p2 = combat(p1.copy(), p2.copy())
	if len(p1) == 0:
		score = points(p2)
	else:
		score = points(p1)
	return score

def task2(p1, p2):
	p1, p2, forced = recursiveCombat(p1.copy(), p2.copy())
	if forced or len(p2) == 0:
		score = points(p1)
	else:
		score = points(p2)
	return score

def main():
	p1 = list()
	p2 = list()
	with open("2020/day_22.in", "r") as f:
		first = True
		for l in f:
			if l == '\n':
				first = False
			elif l == "Player 1:\n" or l == "Player 2:\n":
				continue
			elif first:
				p1.append(int(l.split('\n')[0]))
			else:
				p2.append(int(l.split('\n')[0]))

	res1 = task1(p1.copy(), p2.copy())
	print("Task 1: %d" % res1)

	res2 = task2(p1.copy(), p2.copy())
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()