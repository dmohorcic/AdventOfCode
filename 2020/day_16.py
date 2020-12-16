import numpy as np

def prepareRules(rules):
	r = list()
	for val in rules.values():
		rang = val["low"].split('-')
		r.append(np.array([int(rang[0]), int(rang[1])]))
		rang = val["high"].split('-')
		r.append(np.array([int(rang[0]), int(rang[1])]))
	return r

def isValid(ticket, rules):
	error = None
	for x in ticket:
		legal = False
		for rule in rules:
			if x >= rule[0] and x <= rule[1]:
				legal = True
				break
		if not legal:
			if error == None:
				error = x
			else:
				error += x
	if error == None:
		return True, 0
	else:
		return False, error

def task1(rules, tickets):
	rRules = prepareRules(rules)
	error = 0
	for ticket in tickets:
		valid, e = isValid(ticket, rRules)
		if not valid:
			error += e
	return error

def task2(rules, my, tickets):
	rRules = prepareRules(rules)
	valid_tickets = list()
	for ticket in tickets:
		valid, e = isValid(ticket, rRules)
		if valid:
			valid_tickets.append(ticket)
	valid_tickets = np.array(valid_tickets)

	column_keys = list()
	for i in range(len(valid_tickets[0])):
		col = valid_tickets[:, i]
		possible_rules = list()
		for key, val in rules.items():
			accept_rule = True
			rng_low = [int(x) for x in val["low"].split("-")]
			rng_high = [int(x) for x in val["high"].split("-")]
			for x in col:
				if (x < rng_low[0] or x > rng_low[1]) and (x < rng_high[0] or x > rng_high[1]):
					accept_rule = False
					break
			if accept_rule:
				possible_rules.append(key)
		column_keys.append(possible_rules)

	i = 0
	visited_idx = list()
	while True:
		if len(column_keys[i]) == 1 and i not in visited_idx:
			rule = column_keys[i][0]
			for j in range(len(column_keys)):
				if i == j:
					continue
				try:
					column_keys[j].remove(rule)
				except:
					pass
			visited_idx.append(i)
			i = 0
		else:
			i += 1
		if i == len(column_keys):
			break

	s = 1
	for i in range(len(column_keys)):
		if "departure" in column_keys[i][0]:
			s = int(s) * int(my[i])
	return s

def main():
	rules = dict()
	my = list()
	tickets = list()
	with open("2020/day_16.in", "r") as f:
		r = True
		m = False
		title = 0
		tmp = list()
		for l in f:
			if r:
				if l == '\n':
					r = False
					m = True
				else:
					args = l.split('\n')[0].split(": ")
					d = dict()
					d["low"] = args[1].split(" or ")[0]
					d["high"] = args[1].split(" or ")[1]
					rules[args[0]] = d
			elif m:
				if l == '\n':
					m = False
				else:
					if title == 0:
						title += 1
					else:
						my = np.array([int(x) for x in l.split('\n')[0].split(',')])
			else:
				if title == 1:
					title += 1
				else:
					tmp.append(np.array([int(x) for x in l.split('\n')[0].split(',')]))
		tickets = np.array(tmp)
	
	res1 = task1(rules, tickets)
	print("Task 1: %d" % res1)

	res2 = task2(rules, my, tickets)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()