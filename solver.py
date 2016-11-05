#import super class 
import cipher
# import all cipher classses
import ceaser
import affine
import monoWithKey
import vigener
import completeTable
import completeTableWithKey

# import printer for box printing
import printer

import pipe


# add all ciphers to the solver
ciphers=	[#ceaser.Ceaser()   #,
			 #affine.Affine() #,
			 #pipe.Pipe(ceaser.Ceaser(), affine.Affine()),
			 monoWithKey.MonoWithKey(),
			 #vigener.Vigener(),
			# completeTable.CompleteTable()  #,
			 #pipe.Pipe(completeTable.CompleteTable(),completeTable.CompleteTable())
			# pipe.Pipe(ceaser.Ceaser(),completeTable.CompleteTable()),
			 #pipe.Pipe(affine.Affine(),completeTable.CompleteTable())
			 #affine.Affine()
			 #pipe.Pipe(ceaser.Ceaser(),pipe.Pipe(completeTable.CompleteTable(),completeTable.CompleteTable()))  #,
			# pipe.Pipe(affine.Affine(),pipe.Pipe(completeTable.CompleteTable(),completeTable.CompleteTable()))  #,
			 #completeTableWithKey.CompleteTableWithKey()
			 ]




class Solver:
	def __init__(self):
		self.lCiphers= ciphers



	def printNewTest(self,i,sentence):
		print("\n\n")
		printer.box(["DECODING SENTENCE NUMBER "+str(i),"","CT: "+sentence])
		



	def solve(self,sentences):
		
		for i in range(0,len(sentences)):
			self.printNewTest(i,sentences[i])
			for j in range(0,len(self.lCiphers)):
				
				self.lCiphers[j].solve(sentences[i])

	