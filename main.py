import yaml
from functions import excelCombiner

# зададим переменные
with open('params.yaml', 'r', encoding='UTF-8') as f:
    params = yaml.safe_load(f)

directory = params['directory']
sheet_name = params['sheet_name']
notNANcolumnsList = params['notNANcolumnsList']
outputDirectory = params['outputDirectory']
outputResultFile = params['outputFile']
outputLogFile = params['log']

fullOutputPath = outputDirectory + '/' + outputResultFile
fullLogPath = outputDirectory + '/' + outputLogFile


# выполним объединение
df, log_df = excelCombiner(directory=directory, sheet_name=sheet_name, notNANcolumnsList=notNANcolumnsList)

# выведем результаты
print('\nlog_df =\n  {} '.format(log_df))
print('\ndf = \n {}'.format(df.to_string()))

# сохраним результаты
df.to_excel(fullOutputPath, index=False)
log_df.to_excel(fullLogPath, index=False)
