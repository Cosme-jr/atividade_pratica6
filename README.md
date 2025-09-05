# Projetos Python - Gerador de Senhas e Consultas de APIs

Este repositório contém quatro programas Python que demonstram diferentes funcionalidades: geração de senhas aleatórias e consultas a APIs públicas para obtenção de dados diversos.

## 📋 Índice

- [Descrição dos Projetos](#descrição-dos-projetos)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Funcionalidades](#funcionalidades)
- [APIs Utilizadas](#apis-utilizadas)
- [Estrutura dos Arquivos](#estrutura-dos-arquivos)
- [Exemplos de Uso](#exemplos-de-uso)
- [Tratamento de Erros](#tratamento-de-erros)

## 🎯 Descrição dos Projetos

### 1. Gerador de Senhas Aleatórias
Programa que gera senhas seguras com caracteres especiais, permitindo ao usuário definir o comprimento desejado.

### 2. Gerador de Perfil de Usuário
Utiliza a API Random User Generator para criar perfis aleatórios com nome, email e país.

### 3. Consultor de CEP
Consulta informações de endereço através do CEP usando a API ViaCEP, retornando logradouro, bairro, cidade e estado.

### 4. Consultor de Cotações
Consulta cotações de moedas estrangeiras em relação ao Real Brasileiro usando a AwesomeAPI.

## 🔧 Pré-requisitos

- Python 3.6 ou superior
- Conexão com a internet (para os programas que utilizam APIs)

## 📦 Instalação

1. Clone este repositório:
```bash
git clone [url-do-repositorio]
cd [nome-do-diretorio]
```

2. Instale a biblioteca `requests` (necessária para os programas 2, 3 e 4):
```bash
pip install requests
```

## 🚀 Como Usar

### 1. Gerador de Senhas (`gerador_senhas.py`)
```bash
python gerador_senhas.py
```
- Digite o tamanho desejado da senha quando solicitado
- A senha será gerada automaticamente com letras, números e caracteres especiais

### 2. Gerador de Perfil (`perfil_usuario.py`)
```bash
python perfil_usuario.py
```
- O programa gerará automaticamente um perfil aleatório
- Exibirá nome, email e país do usuário fictício

### 3. Consultor de CEP (`consultor_cep.py`)
```bash
python consultor_cep.py
```
- Digite um CEP válido no formato XXXXX-XXX ou XXXXXXXX
- O programa retornará as informações do endereço correspondente

### 4. Consultor de Cotações (`cotacao_moedas.py`)
```bash
python cotacao_moedas.py
```
- Digite o código da moeda desejada (USD, EUR, GBP, etc.)
- O programa exibirá a cotação atual, máxima, mínima e data de atualização

## ⚡ Funcionalidades

### Gerador de Senhas
- ✅ Senhas com comprimento personalizável
- ✅ Inclui letras maiúsculas e minúsculas
- ✅ Inclui números e caracteres especiais
- ✅ Geração totalmente aleatória

### Gerador de Perfil
- ✅ Perfis realistas gerados pela Random User API
- ✅ Informações em português quando disponível
- ✅ Dados sempre atualizados

### Consultor de CEP
- ✅ Consulta rápida e precisa
- ✅ Tratamento de CEPs inválidos
- ✅ Informações completas do endereço
- ✅ API nacional confiável

### Consultor de Cotações
- ✅ Cotações em tempo real
- ✅ Histórico de máximas e mínimas do dia
- ✅ Data e hora da última atualização
- ✅ Suporte a múltiplas moedas

## 🌐 APIs Utilizadas

| API | Endpoint | Funcionalidade |
|-----|----------|----------------|
| **Random User Generator** | `https://randomuser.me/api/` | Geração de perfis aleatórios |
| **ViaCEP** | `https://viacep.com.br/ws/{cep}/json/` | Consulta de endereços por CEP |
| **AwesomeAPI** | `https://economia.awesomeapi.com.br/json/last/{moeda}-BRL` | Cotações de moedas |

## 📁 Estrutura dos Arquivos

```
projeto/
├── gerador_senhas.py      # Programa 1: Gerador de senhas
├── perfil_usuario.py      # Programa 2: Gerador de perfil
├── consultor_cep.py       # Programa 3: Consultor de CEP
├── cotacao_moedas.py      # Programa 4: Cotações de moedas
└── README.md              # Este arquivo
```

## 📝 Exemplos de Uso

### Exemplo 1: Gerador de Senhas
```
Informe o tamanho da senha: 12
Senha gerada: A7$k9mP@3xQ!
```

### Exemplo 2: Perfil de Usuário
```
Nome: João Silva
Email: joao.silva@example.com
País: Brazil
```

### Exemplo 3: Consulta de CEP
```
Informe o CEP: 01310-100
Logradouro: Avenida Paulista
Bairro: Bela Vista
Cidade: São Paulo
Estado: SP
```

### Exemplo 4: Cotação de Moedas
```
Informe o código da moeda (ex: USD, EUR, GBP): USD
Valor atual: 5.2150
Valor máximo: 5.2500
Valor mínimo: 5.1800
Data da última atualização: 2024-01-15 14:30:00
```

## ⚠️ Tratamento de Erros

Todos os programas incluem tratamento básico de erros:

- **Gerador de Senhas**: Valida se o tamanho informado é um número válido
- **Perfil de Usuário**: Trata falhas de conexão com a API
- **Consultor de CEP**: Identifica CEPs inexistentes ou inválidos
- **Cotação de Moedas**: Verifica se a moeda informada existe

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Em caso de dúvidas ou problemas:
- Verifique sua conexão com a internet
- Certifique-se de que o Python e as dependências estão instalados corretamente
- Consulte a documentação das APIs utilizadas

---

**Desenvolvido com ❤️ em Python**
