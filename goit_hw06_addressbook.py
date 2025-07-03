from collections import UserDict

# Базовий клас для полів (ім’я, телефон)
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для імені
class Name(Field):
    pass

# Клас для телефону з валідацією
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

# Клас для одного запису (контакту)
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

# Клас адресної книги
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Приклад використання 

book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# ✅ Додавання запису John до адресної книги
book.add_record(john_record)
print("✅ Додано запис John до адресної книги.")

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("8765432101")
book.add_record(jane_record)
print("✅ Додано запис Jane до адресної книги.")

# Виведення всіх записів
print("\n📒 Адресна книга:\n", book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Пошук конкретного телефону у записі John
found = john.find_phone("5555555555")
print("🔍 Знайдений номер:", found)

# Видалення запису Jane
book.delete("Jane")
