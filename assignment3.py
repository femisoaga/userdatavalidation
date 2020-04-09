import random

rad = random.randint(20000, 80000)

first_name = input("enter your first name ")
first = first_name[:2]
last_name = input("enter your last name ")
last = last_name[:2]
email_address = input("enter a valid email address ")

password = first + last + str(rad)

print("Your PASSWORD is", password)
resp = input("Are you okay with this password?  ")

if resp.lower() == "yes":
    print("\n \n YOUR DETAILS-:")
    print("\n First name. ", first_name)
    print("\n Last name.  ", last_name)
    print("\n Email address  ", email_address)
    print("\n password. ", password)


else:
    password = input("Choose your password \n \n \n")

    while len(password) < 7:
        print("password must be upto seven letters")
        password = input("re-enter  password")

    else:
        print("\n \n YOUR DETAILS-:")
        print("\n First name  ", first_name)
        print("\n Last name  ", last_name)
        print("\n Email address  ", email_address)
        print("\n password. ", password)