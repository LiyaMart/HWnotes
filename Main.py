from datetime import datetime

# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять.

def create_note():
    note_title = input("Введите заголовок заметки: ").title()
    note_text = input("Введите тело заметки: ")
    note_date = datetime.now().strftime('%Y %B %A %H:%M')
    note = f"{note_date} {note_title} {note_text}\n"
    with open("notes.txt", "w", encoding="UTF-8") as file:
        file.write(note)
        file.close()
    print("Заметка добавлена")  
    
def read_file():
     with open("notes.txt", "r", encoding="UTF-8") as file:
        return file.read()

def print_file():
    print(read_file())

def delete_note():
    title_2 = input("Введите заголовок заметки на удаление: ").title()
    notes_list = read_file().rstrip().split("\n")
    try:
        for note in notes_list:
            notes_l = note.split()
            if title_2 in notes_l[4]:
                with open("notes.txt", "w", encoding="UTF-8") as file:
                    file.truncate(0)
                    notes_list.remove(note)
                    print("Заметка удалена")
                    for note in notes_list:
                        file.write(note + "\n")
            file.close()          
    except Exception:
        print("Некорректный заголовок заметки") 
             
def edit_note():
    title_3 = input("Введите заголовок заметки на редактирование: ").title()
    notes_list = read_file().rstrip().split("\n")
    try:
        for note in notes_list:
            notes_l = note.split()
            if title_3 in notes_l[4]:
                with open("notes.txt", "w", encoding="UTF-8") as file:
                    file.truncate(0)
                    notes_list.remove(note)
                    note_text = input("Введите тело заметки: ")
                    note_date = datetime.now().strftime('%Y %B %A %H:%M')
                    note = f"{note_date} {title_3} {note_text}\n"
                    notes_list.append(note)
                    print("Заметка отредактирована")
                    for note in notes_list:
                         file.write(note + "\n") 
            file.close()
    except Exception:
        print("Некорректный заголовок заметки")
       
def search_note():
    title_1 = input("Введите заголовок заметки для поиска: ").title()
    notes_list = read_file().rstrip().split("\n")
    try:
        for note in notes_list:
                notes_l = note.split()
                if title_1 in notes_l[4]:
                    print(note)
    except Exception:
        print("Некорректный заголовок заметки")

def interface():
    with open("notes.txt", "a", encoding="UTF-8"):
        pass
    command = ""
    while command != "6":
        print("Выберите вариант работы с заметкой:\n"
        "1 - Создание заметки\n"
        "2 - Вывести список заметок\n"
        "3 - Поиск заметки\n"
        "4 - Редакторовать заметку\n"
        "5 - Удалить заметку\n"
        "6 - Выход")
        command = input("Введите номер операции: ")
        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод номера операции!\n"
                  "Повторите ввод")
            command = input("Введите номер операции: ")
        match command:
            case "1":
                create_note()
            case "2":
                print_file()
            case "3":
                search_note()
            case "4":
                edit_note()
            case "5":
                delete_note()
            case "6":
                print("Приложение закрыто!")
                
interface()