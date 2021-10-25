
def name():
    str = input("Enter your file name: ")
    f= open(str)
    words = 0
    characterCount = 0
    for i in f:
        r = i.split()
        words = words+len(r)
    for count in str:
       characterCount = characterCount+1
    print(words)    
    print(characterCount)

name()    