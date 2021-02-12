## Details
So basically what this does is send a GET request to the session server at mojang and grabs all the JSON data from given UUID and searches for the ("legacy": True) part. This only shows up if the account is unmigrated.

# Usage
```bash
requires > python3
requires > requests
```

```bash
python3 checker.py (UUID)
```
