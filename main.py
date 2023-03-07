from calculate_lrc import calculate_lrc
Start = ":"

Slave_address = ""

Function_code = ""

Data_code = ""

LRC = ""

End = "[CR][LF]"


# Example messages
messages = ["010300000001", "01030200EE", "0106000B00FE","010300000007", "01030E00D40000000D0000020100000000"]

# Calculate the LRC value for each message
for message in messages:
    lrc = calculate_lrc(message)
    print(f"Input: {message}, Output: {lrc}")




###################


hex_string = "010300000001"

ascii_string = ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))
print("ASCII string:", ascii_string.encode('utf-8'))



