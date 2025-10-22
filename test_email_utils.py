from email_utils import create_email

def test_add_positive():
    assert create_email("ivan", "test.com") == "ivan@test.com"

def test_add_positive_numbers():
    assert create_email("user123", "mail.ru") == "user123@mail.ru"
