from random import choice 
from console_logging.console import Console
console = Console()


class Hal:
  @staticmethod
  def temperature():
    return choice(range(15,25))

  @staticmethod
  def umidade():
    return choice(range(60,99))

  @staticmethod
  def aquecedor(status: str):
    if status == 'on':
          console.info("aquecedor LIGADO")
    else:
          console.info("aquecedor DESLIGADO")

if __name__ == "__main__":
  hal = Hal()
  hal.aquecedor("on")
 
  hal.aquecedor("off")

  console.log(hal.umidade())
  console.log(hal.temperature())