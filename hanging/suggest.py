import sys

def testword(letters,word):
	if len(letters) < len(word):
		return False
	else:
		n_letters = letters[:]
		w_letters = [w for w in word]
		for w in w_letters:
			try:
				n_letters.remove(w)
			except Exception, ex:
				return False 
		return True


def main():
	letters = [l for l in sys.argv[2]]
	print letters
	f = file(sys.argv[1],'rU')
	for w in f.readlines():
		#print w.strip()
		if testword(letters,w.strip()):
			print w.strip()

if __name__ == '__main__':
	main()


