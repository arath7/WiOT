from BasicArdu import BasicArdu, Frames
from time import sleep, time

# Main Method
def main():
    # simple use example
    print('---Starting Basic Drone---')
    drone  = BasicArdu(connection_string='tcp:127.0.0.1:5762')    # connect to Intel Aero using 'North, East, Down' Reference Basis

    #arming
    drone.handle_arm()
    
    sleep(5)

    #disarming
    if drone.verbose:
        print('> Disarming')
    drone.vehicle.armed=False
    

if __name__ == '__main__':
    main()  # Calls main method if the python file is run directly (python3 filename.py)