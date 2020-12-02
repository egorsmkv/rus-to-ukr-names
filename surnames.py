from utils import get_rows

if __name__ == '__main__':
    rows = get_rows('data/russian_surnames.csv')

    with open('extracted_data/surnames.txt', 'w') as f:
        for row in rows:
            f.write(row['Surname'] + '\n')

    print('End.')
