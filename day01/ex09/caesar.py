import sys

def	do_cypher(alphabet, alphabet_index, string, num):
	def	transform_number(char):
		if char not in alphabet:
			return char
		index_in_abc = (alphabet_index[char.lower()] + num) % len(alphabet)
		if char.upper() == char:
			return alphabet[index_in_abc].upper()
		return alphabet[index_in_abc]

	return "".join( [transform_number(i) for i in string] )

def	caesar_cypher(string : str, num : int) -> str:
	alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
	# is_lower = "".join(["1" if i.lower() != i else "0" for i in string])
	num = (num % len(alphabet) + len(alphabet)) % len(alphabet)
	alphabet_index = dict( zip(alphabet, range(0, len(alphabet))) )
	return do_cypher(alphabet, alphabet_index, string, num)

def main():
	if len(sys.argv) != 4:
		raise Exception("invalid arguments number")
	if not all(ord(i) < 128 for i in sys.argv[2]):
		raise Exception("invalid string")
	if sys.argv[1] == "encode":
		print(caesar_cypher(sys.argv[2], int(sys.argv[3])))
	elif sys.argv[1] == "decode":
		print(caesar_cypher(sys.argv[2], -int(sys.argv[3])))

if __name__ == "__main__":
	main()
