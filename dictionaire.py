def lang():
	spanish = dict()
	spanish['yes'] = 'si'
	spanish['hello'] = 'hola'
	spanish['one'] = 'uno'
	spanish['two'] = 'dos'
	spanish['three'] = 'tres'
	spanish['red'] = 'rojo'
	spanish['black'] = 'negro'
	spanish['green'] = 'verde'
	spanish['blue'] = 'azul'
	return spanish

def main():
	dictionary = lang()
	print(dictionary['two'])
	print(dictionary['red'])

	# Other method, using string format
	numberFormat = 'Count in Spanish: {one}, {two}, {three}, ...'
	withSubstitutions = numberFormat.format(one='uno', two='dos', three='tres')
	print(withSubstitutions)

	#Another method using keyword paramether
	numberKeyword = "{black} is the new {blue}"
	withKeyword = numberKeyword.format(**dictionary)
	print(withKeyword)

	#test splat (*)
	val1, *val2 = dictionary
	print(dictionary)
	print(val1)
	print(val2)

if __name__ == '__main__':
	main()
