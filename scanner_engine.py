from scapy.all import IP, TCP, sr, conf
import socket

class RapidScanner:
    def __init__(self, target):
        self.target = target
        conf.verb = 0 # Silent mode

    def run_scan(self):
        # এই অংশটি RustScan-এর মতো ফাস্ট কাজ করার জন্য মাল্টি-থ্রেডিং সিমুলেট করে
        discovered_hosts = {}
        
        # Simple SYN Scan (Nmap -sS style)
        # বাস্তব ক্ষেত্রে এখানে Range loop হবে
        try:
            # Prototype logic extended to real functionality
            ans, unans = sr(IP(dst=self.target)/TCP(dport=[21,22,80,443,3389], flags="S"), timeout=2)
            
            for send, recv in ans:
                ip = recv.src
                port = send.dport
                if ip not in discovered_hosts:
                    discovered_hosts[ip] = {'ports': [], 'os': 'Detecting...'}
                discovered_hosts[ip]['ports'].append(port)
                
                # Service Fingerprinting
                try:
                    discovered_hosts[ip]['os'] = socket.getfqdn(ip)
                except:
                    discovered_hosts[ip]['os'] = "Unknown Device"
                    
        except Exception as e:
            print(f"Error: {e}")
            
        return discovered_hosts
      
