from dagster import build_op_context

from hello import get_name, hello_someone, say_hello


def test_get_name_should_return_my_name():
    result = get_name()

    assert result == "Atb"


def test_hello_someone_should_return_greetings_to_me():
    context = build_op_context()
    result = hello_someone(context, "Atb")

    assert result == "Hello, Atb"


def test_say_hello():
    result = say_hello.execute_in_process()

    assert result.success
    assert result.output_for_node("get_name") == "Atb"
    assert result.output_for_node("hello_someone") == "Hello, Atb"
