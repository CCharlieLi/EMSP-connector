import sys,time
from EMSPcore.pyEMSP import EMSP

if __name__ == "__main__":

    board = EMSP("/dev/cu.SLAB_USBtoUART",115200)

    try:
        if 'ARM' in sys.argv:
            board.arm()
            print "Board is armed now!"
            print "In 3 seconds it will disarm..."
            time.sleep(3)
            board.disarm()
            print "Disarmed."
            exit(0)

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

            # not working, need modify cleanflight source code to output attitude data immediately
            if 'SET_RAW_RC' in sys.argv:
                rcdata = [1500,1550,1600,1560,1000,1040,1000,1000]
                board.getData('SET_RAW_RC',rcdata,16)

                data = board.getData('ATTITUDE')
                message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(data['angx'],data['angy'],data['heading'],data['elapsed'])
                print message

            if 'MOTOR' in sys.argv:
                data = board.getData('MOTOR')
                message = "m1 = {:+.2f} \t m2 = {:+.2f} \t m3 = {:+.2f} \t m4 = {:+.2f} \t elapsed = {:+.4f} \t".format(data['m1'],data['m2'],data['m3'],data['m4'],data['elapsed'])
                print message


    except Exception,error:
        board.Log("ERR","Error in test. " + str(error))