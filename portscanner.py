from IPy import IP
import socket


def chek_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ip, prt):
    try:
        s = socket.socket()
        s.settimeout(0.2)
        s.connect((ip, int(prt)))
        try:
            banner = get_banner(s).decode().strip("\n")
            print(f"Port {prt} is open : {banner}")
        except:
            print(f"Port {prt} Open.")
    except:
        pass


def scan(target):
    converted_ip = chek_ip(target)
    print("\n" + f"[+_+ Scanning target] {target}")
    for port in range(1, 100):
        scan_port(converted_ip, port)


if __name__ == "__main__":
    targets = input("Enter target/s to scan: (split multiple targets with comma) ")
    port_num = input("Enter the number of ports that you want to scan: ")
    if "," in targets:
        for ipaddress in targets.split(","):
            scan(ipaddress.strip(" "))
    else:
        scan(targets)
