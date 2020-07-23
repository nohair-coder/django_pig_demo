# import xlrd
#
# # 导入数据及x、y散点坐标
# data = xlrd.open_workbook('1.xlsx')
# table = data.sheets()[0]   # 通过索引顺序获取
# Hdata=table.row_values(0)  # 获取每行数据
# Ldata=table.col_values(0)  # 获取每列数据
# x=table.col_values(0)
# x=np.array(x)
# y=table.col_values(1)
# y=np.array(y)
