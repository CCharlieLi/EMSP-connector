import sys
from EMSPcore.pyEMSP import EMSP

if __name__ == "__main__":

    board = EMSP("/dev/cu.SLAB_USBtoUART",115200)

    try:
        while True:
            if 'ATTITUDE' in sys.argv:
                data = board.getData('ATTITUDE')
                message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(data['angx'],data['angy'],data['heading'],data['elapsed'])
                print message
            if 'RC' in sys.argv:
                data = board.getData('RC')
                message = "roll = {:+.2f} \t pitch = {:+.2f} \t yaw = {:+.2f} \t throttle = {:+.2f} \t elapsed = {:+.4f} \t".format(data['roll'],data['pitch'],data['yaw'],data['throttle'],data['elapsed'])
                print message
            if 'RAW_IMU' in sys.argv:
                data = board.getData('RAW_IMU')
                message = "ax = {:+.2f} \t ay = {:+.2f} \t az = {:+.2f} \t gx = {:+.2f} \t gy = {:+.2f} \t gz = {:+.2f} \t elapsed = {:+.4f} \t".format(data['ax'],data['ay'],data['az'],data['gx'],data['gy'],data['gz'],data['elapsed'])
                print message

    except Exception,error:
        board.Log("ERR","Error in test. " + str(error))