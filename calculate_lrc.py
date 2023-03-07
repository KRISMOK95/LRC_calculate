def calculate_lrc(message):
    # Convert the message to a list of bytes
    message_bytes = bytes.fromhex(message)

    # Initialize the LRC value to 0
    lrc = 0

    # Add up the byte numbers and take the one's complement
    for byte in message_bytes:
        lrc = (lrc + byte) & 0xFF

    lrc = ((~lrc) + 1) & 0xFF

    # Convert the LRC value to a hexadecimal string
    lrc_hex = format(lrc, '02X')

    return lrc_hex


