import json

# Функция для загрузки данных из файла
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

# Функция для сохранения данных в файл
def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

# Функция для добавления контакта
def add_contact(name, number, group, contacts):
    if group not in contacts:
        contacts[group] = []
    contacts[group].append({"name": name, "number": number})

# Функция для удаления контакта
def delete_contact(name, group, contacts):
    if group in contacts:
        for contact in contacts[group]:
            if contact["name"] == name:
                contacts[group].remove(contact)
                print(f"Контакт {name} удален из группы {group}")
                break
        else:
            print("Контакт не найден")
    else:
        print("Группа не найдена")

# Функция для поиска контакта по имени
def search_contact_by_name(name, contacts):
    found = False
    for group, group_contacts in contacts.items():
        for contact in group_contacts:
            if contact["name"] == name:
                print(f"Номер {name}: {contact['number']}, Группа: {group}")
                found = True
    if not found:
        print("Контакт не найден")

# Функция для поиска контакта по номеру телефона
def search_contact_by_number(number, contacts):
    found = False
    for group, group_contacts in contacts.items():
        for contact in group_contacts:
            if contact["number"] == number:
                print(f"Контакт с номером {number} найден: {contact['name']}, Группа: {group}")
                found = True
    if not found:
        print("Контакт с указанным номером не найден")

# Функция для изменения контакта
def update_contact(old_name, old_number, new_name, new_number, contacts):
    for group, group_contacts in contacts.items():
        for contact in group_contacts:
            if contact["name"] == old_name and contact["number"] == old_number:
                contact["name"] = new_name
                contact["number"] = new_number
                print("Контакт успешно изменен")
                return
    print("Контакт не найден")

# Функция для импорта контактов из файла
def import_contacts(file_name, contacts):
    imported_data = load_data(file_name)
    contacts.update(imported_data)

# Основная функция программы
def main():
    file_name = "contacts.json"
    contacts = load_data(file_name)

    while True:
        print("\nМеню:")
        print("1. Просмотреть все контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Найти контакт по имени")
        print("5. Найти контакт по номеру телефона")
        print("6. Изменить контакт")
        print("7. Импортировать контакты")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nКонтакты:")
            for group, group_contacts in contacts.items():
                print(f"Группа: {group}")
                for contact in group_contacts:
                    print(f"{contact['name']}: {contact['number']}")
        elif choice == "2":
            name = input("Введите имя: ")
            number = input("Введите номер: ")
            group = input("Введите название группы: ")
            add_contact(name, number, group, contacts)
            save_data(contacts, file_name)
        elif choice == "3":
            name = input("Введите имя контакта, который нужно удалить: ")
            group = input("Введите название группы: ")
            delete_contact(name, group, contacts)
            save_data(contacts, file_name)
        elif choice == "4":
            name = input("Введите имя контакта, который нужно найти: ")
            search_contact_by_name(name, contacts)
        elif choice == "5":
            number = input("Введите номер телефона, который нужно найти: ")
            search_contact_by_number(number, contacts)
        elif choice == "6":
            old_name = input("Введите текущее имя контакта: ")
            old_number = input("Введите текущий номер контакта: ")
            new_name = input("Введите новое имя: ")
            new_number = input("Введите новый номер: ")
            update_contact(old_name, old_number, new_name, new_number, contacts)
            save_data(contacts, file_name)
        elif choice == "7":
            import_file_name = input("Введите имя файла для импорта: ")
            import_contacts(import_file_name, contacts)
            save_data(contacts, file_name)
        elif choice == "8":
            print("Выход из программы")
            break
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()
