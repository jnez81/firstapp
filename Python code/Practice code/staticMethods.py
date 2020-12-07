# Static methods

class Math:

    @staticmethod  # does not change any attribute 'static'
    def add5(x):
        return x + 5

print(Math.add5(5))