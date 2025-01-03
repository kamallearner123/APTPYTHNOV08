# Importing the Required Library
import pywhatkit

# Defining the Phone Number and Message
phone_number1 = "+91 94498 69371" #"+919739858111"
phone_number2 = "+919739858111"
message = "message"

# Sending the WhatsApp Message
pywhatkit.sendwhatmsg_instantly(phone_number1, message)
pywhatkit.sendwhatmsg_instantly(phone_number2, message)

# Displaying a Success Message
print("WhatsApp message sent!")
