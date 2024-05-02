class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

# Usage
manager = ContactManager()
manager.add_contact(Contact("John Doe", "123-456-7890"))
print(manager.find_contact("John Doe").phone)
