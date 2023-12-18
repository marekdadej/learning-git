from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, name, lastname, phone, email):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.email}"

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.lastname}")

    @property
    def label_length(self):
        return len(f"{self.name} {self.lastname}")

class BusinessContact(BaseContact):
    def __init__(self, name, lastname, phone, email, company, workplace, business_phone):
        super().__init__(name, lastname, phone, email)
        self.company = company
        self.workplace = workplace
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.lastname}")

    @property
    def label_length(self):
        return len(f"{self.name} {self.lastname}")

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        if contact_type == "Base":
            contact = BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        elif contact_type == "Business":
            contact = BusinessContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.company(), fake.job(), fake.phone_number())
        contacts.append(contact)
    return contacts

# Tworzenie wizytówek
base_contacts = create_contacts("Base", 5)
business_contacts = create_contacts("Business", 5)

# Wyświetlanie informacji z wizytówek
def display_contacts(contacts):
  for index, contact in enumerate(contacts, start=1):
      print(f"{index}. {contact}")

def display_contact_info(contact):
  print(f"Imię i nazwisko: {contact.name} {contact.lastname}")
  print(f"Email: {contact.email}")

  if isinstance(contact, BaseContact):
      print(f"Numer telefonu: {contact.phone} (Prywatny)")
  elif isinstance(contact, BusinessContact):
      print(f"Numer telefonu: {contact.business_phone} (Służbowy)")

print("Typy danych do wyboru:")
print("1. Dane prywatne")
print("2. Dane firmowe")

choice = input("Wybierz numer (1 lub 2): ")

if choice == "1":
  display_contacts(base_contacts)
  contact_choice = int(input("Wybierz numer kontaktu do wyświetlenia: "))
  if 1 <= contact_choice <= len(base_contacts):
      display_contact_info(base_contacts[contact_choice - 1])
      base_contacts[contact_choice - 1].contact()
  else:
      print("Nieprawidłowy numer kontaktu.")
elif choice == "2":
  display_contacts(business_contacts)
  contact_choice = int(input("Wybierz numer kontaktu do wyświetlenia: "))
  if 1 <= contact_choice <= len(business_contacts):
      display_contact_info(business_contacts[contact_choice - 1])
      business_contacts[contact_choice - 1].contact()
  else:
      print("Nieprawidłowy numer kontaktu.")
else:
  print("Nieprawidłowy wybór.")
