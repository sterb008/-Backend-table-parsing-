from prettytable import PrettyTable
class  example6:
    def readTableF(book, td):#td это просто таблица ниже шапки, то есть список элементов попорядку, который я буду формировать в fiweWays
        sheet = book["Sheet1"]
        i = 1
        a = str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value), str(sheet["C" + str(i)].value), str(
            sheet["D" + str(i)].value), str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value), str(
            sheet["G" + str(i)].value), str(sheet["H" + str(i)].value), str(sheet["I" + str(i)].value), str(
            sheet["J" + str(i)].value), str(sheet["K" + str(i)].value)

        th = a#наша шапка и она всегда одинакова
      #  td = []


        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(table)