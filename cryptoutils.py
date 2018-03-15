from pysodium import *

SALT = b'BabbleBabbleBabb'

def derive_key(passphrase):
    return crypto_pwhash(crypto_aead_chacha20poly1305_ietf_KEYBYTES, passphrase,
                         SALT, crypto_pwhash_OPSLIMIT_INTERACTIVE,
                         crypto_pwhash_MEMLIMIT_INTERACTIVE,
                         crypto_pwhash_ALG_DEFAULT)

def encrypt(message, key):
    nonce = randombytes(crypto_aead_chacha20poly1305_ietf_NPUBBYTES)
    return (nonce + crypto_aead_chacha20poly1305_ietf_encrypt(message, None,
                                                              nonce, key))

def decrypt(message, key):
    nonce = message[:crypto_aead_chacha20poly1305_ietf_NPUBBYTES]
    cipher = message[crypto_aead_chacha20poly1305_ietf_NPUBBYTES:]
    return crypto_aead_chacha20poly1305_ietf_decrypt(cipher, None, nonce, key)

def base_hanzi_encode(message, base):
    return ''.join(base[c] for c in message)

def base_hanzi_decode(message, base):
    return bytes(base.index(c) for c in message)

def babble(message, passphrase, base):
    return base_hanzi_encode(encrypt(message, derive_key(passphrase)), base)

def debabble(message, passphrase, base):
    return decrypt(base_hanzi_decode(message, base), derive_key(passphrase))
