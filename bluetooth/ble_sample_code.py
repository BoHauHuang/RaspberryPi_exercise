import blescan
import sys

import bluetooth._bluetooth as bluez

import time
import math

# BLE
def init_ble():
    try:
        # open hci0 interface
        sock = bluez.hci_open_dev(0)
        print "ble thread started"
    except:
        print "error accessing bluetooth device..."
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)    # set scan params
    blescan.hci_enable_le_scan(sock)            # start scanning

    return sock

def ble_scan(sock):
    rssiDict = dict()   # create a dictionary
    returnedList = blescan.parse_events(sock)

    for beacon in returnedList:
        #print beacon
        uuid = beacon.split(",")[1]
	if uuid == "00000000111111110000000000556601":
            major = beacon.split(",")[2]
            minor = beacon.split(",")[3]
            txpower = beacon.split(",")[4]
            rssi = beacon.split(",")[5]
            cof1 = 0.42093
            cof2 = 6.9476
            cof3 = 0.54992

            ratio = 1.0*float(rssi)/float(txpower)
            
            distance = 0

            if ratio < 1.0:
                distance = pow(ratio,10)
            else:
                distance = cof1*pow(ratio, cof2) + cof3

            print "uuid:", uuid
            print "major:", major, ", minor:", minor, ", txpower:", txpower
            print "rssi", rssi
            print "distance: ", str(distance)
            print "--------"

    return rssiDict

def main():

    sock = init_ble()

    while True:
        rssiDict = ble_scan(sock)


if __name__ == "__main__":
    main()
