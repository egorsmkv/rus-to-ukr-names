from utils import convert_to_ukr

if __name__ == '__main__':
    with open('extracted_data/surnames.txt', 'r') as f:
        with open('extracted_data/ukr_surnames.txt', 'w') as h:
            for name in f:
                v = name.strip().lower()
                ukr_name = convert_to_ukr(v)
                ukr_name = ukr_name.capitalize()
                h.write(f'{ukr_name}\n')

    print('End.')
