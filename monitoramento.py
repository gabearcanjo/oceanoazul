import time
import adafruit_dht
import board
import os

# Função para verificar se estamos no GitHub Actions ou em um ambiente com GPIO
def is_github_actions():
    return 'GITHUB_ACTIONS' in os.environ

# Se estivermos em um ambiente sem GPIO (GitHub Actions), simula os valores
if is_github_actions():
    print("Rodando no GitHub Actions, simulando valores...")
    def ler_temperatura():
        temperatura = 25.0  # Simulando 25°C
        humidade = 60.0     # Simulando 60% de umidade
        return temperatura, humidade
else:
    # Caso contrário, usa o sensor real
    sensor = adafruit_dht.DHT22(board.D4)  # O sensor está conectado no pino GPIO 4

    def ler_temperatura():
        try:
            humidade = sensor.humidity
            temperatura = sensor.temperature

            if humidade is not None and temperatura is not None:
                return temperatura, humidade
            else:
                print("Falha na leitura do sensor.")
                return None, None
        except RuntimeError as e:
            print(f"Erro na leitura do sensor: {e}")
            return None, None

# Função para verificar a temperatura
def verificar_temperatura():
    temperatura, humidade = ler_temperatura()

    if temperatura is not None and humidade is not None:
        print(f"Temperatura: {temperatura}°C, Umidade: {humidade}%")
        limite_min = 18  # Temperatura mínima recomendada para corais
        limite_max = 30  # Temperatura máxima recomendada para corais

        if temperatura < limite_min:
            print("Alerta: Temperatura muito baixa!")
        elif temperatura > limite_max:
            print("Alerta: Temperatura muito alta!")
        else:
            print("Temperatura ideal.")
    time.sleep(10)  # Aguardar 10 segundos antes da próxima leitura

# Loop para monitorar a tem
