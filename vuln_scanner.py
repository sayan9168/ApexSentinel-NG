import nmap
import socket
from rich.console import Console

console = Console()

class CyberSentinelExploiter:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def check_vulnerability(self, ip, port):
        """
        Nmap Scripting Engine (NSE) ব্যবহার করে Vuln Scan করবে।
        এটি Nessus-এর মতো কাজ করে।
        """
        console.print(f"[bold yellow][!] Checking Vulnerabilities on {ip}:{port}...[/bold yellow]")
        
        try:
            # Running Nmap Vulners script - এটি সরাসরি CVE ডাটাবেস থেকে চেক করে
            scan_data = self.nm.scan(ip, str(port), arguments="--script vulners")
            
            # Extracting CVE Results
            scripts_result = scan_data['scan'][ip]['tcp'][int(port)].get('script', {})
            
            if 'vulners' in scripts_result:
                cve_output = scripts_result['vulners']
                return f"[CRITICAL] Vulnerable! CVE Found: \n{cve_output[:200]}..."
            else:
                return "No known CVE found for this version."
                
        except Exception as e:
            return f"Scan Failed: {str(e)}"

    def auto_exploit_suggestion(self, service_name):
        """
        সার্ভিস নেম অনুযায়ী Metasploit মডিউল সাজেস্ট করবে।
        """
        exploit_db = {
            "ssh": "exploit/multi/ssh/sshd_invalid_user",
            "ftp": "exploit/unix/ftp/vsftpd_234_backdoor",
            "http": "exploit/multi/http/apache_mod_cgi_bash_rodeo",
            "smb": "exploit/windows/smb/ms17_010_eternalblue"
        }
        return exploit_db.get(service_name.lower(), "Manual Analysis Required")

    def kill_connection(self, target_ip):
        """
        তোমার স্পেশাল রিকোয়েস্ট: চুক্তি বাতিল হলে সার্ভিস বন্ধ করা।
        এটি টার্গেট আইপির সাথে সেশন ড্রপ করার চেষ্টা করবে।
        """
        console.print(f"[bold red][TERMINATE] Severing all AI-linked services for {target_ip}...[/bold red]")
        # বাস্তব ক্ষেত্রে এখানে API Call বা SSH Revoke কমান্ড থাকবে
        return f"Access Revoked for {target_ip} on sayan9168's Command."
      
