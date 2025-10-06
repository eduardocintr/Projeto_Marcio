# Projeto Marcio — Frontend

Este README documenta apenas a parte do frontend do "Projeto Marcio" e, em particular, descreve a minha contribuição feita neste trabalho.

Resumo da contribuição 

- Tela de Login (página de autenticação): `src/app/login/page.js` (e componentes relacionados).
- Landing page / página inicial: `src/app/page.js`.
- Alteração do layout principal do aplicativo: `src/app/layout.js` e `src/components/layout.js`.
- Criação da sidebar (barra lateral): `src/components/app-sidebar.js` e/ou `src/components/ui/sidebar.jsx`.

Essas alterações/implementações são a parte do frontend que foi desenvolvida — o backend (FastAPI) e outras partes do projeto foram desenvolvidas por outros membros.

## Visão geral do frontend

- Framework: Next.js (React)
- Estilização: TailwindCSS (configuração presente entre dependências)
- Padrões: a aplicação usa a pasta `src/app` (App Router) para páginas e `src/components` para componentes reutilizáveis.

## Como rodar o projeto (apenas frontend) — Windows PowerShell

1) Instalar dependências

```powershell
cd frontend
npm install
```

2) Rodar em modo desenvolvimento

```powershell
npm run dev
```

Abra http://localhost:3000 no seu navegador.

Se for necessário rodar a API localmente (para autenticação/usuários), execute também o backend na pasta `backend` (veja instruções no `../backend/README` ou os comandos descritos neste repositório):

```powershell
cd ..\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Arquivos e componentes principais alterados/implementados (por autor)

- `src/app/login/page.js` — Tela de login, formulário e lógica básica de submissão.
- `src/app/page.js` — Landing page (conteúdo inicial / marketing).
- `src/app/layout.js` — Estrutura global do app (header, footer, wrappers).
- `src/components/layout.js` — Componentização do layout e wrappers reutilizáveis.
- `src/components/app-sidebar.js`` ou `src/components/ui/sidebar.jsx` — Sidebar criada para navegação.
- `src/components/*` — Pequenos componentes UI usados nas telas acima (botões, inputs, cards etc.).

Observação: os nomes exatos dos arquivos podem variar ligeiramente; listei os caminhos mais prováveis com base na estrutura atual do projeto.

## Variáveis de ambiente (frontend)

- `NEXT_PUBLIC_API_URL` — URL pública da API (ex.: `http://localhost:8000`).
- `NEXT_PUBLIC_SUPABASE_URL` e `NEXT_PUBLIC_SUPABASE_KEY` — caso o frontend consuma Supabase diretamente.

Evite comitar segredos no repositório.

## Recomendações para quem for revisar/continuar o trabalho

- Testar o fluxo de login com a API local (garantir que as rotas de autenticação do backend estão disponíveis).
- Validar responsividade da landing page e do layout principal.
- Separar lógica de autenticação em hooks/contexts (ex.: `UserContext.js`) para facilitar testes e reuso.

## Sugestões futuras (opcionais)

- Adicionar testes unitários/integração para o fluxo de login.
- Criar um `frontend/.env.example` com as variáveis mínimas.
- Documentar os componentes principais (Storybook ou MDX) para facilitar revisão.

---

Se quiser, eu posso agora:
- Gerar um `frontend/.env.example` com as variáveis sugeridas.
- Ler automaticamente os arquivos do backend para gerar uma documentação resumida dos endpoints de autenticação (POST /login, POST /register etc.).
Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
