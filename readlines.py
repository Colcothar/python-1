import sys

def read_in():
	lines = sys.stdin.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].replace(' ',' - ')
	return lines

def main():
	lines = read_in()
	print (lines)

if __name__ == '__main__':
	main()
