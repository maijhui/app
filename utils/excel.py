from xlrd import open_workbook


class Excel():
    def __init__(self,excel_path="C:\\Users\\Administrator\\Desktop\\excel.xlsx",
                 has_title=False,
                 sheet_number=1):

        self.excel_path = excel_path  #excel路径
        self.sheet_number = sheet_number  #哪个表
        self.has_title = has_title  #是否有标题

    def excel_reader(self):
        datas=list()  #创建一个list
        workbook=open_workbook(self.excel_path)  #打开excel
        if type(self.sheet_number) ==int:
            sheetx=workbook.sheet_by_index(self.sheet_number)  #判断sheet_number的类型int还是str
        else:
            sheetx=workbook.sheet_by_name(self.sheet_number)

        if self.has_title:
            title=sheetx.row_values(0)
            for col in range(1,sheetx.nrows):
                datas.append(dict(zip(title,sheetx.row_values(col)))) #先拆散，title+0行数据，title+1行数据，title+2行数据，再组合
        else:
            for col in range(0,sheetx.nrows):  #遍历每一列，nrows是所有行，nrow=3
                datas.append(sheetx.row_values(col))  #0行数据，1行数据，2行数据

        return datas

if __name__=="__main__":
    datas=Excel().excel_reader()
    print(datas)
