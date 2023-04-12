from prettytable import PrettyTable
class  example:
    def readTable(book, countStudents):
        sheet = book["Sheet1"]
        i = 1
        a = str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value), str(sheet["C" + str(i)].value), str(
            sheet["D" + str(i)].value), str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value), str(
            sheet["G" + str(i)].value), str(sheet["H" + str(i)].value), str(sheet["I" + str(i)].value), str(
            sheet["J" + str(i)].value), str(sheet["K" + str(i)].value)

        th = a
        td = []
        main_value = []

        for i in range(2, (countStudents + 2)):
            main_value = [str(sheet["A" + str(i)].value), str(sheet["B" + str(i)].value),
                          str(sheet["C" + str(i)].value)[:10], str(sheet["D" + str(i)].value),
                          str(sheet["E" + str(i)].value), str(sheet["F" + str(i)].value),
                          str(sheet["G" + str(i)].value), str(sheet["H" + str(i)].value),
                          str(sheet["I" + str(i)].value), str(sheet["J" + str(i)].value),
                          str(sheet["K" + str(i)].value)]
            # в верхней строке у C столбика вырезал значения часов минут и секнунд (00:00:00)
            td = td + main_value

        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(table)