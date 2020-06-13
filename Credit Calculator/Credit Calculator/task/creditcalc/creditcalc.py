import argparse
import math
from argparse import Namespace

INCORRECT_PARAMETERS = 'Incorrect parameters'


def get_principal(a: float, i: float, n: int) -> int:
    """
    a -- annuity payment
    i -- nominal (monthly) interest rate
    n -- number of payments
    """
    return math.floor(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))


def get_number_of_payments(p: int, a: float, i: float) -> int:
    """
    p -- credit principle
    a -- annuity payment
    i -- nominal (monthly) interest rate
    """
    return math.ceil(math.log(a / (a - i * p), 1 + i))


def get_monthly_payment(p: int, i: float, n: int) -> int:
    """
    p -- credit principle
    i -- nominal (monthly) interest rate
    n -- number of payments
    """
    return math.ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))


def get_last_payment(p: int, i: float, n: int) -> int:
    """
    p -- credit principle
    i -- nominal (monthly) interest rate
    n -- number of payments
    """
    return p - n * get_monthly_payment(p, i, n)


def get_diff_m_payment(p: int, i: float, n: int, m: int) -> int:
    """
    p -- credit principle
    i -- nominal (monthly) interest rate
    n -- number of payments
    """
    return math.ceil(p / n + i * (p - (p * (m - 1)) / n))


def get_year_and_month_string(years: int, months: int) -> str:
    years_s = f"{years} year{'' if years % 10 == 1 else 's'}"
    months_s = f"{months} month{'' if months % 10 == 1 else 's'}"
    result = ''
    if years:
        result += years_s
    if years and months:
        result += ' and '
    if months:
        result += months_s
    return result


def validate_args(args: Namespace) -> bool:
    if args.type not in ['annuity', 'diff']:
        return False

    none_count = 0

    if args.payment is None:
        none_count += 1
    elif args.payment <= 0:
        return False

    if args.principal is None:
        none_count += 1
    elif args.principal <= 0:
        return False

    if args.periods is None:
        none_count += 1
    elif args.periods <= 0:
        return False

    if args.interest is None:
        return False
    elif args.interest <= 0:
        return False

    if none_count != 1:
        return False

    if args.type == 'diff' and args.payment is not None:
        return False

    return True


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=int, )
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

principal_inp = args.principal
annuity_inp = args.payment
periods_inp = args.periods
interest_inp = args.interest * 0.01 / 12 if args.interest is not None else None

if not validate_args(args):
    print(INCORRECT_PARAMETERS)
elif args.type == 'annuity':
    if annuity_inp is None:
        annual = get_monthly_payment(principal_inp, interest_inp, periods_inp)
        print(f"Your annuity payment = {annual}!")
        print(f"Overpayment = {annual * periods_inp - principal_inp}")
    elif principal_inp is None:
        principal = get_principal(annuity_inp, interest_inp, periods_inp)
        print(f"Your credit principal = {principal}!")
        print(f"Overpayment = {annuity_inp * periods_inp - principal}")
    elif periods_inp is None:
        periods = get_number_of_payments(principal_inp,
                                         annuity_inp,
                                         interest_inp)
        print(f"You need "
              f"{get_year_and_month_string(periods // 12, periods % 12)}"
              f" to repay this credit!")
        print(f"Overpayment = {annuity_inp * periods - principal_inp}")
elif args.type == 'diff':
    paid = 0
    for i in range(periods_inp):
        this_month = get_diff_m_payment(principal_inp,
                                        interest_inp,
                                        periods_inp,
                                        i + 1)
        paid += this_month
        print(f"Month {i + 1}: paid out {this_month}")
    print(f"\nOverpayment = {paid - principal_inp}")
