import serial
from serial.tools import list_ports

port_list = []
ports = list_ports.comports()
for port, desc, hwid in sorted(ports):
    port_list.append(port)

print(port_list)
rmc_file = open('gnss_rmc.txt', 'w')
try:
    gnss = serial.Serial('/dev/ttyUSB0', 115200)
    while True:
        ser_bytes = gnss.readline()
        decoded_bytes = ser_bytes.decode('utf-8')
        data = decoded_bytes.split(',')
        if data[0] == '$GNRMC':
            data = str(data)
            print(data)
            rmc_file.write(data + '\n')
    rmc_file.close()
except serial.SerialException:
    print('Ошибка подключения USB')
