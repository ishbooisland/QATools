import pyodbc


def bulkLoad(query):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=Test')
    cursor = cnxn.cursor()
    cursor.execute(query)


from os import listdir
from os.path import isfile, join

mypath = 'C:\\Users\\Darrin\\Desktop\\2015_12A'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for filex in onlyfiles:
    if 'MVM_' in filex:
        print "Bulk Insert CT_AOC From '" + mypath + "\\" + filex + "' with (fieldterminator = '', ROWTERMINATOR = '0x0a')"
        bulkLoad(
            "Bulk Insert CT_AOC From '" + mypath + "\\" + filex + "' with (fieldterminator = '', ROWTERMINATOR = '0x0a')")
print "Done!"
