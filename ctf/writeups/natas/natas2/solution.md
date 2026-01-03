# NATAS2 Writeup

## Starting the challenge
> Starting the challenge by going to the link http://natas2.natas.labs.overthewire.org/

---

It says There is nothing on this page.

This sounds kinda suspicious. Maybe check the source code to inspect further.

### Solution
1. View source code.
- In this specific div element theres an img tag. This contains a .png file.
If we take a closer look at the path the image is located at you see it is under "files".
```html
<div id="content">
There is nothing on this page
<img src="files/pixel.png">
</div>
```

2. Accessing files path
```bash
http://natas2.natas.labs.overthewire.org/files/
```
- We can now see list items in the path. Open "users.txt" to get the password for natas3.
