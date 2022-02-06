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

def make_fault_durations(events):
    durations = {}
    lastTime = 0
    lastBootNum = 1
    for event in events:
        lastTime = event["time"]
        if(event["bootNum"] != lastBootNum):
            for fault, time in durations.items():
                for couple in time:
                    if(couple[1] == -1):
                        couple[1] = lastTime
        if(event["type"]  != "fault_on" and event["type"] != "fault_off"):
            continue

        if(event["fault"] not in durations and event["type"] == "fault_on"):
            durations[event["fault"]] = [[event["time"], -1]]
        elif(event["fault"] in durations):
            if(durations[event["fault"]][-1][1] != -1 and event["type"] == "fault_on"):
                durations[event["fault"]].append([event["time"],-1])
            if(durations[event["fault"]][-1][1] != -1 and event["type"] == "fault_on"):
                durations[event["fault"]][-1][1] = event["time"]
    for fault, time in durations.items():
        for couple in time:
            if(couple[1] == -1):
                couple[1] = lastTime
    return durations

all_durations = make_fault_durations(event_data)
for name, faults, in all_durations.items():
    print (name)
    print ('\n'.join('{} -> {}'.format(a, b) for a, b in faults))
    
    #^5