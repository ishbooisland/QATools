# Search and download subtitles
import requests
import pyodbc
import time


def extract(source, start, end):
    if source.index(start) >= 0:
        temp = source[source.index(start) + len(start):]
        if temp.index(end) >= 0:
            temp = temp[:temp.index(end)]
        else:
            temp = ''
    else:
        temp = ''
    return temp


def download_file(url, filename):
    # local_filename = url.split('/')[-1]
    local_filename = filename
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def getSQLList(query):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=Movie_Subtitles')
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def runQuery(queryToRun):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=Movie_Subtitles')
    cursor = cnxn.cursor()
    cursor.execute(queryToRun)
    cnxn.commit()


# list of movieIds
ids = getSQLList('Select Top 500000 Cast(IDSubtitle as Varchar) AS ID From Subtitles_All Order by IDSubtitle')

for id in ids:
    try:
        print id.ID
        download_file('http://dl.opensubtitles.org/en/download/sub/vrf-108d030f/' + id.ID,
                      'C:\\Users\\Darrin\\Desktop\\subtitles\\' + id.ID + '.zip')
        runQuery(
            "Update [Movie_Subtitles].[dbo].[subtitles_all] Set isComplete = 1 Where IDSubtitle = '" + id.ID + "'")
        time.sleep(1)
    except:
        time.sleep(20)
        download_file('http://dl.opensubtitles.org/en/download/sub/vrf-108d030f/' + id.ID,
                      'C:\\Users\\Darrin\\Desktop\\subtitles\\' + id.ID + '.zip')


        # s = requests.get('http://www.opensubtitles.website/en/opensubtitles-player.subtitles-download/subtitles/' + id.ID)
        # dlPage = s.text
        # vrf = extract(dlPage, 'sub/vrf-', '/')
