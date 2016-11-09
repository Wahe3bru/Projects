#Pig Latin is a game of alterations played on the English language game.
#To create the Pig Latin form of an English word the initial consonant sound
#is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay)

word = input('What is your word? ')
if word[0] not in  ["a","e","i","o","u"]:
    word = word[1:] + "-" + word[0] +"ay"
    print(word)
else:
    print(word)
