#coding=utf-8
import xlrd

class ReadExcle(object):
    '''
    read the excel
    '''

    def __init__(self, file, tag='True'):
        self.file = file
        self.tag = tag

    '''
        Enter the parameters and return all the values in a sheet list
        Sheetname: sheetname of excel file
        N: number of first lines, read from the NTH line
        Num: read num rows
    '''

    def read(self, sheetname, n=1, num=1000):  # i,sheet index
        ExcelFile = xlrd.open_workbook(self.file)
        table = ExcelFile.sheet_by_name(sheetname)
        nrows = table.nrows  # rows
        ncols = table.ncols  # cols
        j = 0  # cycles
        for row in range(1, nrows):
            j += 1
            line = []
            if self.tag == 'True':
                for col in range(0, ncols):
                    line.append(table.cell(row, col).value)
                yield line
            elif self.tag == 'False':
                if j >= n and j < n + num:
                    for col in range(0, ncols):
                        line.append(table.cell(row, col).value)
                    yield line

    '''
         Read the table of page elements
         List1 page element path list
         List2 page element js list
    '''

    def get(self, sheetname):
        ExcelFile = xlrd.open_workbook(self.file)
        sheet = ExcelFile.sheet_by_name(sheetname)  # 'Sheet1'
        nrows = sheet.nrows  # rows
        list0 = []  # List of element names
        list1 = []  # Element path list
        list2 = []  # Js list
        for i in range(1, nrows):  # i for the number of rows
            if sheet.row(i)[2].value != 'null':
                r1 = sheet.row(i)[2].value
                r2 = sheet.row(i)[3].value
                list0.append(sheet.row(i)[0].value)
                list1.append(r1 + '=>' + r2)
                dict1 = dict(zip(list0, list1))
            else:
                list2.append(sheet.row(i)[3].value)
        return dict1, list2

    '''
        Returns the value of a specific cell in an excel sheet
        I and j are the locations of cells
    '''

    def read_1(self, sheetname, i, j):
        ExcelFile = xlrd.open_workbook(self.file)
        table = ExcelFile.sheet_by_name(sheetname)
        # print(table.cell(1,0).value)
        return table.cell(i, j).value

    '''
               Reads a given number of columns, such as number 3 in the table
    '''

    def read_ncols(self, sheetname,i):  # i,sheet索引
        ExcelFile = xlrd.open_workbook(self.file)
        table = ExcelFile.sheet_by_name(sheetname)
        lins=table.col_values(i)
        return lins
