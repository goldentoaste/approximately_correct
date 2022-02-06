
from typing import Any, Dict, List


event_data = [
{
    "type" : "fault_off",
    "fault": "NOT_STABLE",
    "time" : 22,
    "bootNum": 1,
},
{
    "type" : "clock_event",
    "time" : 41,
    "bootNum": 1,
},
{
    "type" : "fault_on",
    "fault": "TOO_HOT",
    "time" : 56,
    "bootNum": 1,
},
{
    "type" : "fault_on",
    "fault": "TOO_HOT",
    "time" : 273,
    "bootNum": 1,
},
{
    "type" : "fault_on",
    "fault": "TOO_HOT",
    "time" : 408,
    "bootNum": 1,
},
{
    "type" : "fault_off",
    "fault": "TOO_HOT",
    "time" : 622,
    "bootNum": 1,
},
{
    "type" : "flight_analytics",
    "time" : 330,
    "bootNum": 1,
},
{
    "type" : "fault_on",
    "fault": "TOO_HOT",
    "time" : 350,
    "bootNum": 2,
},
{
    "type" : "fault_on",
    "fault": "Danger",
    "time" : 366,
    "bootNum": 2,
},
]

def make_fault_durations(events : List[Dict[str,Any]]):
    
    #[start, latest], duration, boot, isOn [key : type, value: [ [1,2]... ] ]
    faults : Dict[str: List[str]] = {}
    lastBoot = 0
    
    for event in events:
        if event["bootNum"] != lastBoot:
            lastBoot = event["bootNum"]
            for key, value in faults.items():
                value[2] += event["time"] - value[1]
                value[1] = event["time"]
                
                
        if event["type"] == "fault_on":
            if event["fault"] not in faults:
                faults[event["fault"]] = [event["time"], event["time"], 0, event["bootNum"], True]
            else: #event occured already
                fault = faults[event["fault"]]
                if not fault[4]: #not on
                    fault[4] = True
                else:
                    fault[2] += event["time"] - fault[1] 
                    fault[1] = event["time"]
        elif event["type"] == "fault_off":
            try:
                fault = faults[event["fault"]]
                if fault[4]: # update time if fault was previously on
                    fault[2] += event["time"] - fault[1] 
                    fault[1] = event["time"]
            except:
                pass #fault deosnt exist, but no need to record
        
        for fault in faults.values():
            fault[2] += events[-1]["time"] - fault[1]
            fault[1] = events[-1]["time"]
    print(faults)

make_fault_durations(event_data)