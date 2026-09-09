# 5.8
usernames = ["admin", "dakota", "legocoyman", "bushdid911", "licoln"]
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you list to see a status report?")
        else:
            print("Hello " + username + "!")
else:
    print("We need to find some users!")

# 5.10
current_users = ["bluecreeper", "tenablesoda2656", "octopusmonkey", "sluggox", "inflamedghost"]
new_users = ["Sluggox", "octopusmonkey", "winchester", "stonesiren", "scoreddoor"]

for user in new_users:
    if user.lower() in current_users:
        print("You will need to enter a new username. " + user + " is taken.")
    else:
        print("The username " + user + " is available")

numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")