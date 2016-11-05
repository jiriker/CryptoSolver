

"""
there is an encode decode interface, basically a super class crypto. 
Then there are subclasses for all different used ciphers
There there is a function in each subclass that return informations about 
For every decode solution run a tokenize
then try to find english words in tokenized sentence
if there is a good match, offer that as solution 


"""

"""
all cipher do inherit from super class cipher, that is were you want to start
ceaser cipher is commented in order to show how cipher.solve should work

"""
import solver
# TODO: in the end there will be one big scheduler that will take all the cipher classes and mix them in possible uses and test sentence as long as it did not find solution 



def loadTask():
	global sentences
	sentences = open("twoTabOut.txt").read().splitlines()
	
	while '' in sentences:
		sentences.remove('')





def main():

	# load sentences that you want to decrypt
	loadTask()

	solv = solver.Solver()
	solv.solve(sentences)


	
if __name__ == "__main__":
    
    main()
   