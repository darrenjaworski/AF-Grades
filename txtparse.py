import csv
import glob

def lineParse(line):
    return lines[line].strip()

def lineSpliceParse(line, start, stop):
    return str(lines[line].strip()[start:stop]).strip()

high = []
low = []

for file in glob.glob("afgradestxt/*.txt"):

    #open file
    with open(file, 'r') as f:
        #per line specific scraping
        lines = f.readlines()

        lowTests = {
            "PK - 08",
            "07 - 08",
            "PK - 04",
            "05 - 08",
            "PK - 05",
            "06 - 08",
            "03 - 04",
            "PK - 06",
            "02 - 05",
            "PK - 01",
            "PK - 03",
            "04 - 05",
            "02 - 03",
            "04 - 06",
            "03 - 05",
            "KG - 05",
            "KG - 06",
            "PK - 02",
            "KG - 08",
            "03 - 06",
            "01 - 06",
            "04 - 08",
            "KG - 02",
            "PK - KG",
            "05 - 06",
            "07 - 09",
            "01 - 02",
            "05 - 06",
            "02 - 04",
            "KG - 04",
            "06 - 07",
            "01 - 05",
            "KG - 09",
            "05 - 06",
            "KG - 02",
            "PK - 07",
            "6",
            "7",
            "8",
            "06",
            "3 - 5",
            "6 - 8",
            "KG - 03",
            "01 - 04",
            "08 - 09",
            "g",
            "05",
            "08",
        }

        yearRange = lineSpliceParse(2, 6, 14)
        schoolCode = lineSpliceParse(2, 100,115)
        schoolCode = schoolCode.replace(" ","")

        if yearRange in lowTests:

            yearRange = yearRange.replace(" ", "")

            #gimmies
            readingNum = lineParse(12)
            readingPI = lineParse(16)
            readingGrade = lineParse(20)

            mathNum = lineParse(13)
            mathPI = lineParse(17)
            mathGrade = lineParse(21)

            scienceNum = lineParse(14)
            sciencePI = lineParse(18)
            scienceGrade = lineParse(22)

            ssNum = lineParse(15)
            ssPI = lineParse(19)
            ssGrade = lineParse(23)

            #more creative
            overallSPNum = lineSpliceParse(26,55,70)
            overallSPPI = lineSpliceParse(26,78,90)
            overallSPGrade = lineSpliceParse(26,101,103)

            # writingNum =
            # writingPI =
            # writingGrade =

            #student growth
            sgreadingNum = lineSpliceParse(29,17,30)
            sgreadingPI = lineSpliceParse(29,39,45)
            sgreadingGrade = lineSpliceParse(29,63,66)

            sgmathNum = lineSpliceParse(32,32,45)
            sgmathPI = lineSpliceParse(32,54,65)
            sgmathGrade = lineSpliceParse(32,78,85)

            sgoverallNum = lineSpliceParse(34,49,60)
            sgoverallPI = lineSpliceParse(34,71,85)
            sgoverallGrade = lineSpliceParse(34,95,100)

            #bottom quartile
            bqreadingNum = lineSpliceParse(39,17,30)
            bqreadingPI = lineSpliceParse(39,39,45)
            bqreadingGrade = lineSpliceParse(39,63,66)

            bqmathNum = lineSpliceParse(41,32,45)
            bqmathPI = lineSpliceParse(41,54,65)
            bqmathGrade = lineSpliceParse(41,78,85)

            bqoverallNum = lineSpliceParse(42,52,60)
            bqoverallPI = lineSpliceParse(42,71,85)
            bqoverallGrade = lineSpliceParse(42,95,100)

            schoolPI = lineSpliceParse(51,40,65)
            schoolGrade = lineSpliceParse(51,66,90)

            f.close()

            #parse all the data I need, store it in list
            array = [
                schoolCode,
                yearRange,

                readingNum,
                readingPI,
                readingGrade,

                mathNum,
                mathPI,
                mathGrade,

                scienceNum,
                sciencePI,
                scienceGrade,

                ssNum,
                ssPI,
                ssGrade,

                overallSPNum,
                overallSPPI,
                overallSPGrade,

                sgreadingNum,
                sgreadingPI,
                sgreadingGrade,

                sgmathNum,
                sgmathPI,
                sgmathGrade,

                sgoverallNum,
                sgoverallPI,
                sgoverallGrade,

                bqreadingNum,
                bqreadingPI,
                bqreadingGrade,

                bqmathNum,
                bqmathPI,
                bqmathGrade,

                bqoverallNum,
                bqoverallPI,
                bqoverallGrade,

                schoolPI,
                schoolGrade,
            ]

            low.append(array)

        else:

            yearRange = yearRange.replace(" ", "")

            #gimmies
            englishNum = lineParse(12)
            englishPI = lineParse(16)
            englishGrade = lineParse(20)

            mathNum = lineParse(13)
            mathPI = lineParse(17)
            mathGrade = lineParse(21)

            scienceNum = lineParse(14)
            sciencePI = lineParse(18)
            scienceGrade = lineParse(22)

            historyNum = lineParse(15)
            historyPI = lineParse(19)
            historyGrade = lineParse(23)

            #more creative
            overallSPNum = lineSpliceParse(25,55,70)
            overallSPPI = lineSpliceParse(25,78,90)
            overallSPGrade = lineSpliceParse(25,101,103)

            # writingNum =
            # writingPI =
            # writingGrade =

            #student growth
            sgenglishNum = lineSpliceParse(28,17,30)
            sgenglishPI = lineSpliceParse(28,39,45)
            sgenglishGrade = lineSpliceParse(28,63,66)

            sgmathNum = lineSpliceParse(30,32,45)
            sgmathPI = lineSpliceParse(30,54,65)
            sgmathGrade = lineSpliceParse(30,78,85)

            sgoverallNum = lineSpliceParse(32,49,60)
            sgoverallPI = lineSpliceParse(32,71,85)
            sgoverallGrade = lineSpliceParse(32,95,100)

            #bottom quartile
            bqenglishNum = lineSpliceParse(38,17,30)
            bqenglishPI = lineSpliceParse(38,39,45)
            bqenglishGrade = lineSpliceParse(38,63,66)

            bqmathNum = lineSpliceParse(39,32,45)
            bqmathPI = lineSpliceParse(39,54,65)
            bqmathGrade = lineSpliceParse(39,78,85)

            bqoverallNum = lineSpliceParse(40,52,60)
            bqoverallPI = lineSpliceParse(40,71,85)
            bqoverallGrade = lineSpliceParse(40,95,100)

            schoolPI = lineSpliceParse(52,50,64)
            schoolGrade = lineSpliceParse(52,65,75)

            f.close()

            array = [
                schoolCode,
                yearRange,

                englishNum,
                englishPI,
                englishGrade,

                mathNum,
                mathPI,
                mathGrade,

                scienceNum,
                sciencePI,
                scienceGrade,

                historyNum,
                historyPI,
                historyGrade,

                overallSPNum,
                overallSPPI,
                overallSPGrade,

                sgenglishNum,
                sgenglishPI,
                sgenglishGrade,

                sgmathNum,
                sgmathPI,
                sgmathGrade,

                sgoverallNum,
                sgoverallPI,
                sgoverallGrade,

                bqenglishNum,
                bqenglishPI,
                bqenglishGrade,

                bqmathNum,
                bqmathPI,
                bqmathGrade,

                bqoverallNum,
                bqoverallPI,
                bqoverallGrade,

                schoolPI,
                schoolGrade,
            ]

            high.append(array)

#write to single row in csv file
with open('high.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(high)

with open('low.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(low)
