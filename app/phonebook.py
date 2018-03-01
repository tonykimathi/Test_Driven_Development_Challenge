class phonebookclass(object):

    contact_list = []
    phonebook = {}

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

        self.phonebook[name] = phone_number

    def add_contact(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

        if name is None or len(name) < 1:
            return "Item must have a name"

        if not isinstance(name, str):
            return "name must be a string"

        if not isinstance(phone_number, int):
            return "phone number must be a int"

        if phone_number is None or len(str(phone_number)) < 6:
            return "phone number should have at least 6 digits"

        self.phonebook[name] = phone_number

        self.contact_list.append(self.phonebook)

        return "Number added successfully"

    def updateContact(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

        self.phonebook[name] = phone_number

        self.contact_list.append(self.phonebook)

        return "Phone book updated correctly"

    def viewContacts(self):
        all_contacts = []

        for item in self.contact_list:
            all_contacts.append(item)

        return all_contacts


    def deleteContacts(self, phone_number):
        count = 0
        for item in self.contact_list:
            if str(phone_number) == phone_number:
                self.contact_list.pop(count)
                del item
                return True
            count += 1

        return "Number has been deleted."

