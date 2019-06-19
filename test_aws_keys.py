from aws_keys import local_fingerprint, fp_format

def test_fp_format():
    in_str = "12345"
    out_str = "12:34:5"
    assert fp_format(in_str) == out_str


def test_local_fingerprint():
    assert local_fingerprint()
