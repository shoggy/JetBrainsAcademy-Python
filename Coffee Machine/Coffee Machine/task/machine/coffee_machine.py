class CoffeeMachine:
    INIT = 'INIT'
    BUY = 'BUY'
    FILL = 'FILL'
    FILL_WATER = 'FILL_WATER'
    FILL_MILK = 'FILL_MILK'
    FILL_COFFEE = 'FILL_COFFEE'
    FILL_CUPS = 'FILL_CUPS'

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.state = None
        self.fill_state = None
        self.init_state()

    def print_state(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")
        self.init_state()

    def update(self, d_water, d_milk, d_coffee, d_money, d_cups):
        if self.water + d_water < 0:
            print("Sorry, not enough water!")
        elif self.milk + d_milk < 0:
            print("Sorry, not enough milk!")
        elif self.coffee + d_coffee < 0:
            print("Sorry, not enough coffee!")
        elif self.cups + d_cups < 0:
            print("Sorry, not enough cups!")
        else:
            if d_cups < 0:
                print("I have enough resources, making you a coffee!")
            self.water += d_water
            self.milk += d_milk
            self.coffee += d_coffee
            self.money += d_money
            self.cups += d_cups

    def buy(self, coffee_type):
        if coffee_type == 1:
            self.update(-250, 0, -16, 4, -1)
        elif coffee_type == 2:
            self.update(-350, -75, -20, 7, -1)
        elif coffee_type == 3:
            self.update(-200, -100, -12, 6, -1)
        self.init_state()

    def fill(self, s):
        if self.fill_state is None:
            print("Write how many ml of water do you want to add:")
            self.fill_state = CoffeeMachine.FILL_WATER
        elif self.fill_state == CoffeeMachine.FILL_WATER:
            self.water += int(s)
            print("Write how many ml of milk do you want to add:")
            self.fill_state = CoffeeMachine.FILL_MILK
        elif self.fill_state == CoffeeMachine.FILL_MILK:
            self.milk += int(s)
            print("Write how many grams of coffee beans do you want to add:")
            self.fill_state = CoffeeMachine.FILL_COFFEE
        elif self.fill_state == CoffeeMachine.FILL_COFFEE:
            self.coffee += int(s)
            print("Write how many disposable cups of coffee do you want to add:")
            self.fill_state = CoffeeMachine.FILL_CUPS
        elif self.fill_state == CoffeeMachine.FILL_CUPS:
            self.cups += int(s)
            self.fill_state = None
            self.init_state()

    def take(self):
        print("I gave you " + str(self.money))
        self.money = 0
        self.init_state()

    def init_state(self):
        self.state = CoffeeMachine.INIT
        print("Write action (buy, fill, take, remaining, exit):")

    def process(self, s):
        if self.state == CoffeeMachine.INIT:
            if s == 'buy':
                self.state = CoffeeMachine.BUY
                print("What do you want to buy? 1 - espresso, 2 - latte, "
                      "3 - cappuccino, back - to main menu:")
            elif s == 'fill':
                self.state = CoffeeMachine.FILL
                self.fill(s)
            elif s == 'take':
                self.take()
            elif s == 'remaining':
                self.print_state()
            elif s == 'exit':
                return True
        elif self.state == CoffeeMachine.BUY:
            buy_input = s
            if buy_input == 'back':
                self.init_state()
            else:
                self.buy(int(buy_input))
        elif self.state == CoffeeMachine.FILL:
            self.fill(s)

        pass


machine = CoffeeMachine()
while not machine.process(input()):
    pass
