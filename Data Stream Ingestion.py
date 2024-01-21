class DataStream:
    def __init__(self):
        self.last_timestamp = {}

    def should_output_data_str(self, timestamp, data_str):
        if data_str not in self.last_timestamp or timestamp - self.last_timestamp[data_str] >= 5:
            self.last_timestamp[data_str] = timestamp
            return True
        else:
            return False

data_stream = DataStream()
output = [
    data_stream.should_output_data_str(timestamp=0, data_str="hello"),
    data_stream.should_output_data_str(timestamp=1, data_str="world"),
    data_stream.should_output_data_str(timestamp=6, data_str="hello"),
    data_stream.should_output_data_str(timestamp=7, data_str="hello"),
    data_stream.should_output_data_str(timestamp=8, data_str="world")
]

print(output)