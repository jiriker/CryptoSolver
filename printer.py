

def description():
	""" Print desctiption of this program and what id does"""


BOX_WIDTH = 160
SENTENCE_WIDTH = BOX_WIDTH - 10

def line(sentence):
	lenSe = len(sentence)  # lenght of sentence
	lenRe = BOX_WIDTH - lenSe -2   # length of remaining space, -2 for box sides
	
	#print(lenSe)
	#nl = 0
	if lenSe > SENTENCE_WIDTH:
		nl = int(lenSe/SENTENCE_WIDTH+0.5)
		for i in range(0,nl):
			line(sentence[i*SENTENCE_WIDTH: (SENTENCE_WIDTH+i*SENTENCE_WIDTH)])
		
	else:
	#print(nl)
	#sentence = sentence[ (SENTENCE_WIDTH+nl*SENTENCE_WIDTH): ]
	#divide if not even
		if sentence is not None:
			if lenRe%2 is not 0:
				lenLe = int(lenRe/2)
				lenRi = int(lenLe+1)
			else:
				lenLe, lenRi = int(lenRe/2), int(lenRe/2)
			print ("|"+lenRi*" "+sentence+lenLe*" "+"|")
	



def box(messagges):
	"""
	OK/FAIL
	----------------------------------------------------------------------------------------------------------------------------------------------------------------
	|
	"""
	

	print(160*"-")
	line("")
	for s in messagges:
		line(s)
		#print(s)
	line("")
	print(160*"-")
	





class Report:
	def __init__(self,name,cipheredText,key,decipheredText, lText="---"):
		self.report= [name,cipheredText,key,decipheredText,lText]
	def getReport(self):
		return self.report
		


