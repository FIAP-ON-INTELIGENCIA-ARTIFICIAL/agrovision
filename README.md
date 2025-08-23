# 🌾 Projeto AgroVision - Aplicação para Apoio ao Agronegócio

## 📌 Resumo do Projeto
O projeto tem como objetivo desenvolver **uma aplicação em Python** para auxiliar agricultores no **cálculo de áreas de plantio, aplicação de insumos e previsão de produção agrícola**.  
Além da implementação prática, o projeto integra **análises estatísticas em R**, permitindo explorar dados coletados de forma mais aprofundada, apoiando a **tomada de decisão no agronegócio**.  

O escopo também inclui:
- **Integração com APIs meteorológicas públicas**, para coleta e análise de dados climáticos.  
- **Uso de GitHub** como plataforma de versionamento e colaboração, simulando um ambiente real de desenvolvimento de software.  
- **Reflexão crítica** sobre o impacto social, ético e ambiental das tecnologias aplicadas ao agronegócio, por meio de atividades de leitura e resumo de artigos acadêmicos.  

---

## 🎥 Apresentação do Seu Jorge do Agro

Conheça o Seu Jorge, agricultor do interior de Goiás e cliente representativo do Projeto AgroVision.  
Neste vídeo, ele compartilha sua experiência no campo e como a tecnologia pode transformar a produção agrícola.(click na imagem)

