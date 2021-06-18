import pandas as pd
import os
import openpyxl as op


def tryer(path, file, sheet_name, notNANcolumnsList):
    full_path = path + file
    try:
        df = pd.read_excel(full_path, sheet_name=sheet_name).dropna(subset=notNANcolumnsList)  # .loc[0,'GTIN\n(Код товара)']


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
        answer = tryer(path=path, file=file, sheet_name=sheet_name, notNANcolumnsList=notNANcolumnsList)
        if isinstance(answer, str):
            log.append(answer)
        else:
            curent_attr_df = answer
            curent_attr_df['fileName'] = file

            if len(full_attr_df) < 1:
                full_attr_df = curent_attr_df.copy()
            else:
                full_attr_df = pd.concat([full_attr_df, curent_attr_df])

    log_df = pd.DataFrame(log)
    log_df = log_df[0].str.split('\t', expand=True)
    log_df = pd.DataFrame(log_df.values, columns=['fileName', 'errorMeassge'])

    return full_attr_df, log_df