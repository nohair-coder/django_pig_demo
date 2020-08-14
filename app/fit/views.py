from django.http import JsonResponse
from django.views import View
from utils.Response import SuccessResponse, FailResponse

# Create your views here.

'''
导入数据及x、y散点坐标
data = xlrd.open_workbook('1.xlsx')
table = data.sheets()[0]   # 通过索引顺序获取
Hdata=table.row_values(0)  # 获取每行数据
Ldata=table.col_values(0)  # 获取每列数据
x=table.col_values(0)
x=np.array(x)
y=table.col_values(1)
y=np.array(y)
'''


# def GetPoint(request):
#     if request.method == 'GET':
#         try:
#             excel = xlrd.open_workbook("1.xlsx")
#             # excel.sheet_names()  # 获取excel里的工作表sheet名称数组
#             sheet = excel.sheet_by_index(0)  # 根据下标获取对应的sheet表
#             # sheet.row_values(0)  # 获取第一行的数据
#             # sheet.col_values(0)  # 获取第一列的数据
#             # rownum = sheet.nrows   # 获取总共的行数
#             # colnum = sheet.ncols   # 获取总共的列数
#             pointdata = []
#             for i in range(0, sheet.nrows):
#                 row_list = sheet.row_values(i)  # 每一行的数据在row_list 数组里
#                 # print(row_list)
#                 pointdata.append(row_list)
#             return SuccessResponse(pointdata)
#         except:
#             return FailResponse('请求失败')

# def GetCoefficient(request):
#     if request.method == 'GET':
#         try:
#             data = xlrd.open_workbook('1.xlsx')
#             table = data.sheets()[0]  # 通过索引顺序获取
#             Hdata = table.row_values(0)  # 获取每行数据
#             Ldata = table.col_values(0)  # 获取每列数据
#             x = table.col_values(0)
#             # print(x)
#             x = np.array(x)
#             y = table.col_values(1)
#             y = np.array(y)
#             # print(y)
#             obj = FitFunction(x, y)
#             SCoefficient = obj.SaturationFit()
#             LCoefficient = obj.LogisticFit()
#             GCoefficient = obj.GompertzFit()
#             C_list = {'SCoefficient': SCoefficient, 'LCoefficient': LCoefficient, 'GCoefficient': GCoefficient}
#             return SuccessResponse(C_list)
#         except:
#             return FailResponse('请求失败')

# class LineFit(View):
#     # 直线函数
#     def get(self, request):
#         X = [1 ,2  ,3 ,4 ,5 ,6]
#         Y = [12.5 ,13.51 ,14.45 ,15.52 ,16.47 ,17.51]
#         z1 = np.polyfit(X, Y, 1)  # 一次多项式拟合，相当于线性拟合
#         p1 = np.poly1d(z1)
#         coefficient = z1.tolist()
#         pointdata = []
#         for i in range(0, len(X)):
#             pointdata.append([X[i], Y[i]])
#         # print(pointdata)
#         return JsonResponse({'coefficient': coefficient, 'pointdata': pointdata}, status=200)
