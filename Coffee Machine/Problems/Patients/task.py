class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # create methods here
    def __repr__(self) -> str:
        return f"Object of the class Patient. name: {self.name}, " \
               f"last_name: {self.last_name}, age: {self.age}"

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}. {self.age}"
