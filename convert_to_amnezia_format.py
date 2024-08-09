from pathlib import Path

if __name__ == "__main__":
    current_dir = Path(".")
    files = [f for f in current_dir.iterdir() if f.is_file()]
    matching_files = [f for f in files if "_subsidiaries.csv" in f.name]

    entries = []
    for company in matching_files:
        with open(f"{company}_subsidiaries.csv", "r") as incsvfile:
            while line := incsvfile.readline():
                netblock = line.split(",")[0]
                rationale = line.split(",")[5]
                if not "duplicate" in rationale.lower() and "/" in netblock and "::" not in netblock:
                    entries.append(f'{{"hostname": "{netblock}"}}')
        
    json_content = "[" + ",".join(entries) + "]"

    with open("split_tunneling_amnezia.json", "w") as outtxtfile:
        outtxtfile.write(json_content)
