


class Base(object):
    def test(self):
        print("-----Base")
class A(Base):
    def test(self):
        print("----A")
class B(Base):
    def test(self):
        print("----B")
class C(A, B):
    def test(self):
        print("-----C")
c = C()
c.test()