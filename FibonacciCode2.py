from flask import Flask
app = Flask(__name__)

@app.route('/')
def fibonacci(n):
    a,b=0,1
    while(a<=n):
        print(a,end=' ')
        a,b=b,a+b
    print()
fibo_entry = int(input("Please enter a positive number: "))
if fibo_entry < 0: 
        print("Incorrect input, please input a positive number and try again!")
fibonacci(fibo_entry)