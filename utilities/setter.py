import os
from base64 import b64decode

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    if key is None:
        raise ValueError("Environment variable 'SERVICE_ACCOUNT_KEY' not found.")
    
    try:
        decoded_key = b64decode(key).decode()
    except Exception as e:
        raise ValueError("Failed to decode the key from base64.") from e
    
    with open('path.json', 'w') as json_file:
        json_file.write(decoded_key)

    print(os.path.realpath('path.json'))

if __name__ == '__main__':
    main()