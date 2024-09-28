from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
carro_tag = Tag(name="Carro", description="Predição do melhor carro para a compra")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de avaliação de carro
@app.post('/carro', tags=[carro_tag],
          responses={"200": CarroViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_carro(form: CarroSchema):
    """Realiza a predição do carro
    Retorna uma representação de um carro

    Args:
        
            buying : 1, 2, 3, 4 (low, med, high, vhigh) 
            maint: 1, 2, 3, 4 (low, med, high, vhigh)
            doors: 2, 3, 4, 5 (5 = Mais de 4)
            persons: 2, 4, 5 (5 = Mais de 4)
            lug_boot: 1, 2, 3 (small, med, big)
            safety: 1, 2, 3 (low, med, high)
            result: 1, 2, 3, 4 (unacc, acc, good, vgood)

    Returns:
        result: Retorna uma resposta dizendo se o carro é uma boa opção
    """
    # Recuperando os dados do formulário
    buying = form.buying
    maint = form.maint
    doors = form.doors
    persons = form.persons
    lug_boot = form.lug_boot
    safety = form.safety
    

    # Preparando os dados para o modelo de predição
    X_input = PreProcessador.preparar_form(form)  # Ajustar para avaliação de carros
    # Carregando modelo de machine learning
    model_path = 'MachineLearning/pipelines/gb_car_pipeline.pkl'
    modelo = Pipeline.carrega_pipeline(model_path)
    
    # Realizando a predição gerar a melhor opção de carro
    predicted_type = int(Model.preditor(modelo, X_input)[0])

    # Criando a instância dos carros com a predição
    carro = Carro(
        buying,
        maint,
        doors,
        persons,
        lug_boot,
        safety,
        result=predicted_type  # Resultado da predição
    )
    
    try:
        # Retorna a representação da melhor opção de carro
        return apresenta_carro(carro), 200
    
    # Caso ocorra algum erro no processo
    except Exception as e:
        error_msg = "Não foi possível encontrar um carro:/"
        logger.warning(f"Erro ao processar dados: {error_msg}")
        return {"message": error_msg}, 400

if __name__ == '__main__':
    app.run(debug=True)