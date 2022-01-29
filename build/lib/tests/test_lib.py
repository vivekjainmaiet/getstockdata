#testing function before production
from getstockdata.lib import try_me

def test_try_me():

    assert try_me() == "Welcome to my Git repository !!! --- Vivek Jain"
