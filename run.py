from flask import Flask
from threading import Thread
from highrise.__main__ import *
import time


class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Funcionando"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()


class RunBot():
  room_id = "669175473fa7ac9ca012c5e4"
            "66be383cb835a2ea28f6c8d5"
  bot_token = "3fc201cb85e4e81de99cd349d00bbbcc9022b069eeb4f8c7176e944c07ac7ed9"
              "78eb4f44f824ef8b94b1890c8fc8a02aec353e9669feaa4c1537d74261e7b5b0"
  bot_file = "main"
  bot_class = "Bot"

  def __init__(self) -> None:
    self.definitions = [
        BotDefinition(
            getattr(import_module(self.bot_file), self.bot_class)(),
            self.room_id, self.bot_token)
    ]  # More BotDefinition classes can be added to the definitions list

  def run_loop(self) -> None:
    while True:
      try:
        arun(main(self.definitions))

      except Exception as e:
        print("Error: ", e)
        time.sleep(5)

if __name__ == "__main__":
  WebServer().keep_alive()

  RunBot().run_loop()