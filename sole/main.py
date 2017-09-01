import serial

def main():
    arduinoSerialData = serial.Serial('/dev/ttyACM0', 9600)
    arduinoSerialData.write('5')

if __name__ == "__main__":
    main()
