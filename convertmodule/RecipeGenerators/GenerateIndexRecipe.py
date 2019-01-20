import os

with open("C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\recipes\\tnm.param.csv", "w") as tnmFile:
    tnmFile.write("TextFile,DictFile,IndexFile\n")
    startPath = "C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\biopsies"
    for directory in os.listdir(startPath):
        curDir = os.path.join(startPath, directory)
        if os.path.isdir(curDir):
            for filename in os.listdir(curDir):
                if filename.endswith(".txt"):
                    filename = os.path.join(curDir, filename)
                    tnmFile.write(filename + "," + "C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\dicttnm.txt," + filename + ".index\n")
                    print(filename + "," + "C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\dicttnm.txt," + filename + ".index")
                    continue

    tnmFile.close()

with open("C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\recipes\\learnTnm.csv", "w") as learnFile:
    learnFile.write("positiveFiles,negativeFiles,DictFile\n")
    startPath = "C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\biopsies"
    dictionary = {}
    for directory in os.listdir(startPath):
        curDir = os.path.join(startPath, directory)
        if os.path.isdir(curDir):
            files = []
            for filename in os.listdir(curDir):
                if filename.endswith(".txt"):
                    filename = os.path.join(curDir, filename)
                    #learnFile.write(filename + "," + "C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\dicttnm.txt" + filename + ".index")
                    files.append(filename + ".index")
        dictionary[directory] = "|".join(files)

    for currentDirectory in dictionary:
        positiveFiles = dictionary[currentDirectory]
        negativeFiles = []
        for otherDirectory in dictionary:
            if currentDirectory == otherDirectory:
                continue
            negativeFiles.append(dictionary[otherDirectory])
        print(positiveFiles+","+"|".join(negativeFiles)+",C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\dicttnm.txt")
        learnFile.write(positiveFiles+","+"|".join(negativeFiles)+",C:\\Users\\Lieven\\Documents\\GitHub\\modulemagic\\data\\dicttnm.txt\n")
    learnFile.close()
