class Carro():

    def __init__(self, 
                    buying:int,
                    maint:int,
                    doors:int,
                    persons:int,
                    lug_boot:int,
                    safety:int,
                    result:int):
                    
        """
            Cria a classe Carro

            Arguments:
            buying : 1, 2, 3, 4 (low, med, high, vhigh)
            maint: 1, 2, 3, 4 (low, med, high, vhigh)
            doors: 2, 3, 4, 5 (5 = Mais de 4)
            persons: 2, 4, 5 (5 = Mais de 4)
            lug_boot: 1, 2, 3 (small, med, big)
            safety: 1, 2, 3 (low, med, high)
            result: 1, 2, 3, 4 (unacc, acc, good, vgood)

        """
        self.buying = buying
        self.maint = maint
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety
        self.result = result
       
        
