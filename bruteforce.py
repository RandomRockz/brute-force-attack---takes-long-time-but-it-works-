import zipfile
import time

folderpath = input("Path to file: ")
folderpath = folderpath.strip()
zipf  = zipfile.ZipFile(folderpath)

except:
    pass
if not zipf:
    print("not password protected; you can safely open !T")

else:
    starttime=time.time()
    result=0
    c=0

    chars =  ['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']
    print("brute force started")
    if result==0:
        print("checking 4 letter passwords")w
        for i in chars:
            for j in chars:
                for k in chars:
                    for l in chars:
                        guess = str(i)+str(j)+str(k)+str(l)
                        password = guess.encode("utf-8").strip()
                        c+=1
                        try: 
                            with zipfile.ZipFile(folderpath,"r") as zf:
                                zf.extractall(pwd=password)
                                print("success, password is "+guess)
                                endtime=time.time()
                                result=1
                        except:
                            pass
                    if result==1:
                        break
                if result==1:
                    break
            if result==1:
                break
    if result==0:
        duration = endtime- starttime
        print("total - "+str(c)+" combinations in "+str(duration)+" seconds")
    else:
        duration = endtime- starttime
        print("congrats: total - "+str(c)+" combinations in "+str(duration)+" seconds")

