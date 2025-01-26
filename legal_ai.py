import streamlit as st
from groq import Groq
from pypdf import PdfReader
import io

# Set Groq API key
GROQ_API_KEY = "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"

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def extract_text_from_pdf(uploaded_file):
    """Extract text content from PDF file using pypdf"""
    reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text[:4000]  # Return first 4000 characters for demo

def generate_response(prompt, context, agent_role):
    """Generate response using Groq's API with role-specific prompting"""
    system_prompt = f"""
    You are a legal {agent_role} AI assistant. Analyze the provided legal document and:
    {{
        "Legal Researcher": "Find relevant precedents, cite legal statutes, and provide authoritative references. Provide detailed research summaries with sources and references specific sections from uploaded documents.",
        "Contract Analyst": "Identify key clauses, highlight risks, and suggest contractual improvements. Specializes in thorough contract review, identifying key terms, obligations, and potential issues. References specific clauses from documents for detailed analysis.",
        "Legal Strategist": "Develop litigation strategies, assess outcomes, and recommend action plans. Focuses on developing comprehensive legal strategies, providing actionable recommendations while considering both risks and opportunities.",
        "Team Lead": "Coordinates analysis between team members, ensures comprehensive responses, properly sourced recommendations, and references to specific document parts. Acts as an Agent Team coordinator for all three agents."
    }}[agent_role]
    """
    
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Document context: {context}\n\nQuestion: {prompt}"}
        ],
        temperature=0.3,
        max_tokens=1024
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("⚖️ Legal AI Assistant")
st.markdown("Upload legal documents and consult with AI specialists")

# Sidebar for document upload
with st.sidebar:
    st.header("Document Setup")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    context = ""
    
    if uploaded_file:
        with st.spinner("Processing document..."):
            context = extract_text_from_pdf(uploaded_file)
            st.success("Document ready for analysis!")

# Main chat interface
analysis_type = st.radio(
    "Select Analysis Type:",
    ["Contract Review", "Legal Research", "Risk Assessment", "Compliance Check", "Custom Queries"],
    horizontal=True
)

# Map analysis types to active agents
analysis_agents = {
    "Contract Review": ["Contract Analyst"],
    "Legal Research": ["Legal Researcher"],
    "Risk Assessment": ["Legal Strategist", "Contract Analyst"],
    "Compliance Check": ["Legal Strategist", "Legal Researcher", "Contract Analyst"],
    "Custom Queries": ["Legal Researcher", "Legal Strategist", "Contract Analyst", "Team Lead"]
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your legal question..."):
    if not context:
        st.warning("Please upload a document first!")
        st.stop()
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner(f"Consulting {analysis_type}..."):
            try:
                # Get active agents for the selected analysis type
                active_agents = analysis_agents[analysis_type]
                response = ""
                
                # Generate responses from each active agent
                for agent in active_agents:
                    agent_response = generate_response(prompt, context, agent)
                    response += f"**{agent}:**\n{agent_response}\n\n"
                
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")