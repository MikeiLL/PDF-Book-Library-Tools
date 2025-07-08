"""
Get list of saved words from Kobo eReader if plugged in.
Get definitions from the `dict` command.
Write them to wordlist.md file.
"""
import os, sqlite3, sys
from pprint import pprint
import subprocess

DB_PATH = "/Volumes/KOBOeReader/.kobo/KoboReader.sqlite"

if not os.path.exists(DB_PATH):
  print("No DB found. Are you sure your reader is mounted?")
  sys.exit()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
res = cur.execute("select text from Wordlist")
wordlist = res.fetchall()
pprint(wordlist)
print(len(wordlist))
with open("wordlist.md", "w") as f:
  for word in [w[0] for w in wordlist]:
    f.write(f"## {word}\n")
    try:
      p = subprocess.check_output([f"/usr/local/bin/dict", word], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
      f.write(f"\n===\n{e.output}\n===\n\n")
      continue
    f.write(f"\n===\n{p}\n===\n\n")
