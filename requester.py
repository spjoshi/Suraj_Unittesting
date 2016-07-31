import csv
import pandas as pd
import urllib2
import os

def url_to_csv(url, fname):
    '''
    Takes a URL to a CSV file, downloads it, and saves it to a file.
    '''
    # url = 'http://winterolympicsmedals.com/medals.csv'

    response = urllib2.urlopen(url)
    csv_f = csv.reader(response)
    medals = []

    for row in csv_f:
        medals.append(row[0:20])

    with open(fname, 'w') as csv_f:
        csv_w = csv.writer(csv_f)
        csv_w.writerows(medals)
        csv_f.close()


def batch_url_to_csv(urls, fnames):
    '''
    Takes a list of URLs to CSV files, downloads them, and saves them
    to files given by the list of names in fnames.
    Returns a list of the filenames saved.
    '''
    filename_list = []

    for i in range(len(urls)):
        try:
            site = urllib2.urlopen(urls[i])
            csv_f = csv.reader(site)
            medals = []
            for row in csv_f:
                medals.append(row[0:20])

            with open(fnames[i], 'w') as csv_f:
                csv_w = csv.writer(csv_f)
                csv_w.writerows(medals)
                csv_f.close()
                file_path = os.path.join(os.getcwd(), fnames[i])
                filename_list.append(file_path)
        except Exception:
            print 'Error processing site'

    # print 'file name is : ',filename_list
    return filename_list

def url_to_df(url):
    '''
    Takes a URL to a CSV file and returns the contents of the URL as a Pandas DataFrame.
    '''
    pandas_df = pd.read_csv(url)
    print pandas_df
    print len(pandas_df.index)
    return pandas_df

if __name__ == "__main__":
    # url_to_csv('http://winterolympicsmedals.com/medals.csv', 'test.csv')
    #
    list_of_urls = ['', 'http://winterolympicsmedals.com/medals.csv', 'http://winterolympicsmedals.com/medals.csv']
    list_of_fname = ['file1.csv', 'file2.csv', 'file3.csv']
    # list_of_urls = ['http://winterolympicsmedals.com/medals.csv', 'run', 'http://surajprasadjoshi.com',
    #                     'http://winterolympicsmedals.com/medals.csv', 'jump', 'http://surajprasadjoshi.com', ]
    # list_of_fname = ['test41.csv', 'test42.csv', 'test43.csv', 'test44.csv', 'test45.csv', 'test46.csv']
    # batch_url_to_csv(list_of_urls, list_of_fname)



    (url_to_df('http://winterolympicsmedals.com/medals.csv'))