
import tabula

dfs = tabula.read_pdf("Enter the filename or path of pdf file", pages='all')
#print(dfs)
tabula.convert_into("Enter the filename or path of pdf file", "Enter the filename or path of csv file", output_format="csv", pages='all/no of specific pages you want')

