"""
    In the following, we want to support send() and receive() functions for 
    switches and lights INDEPENDENT from the underlying wireless protocol used.

    Use the bridge pattern to refactor the code.


"""


def calc_hash( data ):
    return sum( [ord(char) for char in data ] )


class Algorithm():
    def encrypt(self, msg, secret_key):
        raise NotImplementedError 

    def decrypt(self, msg, public_key):
        raise NotImplementedError 



class RSA(Algorithm):
    def encrypt(self, msg, secret_key):
        return secret_key*msg 

    def decrypt(self, msg, public_key):
        return msg/2/public_key


class ECDSA(Algorithm):
    def encrypt(self, msg, secret_key):
        return msg + secret_key

    def decrypt(self, msg, public_key):
        return msg - (2*public_key)



class XMSS(Algorithm):
    def encrypt(self, msg, secret_key):
        return msg - 3

    def decrypt(self, msg, public_key):
        return msg + 3





class SignatureScheme():
    def __init__(self):
        self.algo = None
        self.sk = 42
        self.pk = 21

    def set_algorithm( self, algo ):
        self.algo = algo

    def sign(self, msg):
        msg_hash = calc_hash( msg )
        return self.algo.encrypt(msg_hash, self.sk)

    def verify(self, msg, sig):
        msg_hash = calc_hash( msg )
        return msg_hash == self.algo.decrypt(sig, self.pk)







# Main Function (CHANGE)
# ======================================================
def main():

    msg = "hello world!"
    print("Message: ", msg)
    print("Hash of msg: ", calc_hash(msg), "\n")

    crypto = SignatureScheme()
    crypto.set_algorithm( ECDSA() )


    sig = crypto.sign(msg)
    print("{} Signature: {}".format("ECDSA", sig))
    is_valid = crypto.verify(msg, sig)
    print("Signature is {}\n".format("valid!" if is_valid else "INVALID"))


    crypto.set_algorithm( XMSS() )

    sig = crypto.sign(msg)
    print("{} Signature: {}".format("XMSS", sig))
    is_valid = crypto.verify(msg, sig)
    print("Signature is {}\n".format("valid!" if is_valid else "INVALID"))


#run
main()
