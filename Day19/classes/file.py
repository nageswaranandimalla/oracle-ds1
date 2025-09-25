class Sample:
    orgname="Oracle"
    def __init__(self, name):
        self.name=name
        print("This is Constructor ...  ",name)
        

    def view(self):
        print("This is from View  ...  ",self.name)

    def __del__(self):
        
        print("This is distructor")


#Object /Instance 
s1=Sample("Function")
s1.view()
s2=Sample("Method")
s2.view()
s3=Sample("subroute")
s2.view()