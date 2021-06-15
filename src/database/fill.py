from datetime import date

from .models.user import User
from .models.book import Book

async def fill_with_test_data():
    if await User.all().count() != 0: return
    
    users = [
        await User.create(name = "Adam Reśka", NIP = "9910282393", mail="a.reska@gmail.com"),
        await User.create(name = "Mikołaj Zbrzezny", phone="+48738293624"),
        await User.create(name = "Adam Mickiewić", address="Częstochowa, Marii 23"),
        await User.create(name = "Paulina Szczepiorek", NIP = "9910282393", mail="szczepiorek@gmail.com"),
        await User.create(name = "Kasia", mail="mkasia@gmail.com"),
        await User.create(name = "Andrzej Kapczynski", NIP = "8830273648", mail="akap@gmail.com", phone="+48739639264")
    ]
    
    books = [
        await Book.create(
            author = "Adam Mickiewić",
            title="Czas na zabawy",
            description="Nie ma czasu? Nie ma zabaw? super fajna.",
            publication_date = date(1997, 12, 4),
            info = "Bardzo fajna. klienci kupuja",
            price = 8000,
            count_in_stock = 10,
            discount = None
        ),
        await Book.create(
            author = "Adolph Hitler",
            title="Mein Kampf",
            description="Historia Adolpha Hitlera",
            publication_date = date(1942, 8, 12),
            info = None,
            price = 12000,
            count_in_stock = 20,
            discount = 2000
        ),
    ]
