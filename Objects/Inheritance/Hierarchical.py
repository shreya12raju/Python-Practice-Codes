class Demo1:
    def disp1(self):
        print('Inside disp1')

class Demo2(Demo1):
    def disp2(self):
        print('Inside disp2')

class Demo3(Demo1):
    pass

d2 = Demo2()
d2.disp1()
d2.disp2()