[![Apresentação do Seu Jorge do Agro](https://img.youtube.com/vi/cSJFwvnrj1w/hqdefault.jpg)](https://www.youtube.com/watch?v=cSJFwvnrj1w)

---

## 📂 Estrutura de Pastas

```text
agrovision/
├── app.py                     # Ponto de entrada do backend Flask
├── api/                       # Código da API em Flask
│   └── main.py                # Implementação das rotas
├── requirements.txt            # Dependências Python
├── .env.example                # Exemplo de variáveis de ambiente
├── docker-compose.yml          # Orquestração dos serviços (Flask + R)
│
├── docker/                     # Configurações de container
│   └── web.Dockerfile          # Dockerfile do serviço Flask
│
├── r/                          # Serviço de análise em R
│   ├── plumber.R               # Endpoints estatísticos (Plumber)
│   └── Dockerfile              # Dockerfile do serviço R
│
├── etl/                        # Pipelines de dados em Python
│   └── pipeline.py             # Pipeline simples de ETL
│
├── analysis/                   # Scripts de análise e treino
│   └── train.py                # Script de treino (modelo ML)
│
├── data/                       # Dados de exemplo
│   └── solo.csv                # Arquivo CSV inicial
│
├── web/                        # Frontend PWA
│   ├── index.html              # Página principal
│   ├── app.js                  # Lógica da interface
│   ├── styles.css              # Estilos da aplicação
│   ├── manifest.webmanifest    # Configuração PWA
│   └── service-worker.js       # Suporte offline
│
├── notebooks/                  # (Opcional) Notebooks de análise
│   └── demo.ipynb              # Exploração/EDA ou treino de modelo
│
├── docs/                       # Documentação acadêmica
│   ├── arquitetura.md          # Arquitetura do sistema
│   ├── clima.md                # Notas sobre dados meteorológicos
│   └── etica_impacto.md        # Reflexão ética, social e ambiental
│
└── .github/                    # Integração contínua (CI/CD)
    └── workflows/
        └── ci.yml              # Pipeline de testes no GitHub Actions

```

## Descrição das Pastas e Arquivos

- **app.py**
  Ponto de entrada que expõe a aplicação Flask definida em `api/main.py`.

- **api/**
  Código da API em Flask com as rotas do sistema.

- **requirements.txt**
  Lista de dependências Python necessárias para rodar o projeto.

- **.env.example**  
  Exemplo de configuração de variáveis de ambiente (pode ser copiado para `.env`).

- **docker-compose.yml**  
  Arquivo para orquestração dos containers (Flask + R).

---

### 📂 docker/
- **web.Dockerfile**
  Dockerfile do serviço Flask (backend + PWA).

---

### api/
- **main.py**
  Implementação das rotas da aplicação Flask.

---

### r/
- **plumber.R**
  API estatística desenvolvida em R (Plumber).
- **Dockerfile**
  Dockerfile do serviço R.

---
### etl/
- **pipeline.py**
  Pipeline de ETL simples para preparar dados de solo.

---

### analysis/
- **train.py**
  Script de treino para criação de modelo de machine learning (opcional).

---

### data/
- **solo.csv**  
  Arquivo de dados de exemplo com informações de solo.

---

### web/
- **index.html**  
  Página principal da aplicação (PWA).  
- **app.js**  
  Lógica da interface e integração com a API Flask.  
- **styles.css**  
  Estilos da interface.  
- **manifest.webmanifest**  
  Configuração do PWA (instalável no celular).  
- **service-worker.js**  
  Implementação de cache/offline-first para PWA.

---

### notebooks/
- **demo.ipynb**  
  Notebook opcional para exploração de dados (EDA) e análises adicionais.

---

### docs/
- **arquitetura.md**  
  Descrição da arquitetura da aplicação.  
- **clima.md**  
  Explicação sobre integração com dados meteorológicos.  
- **etica_impacto.md**  
  Reflexão crítica sobre impactos sociais, éticos e ambientais.

---

### .github/workflows/
- **ci.yml**  
  Pipeline de integração contínua (CI) para rodar testes no GitHub Actions.

---

## ⚙️ Principais Dependências Técnicas

### **Python**
- `NumPy` / `Pandas` → manipulação e análise de dados tabulares.  
- `Matplotlib` / `Seaborn` / `Plotly` → visualização de dados.  
- `Shapely` / `GeoPandas` → cálculos de área de plantio e dados geoespaciais.  
- `Requests` → integração com APIs externas.  
- `Flask` ou `FastAPI` *(opcional)* → desenvolvimento de interface web da aplicação.  

### **R**
- `tidyverse` (`dplyr`, `tidyr`, `ggplot2`) → manipulação e visualização de dados.  
- `httr` / `jsonlite` → conexão com APIs meteorológicas.  
- `forecast` → técnicas estatísticas para previsão de produção.  

### **Infraestrutura / Colaboração**
- **Git + GitHub** → versionamento, pull requests, resolução de conflitos.  
- **Markdown / LaTeX** → documentação e relatórios.  

---

## 🌱 Valor Educacional
- Desenvolvimento de **competências técnicas** (programação, análise de dados, integração de APIs).  
- Experiência prática em **colaboração com GitHub**.  
- Formação crítica em **ética, sustentabilidade e responsabilidade social** no agronegócio.

---

## 👥 Time

<table>
  <tr>
    <td width="110" align="center" valign="top">
      <a href="https://github.com/SabrinaOtoni">
        <img src="https://github.com/SabrinaOtoni.png" width="100" height="100" alt="Avatar de Sabrina Otoni" style="border-radius:50%; object-fit:cover;" />
      </a>
    </td>
    <td valign="middle">
      <strong style="font-size:1.05rem;">Sabrina Otoni</strong><br/>
      <a href="https://github.com/SabrinaOtoni">@SabrinaOtoni</a><br/>
      <img alt="Tutor" src="https://img.shields.io/badge/role-Tutor-4C1?style=flat-square" />
    </td>
    <td width="110" align="center" valign="top">
      <a href="https://github.com/henriquehsilva">
        <img src="https://github.com/henriquehsilva.png" width="100" height="100" alt="Avatar de Henrique Silva" style="border-radius:50%; object-fit:cover;" />
      </a>
    </td>
    <td valign="middle">
      <strong style="font-size:1.05rem;">Henrique Silva</strong><br/>
      <a href="https://github.com/henriquehsilva">@henriquehsilva</a><br/>
      <img alt="Papel" src="https://img.shields.io/badge/papel-Desenvolvedor-36a2eb?style=flat-square" />
    </td>
  </tr>
</table>


