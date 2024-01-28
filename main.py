#задача
#Класс Книга должен содержать информацию о названии, авторе и жанре книги.


class Product:
    def __init__(self, name, genre, title):
        self.name = name
        self.genre = genre
        self.title = title

    def show_product(self):
        print(f'Product: {story.name}, genre: {story.genre}, title: {story.title}')

story = Product(name = 'Aria Maiskaya', genre = 'Travel story', title = 'Songs of our forest')
story.show_product()


#Класс БанковскийАккаунт должен хранить информацию о владельце, балансе

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


    def show_BankAccount(self):
        print(f'Product: {account.owner}, balance: {account.balance}')

account = BankAccount(owner = 'Vika Smirnova', balance = '56000')
account.show_BankAccount()