import unittest
from requester import url_to_csv, batch_url_to_csv, url_to_df
import urllib2
import os
import pandas as pd
import csv


class TestFunThings(unittest.TestCase):
    def setUp(self):
        self.site1 = 'http://winterolympicsmedals.com/medals.csv'
        self.site2 = 'http://surajprasadjoshi.com'
        self.site3 = ''
        self.site4 = 'http://winterolympicsmedals.com/medals.csv'
        self.list_unparsable = ['http://surajprasfadjoshi.com','http://josfhisurajprasad.com']
        self.list_invalid = ['run','jump','roll']
        self.list_type = ['http://github.com','http://github.com', 'http://github.com']
        self.list_mixbag = ['http://winterolympicsmedals.com/medals.csv','run', 'http://surajpradddsadjoshi.com','https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data','jump', 'http://surajprasadjoshi.com']
        self.filelist_mixbag = ['test41.csv','test42.csv','test43.csv','test44.csv','test45.csv','test46.csv']
        self.filelist1 = ['test1.csv','test2.csv','test3.csv']
        
    # Task 1
    def test_url_unparsable(self):
        self.assertRaises(TypeError, url_to_csv, self.site1)

    def test_url_error(self):
        self.assertRaises(urllib2.URLError, url_to_csv, self.site2, 'test.csv')

    # Task 2
    def test_url_invalid(self):
        self.assertRaises(ValueError, url_to_csv, self.site3, 'test_site4.csv')

    # Task 3
    def test_batch_no_url_error(self):
        for file in os.listdir(os.getcwd()):
            if file.endswith('.csv'):
                os.remove(file)
        try:
            batch_url_to_csv(self.list_mixbag, self.filelist_mixbag)
        except TypeError as e:
            raise RuntimeError

    # Task 4
    def test_batch_valid_url_number(self):
        for file in os.listdir(os.getcwd()):
            if file.endswith('.csv'):
                os.remove(file)
        self.assertEquals(batch_url_to_csv(self.list_mixbag, self.filelist_mixbag),\
            [os.path.abspath(thefile) for thefile in os.listdir(os.getcwd()) if thefile.endswith(".csv")])

    # Task 5
    def test_batch_url_different(self):
        for file in os.listdir(os.getcwd()):
            if file.endswith('.csv'):
                os.remove(file)
        files5 = batch_url_to_csv(self.list_mixbag, self.filelist_mixbag)
        segment1 = open(files5[0])
        segment2 = open(files5[1])
        self.assertNotEqual(segment1.readline(), segment2.readline())

    # Task 6
    def test_batch_correct_filenames(self):
        self.assertEqual(batch_url_to_csv(self.list_mixbag, self.filelist_mixbag)[0],os.path.abspath(self.filelist_mixbag[0]))
        self.assertEqual(batch_url_to_csv(self.list_mixbag, self.filelist_mixbag)[1], os.path.abspath(
            self.filelist_mixbag[3]))

    # Task 7
    def test_batch_correct_number_files(self):
        self.assertEquals(len(batch_url_to_csv(self.list_mixbag, self.filelist_mixbag)), 2)

    # Task 8
    def test_url_duplicate(self):
        duplicate_list = []
        for i, a in enumerate(self.list_mixbag):
            if self.list_mixbag[i] in duplicate_list:
                raise AssertionError("Duplicate URLs cannot be present in the parameter 'urls'.")
            else:
                duplicate_list.append(self.list_mixbag[i])

    # Task 9
    def test_df_returnsPdDf(self):
        self.assertTrue(type(url_to_df(self.site1)), pd.DataFrame())

    # Task 10
    def test_df_equal_rows(self):
        response = urllib2.urlopen(self.site1)
        csv_f = csv.reader(response, None)
        count = 0
        for i in csv_f:
            count += 1
        self.assertEqual(len(url_to_df(self.site4).index), count-1)


    # python -m unittest discover