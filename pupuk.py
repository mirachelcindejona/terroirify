import argparse
import json
from datetime import datetime

# File to store fertilizer data
DATA_FILE = 'fertilizer_data.json'

# Load data from the file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to the file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add new fertilizer data
def add_fertilizer(args):
    data = load_data()
    fertilizer = {
        'id': args.id,
        'name': args.name,
        'stock': args.stock,
        'reception_date': args.reception_date,
        'usage_notes': args.usage_notes
    }
    data.append(fertilizer)
    save_data(data)
    print("Fertilizer data added successfully.")

# View all fertilizer data
def view_fertilizers(args):
    data = load_data()
    for fertilizer in data:
        print(f"ID: {fertilizer['id']}, Name: {fertilizer['name']}, Stock: {fertilizer['stock']}, Reception Date: {fertilizer['reception_date']}, Usage Notes: {fertilizer['usage_notes']}")

# Setup CLI
def main():
    parser = argparse.ArgumentParser(description="Fertilizer Management CLI")
    subparsers = parser.add_subparsers()

    # Add fertilizer command
    parser_add = subparsers.add_parser('add', help='Add new fertilizer data')
    parser_add.add_argument('--id', type=int, required=True, help='ID of the fertilizer')
    parser_add.add_argument('--name', type=str, required=True, help='Name of the fertilizer')
    parser_add.add_argument('--stock', type=int, required=True, help='Stock of the fertilizer')
    parser_add.add_argument('--reception_date', type=str, required=True, help='Reception date of the fertilizer (YYYY-MM-DD)')
    parser_add.add_argument('--usage_notes', type=str, required=True, help='Usage notes of the fertilizer')
    parser_add.set_defaults(func=add_fertilizer)

    # View fertilizers command
    parser_view = subparsers.add_parser('view', help='View all fertilizer data')
    parser_view.set_defaults(func=view_fertilizers)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
