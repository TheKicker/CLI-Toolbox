import pyclip

# Assumes ASCII text

# Python program to illustrate the
# conversion of Binary to ASCII
original = input("What is the binary? ")

# Initializing a binary string in the form of
# 0 and 1, with base of 2
try: 
    binary_int = int(original, 2);
except ValueError as e:
    print(f"\nYou tried to enter letters or something didn't you? \n Please enter binary only. \n\\ {e}")
  
# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8
  
# Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")
  
# Converting the array into ASCII text
ascii_text = binary_array.decode()

pyclip.copy(ascii_text)

# Getting the ASCII value
print(ascii_text)