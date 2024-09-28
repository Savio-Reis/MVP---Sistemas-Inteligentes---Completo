from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# DataSet de dados que serão testados
url_dados = "MachineLearning/data/dataset_car.csv"
colunas = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'result']
# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
    
# Método para testar pipeline Gradient Boosting a partir do arquivo correspondente
def test_modelo_GB():
    # Importando pipeline de Gradient Boosting
    rf_path = 'MachineLearning/pipelines/gb_car_pipeline.pkl'
    modelo_rf = Pipeline.carrega_pipeline(rf_path)

    # Obtendo as métricas do Gradient Boosting
    acuracia_rf = Avaliador.avaliar(modelo_rf, X, y)
    
    # Testando as métricas do Gradient Boosting
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_rf >= 0.90

