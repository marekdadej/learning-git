print("\n\t\tLista zakupów")

list = {
    "Piekrnia": ["Chleb", "Bułki", "Pączek", "Gniazdko", "Jagodzianka"],
    "Warzywniak": ["Marchew", "Seler", "Rukola", "Ziemniaki"],
    "Mięsny": ["Pierś kurczaka", "Udka", "Golonka", "Szynka"],
    "Samochodowego": ["Olej silnikowy", "Filtr powietrza", "Sprzęgło do matiza"]
}

total_products = 0

for sklep, produkty in list.items():
    produkty_wielka_litera = [produkt.capitalize() for produkt in produkty]
    total_products += len(produkty)
    print(f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {produkty_wielka_litera}.")

print(f"W sumie kupuję {total_products} produktów.")
