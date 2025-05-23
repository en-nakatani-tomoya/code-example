import click


@click.command()
@click.option("--name", default="World", help="Name to greet")
@click.option("--count", default=1, help="Number of greetings")
def main(name, count):
    for _ in range(count):
        click.echo(f"Hello {name} from click-example!")


if __name__ == "__main__":
    main()
