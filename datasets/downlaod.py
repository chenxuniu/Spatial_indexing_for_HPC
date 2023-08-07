#!/usr/bin/python
### the url is "http://spatialhadoop.cs.umn.edu/datasets.html"
import gdown
###use gdown package to download edges datasets from Google Drive
url1 = "https://drive.google.com/uc?id=0B1jY75xGiy7eOG85SHM3TzFVd2c"
output1 = "Edges"
url2 = "https://drive.google.com/uc?id=0B1jY75xGiy7eR3VpNC1XMzB5cWs"
output2 = "Areawater"
url3 = "https://drive.google.com/uc?id=0B1jY75xGiy7ebkNZaVZ0dVlPb3M"
output3 = "Linewater"
url4 = "https://drive.google.com/uc?id=0B1jY75xGiy7eSWFocG94S2ctYXc"
output4 = "Roads"

for i in range(4):
    input_url = "url"+str(i)
    output_file = "output"+str(i)
    gdown.download(input_url, output_file, quiet=False)

