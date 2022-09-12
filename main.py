


def main():
    print("Test")
    #debug = toggle_actuator()
    debug =
    print(debug)
    return debug




def toggle_actuator():
    import serial
    COM_PORT = "COM3"
    BAUD_RATE = 9600
    try:
        actuator = serial.Serial(port=COM_PORT, baudrate=BAUD_RATE)
        print(f"Device Found at Port {COM_PORT}. ")
        print(actuator.is_open)
    except:
        print(f"No device found at Port {COM_PORT}. ")
        return f"No device found at Port {COM_PORT}. "
    try:
        actuator.write(b"GO\r\n")
    except:
        print(f"Device Failed to Respond")
        return "Device failed to respond"
    try:
        actuator.close()
        print(actuator.is_open)
        return "Success"
    except:
        print("No open com port found")
        return "No Open Com Port Found"






def attempt_com():
    try:
        actuator = serial.Serial(port=COM_PORT, baudrate=9600)
        print(f"Device Found at Port {COM_PORT}. ")
        return actuator
    except:
        print(f"No device found at Port {COM_PORT}. ")
        return False

def TEST_toggle_actuator():
    try:
        actuator.write(b"GO\r\n")
        return True
    except:
        print(f"Device Failed to Respond")
        return False


def close_com():
    actuator.close()


if __name__ == '__main__':
    main()


