# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"1594.00","system":"readv2"},{"code":"K51..00","system":"readv2"},{"code":"9356.0","system":"readv2"},{"code":"10888.0","system":"readv2"},{"code":"24299.0","system":"readv2"},{"code":"12845.0","system":"readv2"},{"code":"22757.0","system":"readv2"},{"code":"3986.0","system":"readv2"},{"code":"37185.0","system":"readv2"},{"code":"22659.0","system":"readv2"},{"code":"96896.0","system":"readv2"},{"code":"97649.0","system":"readv2"},{"code":"30419.0","system":"readv2"},{"code":"41136.0","system":"readv2"},{"code":"47681.0","system":"readv2"},{"code":"41895.0","system":"readv2"},{"code":"33440.0","system":"readv2"},{"code":"12359.0","system":"readv2"},{"code":"37373.0","system":"readv2"},{"code":"25278.0","system":"readv2"},{"code":"7870.0","system":"readv2"},{"code":"105178.0","system":"readv2"},{"code":"23941.0","system":"readv2"},{"code":"1345.0","system":"readv2"},{"code":"37918.0","system":"readv2"},{"code":"6819.0","system":"readv2"},{"code":"1057.0","system":"readv2"},{"code":"25974.0","system":"readv2"},{"code":"4575.0","system":"readv2"},{"code":"2285.0","system":"readv2"},{"code":"53883.0","system":"readv2"},{"code":"2846.0","system":"readv2"},{"code":"1903.0","system":"readv2"},{"code":"7175.0","system":"readv2"},{"code":"6882.0","system":"readv2"},{"code":"211.0","system":"readv2"},{"code":"42057.0","system":"readv2"},{"code":"17481.0","system":"readv2"},{"code":"73219.0","system":"readv2"},{"code":"102653.0","system":"readv2"},{"code":"37790.0","system":"readv2"},{"code":"N81","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('female-genital-prolapse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["prolapse---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["prolapse---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["prolapse---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
