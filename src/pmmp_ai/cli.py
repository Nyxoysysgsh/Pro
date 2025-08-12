import click
from rich import print
from rich.table import Table
from .rag import TfidfRag

DEFAULT_STORE = "vector_store"

@click.group()
def cli():
    pass

@cli.command()
@click.argument("paths", nargs=-1)
@click.option("--store", default=DEFAULT_STORE, help="Katalog na wektory")
def ingest(paths, store):
    """Zindeksuj pliki/foldery (md, txt, yml, yaml, php)."""
    if not paths:
        print("[red]Podaj ścieżki do plików lub katalogów[/red]")
        return
    rag = TfidfRag(store)
    count = rag.ingest_paths(list(paths))
    print(f"[green]Zindeksowano dokumentów:[/green] {count}")

@cli.command()
@click.argument("question")
@click.option("--k", default=5, help="Liczba wyników")
@click.option("--store", default=DEFAULT_STORE, help="Katalog na wektory")
def ask(question, k, store):
    """Zapytaj bazę (zwraca najbardziej podobne dokumenty)."""
    rag = TfidfRag(store)
    results = rag.query(question, top_k=k)
    if not results:
        print("[yellow]Brak wyników. Zindeksuj dokumenty komendą ingest.[/yellow]")
        return
    table = Table(title="Wyniki")
    table.add_column("#")
    table.add_column("Score")
    table.add_column("Plik")
    for i, (score, meta) in enumerate(results, start=1):
        table.add_row(str(i), f"{score:.4f}", meta.get("path", "?"))
    print(table)

if __name__ == "__main__":
    cli()