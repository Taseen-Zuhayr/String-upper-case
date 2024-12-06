class ioword:
    # Contructor
    def __init__(self):
        self.word = " "
    # Method 1
    def getword(self):
        self.word = input("Enter Word : ")
    # Method 2
    def display(self):
        print("The upper case value is : ",self.word.upper())
    
word=ioword()
word.getword()
word.display()


