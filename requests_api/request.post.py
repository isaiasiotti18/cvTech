import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'name': 'João Silva',
    'contact': 'joao.silva@example.com',
    'experience': [
        {
            'title': 'Desenvolvedor de Software',
            'company': 'Empresa X',
            'description': 'Desenvolvimento de aplicações web utilizando tecnologias como Python, Django e JavaScript.',
        },
        {
            'title': 'Estagiário em TI',
            'company': 'Empresa Y',
            'description': 'Suporte técnico e manutenção de sistemas internos.',
        },
    ],
    'education': [
        {
            'degree': 'Bacharel em Ciência da Computação',
            'institution': 'Universidade Z',
            'description': 'Formação acadêmica focada em desenvolvimento de software, algoritmos e estruturas de dados.',
        },
        {
            'degree': 'Curso Técnico em Informática',
            'institution': 'Instituição W',
            'description': 'Curso técnico voltado para redes de computadores e programação.',
        },
    ],
}

response = requests.post('http://localhost:8000/api/v1/resume/generate_resume', headers=headers, json=json_data)