# Convert PDF to Text

 ## Two Tools

 `magick {input.pdf} {output.tiff}`
 `tesseract {input.tiff} {output}`

 or for bulk files `for i in *.tif ; do tesseract $i - >> output.txt;  done`

 Ahah!

 ```
 sqlite3 /Volumes/KOBOeReader/.kobo/KoboReader.sqlite
 sqlite> .tables
 sqlite> .schema Bookmarks
 sqlite> select text from Bookmark where VolumeID='38714108-76da-4cf4-8444-a26cb160d6ee';
 ```
