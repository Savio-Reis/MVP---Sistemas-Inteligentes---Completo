document.getElementById('carForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const preco = parseInt(document.getElementById('preco').value);
    const manutencao = parseInt(document.getElementById('manutencao').value);
    const portas = parseInt(document.getElementById('portas').value);
    const capacidade = parseInt(document.getElementById('capacidade').value);
    const portaMalas = parseInt(document.getElementById('portaMalas').value);
    const seguranca = parseInt(document.getElementById('seguranca').value);

    // Montar o form para consulta
    const formData = new FormData();
    formData.append('buying', preco);
    formData.append('maint', manutencao);
    formData.append('doors', portas);
    formData.append('persons', capacidade);
    formData.append('lug_boot', portaMalas);
    formData.append('safety', seguranca);


    let url = 'http://127.0.0.1:5000/carro';

    fetch(url, {
        method: 'post',
        body: formData
    })
        .then((response) =>
            response.json())
        .then((res) => {
            let resultado = '';

            if (res.result == 1)
                resultado = 'Inaceitável (Unacc)';

            if (res.result == 2)
                resultado = 'Aceitável (Acc)';

            if (res.result == 3)
                resultado = 'Bom (Good)';

            if (res.result == 4)
                resultado = 'Muito Bom (VGood)';
        
            // Exibindo o resultado
            document.getElementById('resultado').textContent = `Resultado: ${resultado}`;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});