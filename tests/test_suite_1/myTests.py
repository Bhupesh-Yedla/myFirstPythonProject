import json
import unittest
from pages.ApiFramework import CSVFormatter, KVFormatter, SyslogFormatter
from pages.TicTacToe import OCell, TicTacToe, XCell
from pages.myModules import (
    SpecialBlaException,
    formatJson,
    my_range,
    parseInt,
    sun_angle,
    areDronesConnected,
    prettyCSVTable,
    longestSubstring,
)


class TestMyScenarios(unittest.TestCase):

    @unittest.skip("skipping sun angle test")
    def test1_sun_angle(self):
        result = sun_angle("01:23")
        print("\n" + str(result))

    @unittest.skip
    def test1_2_drones_connection(self):
        result = areDronesConnected(
            (
                "dr101-mr99",
                "mr99-out00",
                "dr101-out00",
                "scout1-scout2",
                "scout3-scout1",
                "scout1-scout4",
                "scout4-sscout",
                "sscout-super",
            ),
            "dr101",
            "sscout",
        )
        print(result)

    @unittest.skip
    def test2_prettytable_csv(self):
        prettyCSVTable("a,b\n1,")

    @unittest.skip
    def test3_longest_substring(self):
        result = longestSubstring("ddvvrwwwrggg")
        print(result)

    @unittest.skip
    def test4_parseInt(self):
        try:
            print(parseInt("one "))
        except SpecialBlaException as e:
            print("SpecialBlaException:", e)

    @unittest.skip
    def test5_my_range(self):
        for i in my_range(3):
            print(i)

    @unittest.skip
    def test6_format_json(self):
        filepath = formatJson("Jsonfile.json")

        with open(filepath, "r") as file:
            json_content = file.read()
            print(json_content)
    
    @unittest.skip
    def test7_tictactoe(self):
        referee = TicTacToe([OCell().value+OCell().value+XCell().value,XCell().value+XCell().value+OCell().value,OCell().value+XCell().value+XCell().value])
        result = referee.checkio()
        print("\n"+result)
        if result == "D":
            print("it's a draw")
        else:
            print("Winner is: "+result)
            
    @unittest.skip
    def test8_api_framework(self):
        json_data = {
                    "className": "Class 1A",
                    "year": 2022,
                     "phoneNumber": None,
                    "active": True,
                    "homeroomTeacher": {"firstName": "Richard", "lastName": "Roe"},
                    "members": [
                            {"firstName": "Jane", "lastName": "Doe"},
                            {"firstName": "Jinny", "lastName": "Roe"},
                            {"firstName": "Johnny", "lastName": "Roe"},
                                ]
                    } 
        
        csv_formatter  = CSVFormatter(json_data)
        csv_body = csv_formatter.prepare_body()

        syslog_formatter = SyslogFormatter(json_data)
        syslog_body = syslog_formatter.prepare_body()

        kv_formatter = KVFormatter(json_data)
        kv_body = kv_formatter.prepare_body()

        print("\nCSV Body: \n"+csv_body)
        print("\nSyslog Body: \n"+syslog_body)
        print("\nKV Body: \n"+kv_body)

if __name__ == "__main__":
    unittest.main()
