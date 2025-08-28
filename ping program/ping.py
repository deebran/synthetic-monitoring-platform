from tabulate import tabulate
import pingparsing

dest = input("\nEnter IP/DNS name: ")

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = dest
transmitter.count = 10
result = transmitter.ping()

# Convert result to dictionary and format as a table
data = ping_parser.parse(result).as_dict()
table = tabulate(data.items(), headers=["Metric", "Value"], tablefmt="pretty")
print(f'\n{table}\n')