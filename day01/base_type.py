def first_demo():
    print("hhhhh")
    print('eeeee')


def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')




 #def int_demo():
     #aint = 21
     # print(type(aint))
def str_demo():
    astr = '24'
    print(type(astr))
def float_demo():
    age = 8.29
    print(type(age))
def add_demo(b,c):
    print(b+c)
def type_zhuanhuan():
    g = 8
    print(type(g))
    print(type(str(g)))
    print(type(int(g)))
def str_jion():
    g = 7
    d = '傻'
    p = 8.29
    print(str(g)+d+str(p))

    print('g是%s,d是%s,p是%s'%(g,d,p))
def jianfa_demo(a,b):
    c = a-b
    return c        #返回值
def jiajian_demo(c,d):
    a = c-d
    return a








if __name__ == '__main__':
    #float_demo()
    #add_demo(800,900)
    #type_zhuanhuan()
    #str_jion()
    #c = jianfa_demo(8,4)
    #d = add_demo(8,4)           #1
    #print(c)
    #print(d)
    #print(type(d))
    a = jianfa_demo(9,5)
    e = add_demo(9,5)
    print(a)
    print(e)
    print(type(e))




