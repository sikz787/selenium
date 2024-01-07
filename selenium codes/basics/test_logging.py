# capture details useful while debugging and show the user details about execution of the programme
# show warnings in case any fail and information, show errors
import logging


# in python there is module name logging,import the module and create and instance

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

