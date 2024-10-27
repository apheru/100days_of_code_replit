print("SECURE LOGIN")
print()
username = input("Username >> ")
password = input("Password >> ")

if username == "Mark" and password == "password":
    print("Welcome Mark!")
elif username == "Suzanne" and password == "Su7anne":
    print("Hey there Suzanne!")
else:
    print("Go away!")