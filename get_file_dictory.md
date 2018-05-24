- see [SETUP_DIRNAME](https://github.com/saltstack/salt/blob/develop/setup.py#L46-L52)
- https://stackoverflow.com/questions/2292703/how-can-i-get-the-executables-current-directory-in-py2exe
- @TODO: what is `sys.frozen`?

```
# Change to salt source's directory prior to running any command
try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    # We're most likely being frozen and __file__ triggered this NameError
    # Let's work around that
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])
```
