import sys
from EMSPcore.pyEMSP import EMSP

if __name__ == "__main__":

    board = EMSP("/dev/ttyUSB0",115200)

    try:
        if 'ATTITUDE' in sys.argv:
            data = board.getData('ATTITUDE')
            message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:.4f} ms \t".format(data['angx'],data['angy'],data['heading'],data['elapsed'])
            print message
        if 'RC' in sys.argv:
            data = board.getData('RC')
            message = "roll = {:+.2f} \t pitch = {:+.2f} \t yaw = {:+.2f} \t throttle = {:+.2f} \t elapsed = {:.4f} ms \t".format(data['roll'],data['pitch'],data['yaw'],data['throttle'],data['elapsed'])
            print message
        if 'RAW_IMU' in sys.argv:
            data = board.getData('RAW_IMU')
            message = "ax = {:+.2f} \t ay = {:+.2f} \t az = {:+.2f} \t gx = {:+.2f} \t gy = {:+.2f} \t gz = {:+.2f} \t elapsed = {:.4f} ms \t".format(data['ax'],data['ay'],data['az'],data['gx'],data['gy'],data['gz'],data['elapsed'])
            print message
        if 'API_VERSION' in sys.argv:
            data = board.getData('API_VERSION')
            massage = "Version : {:d}.{:d}.{:d} \t elapsed = {:.4f} ms \t".format(data['protver'],data['majorver'],data['minorver'],data['elapsed'])
            print massage
        if 'FC_VARIANT' in sys.argv:
            data = board.getData('FC_VARIANT')
            message = "flightControllerIdentifier : {:s} \t elapsed = {:.4f} ms \t".format(data['fcId'],data['elapsed'])
            print message
        if 'FC_VERSION' in sys.argv:
            data = board.getData('FC_VERSION')
            message = "FlightControllerVersion : {:d}.{:d}.{:d} \t elapsed = {:.4f} ms \t".format(data['fcver'],data['majorfcver'],data['minorfcver'],data['elapsed'])
            print message
        if 'BOARD_INFO' in sys.argv:
            data = board.getData('BOARD_INFO')
            message = "boardIdentifier : {:s} \t elapsed = {:.4f} ms \t".format(data['boardId'],data['elapsed'])
            print message
        if 'BUILD_INFO' in sys.argv:
            data = board.getData('BUILD_INFO')
            message = "buildtime : {:s} {:s} \t gitrevision : {:s} \t elapsed = {:.4f} ms \t".format(data['date'],data['time'],data['git'],data['elapsed'])
            print message

    except Exception,error:
        board.Log("ERR","Error in test. " + str(error))