class Demo:
    def disp1(self):
        print('Inside disp1')
    def disp(self,a):
        print('Inside disp with 1 Para')
    def disp(self,a,b):
        print('Inside disp with 2 Para')
d = Demo()
#d.disp()
#d.disp(10)
d.disp(10,20)