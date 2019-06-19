from aws_keys import local_fingerprint, fp_format

def test_fp_format():
    in_str = "12345"
    out_str = "12:34:5"
    assert fp_format(in_str) == out_str


def test_local_fingerprint():
    proper_fp = "65:8f:82:a0:8f:53:77:ad:63:c8:f7:15:d6:36:69:04"
    with open('locally-created-key') as key_file_obj:
        assert local_fingerprint(key_file_obj) == proper_fp
