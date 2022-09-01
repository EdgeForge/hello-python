# WAFW00f
The Web Application Firewall Fingerprinting Tool.
thanks to https://github.com/EnableSecurity/wafw00f

## local
```
pip install -r requirements.txt
python main.py
```

## edgeforge

```bash
myProject="projectid"
functionName="hello-python3-6e36c8"
curl https://${functionName}-${myProject}.xc.edgeforge.com/wafw00f -d 'https://f5.com' -H "Content-type: text/plain"
```
