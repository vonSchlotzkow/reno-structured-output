from importlib import metadata

def test_version():
    assert metadata.version("reno-structured-output") == "0.1.0"

def test_reno_import_available():
    assert metadata.version("reno")
    from reno_structured_output import reno

def test_reno():
    from reno_structured_output import reno
    from reno import lister, loader, scanner, config
    conf = config.Config("./")
    with scanner.Scanner(conf) as scnr:
        relnotes = scnr.get_notes_by_version() # this should be almost it
    assert relnotes
    assert lister == "X"
