from dagster import graph, op


@op
def get_name() -> str:
    return "Atb"


@op
def hello_someone(context, name: str) -> str:
    message = f"Hello, {name}"
    context.log.info(message)
    return message


@graph
def say_hello():
    name = get_name()
    hello_someone(name)
