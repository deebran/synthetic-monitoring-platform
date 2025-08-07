import time
import yaml
import pingparsing
from tabulate import tabulate


CONFIG_FILE = "config.yaml"

def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            data = yaml.safe_load(file)

    except FileNotFoundError:
        print(f"Error: The file '{config_file}' was not found.")
        return 
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return
    return data

def ping_server(host):
    p = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = 4
    result = transmitter.ping()
    
    # Convert result to dictionary and format as a table
    data = p.parse(result).as_dict()
    table = tabulate(data.items(), headers=["Metric", "Value"], tablefmt="pretty")
    print(f'\n{table}\n')


def main():
    config = load_config(CONFIG_FILE)
    if not config:
        return
    
    monitoring_config = config.get("monitoring", {})
    servers = monitoring_config.get("servers", [])
    interval = monitoring_config.get("interval", 10)

    if not servers:
        print("No servers found in config.")
        return

    print(f"Monitoring {len(servers)} servers every {interval} seconds.")
    print("Servers to monitor:")
    for server in servers:
        print(f"  - {server['name']}: {server['host']}")
    
    while True:
        print(f"\n{'='*50}")
        print(f"Starting ping cycle at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}")
        
        for server in servers:
            try:
                ping_server(server['host'])
            except Exception as e:
                print(f"Error pinging {server['name']} ({server['host']}): {e}")
        
        print(f"Waiting {interval} seconds before next cycle...")
        time.sleep(interval)

if __name__ == "__main__":
    main()