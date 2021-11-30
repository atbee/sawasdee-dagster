from hello import get_name


def test_get_name_should_return_my_name():
    result = get_name()

    assert result == "Atb"
