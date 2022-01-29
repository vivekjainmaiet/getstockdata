#testing function before production
from getstockdata.lib import try_me

def test_try_me():

    assert len(try_me()) > 0

    # tests/test_lib.py
