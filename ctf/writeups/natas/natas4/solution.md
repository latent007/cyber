# NATAS4 Writeup

## Starting the challenge
> Starting the challenge by going to the link http://natas4.natas.labs.overthewire.org/

---
We are prompted with **Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"**

- Maybe we should see if we can make it look like we come from natas5 url?
- Lookup the **Curl** command. For bash you can do **man curl**.

```bash
curl -u natas4:natas4passwordhere -e http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org/
```

- You will see the password for natas5 in the response.
