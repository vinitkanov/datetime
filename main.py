import datetime

def greet_user():
    name = input("What's your name? ")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Hey {name}, hope you're doing great! It's currently {current_time}.")

if __name__ == "__main__":
    greet_user()
