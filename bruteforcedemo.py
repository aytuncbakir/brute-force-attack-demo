# import the libraries needed
import itertools
import string

# method takes as argument a string representing a password and returns the number of attempts
# and the password guessed. 
def bruteforce_attack(password):
    chars = string.printable.strip() # extract the characters without any trailing space
    attempts = 0     # variable to count attempts. 
    for length in range(1, len(password) + 1): # take the length of the input
        for guess in itertools.product(chars, repeat=length): # use the itertools to build a character sequence
            attempts += 1 # for every attempt increment the attempt counter 
            guess = ''.join(guess) # join the previously guess sequence with the new one
            print(guess)
            write_guesses_to_file(guess)
            if guess == password: # if the password is correct 
                return (attempts, guess) # return the password as well as number o guesses
    return (attempts, None) # otherwise return guesses 

def write_guesses_to_file(guess):
    f = open(result_file_path, "a")
    f.write(guess+"\n")
    f.close()

def data_leakage(guess):
    if guess:
        f = open(secrets, "r")
        print(f.read())
        f.close()
    
# you can change the password here for different words 
# remember overly complicated passwords will require more computation time

###########################
password = "aaa" 
###########################


result_file_path = 'C:\\Users\\aytun\\Desktop\\CyberSecurity\\Brute Force Attack\\result.txt'
secrets = 'C:\\Users\\aytun\\Desktop\\CyberSecurity\\Brute Force Attack\\secrets.txt'
attempts, guess = bruteforce_attack(password)
if guess: # if the password is correctly guess output number of guesses and password 
    print(f"\nPassword cracked in {attempts} attempts. The password is {guess}.")
    data_leakage(guess)
else: # otherwise return failed and number of guesses 
    print(f"Password not cracked after {attempts} attempts.") 
    
 