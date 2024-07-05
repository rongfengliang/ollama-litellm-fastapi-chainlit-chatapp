# ollama + litellm proxy + chainlit 

## Starting

* install deps

```code
pip install fastapi 'litellm[proxy]' chainlit 
```

* starting litellm proxy

```code
litellm --config ./config.yaml
```

* startning  service

```code
python main.py
```

* view chat app

```code
http://localhost:8000/chainlit
```