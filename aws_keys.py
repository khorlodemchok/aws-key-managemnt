from Crypto.PublicKey import RSA
import hashlib


def fp_format(in_str):
    chunks = [in_str[i:i+2] for i in range(0, len(in_str), 2)]
    return ":".join(chunks)


def local_fingerprint(key_file_obj):
    key = RSA.import_key(key_file_obj.read())
    k_der = key.publickey().export_key(format='DER')
    hash_sum = hashlib.md5(k_der).hexdigest()
    return fp_format(hash_sum)

    
