toEncode = input("Въведете текс за кодиране: ")
encodedMessage = toEncode.encode()
print(str(list(encodedMessage)) + " - Това е кодирания текс")
decodedMessage = encodedMessage.decode()
print(decodedMessage + " - Това е съобщението декодирано")
#Езикът който съм ползвал е Python