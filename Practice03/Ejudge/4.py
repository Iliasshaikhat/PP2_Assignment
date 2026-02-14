class StringHandler :
    def getString(self):
        self.name = input()
        
    def printString(self):
        print(self.name.upper())
        
obj = StringHandler()
obj.getString()
obj.printString()