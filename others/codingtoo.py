event_data = [
{
    "type" : "fault_off",
    "fault": "NOT_STABLE",
    "time" : 100,
    "bootNum": 1,
},
{
    "type" : "clock_event",
    "time" : 22,
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
    "time" : 200,
    "bootNum": 1,
},
{
    "type" : "fault_off",
    "fault": "TOO_HOT",
    "time" : 300,
    "bootNum": 1,
},
{
    "type" : "fault_on",
    "fault": "TOO_HOT",
    "time" : 320,
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

def make_fault_durations(events):
    
    durations = {}
    for event in events:
        if(event["type"]  != "fault_on" and event["type"] != "fault_off"):
            continue
        
        if(event["fault"] not in durations and event["type"] == "fault_on"):
            durations[event["fault"]] = [event["time"], -1]
        elif(event["fault"] in durations):
            
            print("help", durations[event["fault"]][-1])
            
            if(durations[event["fault"]][-1][1] != -1 and event["type"] == "fault_on"):
                durations[event["fault"]].append([event["time"],-1])
            if(durations[event["fault"]][-1][1] != -1 and event["type"] == "fault_on"):
                durations[event["fault"]][-1][1] = event["time"]
            
    return durations

all_durations = make_fault_durations(event_data)
for name, faults, in all_durations.items():
    print (name)
    print ('\n'.join('{} -> {}'.format(a, b) for a, b in faults))