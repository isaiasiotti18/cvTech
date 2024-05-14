# API de Geração de Currículos

Este projeto é uma API construída com FastAPI para gerar currículos em formato compatível com ATS (Applicant Tracking System). A API aceita detalhes de currículos em formato JSON e retorna um documento DOCX com as informações fornecidas.

## Requisitos
- Python 3.8+
- FastAPI
- Uvicorn
- python-dotenv
- python-docx

## Configuração do Ambiente

git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio

## Crie um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

## Instale as dependências

pip install -r requirements.txt

## Execute a aplicação

uvicorn app.main:app --reload

## Endpoints da API

Gerar Currículo:

URL: /api/v1/resume/generate_resume
Método: POST
Content-Type: application/json

## Exemplo de Payload

```{
    "name": "João Silva",
    "contact": "joao.silva@example.com",
    "experience": [
        {
            "title": "Desenvolvedor de Software",
            "company": "Empresa X",
            "description": "Desenvolvimento de aplicações web utilizando tecnologias como Python, Django e JavaScript."
        },
        {
            "title": "Estagiário em TI",
            "company": "Empresa Y",
            "description": "Suporte técnico e manutenção de sistemas internos."
        }
    ],
    "education": [
        {
            "degree": "Bacharel em Ciência da Computação",
            "institution": "Universidade Z",
            "description": "Formação acadêmica focada em desenvolvimento de software, algoritmos e estruturas de dados."
        },
        {
            "degree": "Curso Técnico em Informática",
            "institution": "Instituição W",
            "description": "Curso técnico voltado para redes de computadores e programação."
        }
    ]
}
```
