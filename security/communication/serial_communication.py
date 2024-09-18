from typing import Any
import serial
import time


class SerialCommunication:
    """
    Handle serial communication between the python script
    and the microcontroller
    """
    # CONSTRUCTOR
    def __init__(
                    self,
                    port: str = 'COM3',
                    baud_rate: int = 9600,
                    timeout: float = .1,
                    encoding: str = 'utf-8'

                ) -> None:

        self.__port: str = port
        self.__baud_rate: int = baud_rate
        self.__timeout: float = timeout
        self.__encoding: str = encoding
        self.__serial_connection: Any = None

    # PUBLIC METHODS
    def read(self) -> str:
        self.__connect()
        return self.__serial_connection.read()

    def write(self, message: str) -> None:
        self.__connect()
        self.__serial_connection.write(bytes(message, self.__encoding))

    def close(self) -> None:
        self.__serial_connection.close()
        self.__serial_connection = None

    # PRIVATE METHODS
    def __connect(self) -> None:
        if not self.__serial_connection:
            self.__serial_connection = serial.Serial(
                self.__port,
                self.__baud_rate,
                timeout=self.__timeout
            )
            time.sleep(.001)
