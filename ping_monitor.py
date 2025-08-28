import time
import yaml
import pingparsing
from tabulate import tabulate
from prometheus_client import start_http_server, Gauge
import random


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
    return data

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

    # Start Prometheus server
    start_http_server(8989)

    # Initialize Prometheus metrics 
    avg_rtt = Gauge('avg_rtt', 'Round Trip Time', ["server"])
    packet_loss_count = Gauge('packet_loss_count', 'Packet Loss Count', ["server"])

    print(f"Monitoring {len(servers)} servers every {interval} seconds.")
    print("Servers to monitor:")
    for server in servers:
        print(f"  - {server['name']}: {server['host']}")
    
    while True:
        print(f"\n{'='*50}")
        print(f"Starting ping cycle at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}")
        
        for server in servers:
            host = server['host']
            try:
                data = ping_server(host)
            except Exception as e:
                print(f"Error pinging {server['name']} ({host}): {e}")
            
            # Expose Metric to Prometheus server
            avg_rtt.labels(server=host).set(data['rtt_avg'])
            packet_loss_count.labels(server=host).set(data['packet_loss_count'])
            
        print(f"Waiting {interval} seconds before next cycle...")
        time.sleep(interval)

if __name__ == "__main__":
    main()