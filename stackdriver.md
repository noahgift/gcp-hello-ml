## Install Stackdriver on GAE

1.  Add to requirements.txt
2.  run `make install`
3.  Add to startup

```python
if __name__ == '__main__':
    try:
        import googleclouddebugger
        googleclouddebugger.enable()
    except ImportError:
        pass
    app.run(host='127.0.0.1', port=8080, debug=True)
```


## Reference

* [https://cloud.google.com/debugger/docs/setup/python?hl=en_US&_ga=2.223376920.-2034838952.1534129025](Install Stackdriver)
