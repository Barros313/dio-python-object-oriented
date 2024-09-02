from abc import ABC, abstractmethod


def main():
    controle_samsung = TvControl()

    print(controle_samsung.turn_on())

    return None


class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class TvControl(RemoteControl):
    def turn_on(self):
        print("Ligando TV")

    def turn_off(self):
        print("Deslingando TV")

if __name__ == "__main__":
    main()