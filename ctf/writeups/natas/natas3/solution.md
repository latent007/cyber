# NATAS3 Writeup

## Starting the challenge
> Starting the challenge by going to the link http://natas3.natas.labs.overthewire.org/

---

As with natas2, it says "There is nothing on this page."

This sounds kinda suspicious. Maybe check the source code to inspect further.

### Solution
1. View source code.
- We get no more information leaks it says. Although it states **Not even Google wil find it this time...**
- Maybe we should do a little googling?
- Try to google: **Google Webcrawlers**

#### TLDR
Google Webcrawlers scan websites to update googles search index.
It looks for at path: /robots.txt
Here you specify what parts of your website the crawler is allowed to access.

2. Accessing files path
```bash
http://natas3.natas.labs.overthewire.org/robots.txt
```
- Here you can find a hidden directory **/s3cr3t/**

3. Accessing secret file path
```bash
http://natas3.natas.labs.overthewire.org/s3cr3t/
```
- As with natas2 you can open users.txt and find the password for natas4
