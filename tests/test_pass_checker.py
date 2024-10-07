import pytest

from lib.password_checker import PasswordChecker

checks if password is >=8 char
def test_check_pass_bigger_8_char():
    password_checker = PasswordChecker()
    result = password_checker.check("Qwertyui1")
    assert result == True
    
#checks if password is <8 char, raise error message "Invalid password, must be 8+ characters."
def test_check_small_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as exc_info:  # Check if the exception is raised
        password_checker.check("short")  # A password with only 5 characters (invalid)
    
    # Check that the error message matches what we expect
    assert str(exc_info.value) == "Invalid password, must be 8+ characters."
