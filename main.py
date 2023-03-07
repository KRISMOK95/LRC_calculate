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








