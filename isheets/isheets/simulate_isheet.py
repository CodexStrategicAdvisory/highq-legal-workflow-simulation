import json
from pathlib import Path

def load_isheet(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def print_schema(isheet):
    print(f"iSheet Name: {isheet['name']}")
    print(f"Description: {isheet['description']}\n")
    print("Columns:")
    for col in isheet["columns"]:
        req = "required" if col.get("required") else "optional"
        col_type = col["type"]
        line = f" - {col['name']} ({col_type}, {req})"
        if "options" in col:
            line += f" options={col['options']}"
        print(line)
    print("\nValidation Rules:")
    for rule in isheet.get("validationRules", []):
        print(f" - {rule['name']}: IF {rule['condition']} THEN require {rule['require']}")

def print_sample_rows(isheet):
    print("\nSample Rows:")
    for row in isheet["sampleRows"]:
        print("-" * 40)
        for col in isheet["columns"]:
            name = col["name"]
            print(f"{name}: {row.get(name)}")

if __name__ == "__main__":
