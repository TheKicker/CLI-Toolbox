import pyclip

# Take the text input from the user
original = input("What would you like to say? ")

# Print the original message
print("Original: {0}".format(original))

# Take the string, convert to binary using bytearray, rejoin the resulting string
binary = ''.join(format(ord(i), '08b') for i in original)

#Copy to clipboard
pyclip.copy(binary)

# Print the binary message (convert to ASCII)
print("Binary (copied to clipboard): {0}".format(binary))