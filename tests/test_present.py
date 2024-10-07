import pytest

from lib.present import Present

import sys

def test_virtualenv_active():
    assert sys.prefix != sys.base_prefix, "Virtual environment is not active"

#when we wrap something, we get it back when unwrapping#

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(9)
    assert present.unwrap() == 9
    
    
#when we unwrap before wrapping, we get an error message:

def test_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
         present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."
    
#if we try toadd twice, we get an error message

def test_run_twice():
    present = Present()
    present.wrap(33)
    with pytest.raises(Exception) as e:
         present.wrap(44)
    message = str(e.value)
    assert message == "A contents has already been wrapped."
    
    