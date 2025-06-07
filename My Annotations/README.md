# Convert PDF to Text

 ## Two Tools

 `magick {input.pdf} {output.tiff}`
 `tesseract {input.tiff} {output}`

 or for bulk files `for i in *.tif ; do tesseract $i - >> output.txt;  done`
