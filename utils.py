import csv


def get_rows(filename: str):
    input_file = csv.DictReader(open(filename), delimiter=';')

    rows = []

    for row in input_file:
        rows.append(row)

    return rows


def convert_to_ukr(rus_text: str):
    ukr_text = rus_text.replace('и', 'і').replace('ы', 'и').replace('э', 'е').replace('е', 'є')

    return ukr_text
