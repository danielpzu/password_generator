def run():

    import string as str, secrets as sc, crypt as cr, os

    lower = str.ascii_lowercase
    upper = str.ascii_uppercase
    numbers = str.digits
    special_characters = str.punctuation
    alphabet = lower+upper+numbers+special_characters

    os.system("clear")
    pwd_length = int(input("Choose the length of the password: "))
    pwd = ""
    for i in range(pwd_length):
        pwd += "".join(sc.choice(alphabet))
        encrypted_pwd ="".join(cr.crypt(pwd)) 

    menu = """
    1: Show only the password in plain text
    2: Show only the encrypted password
    3: Show both
    """

    while True: 
        choose = int(input(menu))

        if choose == 1:
            print(f"Your password is: {pwd}")
            break

        elif choose == 2:
            print(encrypted_pwd)
            print(f"Your password is: {encrypted_pwd}")
            break

        elif choose == 3:
            print(pwd,encrypted_pwd)
            print(f"Your encrypted password is: {encrypted_pwd} and your plain text password is: {pwd}")
            break

        else:
            print("I dont understand, please try again")

if __name__ == "__main__":
    run()
