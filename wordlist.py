"""
Get list of saved words from Kobo eReader if plugged in.
Get definitions from the `dict` command.
Write them to wordlist.md file.
"""
import os, sqlite3, sys
from pprint import pprint
import subprocess
import string
from nltk.corpus import wordnet

DB_PATH = "/Volumes/KOBOeReader/.kobo/KoboReader.sqlite"

if not os.path.exists(DB_PATH):
  print("No DB found. Are you sure your reader is mounted?")
  sys.exit()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
res = cur.execute("select text from Wordlist")
wordlist = res.fetchall()
""" with open("wordlist.md", "w") as f:
  for word in [w[0] for w in wordlist]:
    f.write(f"## {word}\n")
    try:
      p = subprocess.check_output([f"/usr/local/bin/dict", word], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
      f.write(f"\n===\n{e.output}\n===\n\n")
      continue
    f.write(f"\n===\n{p}\n===\n\n") """
"""
Maybe I can get short definitions from the https://api.dictionaryapi.dev/api/v2/entries/en/ api.
TODO perhaps if no definition found, prompt for language and try that one.
"""
with open("wordlist.csv", "w") as f:
  for word in [w[0] for w in wordlist]:
    word = word.translate(str.maketrans('', '', string.punctuation))
    '''Word/Phrase	Translation	Part of Speech	IPA	Definition'''
    syns = wordnet.synsets(word)
    try:
      definition = syns[0].definition()
      partofspeach = syns[0].pos()
    except IndexError:
      print(f"Didn't work trying to get {word}\n")
      continue
    f.write(f"{word}\t{definition}\n")
