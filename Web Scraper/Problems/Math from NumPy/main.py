# import the required library
import math


def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    angle = math.radians(angle_in_degrees)
    cosine = math.cos(angle)
    res = round(cosine, 2)
    print(res)
