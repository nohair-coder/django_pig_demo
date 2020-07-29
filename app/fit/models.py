from django.db import models
# from scipy.optimize import curve_fit
# import xlrd
# import numpy as np
# import scipy as sp
# import math


# Create your models here.
'''
# 导入数据及x、y散点坐标
data = xlrd.open_workbook('1.xlsx')
table = data.sheets()[0]   # 通过索引顺序获取
Hdata=table.row_values(0)  # 获取每行数据
Ldata=table.col_values(0)  # 获取每列数据
x=table.col_values(0)
x=np.array(x)
y=table.col_values(1)
y=np.array(y)
'''

# class FitFunction:
#     """
#     三种函数拟合
#     """
#     def __init__(self, m, n):
#         # 导入数据及x、y散点坐标{m:行,n:列},点的坐标为(m,n)
#         # m = self.table.col_values(0)
#         self.m = m
#         # n = self.table.col_values(1)
#         self.n = n
#         # print(self.x)
#
#     # Logistic函数
#     def funl(self, x, a, b, c):
#         return a / (1 + b * np.exp(-c * x))
#
#     # Gompertz函数
#     def fung(self, x, a, b, c):
#         return a * np.exp(-b * np.exp(-c * x))
#
#     # Saturation函数
#     def funs(self, x, a, b):
#         return x / (a + b * x)
#
#     # 均方误差根
#     def rmse(self, y_test, y):
#         return np.lib.scimath.sqrt(np.mean((y_test - y) ** 2))
#
#     # 与均值相比的优秀程度，介于[0~1]。0表示不如均值。1表示完美预测. 
#     def R2(self, y_test, y_true):
#         return 1 - ((y_test - y_true) ** 2).sum() / ((y_true - y_true.mean()) ** 2).sum()
#
#     def R22(self, y_test, y_true):
#         y_mean = np.array(y_true)
#         y_mean[:] = y_mean.mean()
#         return 1 - self.rmse(y_test, y_true) / self.rmse(y_mean, y_true)
#
#     def computeCorrelation(self, X, Y):
#         xBar = np.mean(X)
#         yBar = np.mean(Y)
#         SSR = 0
#         varX = 0
#         varY = 0
#         for i in range(0, len(X)):
#             diffXXBar = X[i] - xBar
#             diffYYBar = Y[i] - yBar
#             SSR += (diffXXBar * diffYYBar)
#             varX += diffXXBar ** 2
#             varY += diffYYBar ** 2
#         SST = math.sqrt(varX * varY)
#         return SSR / SST
#
#     def SaturationFit(self):
#         # 拟合------------Saturation
#         popt, pcov = curve_fit(self.funs, self.m, self.n)
#         # 获取popt里面是拟合系数
#         # print(popt)
#         # print(pcov)
#         a = popt[0]
#         b = popt[1]
#         # yvals = self.funs(self.m, a, b)  # 拟合y值
#         y_test = self.m / (a + b * self.m)
#         # print('ssr/sst:', self.computeCorrelation(y_test, self.n))
#         # print('R2:', self.R2(y_test, self.n))
#         # print('R22', self.R22(y_test, self.n))
#         # print('rmse:', self.rmse(y_test, self.n))
#         rsqu = 'Saturation  R2:' + str(round(self.R2(y_test, self.n), 6))
#         return {'popt': [a,b], 'S_rsqu': rsqu}
#
#     def LogisticFit(self):
#         # 拟合------------Logistic
#         popt, pcov = curve_fit(self.funl, self.m, self.n, bounds=(0, [80, 24., 0.2]))
#         # 获取popt里面是拟合系数
#         a = popt[0]
#         b = popt[1]
#         c = popt[2]
#         # yvals = self.funl(self.m, a, b, c)  # 拟合y值
#         y_test = a / (1 + b * np.exp(-c * self.m))
#         # print('ssr/sst:', self.computeCorrelation(y_test, self.n))
#         # print('R2:', self.R2(y_test, self.n))
#         # print('R22', self.R22(y_test, self.n))
#         # print('rmse:', self.rmse(y_test, self.n))
#         rsqu = 'Logistic  R2:' + str(round(self.R2(y_test, self.n), 6))
#         # 拟合------------Gompertz
#         return {'popt': [a,b,c], 'L_rsqu': rsqu}
#
#     def GompertzFit(self):
#         popt, pcov = curve_fit(self.fung, self.m, self.n, bounds=(0, [100, 10., 0.5]))
#         # 获取popt里面是拟合系数
#         a = popt[0]
#         b = popt[1]
#         c = popt[2]
#         # yvals = self.fung(self.m, a, b, c)  # 拟合y值
#         y_test = a * np.exp(-b * np.exp(-c * self.m))
#         # print('ssr/sst:', self.computeCorrelation(y_test, self.n))
#         # print('R2:', self.R2(y_test, self.n))
#         # print('R22', self.R22(y_test, self.n))
#         # print('rmse:', self.rmse(y_test, self.n))
#         rsqu = 'Gompertz  R2:' + str(round(self.R2(y_test, self.n), 6))
#         return {'popt': [a,b,c], 'G_rsqu': rsqu}
