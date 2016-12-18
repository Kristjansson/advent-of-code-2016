import hashlib

doorID = "ojvtpuvg"
password = ['', '', '', '', '', '', '', '']
answersNeeded = 8
index = 0

while answersNeeded > 0:
    ha = hashlib.md5(doorID + str(index)).hexdigest()
    if ha[0:5] == "00000":
        if '0' <= ha[5] and ha[5] <= '7':
            if password[int(ha[5])] == '':
                password[int(ha[5])] = ha[6]
                answersNeeded = answersNeeded - 1
                print password
    index = index + 1

print ''.join(password)