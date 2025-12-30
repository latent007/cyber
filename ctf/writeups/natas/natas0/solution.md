# NATAS0 Writeup

## Starting the challenge
> Starting the challenge by going to the link http://natas0.natas.labs.overthewire.org/

---

### Solution
1. Sign in to the website
**Username and Password**
```bash
natas0
```

2. Find the credentials for the next level.
- Right click the page and select "View Source" to see the source code.
- You will see a div element containing the password for natas1

```html
<div id="content">
You can find the password for the next level on this page.

<!--The password for natas1 is 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq -->
</div>
```

3. Accessing natas1 by going to natasX.natas.labs.overthewire.org where "X" is the level counter. 
