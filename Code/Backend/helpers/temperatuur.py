sensor_file_name = '/sys/bus/w1/devices/28-01203390a715/w1_slave'
class temperatuur:
    def start():
        sensor_file = open(sensor_file_name,'r')
        for line in sensor_file:
            line = line.rstrip()
            pos = line.find("t=")
            if pos > -1:
                temp = int(line[-5:])/1000
                return temp
                print(f"De temperatuur is: {temp} \u00b0C")
            #print(f"Temp is: {line.find()}")

        sensor_file.close()