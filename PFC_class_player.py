class User:
    def __init__(self):
        self.player = self._test()
        print(self.player)
   
    def _test(self):        
        test= input("Pierre, Feuille, Ciseaux ?")

