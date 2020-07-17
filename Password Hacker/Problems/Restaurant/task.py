import itertools

cs = zip(main_courses, price_main_courses)
ds = zip(desserts, price_desserts)
bs = zip(drinks, price_drinks)
for (c, cp), (d, dp), (b, bp) in itertools.product(cs, ds, bs):
    tot = cp + dp + bp
    if tot <= 30:
        print(c, d, b, tot)
