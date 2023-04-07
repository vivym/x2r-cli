import typer
from cookiecutter.main import cookiecutter

app = typer.Typer()


@app.command()
def create(
    project_name: str,
    template: str = typer.Option(
        default="https://github.com/vivym/x2r-template",
        help="The template to use for the project.",
    )
):
    cookiecutter(template, extra_context={"project_name": project_name})


@app.command()
def config():
    typer.echo("Configuring x2r-cli")


if __name__ == "__main__":
    app()
