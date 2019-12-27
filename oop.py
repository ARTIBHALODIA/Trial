class PublicClass:
    def __init__(self, name):
        self.name = name
    
    def PrintPublic(self):
       print (self.name)

a=PublicClass("public")
a.PrintPublic()


