from EMSPcore.pyEMSP import EMSP

if __name__ == "__main__":

    board = EMSP("/dev/cu.SLAB_USBtoUART",115200)

    try:
        while True:
            data = board.getData('ATTITUDE')
            message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(float(data['angx']),float(data['angy']),float(data['heading']),float(data['elapsed']))
            print message

    except Exception,error:
        board.Log("ERR","Error in test-getATTITUDE. " + str(error))