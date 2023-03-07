
class spisok:
    def __init__(self, data):
        self.First = elm(data, None)
        self.current = self.First

    def goto_s(self):
        self.current = self.First

    def ap_right(self, data):
        a = elm(data, self.current.ra)
        self.current.ra = a

    def next(self):
        self.current = self.current.ra

    def date(self):
        return self.current.da
    def show(self):
        self.current = self.First
        ret = []
        while(self.current.ra != None):
            ret.append(self.current.da)
            self.current = self.current.ra
        return ret
    def check(self,fi):
        self.current = self.First
        while (self.current.ra != None):
            if fi == self.current.da:
                return(True)
            self.current = self.current.ra
        return(False)
    def delit_n(self):
        return


class elm:
    def __init__(self, data, right):
        self.ra = right
        self.da = data

p = spisok(input())
p.ap_right(0)
for i in range(5):
    p.ap_right(input())
p.goto_s()
print(p.show())
print(p.check('9'))
print(p.check('11'))
