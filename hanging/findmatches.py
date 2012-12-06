import sys
import re
import string

def makepattern(letters,excluded_letters=''):
	new_pattern = ''
	used_letters = set(letters).difference(set('?'))
	good_letters = set(string.ascii_lowercase).difference(set(excluded_letters)).difference(used_letters)
	for l in letters:
		if l == '?':
			new_pattern += '[' + ''.join(good_letters) + ']'
		else:
			new_pattern += l
	new_pattern += '$'
	print new_pattern
	return re.compile(new_pattern)


def testmatch(pattern,word):
	if pattern.match(word) is not None:
		return True
	else:
		return False

def main():
	f = file(sys.argv[1],'rU')
	if len(sys.argv) > 3:
		bad_letters = sys.argv[3]
	else:
		bad_letters = ''
	r = makepattern(sys.argv[2],bad_letters)
	for word in f.readlines():
		if testmatch(r,word.strip()):
			print word.strip()

if __name__ == '__main__':
	main()
