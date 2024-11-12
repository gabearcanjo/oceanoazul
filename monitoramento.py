import Adafruit-CircuitPython-DHT
import time

# Definindo o tipo do sensor e o pino GPIO
sensor = Adafruit-CircuitPython-DHT.DHT22
pin = 4  # Alterar para o pino correto onde o sensor está conectado

# Função para ler a temperatura e a umidade
def ler_temperatura():
    # Tenta obter a leitura do sensor
    humidade, temperatura = Adafruit-CircuitPython-DHT.read_retry(sensor, pin)
    
    if humidade is not None and temperatura is not None:
        return temperatura
    else:
        print("Falha na leitura do sensor.")
        return None

# Função para verificar a temperatura
def verificar_temperatura():
    temperatura = ler_temperatura()
    
    if temperatura is not None:
        print(f"Temperatura da água: {temperatura}°C")
        
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



