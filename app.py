import streamlit as st
import google.generativeai as genai
# Removed unused import; GenerationConfig accessed via genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Nexa Agent | Nexa Digital",
    page_icon="🦅",
    layout="wide"
)

# 1. Configuração do Prompt do Sistema Oficial da Nexa
SYSTEM_INSTRUCTION = """
Você é o Nexa Agent, copiloto operacional e consultor especialista em presença local da Nexa Digital.
Seu papel é auxiliar a equipe da Nexa em diagnósticos, prospecção, scripts de vendas, briefing, otimização de Perfil da Empresa no Google, criação de conteúdo mensal, relatórios e controle de qualidade.

DIRETRIZES ESSENCIAIS:
- SEGURANÇA: NUNCA peça nem instrua a pedir senhas do cliente. Acesso sempre via convite de administrador/gerente.
- POLÍTICA: NUNCA prometa \"1º lugar no Google\" ou remoção de críticas válidas. Vendemos presença profissional, clareza e credibilidade.
- MÉTRICAS: NUNCA invente métricas. Se faltar dado, marque \"NÃO INFORMADO\".
- PACOTES OFICIAIS:
  * Essencial: R$ 297 (único) - Presença básica no Google, descrição, serviços, link/QR Code de avaliações.
  * Profissional: R$ 497 (único) - Tudo do Essencial + WhatsApp Business (mensagens, catálogo inicial) e 4 artes.
  * Plano Crescimento: R$ 397/mês (recorrente) - Manutenção, 4 artes/mês, acompanhamento de avaliações e suporte.
  * Express: Arte Instagram (a partir de R$ 25), Cartão Digital (R$ 50), Convite (R$ 30), QR Code (R$ 20).

COMANDOS SUPORTADOS:
- MENU, ANALISAR PRINT, DIAGNÓSTICO EXPRESS, FAÇA POR MIM, ME GUIE, REVISE.
"""

# 2. Inicialização do Cliente Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.sidebar.warning("⚠️ Chave de API não configurada.")
    api_key = st.sidebar.text_input("Cole sua GEMINI_API_KEY aqui:", type="password")

if not api_key:
    st.info("Insira a chave da API do Gemini para começar.")
    st.stop()

# Configura a API do Gemini
genai.configure(api_key=api_key)

# Modelo Gemini a ser usado
model = genai.GenerativeModel("gemini-3.6-flash")

# 3. Interface Visual do App
st.title("🦅 Nexa Agent — Base Operacional")
st.caption("Copiloto interno para prospecção, análise de perfil no Google e suporte operacional.")

# Barra Lateral: Atalhos rápidos e Upload de Prints
with st.sidebar:
    st.subheader("🛠️ Comandos Rápidos")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 MENU"):
            st.session_state.custom_prompt = "MENU"
        if st.button("⚡ EXPRESS"):
            st.session_state.custom_prompt = "DIAGNÓSTICO EXPRESS"
    with col2:
        if st.button("🧭 ME GUIE"):
            st.session_state.custom_prompt = "ME GUIE"
        if st.button("🔍 REVISE"):
            st.session_state.custom_prompt = "REVISE"

    st.markdown("---")
    st.subheader("📸 Análise Visual de Print")
    uploaded_file = st.file_uploader("Envie print do perfil do cliente", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img_preview = Image.open(uploaded_file)
        st.image(img_preview, caption="Print carregado", use_column_width=True)

# 4. Histórico da Sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Processamento de Entrada
user_input = st.chat_input("Digite um comando, cole um briefing ou faça uma pergunta...")

# Se clicou em um botão de comando rápido
if "custom_prompt" in st.session_state and st.session_state.custom_prompt:
    user_input = st.session_state.custom_prompt
    st.session_state.custom_prompt = None

if user_input:
    # Exibe pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Monta os conteúdos para o Gemini
    contents = []
    if uploaded_file:
        contents.append(Image.open(uploaded_file))

    # Adiciona contexto recente da conversa
    for past_msg in st.session_state.messages[-4:]:
        contents.append(f"{past_msg['role'].upper()}: {past_msg['content']}")

    # Insere a instrução do sistema como primeiro conteúdo
    contents.insert(0, SYSTEM_INSTRUCTION)

    contents.append(f"USUÁRIO: {user_input}")

    # Gera resposta via Gemini 2.0 Flash
    with st.chat_message("assistant"):
        with st.spinner("Nexa Agent analisando..."):
            try:
                response = model.generate_content(
                    contents=contents,
                    generation_config=genai.GenerationConfig(
                        temperature=0.3
                    )
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erro ao processar: {e}")
