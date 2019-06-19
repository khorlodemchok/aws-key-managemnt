from aws_keys import local_fingerprint


def test_local_fingerprint():
    assert local_fingerprint()
