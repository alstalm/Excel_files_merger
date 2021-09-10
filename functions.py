import pandas as pd
import os
import openpyxl as op


def tryer(path, file, sheet_name, notNANcolumnsList):
    full_path = path + file
    try:
        df = pd.read_excel(full_path, sheet_name=sheet_name).dropna(subset=notNANcolumnsList)  # .loc[0,'GTIN\n(Код товара)']
        print('func 10: df=\n', df.to_string())

        # df2[['ИНН участника']] = df2[['ИНН участника']].astype('int32')
        # df2.loc[0,'ИНН участника']
        # df2.astype({'ИНН участника': np.int32})
        # df2.dtypes
        return df
    except Exception as e:
        # print(e)
        x = file + '\t' + str(e)  # ' Не иметт вкладки Внесение изменений' +
        return x

def excelCombiner(directory, sheet_name, notNANcolumnsList):
    '''
    directory - папка в которой необходимо выполнить поиск .xls / xlsx файлов,
    sheet_name - вкладка из которой надо прочитать данные
    notNANcolumnsList - по какому столбце ориентироваться для удаления незаполненных строк
    '''

    full_attr_df = pd.DataFrame()
    directory = directory
    file_list = os.listdir(directory)
    log = []

    path = directory + '/'

    for file in file_list:
        print('func 38: file =', file)
        answer = tryer(path=path, file=file, sheet_name=sheet_name, notNANcolumnsList=notNANcolumnsList)
        if isinstance(answer, str):
            log.append(answer)
            print('func 42: результат чтений файла - лог')
        else:
            print('func 44: результат чтений файла - датафрейм')
            curent_attr_df = answer
            curent_attr_df['fileName'] = file

            if len(full_attr_df) < 1:
                full_attr_df = curent_attr_df.copy()
            else:
                print('func 51: объединение датафреймов уже не первое')
                full_attr_df = pd.concat([full_attr_df, curent_attr_df])
                print('func 53: full_attr_df=\n', full_attr_df)
    log_df = pd.DataFrame(log)
    print('func 52: log_df', log_df)
    try:
        log_df = log_df[0].str.split('\t', expand=True)
        log_df = pd.DataFrame(log_df.values, columns=['fileName', 'errorMeassge'])
        print('func 54: log_df', log_df)
    except KeyError:
        log_df = pd.DataFrame(columns=['fileName', 'errorMeassge'])


    print('func 56: log_df', log_df)
    return full_attr_df, log_df