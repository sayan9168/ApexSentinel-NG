import os
import sys
import socket
from rich.console import Console
from rich.table import Table

# কাস্টম মডিউল ইমপোর্ট
from scanner_engine import RapidScanner
from vuln_scanner import CyberSentinelExploiter

console = Console()

def main():
    # স্ক্রিন ক্লিয়ার এবং ব্যানার
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("="*60, style="blue")
    console.print("[bold cyan]APEX SENTINEL v1.0[/bold cyan] - [italic]The Ultimate Network Intelligence[/italic]", justify="center")
    console.print("="*60, style="blue")
    
    # তোমার কাস্টম ফিঙ্গারপ্রিন্ট অথেন্টিকেশন (সিমুলেটেড)
    console.print(f"[bold green][✓] User authenticated via AI-Fingerprint: sayan9168[/bold green]")
    console.print(f"[bold yellow][!] Status: Authorized to Revoke Remote Services[/bold yellow]\n")

    # ইউজার ইনপুট
    target = input("Enter Target IP/Range (e.g., 192.168.1.0/24): ")
    
    # ১. দ্রুত স্ক্যানিং শুরু (Masscan/RustScan Speed)
    scanner = RapidScanner(target)
    console.print(f"\n[*] [bold white]Phase 1:[/bold white] Starting Ultra-Fast Host Discovery...")
    results = scanner.run_scan()

    if not results:
        console.print("[bold red][!] No active hosts found in the given range.[/bold red]")
        return

    # ২. ডিসকভারি রেজাল্ট টেবিল (Zenmap-এর চেয়ে আধুনিক স্টাইল)
    table = Table(title=f"Network Inventory: {target}")
    table.add_column("IP Address", style="magenta", no_wrap=True)
    table.add_column("Open Ports", style="yellow")
    table.add_column("Device/Hostname", style="green")
    table.add_column("Contract Status", style="red")

    for ip, data in results.items():
        table.add_row(
            ip, 
            ", ".join(map(str, data['ports'])), 
            data['os'],
            "Revocable (sayan9168)" # চুক্তি বাতিলের রিমাইন্ডার
        )
    console.print(table)

    # ৩. ভলনারেবিলিটি অ্যানালাইসিস এবং এক্সপ্লয়েট সাজেস্ট (Nessus/Metasploit Style)
    exploiter = CyberSentinelExploiter()
    console.print(f"\n[*] [bold white]Phase 2:[/bold white] Analyzing Vulnerabilities & Service Exploits...")

    for ip, data in results.items():
        for port in data['ports']:
            try:
                # সার্ভিস নাম বের করা
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            # ভালনারেবিলিটি স্ক্যান (NSE Scripts)
            vuln_report = exploiter.check_vulnerability(ip, port)
            console.print(f"\n[bold cyan]>> {ip}:{port} ({service.upper()})[/bold cyan]")
            console.print(f"   [bold red]Report:[/bold red] {vuln_report}")

            # এক্সপ্লয়েট সাজেশন
            suggestion = exploiter.auto_exploit_suggestion(service)
            console.print(f"   [bold yellow]Target Exploit:[/bold yellow] {suggestion}")

    # ৪. সার্ভিস টার্মিনেশন (তোমার চুক্তি বাতিলের সেই কাস্টম পাওয়ার)
    console.print("\n" + "-"*40)
    choice = input("Do you want to terminate any service/connection? (y/n): ")
    if choice.lower() == 'y':
        target_to_kill = input("Enter IP to disconnect from network: ")
        if target_to_kill in results:
            status = exploiter.kill_connection(target_to_kill)
            console.print(f"[SUCCESS] {status}")
        else:
            console.print("[Error] Target IP not found in recent scan results.")

    console.print("\n[bold blue][*] Scan Completed. Apex Sentinel is now in Standby Mode.[/bold blue]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Scan aborted by user (sayan9168).[/bold red]")
        sys.exit()
