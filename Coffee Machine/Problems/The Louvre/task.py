class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year
        self.output = f'"{title}" by {painter} ({year}) ' \
                      f'hangs in the {Painting.museum}.'


painting = Painting(input(), input(), input())
print(painting.output)
