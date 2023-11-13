from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def obter_clima(api_key, cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"
    resposta = requests.get(url)
    dados_clima = resposta.json()

    if resposta.status_code == 200:
        temperatura = dados_clima['main']['temp']
        descricao_clima = dados_clima['weather'][0]['description']
        return f"Clima em {cidade}: {descricao_clima}, Temperatura: {temperatura}°C"
    else:
        return f"Erro ao obter informações de clima para {cidade}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clima',methods=['POST'])
def clima():
    cidade_alvo = request.form['cidade']
    chave_api = 'chave_api'  # Substitua pela sua chave da API OpenWeatherMap
    resultado_clima = obter_clima(chave_api, cidade_alvo)
    return render_template('resultado.html', resultado=resultado_clima)

if __name__ == '__main__':
    app.run(debug=True)