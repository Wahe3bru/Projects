#Count Words in a String - Counts the number of individual words in a
#string. For added complexity read these strings in from a text file and
#generate a summary.

stringy = "sdrawkcab dootsrednu dna sdrawrof devil eb ylno nac efil"
words = stringy.split(" ")
print(len(words))

#need to learn how to open file and count words
textDoc = open("countWords.txt", "r")
textW = textDoc.read()
words2 = textW.split(" ")
print(words2)
print(len(words2))
