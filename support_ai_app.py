import streamlit as st
import ollama

def analyze_customer_email(email: str) -> str:
    extract_prompt = f"""
    Analyze the following customer email.
    1. Classify the intent (refund request, delivery status, product inquiry, complaint, etc.)
    2. Extract key details such as order number, product, sentiment, urgency.
    3. Return the result as JSON with keys: intent, order_number, product, sentiment, urgency, summary.

    Customer Email:
    {email}
    """
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": extract_prompt}]
    )
    return response['message']['content']


def draft_reply(email: str, analysis: str) -> str:
    business_context = """
    You are a professional customer support representative at a consumer electronics company.
    Always:
    - Be polite, empathetic, and concise.
    - Acknowledge the customer situation.
    - Include relevant details (order info, delivery timing, etc.) when available.
    - End positively, reassuring the customer that we value them.
    """

    reply_prompt = f"""
    {business_context}

    The customer sent the following email:
    {email}

    Analysis of their message:
    {analysis}

    Draft a polite, appropriate email response:
    """

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": reply_prompt}]
    )
    return response['message']['content']


# ------------------ UI -------------------------
st.set_page_config(page_title="AI Customer Support Assistant", page_icon="📩")

st.title("📩 AI-Powered Customer Support Assistant")
st.write("Paste a customer email and let AI analyze and draft a polite, professional reply.")

# Input from user
customer_email = st.text_area("Customer Email:", height=200, placeholder="Paste the customer email here...")

if st.button("Generate Reply"):
    if customer_email.strip():
        with st.spinner("🔍 Analyzing email..."):
            analysis = analyze_customer_email(customer_email)
        st.subheader("Extracted Understanding")
        st.json(analysis)

        with st.spinner("✍️ Drafting reply..."):
            reply = draft_reply(customer_email, analysis)

        st.subheader("AI Drafted Reply")
        st.write(reply)
    else:
        st.warning("Please paste a customer email first.")
