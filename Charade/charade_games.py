import secrets
import random
import time
import charade_init as p

class movies:
    def __init__(self):
        self.init = p.initialize()

    def menu(self):
        print(f"""
        ********************************************************
        SELECT WHICH CHARADE YOU WANT
        1. Movies
        2. Action
        3. Exit this program
        ********************************************************
        """)

        self.userinput = input("Enter Your Choice >> ")

        return self.userinput


    def select(self,userinput):
        if userinput == '1':  
            self.display(self.init.movies)          

        elif userinput == '2':
            self.display(self.init.action)
    
    def display(self,data):
        print(
        f"""
        ********************************************************
                 Selected Movies is >>> {random.choice(data)}
        ********************************************************
        """)

        self.exit = input("Exit ? (Y/N) >> ")
        if self.exit == "y":
            print(" ")


if __name__ == "__main__":
    init = movies()
    while True:
        userinput = init.menu()
        init.select(userinput)