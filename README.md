# 🛠️ Automated Network Reconnaissance Toolkit

A Python-based network reconnaissance tool that automates **port scanning, banner grabbing, and advanced Nmap scanning**.

This project is designed for beginners in network pentesting to understand how reconnaissance works and how tools like Nmap operate internally.

---

## 🚀 Features

- 🔍 Custom Port Scanning
  - Scan specific ports (e.g., 22,80,443)
  - Top 1000 ports
  - Full range (1–65535)

- ⚡ Multi-threaded scanning (faster execution)

- 🏁 Scan Types
  - `-sT` → TCP Connect Scan
  - `-sS` → SYN Scan (requires sudo)

- ⏱️ Timing Control
  - `-T 0–5` (similar to Nmap timing templates)

- 🧠 Banner Grabbing
  - Identifies services running on open ports

- 🔬 Advanced Scanning (via Nmap)
  - Service detection (`-sV`)
  - OS detection (`-O`)

- 📁 Output Saving
  - Saves results into a file

---

## 📂 Project Structure


network-recon-toolkit/
│── recon.py
│── results.txt
│── README.md


---

## ⚙️ Requirements

- Python 3.x  
- Kali Linux (recommended)  
- Nmap installed  

Install Nmap:
```bash
sudo apt install nmap
▶️ Usage
🔹 Basic Scan
python3 recon.py -tgt <target_ip>
🔹 Scan Specific Ports
python3 recon.py -tgt <target_ip> -p 21,22,80
🔹 Top 1000 Ports
python3 recon.py -tgt <target_ip> -p top1000
🔹 Full Port Scan
python3 recon.py -tgt <target_ip> -p all

⚠️ Warning: Full scan can be slow.

🔹 Multi-threading
python3 recon.py -tgt <target_ip> -th 200
🔹 Timing Control
python3 recon.py -tgt <target_ip> -T 4
🔹 SYN Scan (Requires Root)
sudo python3 recon.py -tgt <target_ip> -s sS
🔹 Output File
python3 recon.py -tgt <target_ip> -o output.txt
📌 Arguments
Argument	Description
-tgt	Target IP address (required)
-p	Ports: all, top1000, or manual (e.g. 22,80)
-th	Number of threads
-T	Timing template (0–5)
-s	Scan type (sT, sS)
-o	Output file
🧪 Example Output
[+] Target: 192.168.56.101
[+] Scan Type: sS
[+] Timing: T4
[+] Threads: 100

[OPEN] 21
[OPEN] 22
[OPEN] 80

[+] Banner Grabbing:
Port 21: vsFTPd 2.3.4
Port 22: OpenSSH 4.7
Port 80: Apache httpd

[+] Running Advanced Nmap Scan...

[+] Results saved to results.txt
🧠 Learning Objectives
Socket programming in Python
Multi-threading for performance
Network scanning techniques
Service enumeration (banner grabbing)
Automation of Nmap scans
Real-world reconnaissance workflow
⚠️ Disclaimer

This tool is intended for educational purposes only.
Use only on systems you own or have permission to test.
