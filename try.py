import pandas as pd

inputData = pd.read_excel("D:\\sql_input_data.xlsx")

print(inputData.columns[1])

print(inputData.values.tolist())