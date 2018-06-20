Flask front-end that passes commands to [s7mx1/pihat](https://github.com/s7mx1/pihat).

Usage
-----

```
git clone https://github.com/paulherron/status-remotes.git
cd status-remotes
python ./server.py
```

Browse to URLs, e.g:

* [http://localhost:3100/](http://localhost:3100/)
* [http://localhost:3100/on](http://localhost:3100/on)
* [http://localhost:3100/off](http://localhost:3100/off)
* [http://localhost:3100/on?device=10](http://localhost:3100/on?device=10)
* [http://localhost:3100/off?device=10](http://localhost:3100/off?device=10)
