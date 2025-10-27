class Calculator(object):
    def sum(self,x,y):
        return x + y
    
    def sbt(self,x,y):
        return x - y
    
    def mlt(self,x,y):
        return x * y
    
    def div(self,x,y):
        try:
            return x / y
        except ZeroDivisionError as err:
            return 0
        
    def sqr(self,x):
        return x ** 2
    
    def cub(self,x):
        return x ** 3
    
    def exp(self,x,y):
        return x ** y
    
    def flr(self,x,y):
        return x // y
    
    def mod(self,x,y):
        return x % y

    def avg(self,x,y):
        return (x + y)/2
