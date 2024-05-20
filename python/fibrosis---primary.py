# Eleanor L Axson, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"C370.00","system":"readv2"},{"code":"1854801000006104","system":"readv2"},{"code":"1760721000006102","system":"readv2"},{"code":"1855391000006100","system":"readv2"},{"code":"1834221000006107","system":"readv2"},{"code":"1834231000006105","system":"readv2"},{"code":"1708981000006103","system":"readv2"},{"code":"515611000000104","system":"readv2"},{"code":"1854861000006103","system":"readv2"},{"code":"1838061000006100","system":"readv2"},{"code":"1854841000006102","system":"readv2"},{"code":"1854871000006105","system":"readv2"},{"code":"1854851000006100","system":"readv2"},{"code":"1760711000006105","system":"readv2"},{"code":"1834251000006103","system":"readv2"},{"code":"1854881000006108","system":"readv2"},{"code":"515631000000107","system":"readv2"},{"code":"1708961000006108","system":"readv2"},{"code":"698529000","system":"readv2"},{"code":"1834271000006108","system":"readv2"},{"code":"1854661000006104","system":"readv2"},{"code":"1760731000006104","system":"readv2"},{"code":"526071000000104","system":"readv2"},{"code":"776981000000103","system":"readv2"},{"code":"1854901000006105","system":"readv2"},{"code":"1763651000006106","system":"readv2"},{"code":"859041000000103","system":"readv2"},{"code":"426705001","system":"readv2"},{"code":"1763641000006109","system":"readv2"},{"code":"190909002","system":"readv2"},{"code":"1854791000006100","system":"readv2"},{"code":"190905008","system":"readv2"},{"code":"427022004","system":"readv2"},{"code":"86092005","system":"readv2"},{"code":"1854911000006108","system":"readv2"},{"code":"1854771000006101","system":"readv2"},{"code":"1708971000006101","system":"readv2"},{"code":"1834241000006100","system":"readv2"},{"code":"1709341000006101","system":"readv2"},{"code":"526091000000100","system":"readv2"},{"code":"1854831000006107","system":"readv2"},{"code":"1854811000006101","system":"readv2"},{"code":"81423003","system":"readv2"},{"code":"1834261000006101","system":"readv2"},{"code":"1854691000006107","system":"readv2"},{"code":"1854781000006103","system":"readv2"},{"code":"86555001","system":"readv2"},{"code":"E84","system":"readv2"},{"code":"E84","system":"readv2"},{"code":"CA25","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cystic-fibrosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fibrosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fibrosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fibrosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
