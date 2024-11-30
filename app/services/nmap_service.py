
import nmap

def run_nmap_scan(target, options="-sV"):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments=options)

    scan_results = []
    for host in nm.all_hosts():
        scan_results.append({
            "host": host,
            "status": nm[host].state(),
            "protocols": [
                {
                    "protocol": proto,
                    "ports": [
                        {
                            "port": port,
                            "state": nm[host][proto][port]["state"]
                        } for port in nm[host][proto]
                    ]
                } for proto in nm[host].all_protocols()
            ]
        })
    return scan_results
