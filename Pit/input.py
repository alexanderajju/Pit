import requests

def login(username, password):
    data = {'login':username,'pwd':password,'lang':''}
    r = requests.post('http://dms-pit.htb/seeddms51x/seeddms/op/op.Login.php', data=data, allow_redirects=False)
    if r.headers['Location'] == '../out/out.Login.php?msg=Error+signing+in.+User+ID+or+password+incorrect':
        return False
    return True
    # import pdb;pdb.set_trace()


if login("michelle", "michelle"):
    print("Login Successfull[+]")
