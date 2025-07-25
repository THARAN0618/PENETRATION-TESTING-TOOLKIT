# modules/port_scanner.py
import socket

def scan_ports(target, ports):
    print(f"🔍 Scanning {target} on ports {ports}")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"✅ Port {port} is OPEN")
            s.close()
        except:
            print(f"❌ Port {port} is CLOSED")
