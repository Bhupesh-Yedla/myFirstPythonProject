import json

class RequestFormatter:
    def __init__(self, data):
        self.data = data

    def validate_input(self):
        if not isinstance (self.data,dict):
            raise ValueError("incorrect request data")

    def prepare_body(self):
        raise NotImplementedError("Subclasses must implement prepare_body() method")

class CSVFormatter(RequestFormatter):
    def prepare_body(self):
        self.validate_input()
        csv_body = ",".join([f"{key}:{value}" for key, value in self.data.items()])
        return csv_body

class SyslogFormatter(RequestFormatter):
    def prepare_body(self):
        self.validate_input()
        syslog_body = json.dumps(self.data)
        return syslog_body

class KVFormatter(RequestFormatter):
    def prepare_body(self):
        self.validate_input()
        kv_body = "\n".join([f"{key}={value}" for key, value in self.data.items()])
        return kv_body