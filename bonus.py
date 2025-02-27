# Function to check if an IP is valid
def is_valid_ip(ip: str):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    return all(is_valid_part(part) for part in parts)

# Function to validate individual parts of the IP
def is_valid_part(part):
    try:
        i_part = int(part)
        if part.startswith('0') and len(part) > 1:  # Rejects leading zeros (except single '0')
            return False
        return 0 <= i_part < 256
    except ValueError:
        return False

# Convert decimal to binary (Recursive)
def decimal_to_binary(n):
    if n == 0: return '0'
    if n == 1: return '1'
    next, digit = divmod(n, 2)
    return decimal_to_binary(next) + str(digit)

# Convert binary to decimal (Recursive)
def binary_to_decimal(b: str):
    if not b: return 0  # Base case
    return int(b[0]) * (2 ** (len(b) - 1)) + binary_to_decimal(b[1:])  # Corrected slicing

# Convert IP to binary
def ip_to_binary(ip: str):
    """Converts a valid IPv4 address to binary format."""
    if not is_valid_ip(ip):
        return "Invalid IP"
    return '.'.join(decimal_to_binary(int(part)).zfill(8) for part in ip.split('.'))

# Convert binary to decimal IP
def binary_to_ip(binary_ip: str):
    """Converts a binary IP back to decimal format."""
    parts = binary_ip.split('.')
    if len(parts) != 4 or any(len(part) != 8 for part in parts):
        return "Invalid Binary IP"
    return '.'.join(str(binary_to_decimal(part)) for part in parts)

# Generalized function to detect input type and convert
def ip_convert(ip_or_binary: str):
    """Determines input type and converts accordingly."""
    if '.' in ip_or_binary:
        if all(c in '01.' for c in ip_or_binary) and len(ip_or_binary.replace('.', '')) % 8 == 0:
            return binary_to_ip(ip_or_binary)  # It's a binary IP
        else:
            return ip_to_binary(ip_or_binary)  # It's a decimal IP
    return "Invalid Input"

# Test cases
print(ip_convert("192.168.1.1"))      # Converts to binary
print(ip_convert("11000000.10101000.00000001.00000001"))  # Converts to decimal
print(ip_convert("999.999.999.999"))  # Invalid IP
print(ip_convert("10101010.11110000.10101010.11110000"))  # Converts to decimal
