from utils import get_rows

if __name__ == '__main__':
    rows = get_rows('data/russian_names.csv')

    with open('extracted_data/names.txt', 'w') as f:
        for row in rows:
            f.write(row['Name'] + '\n')

    print('End.')
