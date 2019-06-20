from Crypto.PublicKey import RSA
import hashlib


def fp_format(in_str):
    chunks = [in_str[i:i+2] for i in range(0, len(in_str), 2)]
    return ":".join(chunks)


def md5_fingerprint(key_file_obj):
    key = RSA.import_key(key_file_obj.read())
    k_der = key.publickey().export_key(format='DER')
    hash_sum = hashlib.md5(k_der).hexdigest()
    return fp_format(hash_sum)

def sha1_fingerprint(key_file_obj):
    key = RSA.import_key(key_file_obj.read())
    k_der = key.export_key(format='DER', pkcs=8)
    hash_sum = hashlib.sha1(k_der).hexdigest()
    return fp_format(hash_sum)

def fingerprint(key_file_obj, origin):
    if not origin in ["local", "aws"]:
        raise AttributeError
    if origin == 'local':
        return md5_fingerprint(key_file_obj)
    elif origin == 'aws':
        return sha1_fingerprint(key_file_obj)
