import base64

def base64_decode(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

# Example base64-encoded string
encoded_string = "SGVsbG8gV29ybGQhCg=="
decoded_string = base64_decode(encoded_string)
print(decoded_string)
