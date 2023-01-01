import pywhatkit

# Example 1 : send schedule message to number and auto closed the window after 5 second of wait
# enter your mobile number with country code
number = "+92333123456789"
message = "Hello, are you there?"
# pywhatkit.sendwhatmsg(number, message, 23, 8, 30, True, 5)


# Example 2 : send message & image to the number
message = "Image is sending !!!!"
#pywhatkit.sendwhats_image(number, "C:\\Users\\PycharmProjects\\Practice\\hello.jpg", message)


# Example 3 : send schedule message to the group.
# Only Admin can send message to the group, find group link in the whatsapp
# go to invite member then you will find the link like below
#https://chat.whatsapp.com/DnmlBkz111xXRXJaoixjYsQBuX3Y

message = "Hello Guys, Bye"
pywhatkit.sendwhatmsg_to_group("DnmlBkz111xXRXJaoixjYsQBuX3Y", message, 23, 40, 30, True, 5)
