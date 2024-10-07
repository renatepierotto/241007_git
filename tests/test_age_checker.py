from lib.age_checker import AgeChecker
import pytest


def test_input_birthday():
    age_checker = AgeChecker("1960-10-21")
    result = age_checker.birthdate
    assert result == "1960-10-21"

def test_check_age():
    age_checker = AgeChecker("1992-01-11")
    result = age_checker.return_age()
    assert result == 32

def test_check_too_young():
    age_checker = AgeChecker("2020-01-11")
    result = age_checker.check_age()
    assert result == "Access Denied, you are 4 years old, wait another 12 years"

def test_check_old_enough():
    age_checker = AgeChecker("1992-01-11")
    result = age_checker.check_age()
    assert result == "Access granted"

def test_wrong_format_date():
    age_checker = AgeChecker(19920111)
    with pytest.raises(Exception) as e:
        age_checker.check_age()
    error_message = str(e.value)
    assert error_message == "Date is the incorrect format"

def test_wrong_string_format_date():
    age_checker = AgeChecker("19920111")
    with pytest.raises(Exception) as e:
        age_checker.check_age()
    error_message = str(e.value)
    assert error_message == "Date is the incorrect format"