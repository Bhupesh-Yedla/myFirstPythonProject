from prettytable import PrettyTable

# check whether sun can be seen when input certain time

def sun_angle(time):
    angles = time.split(':')
    hour = int(angles[0])
    minutes = int(angles[1])
    if hour < 18 and hour >= 6:
        result =  (hour-6+minutes*(1/60))*0.25*60
    elif hour==18:
        if minutes==0:
            result =  (hour-6+minutes*(1/60))*0.25*60
        else:
            result =  "I don't see the sun!"
    else:
        result =  "I don't see the sun!"

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result

# check connections between drones

def areDronesConnected(network, drone1, drone2):
    visited = set()
    connections = dict()

    for connection in network:
        a,b = connection.split("-")
        connections.setdefault(a,[]).append(b)
        connections.setdefault(b,[]).append(a)
    
    def dfs(drone):
        if drone == drone2:
            return True
        
        visited.add(drone)

        for relation in connections.get(drone,[]):
            if relation not in visited:
                if dfs(relation):
                    return True
        return False
    
    return dfs(drone1)

# Format csv text into PrettyTable

def prettyCSVTable(csvtext):
    def addToList(row):
        rowData = row.split(",")

        rowList = list()

        for data in rowData:
            rowList.append(data)
        
        return rowList
    
    table = PrettyTable()
    
    rows = csvtext.split("\n")

    headerList = addToList(rows[0])

    table.field_names = headerList

    for i in range(1,len(rows)):
         table.add_row(addToList(rows[i]))
    
    print(table)

#length of the longest substring that consists of the same letter
def longestSubstring(str):
    if len(str) == 1:
        return 1
    left=0
    right=1
    maxLen = 0
    while right<len(str) :
        c = str[right]
        if c==str[left]:
            maxLen = max(maxLen,right-left+1)
        else:
            left=right
        right+=1
    
    return maxLen

class SpecialBlaException(Exception):
    pass

def parseInt(str):
    try:
        num  = int(str)
        if num < 10:
            return num
        else:
            raise SpecialBlaException("Invalid Data")
    except ValueError:
        raise SpecialBlaException("Invalid Data")

def myrange(num):
    numList = []
    i=0
    while i<=num:
        numList.append(i)
        i+=1
    return numList

def my_range(num):
    i=0
    while i<=num:
        yield i
        i+=1
    
    


