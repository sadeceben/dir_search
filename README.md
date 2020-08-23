## What is Directory Traversal Attack
Details:[click me.](https://null-byte.wonderhowto.com/how-to/hack-like-pro-find-directories-websites-using-dirbuster-0157593/)

### How to install  ?

Firstly, if not installed "requests" library :

```sh
pip3 install requests
```

then...

```sh
git clone https://github.com/sadeceben/dir_search.git
```

finally

```sh
cd dir_search/ && chmod +x main.py
```

### How to using ?

```sh
./main.py {site_url} {world_list_path}
```

example : 

```sh
./main.py "http://cemaltiryaki.com" ~/wordlist/common.txt
```

