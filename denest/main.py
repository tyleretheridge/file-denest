import typer
from rich import print

app = typer.Typer()


@app.callback()
def callback():
    """
    A CLI Tool to aid in the management of large amounts of files in a
    nested file structure
    """


@app.command()
def find(
    directory: str,
    include_extension: str = typer.Option(
        None, help="Comma separated list of extensions to search"
    ),
    exclude_extension: str = typer.Option(
        None, help="Comma separated list of extensions to exclude"
    ),
):
    find_print(directory, include_extension, exclude_extension)


# Test that options work properly
def find_print(directory: str, include_extensions: str, exclude_extension: str) -> None:
    print("Searching in directory:", directory)
    if include_extensions:
        print("Including extensions: ", include_extensions)

    if exclude_extension:
        print("Excluding extensions: ", exclude_extension)
