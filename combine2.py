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

    for line in result[key]["TBFV_TEXTVALUE"].lower().split("\n"):
        if "tnm" not in line:
            continue

        for tlabel in [
                        "tis",
                        "tx",
                        "ta",
                        "t0",
                        "t1", "t1a", "t1b", "t1c",
                        "t2", "t2a", "t2b", "t2c",
                        "t3", "t3a", "t3b", "t3c",
                        "t4", "t4a", "t4b", "t4c",
        ]:
            if tlabel in line:
                t = tlabel[1:]

        for nlabel in [
                        "nx",
                        "n0",
                       "n1", "n1a", "n1b","n1c"
                        "n2", "n2a", "n2b","n2c"
                        "n3", "n3a", "n3b","n3c"
                        "n4", "n4a", "n4b","n4c"
                        ]:
            if nlabel in line:
                n = nlabel[1:]

        for mlabel in ["m0", "m1"]:
            if mlabel in line:
                m = mlabel[1:]

    printshort = True
    if result[key]["TBFV_TEXTVALUE"] != "":
        if printshort:
            print(key + ";" + t + ";" + n + ";" + m + ';"' + result[key]["TBFV_STRINGVALUE"] + '"')
        else:
            print(key + ";" + t + ";" + n + ";" + m + ';"' + result[key]["TBFV_STRINGVALUE"] + ';"'+ result[key]["TBFV_TEXTVALUE"].replace('"','') + '"')
