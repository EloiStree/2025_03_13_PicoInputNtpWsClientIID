import adafruit_rsa
import os
import hashlib

class KeyPair:
    private_key = """
    """
    

class RSASignature512PicoW:
    private_key_path = "private_key.pem"
    public_key_path = "public_key.pem"
    def __init__(self, rsa_info, key_size=512):
        """
        Initializes the RSASignature class, generating a public/private key pair.
        :param key_size: Size of the RSA key in bits (default is 512).
        """
        self.key_size = key_size
        self.private_key_object = None
        self.public_key_object = None
        
        
        if rsa_info==None or rsa_info.strip()=="":                
            print("Generating RSA key pair...")
            
            (public_key, private_key) = adafruit_rsa.newkeys(512)
            self.private_key_object = private_key
            self.public_key_object = public_key
            print("Public Key:")
            print (public_key)
            
            print("Private Key:")
            print (private_key)
            
            print("> Public Key:")
            print(f"n (modulus): {public_key.n}")
            print(f"e (public exponent): {public_key.e}")
            print("> Private Key:")
            print(f"n (modulus): {private_key.n}")
            print(f"d (private exponent): {private_key.d}")
            print(f"p (prime 1): {private_key.p}")
            print(f"q (prime 2): {private_key.q}")
            public_key_as_str = f"n:{public_key.n},e:{public_key.e}"
            private_key_as_str = f"n:{private_key.n},d:{private_key.d},p:{private_key.p},q:{private_key.q}"
            print (f"Public Key: {public_key_as_str}")
            print (f"Private Key: {private_key_as_str}")   
        else :
            print("Using RSA key pair from KeyPair class...")
            self.pn_modulus =""
            self.pe_public_exponent =""
            self.pd_private_exponent =""
            self.pp_prime_1 =""
            self.pq_prime_2 =""
            
            pieces = rsa_info.split(",")
            for piece in pieces:
                key,value = piece.split(":")
                if key == "n":
                    self.pn_modulus = value
                elif key == "e":
                    self.pe_public_exponent = value
                elif key == "d":
                    self.pd_private_exponent = value
                elif key == "p":
                    self.pp_prime_1 = value
                elif key == "q":
                    self.pq_prime_2 = value
                
            self.public_key_object=  adafruit_rsa.PublicKey(int(self.pn_modulus), int(self.pe_public_exponent))
            self.private_key_object=  adafruit_rsa.PrivateKey(int(self.pn_modulus), int(self.pe_public_exponent), int(self.pd_private_exponent), int(self.pp_prime_1), int(self.pq_prime_2))
        
   
    
    def sign_message(self, message):
        """
        Signs a given message using the private key.
        :param message: The message to sign (should be a bytes-like object).
        :return: The signature of the message.
        """
        # adafruit_rsa.sign(hashed_message, self.private_key_object)
        
        signed = adafruit_rsa.sign(message, self.private_key_object, "SHA-256")
        return signed
        

    def verify_signature(self, message, signature):
        """
        Verifies that a given signature is valid for the message using the public key.
        :param message: The message to verify.
        :param signature: The signature to verify.
        :return: True if the signature is valid, False otherwise.
        """
              
        
        bool_result = adafruit_rsa.verify(message, signature, self.public_key_object)
        
        return bool_result
    def test(self,message):
    
        signature = self.sign_message(message)
        print("Signed message:", signature)
        # Verify the signature
        if self.verify_signature(message, signature):
            print("The signature is valid!")
        else:
            print("The signature is invalid.")



# # Example usage
# if __name__ == "__main__":
#     # Create the RSASignature instance with default key size (512 bits)
#     rsa = RSASignature(key_size=512)

#     # Define the message to be signed
#     message = b"Hello, this is a test message!"

#     # Sign the message
#     signature = rsa.sign_message(message)
#     print("Signed message:", signature)

#     # Verify the signature
#     if rsa.verify_signature(message, signature):
#         print("The signature is valid!")
#     else:
#         print("The signature is invalid.")
