import serial # import pyserial library

ser = serial.Serial('COM4', 9600) # Initialize the serial port at 9600 baud

while True:
    if ser.in_waiting > 0:
        
        data = ser.readline().rstrip()  # Read data from serial port and remove newline characters
        data_str = data.decode("utf-8")
        
        print(data_str) # prints the received data

        # based on the code received we give a different output
        # if you want you can add another conditions

        if(data_str == "RFID CODE"): # change "rfid code" to your tag code
            data_str = " " # associate the desired output
            print(data_str)
        elif(data_str == "RFID CODE"): # change "rfid code" to your tag code
            data_str = " "  # associate the desired output
            print(data_str)
        else:
            print("Sorry, i can't recognize the code")
            print(data_str)


