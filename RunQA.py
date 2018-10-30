import pyodbc
import os

database = ""


def cleanSpaces(input):
    return input.replace('\r', ' ').replace('\n', ' ').replace(' ', '{}').replace('}{', '').replace('{}', ' ')


def getSQLList(query):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=' + database)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def appendLine(filename, text):
    with open(filename, 'a') as g:
        g.write(text)


def runOnlineIndex(sourceInput, directory):
    try:
        queriesOI = getSQLList("Select F1 From Zeus.Data_Dev.dbo.Online_Index_Prints Where ID not in ('1.01','1.02') " +
                               "Order by ID")
        source = sourceInput

        if not os.path.isdir(directory):
            os.mkdir(directory)

        with open(directory + source + '_OnlineIndex_QA_Results.sql', 'w') as f:
            f.write(source)

        for query in queriesOI:
            print cleanSpaces(query.F1).replace('xxxxx', source)
            results = getSQLList(cleanSpaces(query.F1).replace('xxxxx', source))

            if len(results) > 0:
                appendLine(directory + source + '_OnlineIndex_QA_Results.sql', '\n\n' +
                           cleanSpaces(query.F1).replace('xxxxx', source))
                for result in results:
                    amountOfColumns = len(result)
                    resultToPrint = ''

                    for i in range(0, amountOfColumns):
                        if result[i] is None:
                            resultToPrint = resultToPrint + '' + '|'
                        else:
                            resultToPrint = resultToPrint + str(result[i]) + '|'

                    appendLine(directory + source + '_OnlineIndex_QA_Results.sql',
                               '\n' + resultToPrint)

                appendLine(directory + source + '_OnlineIndex_QA_Results.sql', '\n\n' +
                           'Rows Affected(' + str(len(results)) + ')')
                appendLine(directory + source + '_OnlineIndex_QA_Results.sql', '\n' +
                           '-----------------------------------------------------------------------------------' +
                           '------------------------------------------------------------------------------------')
            results = ''
    except Exception, e:
        print e


def runOffenses(sourceInput, directory):
    try:
        queriesOF = getSQLList("Select F1 From Zeus.Data_Dev.dbo.Offenses_Prints Order by ID")
        source = sourceInput

        if not os.path.isdir(directory):
            os.mkdir(directory)

        with open(directory + source + '_Offenses_QA_Results.sql', 'w') as f:
            f.write(source)

        for query in queriesOF:
            print cleanSpaces(query.F1).replace('xxxxx', source)
            results = getSQLList(cleanSpaces(query.F1).replace('xxxxx', source))

            if len(results) > 0:
                appendLine(directory + source + '_Offenses_QA_Results.sql', '\n\n' +
                           cleanSpaces(query.F1).replace('xxxxx', source))
                for result in results:
                    amountOfColumns = len(result)
                    resultToPrint = ''

                    for i in range(0, amountOfColumns):
                        if result[i] is None:
                            resultToPrint = resultToPrint + '' + '|'
                        else:
                            resultToPrint = resultToPrint + str(result[i]) + '|'

                    appendLine(directory + source + '_Offenses_QA_Results.sql',
                               '\n' + resultToPrint)

                appendLine(directory + source + '_Offenses_QA_Results.sql', '\n\n' +
                           'Rows Affected(' + str(len(results)) + ')')
                appendLine(directory + source + '_Offenses_QA_Results.sql', '\n' +
                           '-----------------------------------------------------------------------------------' +
                           '------------------------------------------------------------------------------------')
            results = ''
    except Exception, e:
        print e


inputSource = raw_input('Source? > ')
qaDirectory = raw_input('Directory? > ')
runOnlineIndex(inputSource, qaDirectory)
print "Running Offenses"
runOffenses(inputSource, qaDirectory)
