# Nexa Agent – Copiloto Operacional da Nexa Digital

## Descrição

Este repositório contém a aplicação **Nexa Agent**, um assistente interno desenvolvido com **Streamlit** e a API **Gemini** (Google Generative AI). O agente ajuda a equipe da Nexa Digital em diagnósticos, prospecção, scripts de vendas, otimização de perfil no Google, criação de conteúdo e muito mais.

---

## Pré‑requisitos

- **Python 3.9+** instalado.
- **pip** (gerenciador de pacotes Python).
- Uma conta no **Google Gemini** e a sua **GEMINI_API_KEY**. [Obtenha a chave aqui](https://ai.google.dev/gemini-api/docs/api-key).
- (Opcional) Conta no **GitHub** caso queira fazer deploy no Streamlit Cloud.

---

## Instalação passo a passo

1. **Clonar o repositório** (ou baixar o zip) e entrar na pasta do projeto:
   ```powershell
   git clone <URL_DO_REPOSITORIO>
   cd agent_ia_nexa
   ```

2. **Criar o arquivo de variáveis de ambiente**
   Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:
   ```text
   GEMINI_API_KEY=SUACHAVEAQUI
   ```
   > **⚠️** Não compartilhe este arquivo publicamente.

3. **Criar e ativar o ambiente virtual**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # PowerShell
   # ou, para CMD:
   # .\.venv\Scripts\activate.bat
   ```

4. **Instalar as dependências**
   ```powershell
   pip install -r requirements.txt
   ```
   Isso instalará:
   - `streamlit`
   - `google-generativeai`
   - `python-dotenv`
   - `Pillow`
   - outras bibliotecas necessárias.

---

## Executando a aplicação

Com o ambiente ativado, rode:
```powershell
streamlit run app.py
```
A aplicação será iniciada em `http://localhost:8501`. Abra esse endereço no navegador.

---

## Deploy no Streamlit Cloud (opcional)

1. **Commit e push** do seu código para um repositório GitHub.
2. Acesse [share.streamlit.io](https://share.streamlit.io) e conecte‑se ao seu repositório.
3. Na página de **Settings → Secrets**, adicione a secret `GEMINI_API_KEY` com o mesmo valor usado no `.env`.
4. O Streamlit Cloud instalará automaticamente as dependências listadas em `requirements.txt` e iniciará a app.

---

## Estrutura do projeto

- `app.py` – Código principal da aplicação Streamlit.
- `requirements.txt` – Lista de dependências Python.
- `.env` – Arquivo de variáveis de ambiente (não versionado).
- `README.md` – Este documento.

---

## Ajuda & Contribuição

Para dúvidas, abra uma *issue* neste repositório ou entre em contato com a equipe da Nexa Digital.

---

**Links úteis**
- Código da aplicação: [app.py](file:///C:/Users/felip/agent_ia_nexa/app.py)
- Dependências: [requirements.txt](file:///C:/Users/felip/agent_ia_nexa/requirements.txt)
- Variáveis de ambiente: [.env](file:///C:/Users/felip/agent_ia_nexa/.env)

Bom desenvolvimento! 🚀
