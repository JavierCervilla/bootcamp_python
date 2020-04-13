#!/usr/bin/env python3

def main():
	languages = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf'
	}
	for i in languages:
		str = "{} was created by {}".format(i, languages[i])
		print (str)
if __name__ == "__main__":
    main()
