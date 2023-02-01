import openpyxl
from openpyxl import Workbook , load_workbook 

book = load_workbook("dars.xlsx")
sheet = book.active
print(sheet["A10"].value) 