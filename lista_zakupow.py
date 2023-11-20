print("\n\t\tLista zakupów")

list = {
    "Piekrnia": ["Chleb", "Bułki", "Pączek"],
    "Warzywniak": ["Marchew", "Seler", "Rukola"]
}

total_products = 0

for sklep, produkty in list.items():
    produkty_wielka_litera = [produkt.capitalize() for produkt in produkty]
    total_products += len(produkty)
    print(f"Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {produkty_wielka_litera}.")

print(f"W sumie kupuję {total_products} produktów.")
