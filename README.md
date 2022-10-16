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
/opt/homebrew/opt/python@3.10/bin/python3 -m venv ~/VENV/metal3.10
```

### select the interpreter in VS code
select the interpreter -> enter interpreter path -> `~/VENV/metal3.10/bin/python3.10`

### install packages
In VS code terminal after the VENV is activate:

```console
python3 -m pip uninstall -y tensorflow tenstensorflow-macos tensorflow-metal tensorflow-federated
python3 -m pip install -r requirements.txt
```

(optional) from a terminal
```
# <venv_paht>/bin/activate
source ~/VENV/metal3.10/bin/activate
pip install --upgrade pip
pip install -r <path>/requirements.txt
deactivate
```

### Add a jupyter notebook kernel to VENV
```console
source ~/VENV/metal3.10/bin/activate
pip install ipykernel
ipython kernel install --user --name=metal3.10
```
Then you need to restart the vs code, to select the venv as jupyter notebook kernel,
projectname/name is `metal3.10`, which is the venv name.

Reference:
* https://anbasile.github.io/posts/2017-06-25-jupyter-venv/


