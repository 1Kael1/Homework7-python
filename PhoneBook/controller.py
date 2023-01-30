import view
import functions


def Start():
    current_phonebook = functions.GetDataFromColumns('PhoneBook\PBdata.txt')
    stop = False

    while not stop:
        user_choice = view.GetUserChoice()

        if user_choice == '1':
            new_phone = view.GetNewPhone()
            functions.MatchingNumbers(current_phonebook, new_phone)

        elif user_choice == '2':
            path = view.GetFilePath()
            if int(view.GetDataType('import')) - 1:
                new_phones = functions.GetDataFromRows(path)
            else:
                new_phones = functions.GetDataFromColumns(path)
            functions.MatchingNumbers(current_phonebook, new_phones)

        elif user_choice == '3':
            path = view.GetFilePath()

            if int(view.GetExportFileType()) - 1:
                if int(view.GetDataType('export')) - 1:
                    functions.ExportContactsInTXTColumns(path, current_phonebook)
                else:
                    functions.ExportContactsInCSV(path, '\contacts.txt', current_phonebook)
                    
            else:
                functions.ExportContactsInCSV(path, '\contacts.csv', current_phonebook)
        else:
            stop = True

    functions.SaveData(current_phonebook)
