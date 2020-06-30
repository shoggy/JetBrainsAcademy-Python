# Write your code here
import random
import sqlite3

ENTER_MONEY_TRANSFER = "Enter how much money you want to transfer:\n"

ENTER_CARD_NUMBER = "Enter card number:\n"

DB_DELETE_BY_ID = '''
    delete from card
    where id=:c_id
    '''

DB_GENERATE_ID = '''
        select coalesce(max(id) + 1, 1)
        from card
        '''

DB_INSERT = '''
        insert into card (id, number, pin, balance)
        values (:c_id, :num, :pin, :bal)
        '''

DB_UPDATE_BY_ID = '''
        update card
        set number=:num, pin=:pin, balance=:bal
        where id=:c_id
        '''

DB_SELECT_BY_NUMBER = '''
    select id, number, pin, balance
    from card
    where number=:num
    '''

DB_CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS card (
        id INTEGER,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
    )
    '''

ENTER_PIN = "Enter your PIN:\n"

ENTER_CARD = "Enter your card number:\n"

ENTER_INCOME = "Enter income:\n"

MAIN_MENU = '''
1. Create an account
2. Log into account
0. Exit
'''

CARD_MENU = '''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
'''

CARD_CREATE_REPORT = '''
Your card has been created
Your card number:
{}
Your card PIN:
{}
'''

ERROR_WRONG_CREDS = "Wrong card number or PIN!"

ERROR_LOW_MONEY = "Not enough money!"

ERROR_SAME_ACCOUNT = "You can't transfer money to the same account!"

ERROR_LUHN = "Probably you made mistake in the card number. Please try again!"

ERROR_CARD_DOES_NOT_EXISTS = "Such a card does not exist."

SUCCESSFUL_CREDS = "You have successfully logged in!"

SUCCESSFUL_LOG_OUT = "You have successfully logged out!"

SUCCESSFUL_INCOME = "Income was added!"

SUCCESSFUL_CLOSED = "The account has been closed!"

SUCCESS = "Success!"

BYE = "Bye!"


class Card:
    def __init__(self, number, pin, balance=0, c_id=None):
        self.c_id = c_id
        self.number = number
        self.pin = pin
        self.balance = balance

    def __repr__(self) -> str:
        return f"Card: [id: {self.c_id}, number: {self.number}, " \
               f"pin: {self.pin}, balance: {self.balance}]"


def add_last_digit_by_luhn(seq: str) -> str:
    nums = [int(x) for x in seq]
    nums = [nums[i] if i % 2 else 2 * nums[i] for i in range(len(nums))]
    nums = [i if i < 10 else i - 9 for i in nums]
    acc = sum(nums)
    return seq + str((10 - (acc % 10)) % 10)


def generate_card_number():
    return add_last_digit_by_luhn(f"400000"
                                  f"{random.randint(0, 999_999_999):09d}")


def generate_pin():
    return f"{random.randint(0, 9999):04d}"


def save_card(card: Card):
    print(f"DEBUG: save: {card}")
    if card.c_id is None:
        cursor = conn.execute(DB_GENERATE_ID)
        card.c_id = cursor.fetchone()[0]
        print(f"DEBUG: insert: {card}")
        conn.execute(DB_INSERT,
                     {"c_id": card.c_id, "num": card.number,
                      "pin": card.pin, "bal": card.balance})
    else:
        print(f"DEBUG: update: {card}")
        conn.execute(DB_UPDATE_BY_ID,
                     {"c_id": card.c_id, "num": card.number,
                      "pin": card.pin, "bal": card.balance})
    conn.commit()
    # cards[card.number] = card


def delete_card(card: Card):
    print(f"DEBUG: delete: {card}")
    conn.execute(DB_DELETE_BY_ID, {"c_id": card.c_id})
    conn.commit()


def is_valid_card_pin(number, pin) -> bool:
    card = get_card(number)
    return card is not None and card.pin == pin


def get_card(number: str) -> Card:
    cursor = conn.execute(DB_SELECT_BY_NUMBER, {"num": number})
    ress = cursor.fetchall()
    if len(ress):
        res = ress[0]
        c = Card(res[1], res[2], res[3], c_id=res[0])
        print(f"DEBUG: get: {c}")
        return c
    else:
        return None


def main_loop():
    while True:
        print(MAIN_MENU)
        main_choice = input().strip()
        if main_choice == "1":
            card = Card(generate_card_number(), generate_pin())
            save_card(card)
            print(CARD_CREATE_REPORT.format(card.number, card.pin))
        elif main_choice == "2":
            user_card_number = input(ENTER_CARD)
            user_pin = input(ENTER_PIN)
            if not is_valid_card_pin(user_card_number, user_pin):
                print(ERROR_WRONG_CREDS)
                continue
            print(SUCCESSFUL_CREDS)
            card = get_card(user_card_number)
            while True:
                print(CARD_MENU)
                card_choice = input().strip()
                if card_choice == "0":
                    main_choice = "0"
                    break
                elif card_choice == "1":
                    print(f"Balance: {card.balance}")
                elif card_choice == "2":
                    income = int(input(ENTER_INCOME))
                    card.balance += income
                    save_card(card)
                    print(SUCCESSFUL_INCOME)
                elif card_choice == "3":
                    print("Transfer")
                    r_num = input(ENTER_CARD_NUMBER)
                    if add_last_digit_by_luhn(r_num[:-1]) != r_num:
                        print(ERROR_LUHN)
                        continue
                    r_card = get_card(r_num)
                    print(f"DEBUG: from: {card}")
                    print(f"DEBUG: to: {r_card}")
                    if r_card is None:
                        print(ERROR_CARD_DOES_NOT_EXISTS)
                        continue
                    r_rate = int(input(ENTER_MONEY_TRANSFER))
                    if r_rate > card.balance:
                        print(ERROR_LOW_MONEY)
                        continue
                    # if r_num == card.number:
                    #     print(ERROR_SAME_ACCOUNT)
                    #     continue
                    r_card.balance += r_rate
                    save_card(r_card)
                    card.balance -= r_rate
                    save_card(card)
                    print(SUCCESS)
                elif card_choice == "4":
                    delete_card(card)
                    card = None
                    print(SUCCESSFUL_CLOSED)
                    break
                elif card_choice == "5":
                    card = None
                    print(SUCCESSFUL_LOG_OUT)
                    break
        if main_choice == "0":
            print(BYE)
            break


# cards = dict()

with sqlite3.connect('card.s3db') as conn:
    # cursor = conn.cursor()
    # cursor.execute(DB_CREATE_TABLE)
    conn.execute(DB_CREATE_TABLE)
    main_loop()
