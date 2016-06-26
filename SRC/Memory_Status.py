import psutil
import time

# This is the upper RAM consumption limit in Bytes, currently set to 30%
criticalMemoryLeftPercentage = 30

# Function to start RAM consumption status checker and notifier
# parameters: None
# returns: None
def memoryConsumptionStatus():
    ram = psutil.virtual_memory()
    while(1):
        totalMemoryConsumptionPercentage = int(ram.percent)
        if ((100.0 - totalMemoryConsumptionPercentage) < criticalMemoryLeftPercentage):
            print 'RAM overuse!!! Current consumption: ',str(totalMemoryConsumptionPercentage),'%\nThreshold: ', str(criticalMemoryLeftPercentage),'%'
            break
        else:
            # Check again after 1 minute
            time.sleep(60)

memoryConsumptionStatus()
