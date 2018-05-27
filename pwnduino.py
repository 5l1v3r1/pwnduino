#!/usr/bin/python
import argparse
import subprocess
import serial
import commands

HID_HEX = "./lib/Arduino-keyboard.hex"
SERIAL_HEX = "./lib/Arduino-usbserial.hex"

def main():

    # Instantiate ArgumentParser
    parser = argparse.ArgumentParser(description='Hacking with the Arduino Uno')
    parser.add_argument('--flash', '-f', action="store_true",
        help='Flash your Arduino Uno into a malicious HID Device')
    parser.add_argument('--unflash', '-uf', action="store_true",
        help='Revert your Arduino Uno into a regular serial device')
    parser.add_argument('--detect', '-d', action="store_true",
        help='Attempts to detect your regular Arduino serial device')

    # Parse arguments
    args = parser.parse_args()

    # Ensure dfu-programmer exists as a command
    status, _ = commands.getstatusoutput('dfu-programmer --help')
    if status != 0:
        print("Unable to call dfu-programmer command. Is it installed or in PATH?")
        exit(1)

    # Detect Arduino (as serial device)
    if args.detect:
        arduino_ports = [
            p.device for p in serial.tools.list_ports.comports() if 'Arduino' in p.description
        ]

        if not arduino_ports:
            print "No Arduino found! If it is flashed, it will not be detected as a serial device"
        else:
            ser = serial.Serial(arduino_ports[0])
            print "Arduino found!"

        if len(arduino_ports) > 1:
            print "Multiple Arduinos found!"

    # Flash as HID
    elif args.flash:
        print "Please short GND and ICSP header pins. Press Enter to continue when complete."
        raw_input()
        subprocess.call(["dfu-programmer", "atmega16u2", "erase"])
        subprocess.call(["dfu-programmer", "atmega16u2", "flash", "--debug", "1", HID_HEX])
        subprocess.call(["dfu-programmer", "atmega16u2", "reset"])
        print "Done! You may now use your new HID pwnduino!\n"

    # Flash as a regular serial device
    elif args.unflash:
        print "Please short GND and ICSP header pins. Press Enter to continue when complete."
        raw_input()
        subprocess.call(["dfu-programmer", "atmega16u2", "erase"])
        subprocess.call(["dfu-programmer", "atmega16u2", "flash", "--debug", "1", SERIAL_HEX])
        subprocess.call(["dfu-programmer", "atmega16u2", "reset"])
        print "Done! You may now use your Arduino as a regular serial device!\n"

    # Print default help if none provided
    else:
        print parser.print_help()


if __name__ == "__main__":
    main()
