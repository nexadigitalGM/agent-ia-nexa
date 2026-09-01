# Nexa Agent – Assistente Operacional da Nexa Digital

> **Visão geral**
> Um pequeno aplicativo Streamlit que utiliza o modelo Gemini 3.6 Flash (Google Generative AI) para responder a comandos de apoio operacional (MENU, DIAGNÓSTICO EXPRESS, ME GUIE, REVISE) e analisar imagens de prints de perfil.

---

## 📦 Pré‑requisitos

- **Python 3.13** (ou superior) instalado no Windows.
- **Git** (opcional, se for clonar o repositório).
- Uma **chave de API do Gemini** (`GEMINI_API_KEY`). Você pode obtê‑la em https://aistudio.google.com/app/apikey.

---

## 🚀 Passo a passo para instalar e rodar

1. **Obter o código**
   ```powershell
   # Se ainda não tem o projeto, clone o repositório (ou copie a pasta existente)
   git clone <URL_DO_SEU_REPOSITORIO> nexa-agent
   cd nexa-agent
   ```
   *Se você já tem a pasta `c:\Users\felip\agent_ia_nexa`, basta entrar nela.*

2. **Criar e ativar um ambiente virtual**
   ```powershell
   python -m venv .venv          # cria a venv na pasta .venv
   .\.venv\Scripts\Activate.ps1 # ativa a venv (PowerShell)
   # ou, no cmd: .\.venv\Scripts\activate.bat
   ```

3. **Instalar as dependências**
   ```powershell
   pip install -r requirements.txt
   ```
   O arquivo `requirements.txt` já contém:
   ```text
   streamlit==1.38.0
   google-generativeai==0.7.2
   Pillow==10.4.0
   python-dotenv==1.0.0
   ```

4. **Criar o arquivo de variáveis de ambiente**
   ```text
   # Na raiz do projeto, crie um arquivo chamado .env
   GEMINI_API_KEY=SUA_CHAVE_AQUI
   ```
   > **Dica:** não inclua aspas nem espaços extras.

5. **Iniciar a aplicação**
   ```powershell
   & .\.venv\Scripts\python -m streamlit run app.py
   ```
   O terminal exibirá algo como:
   ```
   You can now view your Streamlit app in your browser.
   Local URL: http://localhost:8501
   ```
   Abra o URL no navegador. Na primeira execução o Streamlit pode mostrar uma tela de boas‑vindas; basta deixá‑la em branco e apertar **Enter** para ir ao app principal.

6. **Usar a interface**
   - A barra lateral contém botões **MENU**, **EXPRESS**, **ME GUIE** e **REVISE**.
   - Use o uploader para enviar prints de perfil; o app enviará a imagem ao Gemini junto com o prompt do sistema.
   - As respostas aparecem no chat ao centro da página.

---

## 🛠️ Desenvolvimento adicional

- **Alterar o modelo**: se quiser usar outro modelo da Gemini, troque o nome em `app.py` (linha onde `genai.GenerativeModel("gemini-3.6-flash")` é instanciado).
- **Customizar o prompt**: o bloco `SYSTEM_INSTRUCTION` contém as diretrizes do agente; edite‑lo conforme necessário.
- **Executar testes** (se houver): adicione scripts de teste ao diretório `tests/` e execute `pytest` dentro da venv.

---

## 📄 Licença

Este projeto está sob a licença MIT – sinta‑se livre para adaptar e distribuir.

---

*Criado por Antigravity – assistente de codificação avançada.*
