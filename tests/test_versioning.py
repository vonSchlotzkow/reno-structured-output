from importlib import metadata

def test_version():
    assert metadata.version("reno-structured-output") == "0.1.0"

def test_reno_import_available():
    assert metadata.version("reno")
    from reno_structured_output import reno

import yaml
from pathlib import Path

def test_reno():
    from reno_structured_output import reno
    from reno import scanner, config
    conf = config.Config("./")
    with scanner.Scanner(conf) as scnr:
        relnotes = scnr.get_notes_by_version() # this should be almost it

    # check structure

    x ={}
    x.items

    for version, version_details in relnotes.items():
        print(version)
        print(version_details)

    print("---===###===---")

    from collections import defaultdict

    relnotes_content = {} # defaultdict(lambda : defaultdict(list))
    for version, version_details in relnotes.items():
        print(version_details)
        version_files = [x[0] for x in version_details]
        print(version_files)
        for f in version_files:
            version_file_content = yaml.load(Path(f).read_text(), Loader=yaml.FullLoader)
            for category, notes in version_file_content.items():
                if category != "prelude":
                    relnotes_content.setdefault(version,{}).setdefault(category,[]).extend(notes)
    print(relnotes_content)

    # yamls=yaml.dump(relnotes_content, sort_keys=False)
    # print(yamls)

    import json
    print(json.dumps(relnotes_content, indent=2))

    assert relnotes == "X"
