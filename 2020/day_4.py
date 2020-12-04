import numpy as np
import re

def correct_fields(passport):
	byr = re.fullmatch("[0-9]{4}", passport["byr"])
	if byr is not None:
		byr = int(passport["byr"])
		if byr < 1920 or byr > 2002:
			return False
	else:
		return False

	iyr = re.fullmatch("[0-9]{4}", passport["iyr"])
	if iyr is not None:
		iyr = int(passport["iyr"])
		if iyr < 2010 or iyr > 2020:
			return False
	else:
		return False

	eyr = re.fullmatch("[0-9]{4}", passport["eyr"])
	if eyr is not None:
		eyr = int(passport["eyr"])
		if eyr < 2020 or eyr > 2030:
			return False
	else:
		return False

	hgt = re.fullmatch("[0-9]+((cm)|(in))", passport["hgt"])
	if hgt is not None:
		hgt = int(passport["hgt"][:-2])
		if passport["hgt"][-2:] == "cm":
			if hgt < 150 or hgt > 193:
				return False
		else:
			if hgt < 59 or hgt > 76:
				return False
	else:
		return False

	hcl = re.fullmatch("#[0-9a-f]{6}", passport["hcl"])
	if hcl is None:
		return False

	if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		return False

	pid = re.fullmatch("[0-9]{9}", passport["pid"])
	if pid is not None:
		pid = int(passport["pid"])
		if pid == 0:
			return False
	else:
		return False

	return True


def task1(arr):
	valid = 0
	required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	for passport in arr:
		v = True
		for key in required:
			if key not in passport.keys():
				v = False
				break
		if v:
			valid += 1
	return valid

def task2(arr):
	valid = 0
	required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	for passport in arr:
		v = True
		for key in required:
			if key not in passport.keys():
				v = False
				break
		if v:
			v = correct_fields(passport)
		if v:
			valid += 1
	return valid

def main():
	lst = list()
	with open("2020/day_4.in") as f:
		d = dict()
		for l in f:
			if l == '\n':
				lst.append(d)
				d = dict()
			else:
				fields = l.split(' ')
				for field in fields:
					entry = field.split(':')
					d[entry[0]] = entry[1].split('\n')[0]
		lst.append(d)

	arr = np.array(lst)

	res1 = task1(arr)
	print("Task 1: %d" % res1)

	res2 = task2(arr)
	print("Task 2: %d" % res2)

if __name__ == "__main__":
	main()