from src.task_app.validation import Validation


def test_valid_title():
    assert Validation.validate_title("Learn Python") is True


def test_invalid_title():
    assert Validation.validate_title("   ") is False


def test_valid_description():
    assert Validation.validate_description("Practice Python daily") is True


def test_invalid_description():
    assert Validation.validate_description("   ") is False


def test_valid_priority():
    assert Validation.validate_priority("High") is True
    assert Validation.validate_priority("Medium") is True
    assert Validation.validate_priority("Low") is True


def test_invalid_priority():
    assert Validation.validate_priority("Urgent") is False


def test_valid_id():
    assert Validation.validate_id(1) is True


def test_invalid_id():
    assert Validation.validate_id(0) is False
    assert Validation.validate_id(-1) is False