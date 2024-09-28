from pydantic import BaseModel
from model import Carro

class CarroSchema(BaseModel):
    """ Define como será realizada a pesquisa de preço
    """

    buying: int = 1
    maint: int = 3
    doors: int = 5
    persons: int = 5
    lug_boot: int = 1
    safety: int = 3

class CarroViewSchema(BaseModel):
    """ Define como irá retornar o carro
    """
    
    buying: int = 1
    maint: int = 3
    doors: int = 5
    persons: int = 5
    lug_boot: int = 1
    safety: int = 3
    result: int = 3

# Apresenta apenas os dados de um animal    
def apresenta_carro(carro: Carro):
    """ Retorna uma representação do carro seguindo o schema definido em
        CarroViewSchema.
    """
    return {
        "buying": carro.buying,
        "maint": carro.maint,
        "doors": carro.doors,
        "persons": carro.persons,
        "lug_boot": carro.lug_boot,
        "safety": carro.safety,
            "result": carro.result
    }
