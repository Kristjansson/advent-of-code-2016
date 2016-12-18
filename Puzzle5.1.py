import hashlib

doorID = "ojvtpuvg"
password = ""
index = 0
while len(password) < 8:
    ha = hashlib.md5(doorID + str(index)).hexdigest()
    if ha[0:5] == "00000":
        password = password + ha[5]
        print password
    index = index + 1