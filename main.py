from calculate_lrc import calculate_lrc
from calculate_lrc import hex_to_ascii

Start = "58" # : = 58 = 3A = 0011 1010

Slave_address = "4849" # default 01 = 4849 = 3031 = 0011 0000 0011 0001

# Function_code
# registers = memory locations within a device that store data values
# 03(03h) = Reading multiple registers
Function_code = "4851" # 03 = 4851

# Head address of specified register (which register start to read)
Data_code_1 = "48484848" # 0000 =48484848

#Quantity of register to read ( how many to read)
# Max register map = 0000h = 000Bh
Data_code_2 = "48484866" # 000Bh = 48484866


LRC = ""

End = "48684865" # [CR][LF] = OD OA =48 68 48 65


# Example messages
messages = ["010300000001", "01030200EE", "0106000B00FE","010300000007", "01030E00D40000000D0000020100000000"]

# Calculate the LRC value for each message
for message in messages:
    lrc = calculate_lrc(message)
    print(f"Input: {message}, Output: {lrc}")

###################

##  File | File Properties | File Encoding from the main menu or click the File Encoding


message = bytes.fromhex("3A 30 31 30 33 30 30 30 30 30 30 30 42")
print(message)
