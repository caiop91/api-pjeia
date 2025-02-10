# PJeIA API

API oficial do PJeIA

## Endpoint Base

```
https://pjeia-backend.vercel.app/api/v1/external
```

## Autenticação

Para utilizar a API, você precisará de uma API Key. Entre em contato através do email suporte@pjeia.com.br para solicitar acesso.

## Endpoints

### Gerar Resposta

```https
POST /completions
```

Endpoint para gerar respostas utilizando a IA do PJeIA. A resposta é retornada em streaming e em formato markdown para melhor experiência do usuário. 

### Exemplos

#### Terminal (curl)
```bash
curl -X POST https://pjeia-backend.vercel.app/api/v1/external/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: SUA_CHAVE_DE_API" \
  -d '{"prompt": "resuma o inteiro teor"}'
```

#### JavaScript (Node.js)
```javascript
const response = await fetch('https://pjeia-backend.vercel.app/api/v1/external/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-API-Key': 'SUA_CHAVE_DE_API'
  },
  body: JSON.stringify({ prompt: 'resuma o inteiro teor' })
});

for await (const chunk of response.body) {
  process.stdout.write(new TextDecoder().decode(chunk));
}
```

#### Python
```python
import requests

response = requests.post(
    'https://pjeia-backend.vercel.app/api/v1/external/completions',
    headers={
        'Content-Type': 'application/json',
        'X-API-Key': 'SUA_CHAVE_DE_API'
    },
    json={'prompt': 'resuma o inteiro teor'},
    stream=True
)

for chunk in response.iter_content(chunk_size=None):
    print(chunk.decode(), end='')
```

#### Ruby on Rails
```ruby
require 'net/http'
require 'json'

uri = URI('https://pjeia-backend.vercel.app/api/v1/external/completions')
request = Net::HTTP::Post.new(uri)
request['Content-Type'] = 'application/json'
request['X-API-Key'] = 'SUA_CHAVE_DE_API'
request.body = { prompt: 'resuma o inteiro teor' }.to_json

Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
  http.request(request) do |response|
    response.read_body do |chunk|
      print chunk
    end
  end
end
```

## Códigos de Erro

| Código | Descrição                                    |
|--------|----------------------------------------------|
| 400    | Requisição inválida                          |
| 401    | API Key inválida ou expirada                 |
| 413    | Conteúdo muito grande                        |
| 429    | Rate limit excedido                          |
| 500    | Erro interno do servidor                     |

## Suporte

Para dúvidas, sugestões ou relatar problemas:

- Email: suporte@pjeia.com.br

## Segurança

- Todas as requisições devem ser feitas usando HTTPS
- Mantenha a chave de API em variável de ambiente 