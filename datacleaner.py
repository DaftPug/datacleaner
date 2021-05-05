import csv

provinces = {'copenhagen' : {}}


def cleaner(unclean_file, report_file, charge_file):
    """TODO: Docstring for cleaner.
    :returns: TODO

    """
    with open(unclean_file, newline='') as f:
        # dialect = csv.Sniffer().sniff(f.read1024))
        # reader = csv.DictReader(f, dialect=dialect)

        reader = csv.reader(f, delimiter=';')
        # reader = csv.DictReader(f, delimiter=';')
        header = next(reader)
        # print (next(reader))
        # print (next(reader))
        # print (next(reader))
        # prwint (next(reader))
        with open(report_file, 'w', newline='') as w, open(charge_file, 'w', newline='') as x:
            report_writer = csv.writer(w, delimiter=';')
            charge_writer = csv.writer(x, delimiter=';')
            row_h1 = ''
            row_h2 = ''
            # header[0] = 'Reported criminal offences'
            header[1] = 'Offence'
            header[2] = 'Region / City'
            i = 3
            header_length = len(header)

            while i < header_length:
                year = str(2007 - 3 + i)
                header[i] = year
                i += 1

            header.pop(0)
            report_writer.writerow(header)

            # header[0] = 'Charged criminal offences'
            charge_writer.writerow(header)
            for row in reader:
                if row[0] != '':
                    row_h1 = row[0]
                else:
                    row[0] = row_h1
                if row[1] != '':
                    row_h2 = row[1]
                else:
                    row[1] = row_h2
                if row[0] == 'Reported criminal offences':
                    row.pop(0)
                    report_writer.writerow(row)
                else:
                    row.pop(0)
                    charge_writer.writerow(row)



def main():
    cleaner('./data/cities_STRAF22.csv', './data/cities_reported.csv', './data/cities_charged.csv')
    cleaner('./data/regions_STRAF22.csv', './data/regions_reported.csv', './data/regions_charged.csv')


            # print(row)


if __name__ == "__main__":
    main()

