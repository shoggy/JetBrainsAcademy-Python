class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = self.a * self.b / 2
        # calculate the area here


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if input_a * input_a + input_b * input_b == input_c * input_c:
    t = RightTriangle(input_c, input_a, input_b)
    print(f'{t.area:.1f}')
else:
    print("Not right")
