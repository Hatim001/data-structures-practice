

class A:
    def function1(self):
        print(self.val1)


class B(A):

    val1 = "Hi there!!"

    def __init__(self):
        self.function1()

obj1 = B()