class BusinessCard:
  def __init__(self, name, lastname, company, workplace, email):
      self.name = name
      self.lastname = lastname
      self.company = company
      self.workplace = workplace
      self.email = email

  def __str__(self):
      return f"{self.name} {self.lastname} - {self.email}"

  def contact(self):
      print(f"Kontaktuję się z {self.name} {self.lastname}, {self.workplace}, email: {self.email}")

  @property
  def full_name_length(self):
      return len(f"{self.name} {self.lastname}")

# Tworzenie obiektów reprezentujących wizytówki
card1 = BusinessCard(name="Janusz", lastname="Sawicki", company="Ernst Home Centers", workplace="Upholsterer", email="JanuszSawicki@jourrapide.com")
card2 = BusinessCard(name="Lucjusz", lastname="Król", company="Quality Merchant Services Occupation", workplace="Coin, vending, and amusement machine servicer", email="LucjuszKrol@armyspy.com")
card3 = BusinessCard(name="Witołd", lastname="Wiśniewski", company="Jay Jacobs", workplace="Local truck driver", email="WitoldWisniewski@armyspy.com")
card4 = BusinessCard(name="Zygmunt", lastname="Nowakowski", company="King Carol", workplace="Hotel detective", email="ZygmuntNowakowski@armyspy.com")
card5 = BusinessCard(name="Przemko", lastname="Grabowski", company="Delchamps", workplace="Public health dentist", email="PrzemkoGrabowski@jourrapide.com")

# Lista przechowująca wizytówki
cards_list = [card1, card2, card3, card4, card5]

# Wyświetlanie informacji z wizytówek
for index, card in enumerate(cards_list, start=1):
  print(f"{index}. {card}")

# Wybór kontaktu przez użytkownika
choice = int(input("Wybierz numer kontaktu (od 1 do 5): "))

if 1 <= choice <= 5:
  chosen_card = cards_list[choice - 1]
  chosen_card.contact()
  print(f"Długość imienia i nazwiska {chosen_card.name} {chosen_card.lastname}: {chosen_card.full_name_length}")
else:
  print("Nieprawidłowy wybór. Wybierz numer od 1 do 5.")

