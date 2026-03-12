import json
import sys
import urllib.request
import urllib.parse

ENDPOINT = "https://api.zerone.market/api"

def fetch_json(url):
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode()
            if response.status == 200:
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    return content
            else:
                print(f"Error: API returned status {response.status}", file=sys.stderr)
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
    return None

def list_skills():
    url = f"{ENDPOINT}/skills?lang=en"
    data = fetch_json(url)
    if data and "data" in data:
        print(json.dumps(data["data"], indent=2, ensure_ascii=False))
    else:
        print("Failed to fetch skill list.")

def skill_info(name):
    url = f"{ENDPOINT}/skills/{urllib.parse.quote(name)}?lang=en"
    data = fetch_json(url)
    if data:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Failed to fetch info for skill '{name}'.")

def install_skill(name, framework):
    url = f"{ENDPOINT}/skills/{urllib.parse.quote(name)}/install?framework={urllib.parse.quote(framework)}&lang=en"
    data = fetch_json(url)
    if data:
        if isinstance(data, dict):
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(data)
    else:
        print(f"Failed to fetch install tutorial for skill '{name}' with framework '{framework}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python market.py <list|info|install> [name] [framework]")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "list":
        list_skills()
    elif cmd == "info":
        if len(sys.argv) < 3:
            print("Usage: python market.py info <skill-name>")
            sys.exit(1)
        skill_info(sys.argv[2])
    elif cmd == "install":
        if len(sys.argv) < 4:
            print("Usage: python market.py install <skill-name> <framework>")
            sys.exit(1)
        install_skill(sys.argv[2], sys.argv[3])
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
