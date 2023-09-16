# Status - OK
from Crypto.PublicKey import RSA

def GenerateKeys(privateKeyFile, publicKeyFile):
    '''
        This function generates a public/private key pair.
    '''
    rsa = RSA.generate(2048)
    privateKey = rsa.export_key()

    with open(privateKeyFile, "wb") as privKey:
        privKey.write(privateKey)

    with open(publicKeyFile, "wb") as pubKey:
        pubKey.write(rsa.public_key().exportKey())

if __name__=='__main__':
  
    print("[+] Generating Public/Private keypairs ...")
    GenerateKeys("RSA_PrivateKey.key", "RSA_PublicKey.pub")
    print("[+] Keys saved !!")