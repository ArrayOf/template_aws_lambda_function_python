# AWS Lambda Function Template for Python

Este é um modelo [cookiecutter](https://github.com/audreyr/cookiecutter) para gerar
um aplicativo para execução na AWS Lambda Function.

# Recursos

- [pytest](https://github.com/pytest-dev/pytest/) para executar testes
(análise e manipulação de comandos, argumentos, opções, etc.)
- `yml` arquivo para [Travis](http://travis-ci.org/) CI
- Diferentes opções de licença de código aberto

# Compilar o projeto
- Instale os requisitos
```
git clone https://github.com/ArrayOf/template_aws_lambda_function_python.git template
cd template
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

# Uso do template

- Instale os requisitos
```
pip install cookiecutter
```
- Gerar código inicial do projeto
```
cookiecutter https://github.com/ArrayOf/template_aws_lambda_function_python.git
```
ou
```
python -m cookiecutter https://github.com/ArrayOf/template_aws_lambda_function_python.git
```

# Contribuindo

Os colaboradores são sempre bem-vindos! Ainda não há diretrizes de contribuição.
Sinta-se à vontade para levantar uma questão ou enviar um PR.

# Autores

<table>
  <tr>
    <td align="center"><a href="https://arrayof.io"><img style="border-radius: 50%;" src="https://avatars2.githubusercontent.com/u/3305437?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Thiago Filadelfo</b></sub></a><br /><a href="https://github.com/trfiladelfo" title="Github">👨‍</a></td>
  </tr>
</table>
