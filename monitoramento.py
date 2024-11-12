import time
import adafruit_dht
import board

# Definindo o tipo do sensor e o pino GPIO
sensor = adafruit_dht.DHT22(board.D4)  # O sensor está conectado no pino GPIO 4

# Função para ler a temperatura e a umidade
def ler_temperatura():
    try:
        # Tenta obter a leitura do sensor
        humidade = sensor.humidity
        temperatura = sensor.temperature

        if humidade is not None and temperatura is not None:
            return temperatura, humidade
        else:
            print("Falha na leitura do sensor.")
            return None, None
    except RuntimeError as e:
        # Erro de leitura, por exemplo, falha na comunicação com o sensor
        print(f"Erro na leitura do sensor: {e}")
        return None, None

# Função para verificar a temperatura
def verificar_temperatura():
    temperatura, humidade = ler_temperatura()

    if temperatura is not None and humidade is not None:
        print(f"Temperatura da água: {temperatura}°C, Umidade: {humidade}%")

        # Definir limites críticos para a temperatura
        limite_min = 18  # Temperatura mínima recomendada para corais
        limite_max = 30  # Temperatura máxima recomendada para corais

        if temperatura < limite_min:
            print("Alerta: Temperatura da água muito baixa! Isso pode prejudicar a vida marinha.")
        elif temperatura > limite_max:
            print("Alerta: Temperatura da água muito alta! Isso pode prejudicar a vida marinha.")
        else:
            print("Temperatura ideal para a vida marinha.")
    time.sleep(10)  # Aguardar 10 segundos antes da próxima leitura

# Loop para monitorar a temperatura
while True:
    verificar_temperatura()
