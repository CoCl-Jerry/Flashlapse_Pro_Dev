def crc16(data: str, poly: int = 0x18005) -> str:
    # convert the hexadecimal string to a bytes object
    data = bytes.fromhex(data)
    # initialize the CRC to 0
    crc = 0
    # loop over the data, one byte at a time
    for byte in data:
        # XOR the current byte with the high byte of the CRC
        crc = crc ^ (byte << 8)
        # initialize a mask to 0x8000 (the highest bit)
        mask = 0x8000
        # loop over the 8 bits of the current byte
        for _ in range(8):
            # if the highest bit of the CRC is set
            if crc & mask:
                # shift the CRC and XOR it with the polynomial
                crc = (crc << 1) ^ poly
            else:
                # otherwise, just shift the CRC
                crc = crc << 1
            # clear the highest bit of the mask
            mask = mask >> 1
    # return the final CRC value as a hexadecimal string
    return hex(crc)
