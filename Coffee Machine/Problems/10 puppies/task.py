class Puppy:
    n_puppies = 0

    # define __new__
    def __new__(cls):
        if Puppy.n_puppies < 10:
            Puppy.n_puppies += 1
            return super().__new__(cls)
        return None
