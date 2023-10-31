class Rectangle:
    def __init__(self,chieuDai,chieuRong, Color):
        self.chieuDai =chieuDai
        self.chieuRong =chieuRong
        self.Color = Color
    
    def perimeter(self):
        return (self.chieuDai+self.chieuRong)*2

    def area(self):
        return self.chieuDai*self.chieuRong
    
    def color(self):
        mauSac = str(self.Color)
        return mauSac[0].upper() + self.mauSac[1::].lower()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.a10rea(), r.color()))
    