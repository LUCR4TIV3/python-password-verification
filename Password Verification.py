import random
import time
attempts = 1
count = 0
secs = 10
n = 0
pass1 = "flash11"
pass2 = "spiderman10"
pass3 = "batman7"
passarr = [pass1, pass2, pass3]
actkey = random.choice(passarr)
password = input("What is your password?")


if password == actkey:
    print("Welcome")
else:
    while password != actkey:
        count = count + 1
        print("Incorrect!")
        print("You have", attempts, "more attempts to get it right")
        attempts = attempts - 1
        if count > 1:
            print("You have got your password wrong too many times.")
            print("You are locked out of the system for", secs + n, "seconds.")
            count = 1
            attempts = 0
            time.sleep(secs + n)

            n = n + 10
            password = input("What is your password?")

        else:
            password = input("What is your password?")

    else:
        print("welcome")
