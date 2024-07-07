def hex_to_binary(hex_code):
	bin_code = bin(hex_code)[2:]
	padding = (4-len(bin_code)%4)%4
	return "0"*padding + bin_code

def task1(bseq):
	...

if __name__ == "__main__":
	with open("2021/day_16.in", "r") as f:
		BITS = f.readline().split("\n")[0]
	bseq = hex_to_binary(int("0x"+BITS, base=16))