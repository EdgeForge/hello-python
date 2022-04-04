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
curl https://api-default-${myProject}.dev.edgeforge.com/wafw00f -d 'https://f5.com' -H "Content-type: text/plain"
```
