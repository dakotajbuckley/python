guest_list = ["Epictetus", "Socrates", "Marcus Aerelius", "Freddie Mercury"]
print("Hey " + guest_list[0] + ", come on over for dinner. On me!")
print("Hey " + guest_list[1] + ", i'd love to have you over for dinner! We can talk philosophy")
print("Hey " + guest_list[2] + ", come on over for dinner. On me!")
print("Hey " + guest_list[3] + ", come on over for dinner. On me!")

unattending_guest = str(guest_list.remove("Marcus Aerelius"))
guest_list.append("Joan of arc")

print ("Sorry, " + unattending_guest + " Isnt able to make it to dinner")

print("Hey " + guest_list[0] + ", come on over for dinner. On me!")
print("Hey " + guest_list[1] + ", i'd love to have you over for dinner! We can talk philosophy")
print("Hey " + guest_list[2] + ", come on over for dinner. On me!")
print("Hey " + guest_list[3] + ", come on over for dinner. On me!")

print("Hey all, I found a bigger table so inviting more people!")
guest_list.insert(0, "Jesus Christ")
guest_list.insert(2, "Great Great Grandpa")
guest_list.append("Joe Keery")

print("Hey " + guest_list[0] + ", come on over for dinner. On me!")
print("Hey " + guest_list[1] + ", i'd love to have you over for dinner! We can talk philosophy")
print("Hey " + guest_list[2] + ", come on over for dinner. On me!")
print("Hey " + guest_list[3] + ", come on over for dinner. On me!")
print("Hey " + guest_list[4] + ", come on over for dinner. On me!")
print("Hey " + guest_list[5] + ", i'd love to have you over for dinner! We can talk philosophy")
print("Hey " + guest_list[6] + ", come on over for dinner. On me!")
print("\nUnfortuantely I can only invite two people")
print("I am sorry I dont have space for you " + guest_list.pop())
print("I am sorry I dont have space for you " + guest_list.pop())
print("I am sorry I dont have space for you " + guest_list.pop())
print("I am sorry I dont have space for you " + guest_list.pop())
print("I am sorry I dont have space for you " + guest_list.pop())
print("\nHey, " + guest_list[0] + " you are still invited! Hope you can make it!")
print("\nHey, " + guest_list[1] + " you are still invited! Hope you can make it!")
del guest_list[1]
del guest_list[0]
print(guest_list)
print(len(guest_list))