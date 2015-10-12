import serial
import time, os
import struct
import ConfigParser

class EMSP:

    # Class initialization
    def __init__(self, serPort, baudRate):

        #read config
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini'))
        #init serial port
        self.ser = serial.Serial()
        self.ser.port = serPort
        self.ser.baudrate = baudRate
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 2
        self.ser.xonxoff = False
        self.ser.rtscts = False
        self.ser.dsrdtr = False
        self.ser.writeTimeout = 2

        try:
            self.Log("SYS","Trying to connect board on ..." )
            self.ser.open()
        except Exception, error:
            self.Log("ERR","Error opening " + self.ser.port + " port. " + str(error))



    # Function for logging output
    def Log(self, flag, msg):
        print "{0} {1} - {2}".format(time.ctime(),flag,msg) 



    # Function for sending a command to the board
    def sendCMD(self, dataLength, code, data):

        checkSum = 0
        total_data = ['$', 'M', '<', dataLength, code] + data
        for i in struct.pack('<2B%dh' % len(data), *total_data[3:len(total_data)]):
            checkSum = checkSum ^ ord(i)
        total_data.append(checkSum)

        try:
            self.ser.write(struct.pack('<3c2B%dhB' % len(data), *total_data))
        except Exception, error:
            self.Log("ERR","Error in sendCMD. " + str(error))
            pass

    # Function to receive a data packet from the board
    def getData(self, cmd):
        try:

            ### get data

            start = time.time()

            self.sendCMD(0,int(self.config.get('Code',cmd)),[])

            while True:
                header = self.ser.read()
                if header == '$':
                    header = header + self.ser.read(2)
                    break

            datalength = struct.unpack('<b', self.ser.read())[0]
            code = struct.unpack('<b', self.ser.read())
            data = self.ser.read(datalength)
            temp = struct.unpack('<'+'h'*(datalength/2),data)

            self.ser.flushInput()
            self.ser.flushOutput()

            elapsed = time.time() - start

            ###

            if cmd == 'ATTITUDE':
                return self.getATTITUDE(temp, elapsed)
            elif cmd == 'RC':
                return self.getRC(temp, elapsed)
            elif cmd == 'RAW_IMU':
                return self.getRAW_IMU(temp, elapsed)
            else:
                return "No return error!"

        except Exception, error:
            self.Log("ERR","Error in getData. " + str(error))
            pass

    def getATTITUDE(self, temp, elapsed):
        data = {}
        data['angx'] = float(temp[0]/10.0)
        data['angy'] = float(temp[1]/10.0)
        data['heading'] = float(temp[2])
        data['elapsed'] = round(elapsed,3)
        return data

    def getRC(self, temp, elapsed):
        data = {}
        data['roll'] = float(temp[0])
        data['pitch'] = float(temp[1])
        data['yaw'] = float(temp[2])
        data['throttle'] = float(temp[3])
        data['elapsed'] = round(elapsed,3)
        return data

    def getRAW_IMU(self, temp, elapsed):
        data = {}
        data['ax'] = float(temp[0])
        data['ay'] = float(temp[1])
        data['az'] = float(temp[2])
        data['gx'] = float(temp[3])
        data['gy'] = float(temp[4])
        data['gz'] = float(temp[5])
        data['elapsed'] = round(elapsed,3)
        return data

