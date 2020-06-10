# put your python code here
duration = int(input())
food = int(input())
one_way_ticket = int(input())
hotel_cost = int(input())
print(duration * food + one_way_ticket * 2 + (duration - 1) * hotel_cost)
