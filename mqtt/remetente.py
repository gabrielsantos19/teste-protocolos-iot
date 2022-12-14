"""
Autor: Gabriel Oliveira Santos
Referência: https://github.com/eclipse/paho.mqtt.python
"""

import paho.mqtt.client as mqtt
import time


CENARIO = 6
INTERVALO = 40    # em milissegundos

BROKER_HOST = "192.168.56.1"
BROKER_PORT = 1883
LOG_FILE = f"../_logs/mqtt_remetente_cenario_{CENARIO}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"
ARQUIVO_TESTE = f"../_arquivos_teste/cenario_{CENARIO}.txt"
INTERVALO_NS = INTERVALO * 1000000    # Converter para segundo


log_file = open(LOG_FILE, "w")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    

try:
    print(f'CENARIO={CENARIO}')
    print(f'INTERVALO={INTERVALO}')
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_start()

    contador = 0
    t = time.time_ns()
    print(f"INICIO,{t}")
    with open(ARQUIVO_TESTE, "r") as f:
        for l in f.readlines():
            l = l[:-1]    # Remover o \n do final da linha
            t = time.time_ns()
            m = f"{contador:04},{t},{l}"
            e = m.encode("utf-8")
            client.publish("ponte/x", m)
            print(contador)
            print(m, file=log_file)
            contador += 1

            delta = INTERVALO_NS - (time.time_ns() - t)
            if delta > 0:
                time.sleep(delta / 1000000000)
    
    # Atraso pré-finalização, para permitir eventuais procedimentos da última mensagem
    time.sleep(5)
    t = time.time_ns()
    print(f"FIM,{t}")
    client.loop_stop(force=False)
except KeyboardInterrupt:
    pass
finally:
    log_file.close()