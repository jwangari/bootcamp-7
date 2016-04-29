class PrimeChecker:
    """
    Class PrimeChecker(number), that takes in a string argument.
    When the instance of the class is called with .is_prime():
        -it should return true if number is a prime number 
        -false if it isn't prime.
    """
    def __init__(self, string=''):
        self.string= string          
    
    def is_prime(self):
        if self.string == "":
            return False

        if self.string.isdigit() == True:
            self.string = int(self.string)
        else:
            return "Enter string of numbers"
            
        if self.string == 1 :
            return True
        elif self.string == 2:
            return True
        else:
            for i in range(2, self.string):
                if (self.string % i) == 0:
                    return False
                else:
                    return True 

p = PrimeChecker("12")
p1 = PrimeChecker("2")
p2 = PrimeChecker("13")
p3 = PrimeChecker("")

print p.is_prime()
print p1.is_prime()
print p2.is_prime()
print p3.is_prime()


