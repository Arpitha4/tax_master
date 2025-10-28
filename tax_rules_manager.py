import json

TAX_FILE = "tax_structures.json"


def load_tax_rules():
    try:
        with open(TAX_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "default": {
                "INDIA": {"Above2000": 10, "BelowOrEqual2000": 0},
                "OTHERS": {"Any": 0}
            }
        }


def save_tax_rules(rules):
    with open(TAX_FILE, "w") as file:
        json.dump(rules, file, indent=2)


def get_tax_rate(item_rate, country_code):
    rules = load_tax_rules()
    country = country_code.upper()

    if country in ["IN", "INDIA"]:
        if item_rate > 2000:
            return rules["default"]["INDIA"]["Above2000"]
        else:
            return rules["default"]["INDIA"]["BelowOrEqual2000"]
    else:
        return rules["default"]["OTHERS"]["Any"]


def update_tax_structures():
    rules = load_tax_rules()
    print("\nCurrent Tax Rules:")
    print(json.dumps(rules, indent=2))

    country = input("Enter new country code (or press Enter to skip): ").upper()
    if country:
        above_2000 = float(input("Tax % for items > 2000: "))
        below_2000 = float(input("Tax % for items <= 2000: "))

        if "default" not in rules:
            rules["default"] = {}
        rules["default"][country] = {
            "Above2000": above_2000,
            "BelowOrEqual2000": below_2000
        }

        save_tax_rules(rules)
        print("Tax structure updated successfully.")
