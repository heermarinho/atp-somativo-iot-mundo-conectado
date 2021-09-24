from time import sleep
import paho.mqtt.client as mqtt 
from random import choice 
from hal import Hal
from definitions import user, password, client_id, server, port 

hardware =  Hal()

def mensagem(client, userdata, msg):
  vetor = msg.payload.decode().split(",")
  hardware.aquecedor("on" if vetor[1] == '1' else 'off')
  client.publish('v1/{}/things/{}/response'.format(user,client_id),
  f'ok,{vetor[0]}')
  



client = mqtt.Client(client_id)
client.username_pw_set(user,password)
client.connect(server,port)

client.on_message = mensagem
client.subscribe('v1/{}/things/{}/cmd/2'.format(user,client_id))
client.loop_start()

def main():
  while True:
      client.publish('v1/{}/things/{}/data/0'.format(user,client_id), hardware.temperature())
      client.publish('v1/{}/things/{}/data/1'.format(user,client_id),hardware.umidade())

      sleep(10)



if __name__ == "__main__":
     main()
     client.disconnect()
