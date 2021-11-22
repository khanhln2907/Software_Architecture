"""
    Improve the code with the strategy pattern to support all 
    three algorithms in a unified way. Implement the class 
    Algorithm that provides the functions encrypt and decrypt.


"""


def calc_hash( data ):
    return sum( [ord(char) for char in data ] )



class RSA():
    def encrypt(self, msg, secret_key):
        return secret_key*msg 

    def decrypt(self, msg, public_key):
        return msg/2/public_key


class ECDSA():
    def encrypt(self, msg, secret_key):
        return msg + secret_key

    def decrypt(self, msg, public_key):
        return msg - (2*public_key)


class XMSS():
    def encrypt(self, msg, secret_key):
        return msg - 3

    def decrypt(self, msg, public_key):
        return msg + 3








# Main Function (CHANGE)
# ======================================================
def main():

    msg = "hello world!"
    secret_key = 42 
    public_key = 21

    ecdsa = ECDSA()
    rsa = RSA()

    # Sender: signing
    print("Sender: Signing msg='{}'".format(msg))
    msg_hash = calc_hash( msg )
    print("Sender: Hash of msg: ", calc_hash(msg))
    sig = ecdsa.encrypt(msg_hash, secret_key)
    print("Sender: Signature={}".format(sig))

    # sending msg + sig to receiver ...

    # Receiver: verifying
    print("Receiver: received msg='{}' and Signature={} ".format(msg, sig))
    msg_hash = calc_hash( msg )
    signed_hash = ecdsa.decrypt(sig, public_key)
    print("Receiver: decrypted hash={}".format(signed_hash)) 

    is_valid = (signed_hash == msg_hash)
    print("Receiver: Signature is", "valid!" if is_valid else "INVALID")



#run
main()
