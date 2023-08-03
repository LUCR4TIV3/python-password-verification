'''
A python program that asks the user for a password and then checks if it is correct.
'''


# TODO: make sure the sleep is working as expected
# TODO: add a hint to the user

# Importing the required modules
import random
import time
import os
import pyfiglet
from dotenv import load_dotenv
from termcolor import colored

load_dotenv()

# load variables
max_attempts = int(os.getenv('MAX_ATTEMPTS'))
passwords = os.getenv('PASSWORDS').split(',')
count = 0 # 
secs = 10
n = 0
input_received = None


def print_huge_ascii(title, font='slant'):
  ascii_art = pyfiglet.figlet_format(title, font=font)
  colored_ascii_art = colored(ascii_art, 'green')
  print(colored_ascii_art)

def prompt_user_for_password():
  while password is None:
    return input("What is your password?\n> ")
  
def display_hint(password):
  print("The password is %s characters long" % len(password))

if __name__ == "__main__":
  print_huge_ascii("Password Verification")

  act_key = random.choice(passwords) 
  password = prompt_user_for_password()
  if password == act_key: print("Welcome Back!")
  else:
    while password != act_key:
      count += 1
      print(colored("Incorrect!", 'red'))
      print("You have %s more attempts to get it right" % max_attempts)
      max_attempts -= 1
      if count < max_attempts + 1:
        print("You have got your password wrong too many times.")
        print("You are locked out of the system for %s seconds." % (secs + n))
        count = 1
        attempts = 0
        password = None
        time.sleep(secs + n)
        n = n + 10
        password = prompt_user_for_password()
      else:
        password = prompt_user_for_password()
    else:
      print("welcome")
