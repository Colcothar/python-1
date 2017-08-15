inFile = open('sample2.txt', 'r')
content = inFile.read()
inFile.close()

#overitting or create a new file
#outFile = open('sample.txt','w')
#outFile.write('merging content from another file\n')
#outFile.write(content)
#outFile.close()

#appends content to the existing file
with open('sample.txt','a') as myfile:
	myfile.write(content)
