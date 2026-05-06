class Vault:
    def __init__(self, galleons=0, sickles=0 , knuts=0):
        self.galleons = galleons
        self.sickels = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"
    

potter = Vault(100, 50, 25)
print(potter)

wesaley = Vault(25, 50, 100)
print(wesaley)


galleons = potter.galleons + wesaley.galleons
sickles = potter.sickels + wesaley.sickels
knuts = potter.knuts + wesaley.knuts

total = Vault(galleons, sickles, knuts)
print(total)