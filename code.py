from microbit import *
from bme688 import *

# Initialize the BME688 sensor
init_sensor()
init_gas_sensor()

while True:
    # Read environmental data from the BME688 sensor
    read_data_registers()
    
    # Calculate air quality parameters
    eCO2Value = calc_air_quality()[2]
    iaqScore = calc_air_quality()[0]
    iaqPercent = calc_air_quality()[1]
    
    # Print the results to the serial console
    print("eCO2 Value (ppm):", eCO2Value)
    print("IAQ Score:", iaqScore)
    print("IAQ Percent:", iaqPercent)
    
    # Display a status indicator on the LED matrix
    if iaqScore > 100:  # Example threshold for poor air quality
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
    
    # Wait before taking the next reading
    sleep(1000)
