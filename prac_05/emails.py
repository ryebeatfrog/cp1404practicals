'''
estimated time: 1hr
actual time

'''
def main():

    emails = {}
    email = input("What is your email?: ")
    while email != "":
        email = input("What is your email?: ")
        name = extract_email(email)
        valid = input(f"is your name, {name}? [y/n]").lower()
    if valid == "n":
        name = input("Name: ")
        emails[name]= name
    for email, name in emails.items():
        print(f"{name:2}: {email:3}")




def extract_email(email):
    parts = email.split("@")[0]
    name = "".join(parts)
    # print(name)
    return name




main()
