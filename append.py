import argparse
import json
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Append json to another json")
    parser.add_argument("json", nargs='+', help="Json files to append")
    parser.add_argument("--settings", "-o", type=str, default=".vscode/settings.json")

    args = parser.parse_args()


    settings = dict()
    for json_filename in args.json:
        print(f"> Load {json_filename}")
        with open(json_filename) as f:
            loaded = json.load(f)
            settings.update(loaded)

    print(settings)
    output_filename = Path(args.settings)
    if not output_filename.parent.exists():
        output_filename.parent.mkdir()

    if output_filename.exists():
        text = f"> Append settings to {output_filename}."
    else:
        text = f"> Create a new settings in {output_filename.parent}."

    with open(args.settings, "w") as f:
        dumped = json.dumps(settings, indent=4)
        f.write(dumped)

    print(text)
