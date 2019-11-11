#coding=utf-8
from common.getfilename import GetFileName
import time
import xlwt
import os
import xlrd
from xlutils.copy import copy
class WriteExcel():
    def creat_excel(self):
        '''
        create xls file
        '''
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        exceldir = '../excelreport/'
        excelname = exceldir+ rq + '.xls'
        workbook = xlwt.Workbook()
        workbook.add_sheet('Sheet')
        workbook.save(excelname)


    def write_excel(self,row, data):
        '''
        write data to xls
        :param row:which row
        :param data:the rows data
        :return:
        '''
        #get downloadfile all file names
        dir = os.path.abspath('..')
        url = dir + "\\excelreport\\"
        files=GetFileName().getfilename(url)
        # calculate the length of the file
        len1 = len(os.listdir(url))
        out_path = url + files[len1 - 1]
        #write to xls
        wbk = xlwt.Workbook(encoding='utf-8')
        sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
        for i in range(len(data)):
            sheet.write(row, i, data[i])
        print(out_path)
        wbk.save(out_path)

    def write_excel_xls_append(self,value):
        'Gets the file name under the downloadfile folder'
        dir = os.path.abspath('..')
        url = dir + "\\excelreport\\"
        files = GetFileName().getfilename(url)
        # Calculate folder length
        len1 = len(os.listdir(url))
        out_path = url + files[len1 - 1]

        workbook = xlrd.open_workbook(out_path)  # open the workbook
        sheets = workbook.sheet_names()  # Gets all the tables in the workbook
        worksheet = workbook.sheet_by_name(sheets[0])  # Gets the first of all tables in the workbook
        rows_old = worksheet.nrows  # Gets the number of rows of data that already exist in the table
        new_workbook = copy(workbook)  # Convert the XLRD object copy to an XLWT object
        new_worksheet = new_workbook.get_sheet(0)  # Gets the first table in the transformed workbook
        for i in range(0,len(value)):
            new_worksheet.write(rows_old, i, value[i])  # Append write data
        new_workbook.save(out_path)  # Save workbook
        print("xls additional data success！")