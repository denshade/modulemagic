import csv

result = {}
with open("C:\\test\\SELECT.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', )
    for row in reader:
        idx = row["TBFV_FK_CONTENT"]
        TBFV_STRINGVALUE = row["TBFV_STRINGVALUE"]
        TBFV_TEXTVALUE = row["TBFV_TEXTVALUE"]
        if idx not in result:
            result[idx] = {"TBFV_STRINGVALUE": "", "TBFV_TEXTVALUE": ""}

        if TBFV_STRINGVALUE != "":
            result[idx]["TBFV_STRINGVALUE"] = TBFV_STRINGVALUE

        if TBFV_TEXTVALUE != "":
            result[idx]["TBFV_TEXTVALUE"] = TBFV_TEXTVALUE

for key in result:
    t = "?"
    n = "?"
    m = "?"

    examples = [
        {"tnm": "pT1 ", "t": "1", "n": "0", "m": "0"},
        {"tnm": "pT1 pN0", "t": "1", "n": "0", "m": "0"},
        {"tnm": "pT1 pN1", "t": "1", "n": "1", "m": "0"},
        {"tnm": "pT1a n0", "t": "1a", "n": "0", "m": "0"},
        {"tnm": "pT1a n1", "t": "1a", "n": "1", "m": "0"},
        {"tnm": "pT1b", "t": "1b", "n": "0", "m": "0"},
        {"tnm": "pT1b n0", "t": "1b", "n": "0", "m": "0"},
        {"tnm": "pT1bn1", "t": "1b", "n": "1", "m": "0"},
        {"tnm": "pT1bn1a", "t": "1b", "n": "1a", "m": "0"},
        {"tnm": "pT1bn1b", "t": "1b", "n": "1b", "m": "0"},
        {"tnm": "pT1bn2", "t": "1b", "n": "2", "m": "0"},
        {"tnm": "pT1b pn0", "t": "1b", "n": "0", "m": "0"},
        {"tnm": "pT1b pn1", "t": "1b", "n": "1", "m": "0"},
        {"tnm": "pT1b pn1a", "t": "1b", "n": "1a", "m": "0"},
        {"tnm": "pT1b pn2", "t": "1b", "n": "2", "m": "0"},
        {"tnm": "pT1b(m)N2a", "t": "1b", "n": "2a", "m": "0"},
        {"tnm": "pT1b, pn0", "t": "1b", "n": "0", "m": "0"},
        {"tnm": "pT1c", "t": "1c", "n": "0", "m": "0"},
        {"tnm": "pT1c N0", "t": "1c", "n": "0", "m": "0"},
        {"tnm": "pT1c N1", "t": "1c", "n": "1", "m": "0"},
        {"tnm": "pT1c (m) N3a", "t": "1c", "n": "3a", "m": "0"},
        {"tnm": "pT1c pN0", "t": "1c", "n": "0", "m": "0"},
        {"tnm": "pT1c N1", "t": "1c", "n": "1", "m": "0"},
        {"tnm": "pT1c pN1a", "t": "1c", "n": "1a", "m": "0"},
        {"tnm": "pT2", "t": "2", "n": "0", "m": "0"},
        {"tnm": "pT2 N1", "t": "2", "n": "1", "m": "0"},
        {"tnm": "pT2 N1a", "t": "2", "n": "1a", "m": "0"},
        {"tnm": "pT2 N1c", "t": "2", "n": "1c", "m": "0"},
        {"tnm": "pT2 pN1", "t": "2", "n": "1", "m": "0"},
        {"tnm": "pT2 pN1a", "t": "2", "n": "1a", "m": "0"},
        {"tnm": "pT2 pN2", "t": "2", "n": "2", "m": "0"},
        {"tnm": "pT2c", "t": "2c", "n": "0", "m": "0"},
        {"tnm": "pT2c pN0", "t": "2c", "n": "0", "m": "0"},
        {"tnm": "pT2N0", "t": "2", "n": "0", "m": "0"},
        {"tnm": "pT2 pN1", "t": "2", "n": "1", "m": "0"},
        {"tnm": "pT2 pN2", "t": "2", "n": "2", "m": "0"},
        {"tnm": "pT3 pN1a", "t": "3", "n": "1a", "m": "0"},
        {"tnm": "pT3 pN1a", "t": "3", "n": "1a", "m": "0"},
        {"tnm": "pT3 pN2", "t": "3", "n": "2", "m": "0"},
        {"tnm": "pT3 pN2a", "t": "3", "n": "2a", "m": "0"},
        {"tnm": "pT4a pN2", "t": "4a", "n": "2", "m": "0"},
        {"tnm": "pT4b N1a", "t": "4b", "n": "1a", "m": "0"},
        {"tnm": "pT4b N1b", "t": "4b", "n": "1b", "m": "0"},
    ]

    for example in examples:
        if example["tnm"].lower().replace(" ","") in result[key]["TBFV_TEXTVALUE"].lower().replace(" ",""):
            t = example["t"]
            n = example["n"]
            m = example["m"]

    printshort = True
    if result[key]["TBFV_TEXTVALUE"] != "":
        if printshort:
            print(key + ";" + t + ";" + n + ";" + m + ';"' + result[key]["TBFV_STRINGVALUE"] + '"')
        else:
            print(key + ";" + t + ";" + n + ";" + m + ';"' + result[key]["TBFV_STRINGVALUE"] + ';"'+ result[key]["TBFV_TEXTVALUE"].replace('"','') + '"')
