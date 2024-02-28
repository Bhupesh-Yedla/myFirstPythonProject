import json
from prettytable import PrettyTable

# check whether sun can be seen when input certain time


def sun_angle(time):
    angles = time.split(":")
    hour = int(angles[0])
    minutes = int(angles[1])
    if hour < 18 and hour >= 6:
        result = (hour - 6 + minutes * (1 / 60)) * 0.25 * 60
    elif hour == 18:
        if minutes == 0:
            result = (hour - 6 + minutes * (1 / 60)) * 0.25 * 60
        else:
            result = "I don't see the sun!"
    else:
        result = "I don't see the sun!"

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result


# check connections between drones


def areDronesConnected(network, drone1, drone2):
    visited = set()
    connections = dict()

    for connection in network:
        a, b = connection.split("-")
        connections.setdefault(a, []).append(b)
        connections.setdefault(b, []).append(a)

    def dfs(drone):
        if drone == drone2:
            return True

        visited.add(drone)

        for relation in connections.get(drone, []):
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

    for i in range(1, len(rows)):
        table.add_row(addToList(rows[i]))

    print(table)


# length of the longest substring that consists of the same letter
def longestSubstring(str):
    if len(str) == 1:
        return 1
    left = 0
    right = 1
    maxLen = 0
    while right < len(str):
        c = str[right]
        if c == str[left]:
            maxLen = max(maxLen, right - left + 1)
        else:
            left = right
        right += 1

    return maxLen


class SpecialBlaException(Exception):
    pass


def parseInt(str):
    try:
        num = int(str)
        if num < 10:
            return num
        else:
            raise SpecialBlaException("Invalid Data")
    except ValueError:
        raise SpecialBlaException("Invalid Data")


def myrange(num):
    numList = []
    i = 0
    while i <= num:
        numList.append(i)
        i += 1
    return numList


def my_range(num):
    i = 0
    while i <= num:
        yield i
        i += 1


def formatJson(filepath):

    with open(filepath, "r") as file:
        json_content = file.read()

    dataJson = json.loads(json_content)
    dataJson["a"]["b"] = 2

    with open(filepath, "w") as file:
        result = json.dump(dataJson, file, indent=4)

    return filepath


def matrixSum(matrix):

    result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    if isMatrixValid(matrix) == True:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):

                if row - 1 < 0:
                    top = matrix[len(matrix) - 1][col]
                else:
                    top = matrix[row - 1][col]
                if col - 1 < 0:
                    left = matrix[row][len(matrix[row]) - 1]
                else:
                    left = matrix[row][col - 1]
                if col + 1 > len(matrix[row]) - 1:
                    right = matrix[row][0]
                else:
                    right = matrix[row][col + 1]
                if row + 1 > len(matrix) - 1:
                    bottom = matrix[0][col]
                else:
                    bottom = matrix[row + 1][col]

                result = int(left) + int(right) + int(top) + int(bottom)
                result_matrix[row][col] = result
        return result_matrix
    else:
        return False


def isMatrixValid(matrix):
    if not matrix:
        return False
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            return False

    return True
