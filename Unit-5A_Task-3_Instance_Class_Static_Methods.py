class Demo:
    college = "NRIU"  

    def show_name(self, name):  
        self.name = name
        print("Instance:", self.name)

    @classmethod
    def show_college(cls):
        print("Class:", cls.college)

    @staticmethod
    def info():
        print("Static: utility message")

obj = Demo()
obj.show_name("Anu")
Demo.show_college()
Demo.info()