from importlib import metadata

def test_version():
    assert metadata.version("reno-structured-output") == "0.1.0"

def test_reno_import_available():
    assert metadata.version("reno")
    from reno_structured_output import reno
