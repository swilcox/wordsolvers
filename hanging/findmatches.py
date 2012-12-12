import sys
import re
import string
import operator


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
	return re.compile(new_pattern)


def testmatch(pattern,word):
	if pattern.match(word) is not None:
		return True
	else:
		return False

def main():
	counts = dict([(l, 0) for l in string.ascii_lowercase])	
	f = file(sys.argv[1],'rU')
	if len(sys.argv) > 3:
		bad_letters = sys.argv[3]
	else:
		bad_letters = ''
	r = makepattern(sys.argv[2],bad_letters)
	for word in f.readlines():
		if testmatch(r,word.strip()):
			print word.strip()
			for l in word.strip():
				counts[l] += 1
	
	for l,c in sorted(counts.iteritems(), key=operator.itemgetter(1),reverse=True):	
		if l not in sys.argv[2] and c > 0:
			print l + ': ' + str(c)

if __name__ == '__main__':
	main()
