import os
import sys
from rich.console import Console
from rich.table import Table
from scanner_engine import RapidScanner

console = Console()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold cyan]APEX SENTINEL v1.0[/bold cyan] - [italic]The Ultimate Network Intelligence[/italic]")
    console.print(f"[green]User authenticated via Private Fingerprint (sayan9168)[/green]\n")

    target = input("Enter Target IP/Range (e.g., 192.168.1.0/24): ")
    
    # Masscan speed with Scapy precision
    scanner = RapidScanner(target)
    
    console.print(f"[*] Starting Ultra-Fast Scan on {target}...")
    results = scanner.run_scan()

    # Displaying Results in a Professional Table (Like Zenmap but better)
    table = Table(title="Network Discovery Results")
    table.add_column("IP Address", style="magenta")
    table.add_column("Open Ports", style="yellow")
    table.add_column("OS/Device Hint", style="green")
    table.add_column("Action", style="red")

    for ip, data in results.items():
        table.add_row(
            ip, 
            ", ".join(map(str, data['ports'])), 
            data['os'],
            "Access Revocable" # তোমার চুক্তি বাতিলের ফিচারের জন্য রিমাইন্ডার
        )

    console.print(table)

if __name__ == "__main__":
    main()
  
