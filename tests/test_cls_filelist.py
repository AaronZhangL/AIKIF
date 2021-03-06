#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_cls_file.py
# unit testing for collection class


import unittest
import os
import sys

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'lib')
op_folder = os.path.join(root_folder, 'tests', 'test_results')

import cls_filelist as fl 
                    
class TestClassFile(unittest.TestCase):
 
    def setUp(self):
        self.fname = root_folder + os.sep + 'tests/test_results/cls_filelist_results1.csv'
        
    def test_01_file_result(self):
        """
        test filelist with one file
        """
        lst1 = fl.FileList([root_folder + os.sep + 'tests'], ['test_*.py'], [],  self.fname)
        self.assertEqual(len(lst1.get_list()) > 18, True) 
        self.assertTrue(len(lst1.TodayAsString()) > 10)
        
    def test_02_multiple_file_result(self):
        """
        test Collecting multiple file metadata
        """
        lst2 = fl.FileList([root_folder + os.sep + 'tests'], ['*.*'], [],  self.fname)
        self.assertEqual(len(lst2.get_list()) > 30, True) 
        
    def test_03_exclude_files(self):
        """
        test exclude files
        """
        #lst3 = fl.FileList([root_folder + os.sep + 'tests'], ['*.*'], ['myenv', '__pycache__', 'htmlcov'],  self.fname)
        # self.assertEqual(len(lst3.get_list()) > 3, True) 
        # self.assertEqual(len(lst3.get_file_list([root_folder + os.sep + 'tests'], ['*.*'], ['myenv', 'pycache'],VERBOSE=True)) > 3, True) 
        pass 
        
        
    def test_04_save_filelist(self):
        """ 
        test saving filelist  
        """
        
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        aikif_fl = fl.FileList([root_folder + os.sep + 'tests'], ['*.py'], [],  self.fname)
        aikif_fl.save_filelist(self.fname, ["name", "path", "size", "date"])
        if os.path.isfile(self.fname):
            self.assertEqual("File Exists", "File Exists") 
        else:
            self.assertEqual("File Exists", "Whoops - nope") 

    def test_05_check_metadata(self):
        """ 
        make sure metadata is correct for this file 
        """
        lst5 = fl.FileList([os.path.dirname(os.path.abspath(__file__))], ['test_cls_filelist.py'], [],  self.fname)
        files = lst5.get_metadata()
        for file_dict in files:
            self.assertEqual(file_dict["name"], 'test_cls_filelist.py') 
            self.assertTrue(file_dict["size"] > 2500) 
            self.assertTrue(file_dict["date"] > '2014-08-12 21:32:57') 
            self.assertEqual(file_dict["path"], os.path.dirname(os.path.abspath(__file__))) 
    
    def test_06_check_duplicate_folders(self):
        """ 
        not really a test but more checking the version of python works as expected 
        """
        lst = ['C:\\AAA', 'C:\\BBB', 'C:\\BBB', 'C:\\CCC', 'C:\\BBB', 'C:\\CCC']
        self.assertEqual(len(lst), 6)
        self.assertEqual(len(list(set(lst))), 3)

    def test_07_filelistGroup(self):
        fl_grp = fl.FileListGroup("AIKIF lib files", os.getcwd(), "E:\\backup")
        print(fl_grp)
        self.assertTrue(len(str(fl_grp)) > 6, True)
 
        
    def test_08_metadata_columns(self):
        fldr = os.path.dirname(os.path.abspath(__file__))
        fl8 = fl.FileList([fldr], ['*.py'], [], "sample_filelist.csv")
        #col_headers = ["name", "size", "date", "path"]
        #col_headers = ["name", "date", "size"]
        col_headers = ["name", "path", "size", "date", "fullfilename"]
        for f in fl8.fl_metadata:
            txt = fl8.print_file_details_in_line(f["fullfilename"], col_headers)
            self.assertTrue(len(str(txt)) > 6, True)
    
        line = fl8.print_file_details_as_csv('fake file', ["name", "path", "size", "date", "fullfilename"])
        print(line)
        self.assertEqual(line, '"fake file","","Unknown size","Unknown Date","fake file",')
    

        
        
if __name__ == '__main__':
    unittest.main()