# python-every-day
this repository contains python3 code snippets for repetitive problems and understanding new concepts


# python venv installation
## MacOSX
### Find the python path
```
brew search python
brew install python@3.10
brew info python@3.10
```
console outputs:
```console
/opt/homebrew/opt/python@3.10/bin/python3
```

### Create VENV with specifiy python version
```
/opt/homebrew/opt/python@3.10/bin/python3 -m venv ~/VENV/python3.10
```

### select the interpreter in VS code
select the interpreter -> enter interpreter path -> `~/VENV/python3.10/bin/python3.10`

### install packages
In VS code terminal after the VENV is activate:

```console
pip install -r requirements.txt
```

(optional) from a terminal
```
# <venv_paht>/bin/activate
source ~/VENV/python3.10/bin/activate
pip install -r <path>/requirements.txt
deactivate
```


