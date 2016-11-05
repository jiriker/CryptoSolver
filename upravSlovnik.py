def createAlphabetDictionary():
	""" create dictionaries for easy char to integer handling """
	global alphabet, LS,lsi,ctoi,itoc, numbers
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	LS = list(enumerate(alphabet))
	lsi = [(item,index) for index,item in LS]
	ctoi = dict(lsi)
	itoc = dict(LS)
	#print(alphabet,"\n")
	#print(LS,"\n")
	#print(lsi,"\n")
	#print(ctoi,"\n")  # char to integer, use as ctoi[char]
	#print(itoc,"\n")  # integer to char, use as itoc[integer]

def deleteSpecialCharacters(sentence):
		""" checks if there are only characters from eng alphabet in sentence, if there 
		is a differencet character, delete it"""
		l_not_char=[]
		for i in range(0,len(sentence)):
			
			if sentence[i]  not in alphabet:
				l_not_char.append(sentence[i])

		for i in range(0,len(l_not_char)):
			if l_not_char[i] in sentence:
				sentence = sentence.replace(l_not_char[i],"")

		## TODO NAHRAD DIAKRITIKU 
		return sentence

def loadTask():
	global sentences
	sentences = open("slovnik.txt",encoding='windows-1250').read().splitlines()
	f  = open("sl.txt",'w',encoding='windows-1250')
	
	for s in sentences:
		#sentences.remove('')
		se=deleteSpecialCharacters(s.upper())
		print(se)
		se = se.replace("\t", "")
		f.write(se+"\n")
	f.close

createAlphabetDictionary()
loadTask()