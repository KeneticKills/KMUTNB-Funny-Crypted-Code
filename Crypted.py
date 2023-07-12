class Encryptor:
    def __init__(self,key: str):
        self.key = key
    
    def encryption(self,txt):
        encrypted_word = ""
        bits = (1 << 32) -1
        for i in range(len(txt)):
            left = ord(self.key[i%len(self.key)]) % 16
            right = 32-left
            encrypted_word += chr(ord(txt[i]) << left & bits | ord(txt[i]) >> right)
        return encrypted_word
    
    def decryption(self,txt):
        decrypted_word = ""
        bits = (1 << 32) -1
        for i in range(len(txt)):
            right = ord(self.key[i%len(self.key)]) % 16
            left = 32-right
            decrypted_word += chr(ord(txt[i]) << left & bits | ord(txt[i]) >> right)
        return decrypted_word