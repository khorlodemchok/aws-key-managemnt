def fp_format(in_str):
    chunks = [in_str[i:i+2] for i in range(0, len(in_str), 2)]
    return ":".join(chunks)


def local_fingerprint():
    return "something"
