# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"1750.0","system":"readv2"},{"code":"46339.0","system":"readv2"},{"code":"19050.0","system":"readv2"},{"code":"66379.0","system":"readv2"},{"code":"83479.0","system":"readv2"},{"code":"28040.0","system":"readv2"},{"code":"48218.0","system":"readv2"},{"code":"5004.0","system":"readv2"},{"code":"1652.0","system":"readv2"},{"code":"2286.0","system":"readv2"},{"code":"14872.0","system":"readv2"},{"code":"631.0","system":"readv2"},{"code":"5351.0","system":"readv2"},{"code":"2447.0","system":"readv2"},{"code":"20632.0","system":"readv2"},{"code":"3420.0","system":"readv2"},{"code":"18931.0","system":"readv2"},{"code":"16175.0","system":"readv2"},{"code":"89963.0","system":"readv2"},{"code":"84375.0","system":"readv2"},{"code":"826.0","system":"readv2"},{"code":"2287.0","system":"readv2"},{"code":"83494.0","system":"readv2"},{"code":"27604.0","system":"readv2"},{"code":"44748.0","system":"readv2"},{"code":"2060.0","system":"readv2"},{"code":"33955.0","system":"readv2"},{"code":"3145.0","system":"readv2"},{"code":"5669.0","system":"readv2"},{"code":"4163.0","system":"readv2"},{"code":"52417.0","system":"readv2"},{"code":"21695.0","system":"readv2"},{"code":"15703.0","system":"readv2"},{"code":"57237.0","system":"readv2"},{"code":"96345.0","system":"readv2"},{"code":"67132.0","system":"readv2"},{"code":"12255.0","system":"readv2"},{"code":"18606.0","system":"readv2"},{"code":"17020.0","system":"readv2"},{"code":"28602.0","system":"readv2"},{"code":"2576.0","system":"readv2"},{"code":"89708.0","system":"readv2"},{"code":"37274.0","system":"readv2"},{"code":"72070.0","system":"readv2"},{"code":"69708.0","system":"readv2"},{"code":"11863.0","system":"readv2"},{"code":"9071.0","system":"readv2"},{"code":"4233.0","system":"readv2"},{"code":"7919.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('female-genital-prolapse-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["female-genital-prolapse-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["female-genital-prolapse-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["female-genital-prolapse-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
