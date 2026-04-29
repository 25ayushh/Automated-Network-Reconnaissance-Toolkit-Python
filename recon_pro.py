import socket
import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# -------- ARGUMENTS --------
parser = argparse.ArgumentParser(description="Automated Network Recon Toolkit")

parser.add_argument("-tgt", "--target", required=True, help="Target IP")
parser.add_argument("-p", "--ports", default="top1000",
                    help="Port selection: all / top1000 / manual (e.g. 22,80,443)")
parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads")
parser.add_argument("-T", "--timing", type=int, choices=range(0,6), default=3,
                    help="Timing template (0-5)")
parser.add_argument("-s", "--scan", choices=["sT", "sS"], default="sT",
                    help="Scan type: sT (TCP), sS (SYN)")
parser.add_argument("-o", "--output", default="results.txt", help="Output file")

args = parser.parse_args()

open_ports = []

# -------- PORT SELECTION --------
def get_ports(port_option):
    if port_option == "all":
        return range(1, 65536)
    elif port_option == "top1000":
        return list(range(1, 1001))
    else:
        return [int(p.strip()) for p in port_option.split(",")]

# -------- PORT SCAN --------
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((args.target, port))
        if result == 0:
            print(f"[OPEN] {port}")
            open_ports.append(port)
        sock.close()
    except:
        pass

# -------- BANNER GRAB --------
def banner_grab(port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((args.target, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return "No banner"

# -------- NMAP SCAN --------
def run_nmap():
    print("\n[+] Running Advanced Nmap Scan...")

    scan_type = "-sT" if args.scan == "sT" else "-sS"

    command = [
        "nmap",
        scan_type,
        "-T", str(args.timing),
        "-sV",
        "-O",
        args.target
    ]

    try:
        result = subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return result.decode()
    except:
        return "Nmap scan failed (try sudo for SYN scan)"

# -------- MAIN --------
def main():
    start = datetime.now()
    print(f"\n[+] Target: {args.target}")
    print(f"[+] Scan Type: {args.scan}")
    print(f"[+] Timing: T{args.timing}")
    print(f"[+] Threads: {args.threads}")

    ports = get_ports(args.ports)

    print(f"\n[+] Scanning {len(ports)} ports...\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(scan_port, ports)

    print("\n[+] Banner Grabbing:")
    for port in open_ports:
        banner = banner_grab(port)
        print(f"Port {port}: {banner}")

    nmap_output = run_nmap()

    # -------- SAVE --------
    with open(args.output, "w") as f:
        f.write(f"Target: {args.target}\n")
        f.write(f"Open Ports: {open_ports}\n\n")

        f.write("Banner Results:\n")
        for port in open_ports:
            f.write(f"Port {port}: {banner_grab(port)}\n")

        f.write("\nNmap Scan:\n")
        f.write(nmap_output)

    end = datetime.now()
    print(f"\n[+] Completed in: {end - start}")
    print(f"[+] Results saved to {args.output}")

if __name__ == "__main__":
    main()