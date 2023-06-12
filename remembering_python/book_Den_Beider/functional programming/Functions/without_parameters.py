# def без параметров
def hello():
    print("Hello")

hello()  # Hello

# local def
def welcome():
    def to_home():
        print("welcome to home")
    to_home()

welcome()  # welcome to home

# Greeting
def hello_and_welcome():
    hello()
    welcome()

# Hello
# welcome to home