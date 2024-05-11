# Builder

Uma Maneira simples de gerar HTML usando python

## Exemplo de Uso

```python
from builder.tags import Body, H1

body = Body(classes=["container", "dark-theme"], children=[
            H1(["Hello world"])
       ])
result = body.build() # result == <body class="container dark-theme"><h1>Hello world</h1></body>
```
