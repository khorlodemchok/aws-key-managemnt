import pytest
from aws_keys import md5_fingerprint, sha1_fingerprint, fp_format, fingerprint

def test_fp_format():
    in_str = "12345"
    out_str = "12:34:5"
    assert fp_format(in_str) == out_str


def test_md5_fingerprint():
    proper_fp = "65:8f:82:a0:8f:53:77:ad:63:c8:f7:15:d6:36:69:04"
    with open('locally-created-key') as key_file_obj:
        assert fingerprint(key_file_obj, origin='local') == proper_fp

def test_sha1_fingerprint():
    proper_fp = "f7:35:02:f7:1e:f4:7c:e7:16:7b:f3:98:dc:f9:16:d6:d2:fd:13:21"
    with open('aws-created-key') as key_file_obj:
        assert fingerprint(key_file_obj, origin='aws') == proper_fp

def test_fingerprint_bad_origin():
    with open('aws-created-key') as f_obj:
        with pytest.raises(AttributeError):
            fingerprint(f_obj, origin='eggs')
