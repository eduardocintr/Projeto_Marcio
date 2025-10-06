# 🧠 Projeto Marcio

## 🎯 Objetivo

O Projeto Marcio é uma plataforma web desenvolvida para conscientização sobre fake news, suporte ao usuário e gestão de contas, integrando recursos de inteligência artificial, autenticação segura e arquitetura moderna.

O objetivo é oferecer uma experiência intuitiva, segura e escalável, promovendo o combate à desinformação e facilitando o acesso ao suporte.

## 🧰 Tecnologias Utilizadas

- **Back-end:**
  - FastAPI (Python)
  - Supabase (autenticação e banco de dados)
  - Uso da API do Groq console para integração com inteligência artificial
- **Front-end:**
  - Next.js (React)
  - TailwindCSS
- **Banco de Dados:**
  - Supabase (PostgreSQL)
- **Criptografia & Autenticação:**
  - JWT para autenticação segura e proteção de rotas
- **Inteligência Artificial:**
  - Uso de Chat-GPT e Copilot para auxílo de código
- **Arquitetura da Aplicação:**
  - Separação entre frontend (Next.js) e backend (FastAPI)
  - Comunicação via API REST
  - Autenticação baseada em JWT
  - Integração com Supabase para dados e autenticação

## 🏗️ Estrutura do Projeto

```
Projeto-Marcio/
├── backend/                  # API REST com FastAPI, rotas, autenticação, IA
├── frontend/                 # Interface web com Next.js
│   ├── src/
│   │   ├── app/             # Páginas (fake news, suporte, login, dashboard)
│   │   ├── components/      # Componentes reutilizáveis
│   │   └── contexts/        # Contextos globais (ex: autenticação)
└── README.md
```

# Frontend

Este README documenta a parte frontend do Projeto Marcio, descrevendo as páginas e componentes que desenvolvi pessoalmente no decorrer do trabalho.

## ✍️ Contribuição Pessoal

Durante o desenvolvimento do frontend, fiquei responsável principalmente pelas páginas da aplicação. Minhas entregas foram:

- **📰 Página de Fake News**
    - Implementação da interface e lógica visual para exibição e interação com conteúdos relacionados a fake news.
    - Arquivo principal: `src/app/fakenews/page.js`

- **🆘 Página de Suporte**
    - Desenvolvimento da página voltada para contato/ajuda aos usuários, com estrutura clara e responsiva.
    - Arquivo principal: `src/app/suporte/page.js`

- **🏠 Página Inicial**
    - Estruturação da home page da aplicação.
    - Arquivo principal: `src/app/page.js`

Essas páginas compõem a base da experiência do usuário no frontend e foram construídas com foco em clareza, organização e estilo consistente com o restante do projeto.

## 🧠 Visão Geral do Frontend

- **Framework:** Next.js (React)
- **Estilização:** TailwindCSS

### Arquitetura

- **Páginas:** localizadas em `src/app` (App Router)
- **Componentes:** localizados em `src/components` para reaproveitamento

> O backend foi desenvolvido separadamente pela equipe, utilizando FastAPI, não fazendo parte direta das minhas contribuições.
