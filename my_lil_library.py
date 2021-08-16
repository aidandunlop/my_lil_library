import numpy as np
import click


def function_one():
    print("hi from function one")
    return "a string"


def function_two():
    print("hi from function two")
    return "another string"


def function_three():
    a_variable = np.float("0.3")
    return a_variable


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(name):
    click.echo(f"Hello {name}!")


@click.group(help="Example CLI tool")
def mylilcli():
    click.secho(f"Running my lil library...", fg="blue")


mylilcli.add_command(hello)

if __name__ == "__main__":
    mylilcli()
