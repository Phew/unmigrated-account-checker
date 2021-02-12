import requests, json, os, re, sys

def main():
    os.system('cls')
    uuid = sys.argv[0]
    os.system('cls')
    url = f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}'
    headers = {"Content-Type": "application/json"}
    r = requests.get(url, headers=headers)
    op = json.loads(r.text)
    find = re.search(r'("legacy")', r.text)
    bad = re.search(r'("Bad Request")', r.text)
    try:
        if find:
            print('Unmigrated: True')
        if bad:
            print('The UUID you gave is invalid.')
        else:
            print('This account is migrated :/')
    except Exception as e: print(e)

main()
