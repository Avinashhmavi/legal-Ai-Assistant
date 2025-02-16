## 🚀🧑‍⚖️ Legal AI Assistant

Welcome to the **Legal AI Assistant** – your AI-powered legal team in a single application! This Streamlit-based web app is designed to revolutionize legal document analysis by leveraging multiple specialized AI agents. Whether you're a legal professional, a law firm, or an individual seeking quick legal insights, this tool is here to help.

---
## 🌐 Live Demo

Try out the **Legal AI Assistant** live! Click the link below to access the app:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://legal-ai-assistant.streamlit.app/)

[Try the Legal AI Assistant Live](https://legal-ai-assistant.streamlit.app/)


## 🌟 Features

## 🤖 AI Agent Team

Our application features a team of specialized AI agents, each with a unique role:

1. **🔍 Legal Researcher**:
   - Finds and cites relevant legal cases, precedents, and statutes.
   - Provides detailed research summaries with authoritative references and specific document sections.

2. **📑 Contract Analyst**:
   - Specializes in thorough contract review.
   - Identifies key terms, obligations, and potential issues.
   - References specific clauses for detailed analysis.

3. **🎯 Legal Strategist**:
   - Develops comprehensive legal strategies.
   - Provides actionable recommendations while considering risks and opportunities.

4. **👨‍💼 Team Lead**:
   - Coordinates analysis between team members.
   - Ensures comprehensive responses, properly sourced recommendations, and references to specific document parts.
   - Acts as the coordinator for all three agents.

## 📊 Analysis Types

The application offers five distinct types of analysis, each tailored to specific legal needs:

| **Analysis Type**   | **Active Agents**                          | **Focus**                                                                 | **Deliverables**                                                                 |
|----------------------|--------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Contract Review**  | Contract Analyst                          | Detailed analysis of terms, conditions, obligations, and potential issues. | Term breakdown, risk identification, and obligation summary.                     |
| **Legal Research**   | Legal Researcher                          | Finding relevant cases, precedents, and legal context.                    | Comprehensive research summary with citations and references.                    |
| **Risk Assessment**  | Legal Strategist, Contract Analyst        | Identifying potential legal risks and liability exposure.                 | Risk analysis report with mitigation strategies.                                 |
| **Compliance Check** | Legal Strategist, Legal Researcher, Contract Analyst | Comprehensive regulatory compliance analysis.                | Compliance status report with specific recommendations.                          |
| **Custom Queries**   | Full Legal Team (All Agents)              | Tailored analysis based on specific user questions.                       | Customized reports addressing the user's unique needs.                           |

---

## 🛠️ Pre-Installation Requirements

Before running the application, ensure you have the following installed:

1. **Python 3.8 or higher**:
   - Download and install Python from [python.org](https://www.python.org/).

2. **Required Python Libraries**:
   - Install the necessary libraries using the following command:
     ```bash
     pip install streamlit groq pypdf
     ```

3. **Groq API Key**:
   - Sign up for a Groq API key from [Groq's website](https://groq.com/).
   - Replace the placeholder `GROQ_API_KEY` in the code with your actual API key.

---

## 🚀 How It Works

1. **Document Upload**:
   - Users upload a PDF document containing legal content.
   - The application extracts the text from the document (limited to the first 4000 characters for demonstration purposes).

2. **Analysis Type Selection**:
   - Users select the type of analysis they need from the available options:
     - Contract Review
     - Legal Research
     - Risk Assessment
     - Compliance Check
     - Custom Queries

3. **Question Input**:
   - Users ask specific legal questions related to the uploaded document.

4. **Agent Coordination**:
   - Based on the selected analysis type, the application activates the relevant AI agents.
   - Each agent generates a response based on its specialized role.

5. **Response Display**:
   - The application displays the combined responses from all active agents in a structured format.

---

## 🖥️ Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/Avinashhmavi/legal-Ai-Assistant.git
   cd legal-ai-assistant
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run legal_ai_assistant.py
   ```

3. Access the application:
   - Open your web browser and navigate to `http://localhost:8501`.

4. Use the application:
   - Upload a PDF document.
   - Select the desired analysis type.
   - Ask legal questions and view the AI-generated responses.

---

## 📋 Example Usage

### Contract Review
- **User Question**: "What are the key terms in this contract?"
- **AI Response**:
  ```
  **Contract Analyst:**
  The key terms in this contract include [term 1], [term 2], and [term 3]. These terms are defined in sections [section 1], [section 2], and [section 3] of the document.
  ```

### Risk Assessment
- **User Question**: "What are the potential risks in this agreement?"
- **AI Response**:
  ```
  **Legal Strategist:**
  The potential risks include [risk 1], [risk 2], and [risk 3]. I recommend [strategy 1] and [strategy 2] to mitigate these risks.

  **Contract Analyst:**
  The risks are primarily associated with clauses [clause 1] and [clause 2]. These clauses could lead to [potential issue 1] and [potential issue 2].
  ```

### Custom Queries
- **User Question**: "What is the best course of action for this case?"
- **AI Response**:
  ```
  **Legal Researcher:**
  Based on my research, the relevant precedents are [precedent 1] and [precedent 2]. These cases suggest [recommendation 1].

  **Legal Strategist:**
  The best course of action would be to [strategy 1] and [strategy 2]. This approach minimizes risks and maximizes opportunities.

  **Contract Analyst:**
  I recommend reviewing clauses [clause 1] and [clause 2] to ensure they align with the proposed strategy.

  **Team Lead:**
  Based on the analysis from all team members, the recommended course of action is [final recommendation]. This approach is supported by [evidence 1] and [evidence 2].
  ```

---

## 🚀 Future Enhancements

1. **Support for Larger Documents**:
   - Extend text extraction beyond 4000 characters for more comprehensive analysis.

2. **Integration with Legal Databases**:
   - Enhance the Legal Researcher's capabilities by integrating with legal databases for real-time case law and statute references.

3. **Multi-Document Analysis**:
   - Allow users to upload multiple documents for cross-referencing and comparative analysis.

4. **User Authentication**:
   - Add user authentication to save analysis history and preferences.

5. **Export Reports**:
   - Enable users to export analysis reports in PDF or Word format.

---


## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## 📧 Contact

For questions or feedback, please contact:
- **Avinash HM **
- **Email**: avi.hm24@gmail.com
---

Enjoy using the **Legal AI Assistant**! ⚖️✨
