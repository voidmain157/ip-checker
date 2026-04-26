import socket
import requests
from pprint import pprint

def get_ip(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Gagal resolve domain")
        return None

def get_geolocation(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] == "success":
            return data
        else:
            print("[!] Gagal ambil data lokasi")
            return None

    except requests.exceptions.RequestException:
        print("[!] Error koneksi ke API")
        return None

def main():
    target = input("Enter domain or IP: ")

    # cek apakah input sudah IP atau domain
    if target.replace(".", "").isdigit():
        ip = target
    else:
        ip = get_ip(target)

    if not ip:
        return

    print(f"\n[+] IP Address: {ip}")

    geo = get_geolocation(ip)

    if geo:
        print("\n[+] Geolocation Info:")
        pprint({
            "Country": geo.get("country"),
            "Region": geo.get("regionName"),
            "City": geo.get("city"),
            "ISP": geo.get("isp"),
            "Org": geo.get("org"),
            "Timezone": geo.get("timezone"),
            "Lat,Long": f"{geo.get('lat')}, {geo.get('lon')}"
        })

if __name__ == "__main__":
    main()
