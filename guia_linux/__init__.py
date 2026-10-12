__version__ = "2.2.1"

def main(argv=None):
    """Backward-compatible entry without loading content on package import."""
    from guia_linux.cli import main as cli_main
    return cli_main(argv)

__all__ = ["main", "__version__"]
