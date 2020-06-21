# put your python code here
init_list = input().split()
x = input().strip()
position_list = [str(i) for i in range(len(init_list)) if init_list[i] == x]
print(" ".join(position_list) if len(position_list) > 0 else "not found")
