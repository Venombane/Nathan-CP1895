class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Other(Publication):
    def __init__(self, period, publisher, title, price):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, author, title, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Other):
    def __init__(self, period, publisher, title, price):
        super().__init__(period, publisher, title, price)


class Newspaper(Other):
    def __init__(self, publisher: str, title: str, price: float, period: str):
        super().__init__(period, publisher, title, price)


def main():
    book1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
    news1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
    mag1 = Magazine("Monthly", "Scientific American", "Springer Nature", 5.99)

    print(book1.author)
    print(news1.publisher)
    print(book1.price, mag1.price, news1.price)


if __name__ == "__main__":
    main()
