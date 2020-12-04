from random import randint

letter_small = "abcdefghijklmnopqrstuvwxyz"
letter_cap =  letter_small.upper()
digit = "0123456789"
char_special = "!@#$%-_+"
check = False

while check == False:
    try:
        password = letter_small + letter_cap + digit + char_special
        password_length = int(input("Enter length of password, at least 8 characters:\n>> "))

        gen_pass = ""
        length = 0
        if password_length < 12 or password_length > 128:
            print("\n[!] Invalid value. Password should be at least 12 characters and maximum 128 characters.\n")
        else:
            while length < password_length:
                gen_pass = gen_pass + password[randint(0, len(password)-1)]
                length+=1
            print(f"Your new password is: {gen_pass}")
            print("\nThank you for using password generator :3\n")
            check = True      
    except ValueError:
        print("\n[!] Error. Enter a valid value.\n")
35345
    
