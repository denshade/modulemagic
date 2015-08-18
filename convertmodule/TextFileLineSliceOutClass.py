__author__ = 'lveeckha'


def execute(row):
    SourceFile = row["SourceFile"]
    RowNumbers = row["RowNumbers"]
    Outputfile = row["Outputfile"]
    write_file = open(Outputfile, 'w')
    read_file = open(SourceFile, 'r')
    counter = 1
    numbers = RowNumbers.split(";")
    numbers = list(map(int, numbers))
    for line in read_file:
        if counter in numbers:
            counter += 1
            continue
        write_file.write(line)
        counter += 1


def show_params():
    return "SourceFile;RowNumbers;Outputfile\nThe text file to slice data out of.;semicolon separated lines to slice out.;The file to write to."
