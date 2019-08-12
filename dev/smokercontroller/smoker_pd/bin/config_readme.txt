TODO: config.json will be tied in to the operation of fc.py and then subsequently will be used with API calls when django is implemented

NOTE: This is a rough design that will be improved


"GLOBAL"

"NUM_OF_PROBES": "1",
Nuff said

"INTERVAL": "5",
Interval at which it will probe temps

"SWING": "1",
Temperature swing

"FAN_COEFFICIENT": "1", 
Coefficient of fan speed -- with 4 wire (PWM) fans, this controls the ratio of
temperature differential (target temp compared to measured temp or concatenated
measured temps)

"CONCAT": "AVERAGE"
When combining probes, this can be Min, Max, average. Min or MAX means that as
soon as a single fan crosses the threshold the fan action is triggered. 
Average means that it averages the temps into one temp.


"PROBES"

"1":
"TYPE": "MAX31855",
Type. Example MAX31855 MAX31856, 1Wire

"AFFECTS_FAN": "1", (it only affects fans if this is set. otherwise a reading just gets displayed


