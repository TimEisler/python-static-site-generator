import ssg.parsers
import typer

from ssg.site import Site

def main(*, source="content", dest="dist"):
    config = {"source": source, "dest": dest, "parsers": [ssg.parsers.ResourceParser()]}
    Site(**config).build()

if __name__ == "__main__":
    typer.run(main)