#!/usr/bin/python3
import requests

url = "https://adventofcode.com/2023/leaderboard/private/view/1550660.json"

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://adventofcode.com/2023/leaderboard/private/view/1550660",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.2.896107865.1701362125; _gid=GA1.2.743336869.1701362125; _ga_MHSNPJKWC7=GS1.2.1701451150.6.1.1701452898.0.0.0; session=53616c7465645f5f234cfdb4aaf40d50168e4e45a7d442bfcf4cf42490763c45df18d5b554b981e0976c43d6d878590a7710f335b934e7ba234855dd4d17ddd2; _gat=1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
}

response = requests.request("GET", url, data=payload, headers=headers).json()
members = response["members"]
leaderboard = []
for e in members.values():
    leaderboard.append((e["name"], e["local_score"], e["stars"]))
leaderboard.sort(key=lambda x: x[1], reverse=True)
for i, (n, sc, st) in enumerate(leaderboard):
    print(f"Name: {n} | Score: {sc} - Stars: {st}")
    if i == 9:
        break
