class master:
    def header(self, id):  # original
        print("This is main header", 1)

    def footer(Self, id):
        print("This is main footer", 1)


class home(master):
    def header(self, id):  # xerox
        return super().header(id)


class about(master):
    def header(self, id):
        return super().header(id)
