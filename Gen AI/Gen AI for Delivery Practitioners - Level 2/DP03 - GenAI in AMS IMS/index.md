# DP03 - GenAI in AMS/IMS

### Hands-On Session: Key Learning Points

#### Objectives
1. **Establish a Living Knowledge Base**
2. **Leverage the Knowledge Base for Hyper Automation** (focused on ticket resolution)

#### Components of a Living Knowledge Base
1. **Standard Operating Procedures (SOPs)**: Existing knowledge base articles and diagnostic information.
2. **Implicit Knowledge**: Knowledge held by Subject Matter Experts (SMEs).
3. **Reverse Engineering**: Generating documentation from code, even if no documentation exists.

#### Hyper Automation Use Case
- **Ticket Resolution**: Implementing automation to resolve support tickets.

#### Demo Overview
1. **GEN A Landing Page**: Access various projects.
   - For demo: Click on "Banking Form" project.
   - View available use cases on the left panel.

2. **Building the Knowledge Base**:
   - **Input Data Sources**:
     - SOPs and knowledge articles.
     - Tools like Selinus for process diagnostics.
   - **Implicit Knowledge Capture**:
     - Record and transcribe transition sessions to capture SME insights.
     - Use deep learning models to synthesize information into a System Understanding Document.

3. **Reverse Engineering Process**:
   - Upload application source code from GitHub.
   - **Output**:
     - **Code Explanation**: Overview of the functionality.
     - **User Stories**: Derived from business rules in the code.
     - **Test Cases**: Generated for regression testing, including Selenium scripts.
     - **Documentation**: Create a wiki summarizing the application’s architecture and features.

4. **Using the Knowledge**:
   - Implement a digital assistant for Q&A:
     - Supports developers and support engineers with immediate responses from the knowledge base.

#### Key Differentiators
- **Built-in Prompt Library**: Unlike traditional models, GEN A has pre-configured prompts for efficient documentation and knowledge extraction.
- **Data Security**:
  - Code remains proprietary; processed securely in an enterprise environment.
  - Use of Azure OpenAI ensures no data storage by the provider.

#### Technologies Supported
- **Languages**: Java, .NET, Python, Angular, and more.
- **Continuous Improvement**: Regular updates to maintain accuracy in documentation and knowledge.

---

Sure! Here’s a more structured and concise version of the content focused on core learning points:

---

### Key Concepts of Ticket Automation and Resolution

1. **Editing and Retention**:
   - Any edits made to documents or tickets are retained in the system.
   - Accuracy scores indicate the reliability of generated content.

2. **Automating Ticket Resolution**:
   - AI has been used for automatic ticket resolution for several years.
   - Traditional process:
     - User calls service desk → Engineer summarizes call → Ticket created → L2/L3 resolves without user interaction.
   - Issues:
     - Information loss during manual summarization.
  
3. **AI-Driven Ticket Creation**:
   - AI captures and transcribes the user conversation.
   - Generates a standard ticket template automatically, minimizing information loss.

4. **Resolution Steps**:
   - Upon logging a ticket, resolution steps from the knowledge base are suggested.
   - Workflow tab shows the sequence of automated steps taken to resolve the ticket.

5. **Intelligent Workflows**:
   - Workflows include decision points that adapt based on previous results.
   - Some steps may require human approval, which can be tracked via chat or email.

6. **Root Cause Analysis**:
   - AI performs root cause analysis and suggests resolutions based on captured data.
   - Provides a draft resolution script for expert review before execution.

7. **Explainability**:
   - The system can explain why a particular workflow was chosen based on ticket descriptions.
   - Users can trace back the decision-making process without waiting for numerous similar tickets.

8. **Integration and Prerequisites**:
   - Prerequisites include access to necessary servers, databases, and logs based on the use case.
   - Existing automation scripts can be integrated into the knowledge base for reuse.

9. **Monitoring System Integration**:
   - AI can also respond to issues detected by monitoring tools.
   - Provides a visual topology of the system to understand the origin and impact of failures.

10. **End-to-End Flow**:
    - From user-reported issues to system-generated alerts, both types of tickets follow similar resolution processes.



## raw
DP03 - GenAI in AMS/IMS
Version 1.0


This course helps us to understand the importance of Gen AI in the AMS/IMS Lifecycle.



Prerequisites: DP01, DP02

Last Updated 6 months ago

Managed by GenAI TDLC Team

Banner
1. Gen AI for AMS/IMS and its use cases
This module gives an overview of Gen AI in AMS/IMS, Gen AI Capabilities across the AIOps Lifecycle.

Lesson 1

AMS Use Case Demo on GenWizard
36:00
Lab 1

Lab: Do it Yourself Exercise - AMS/IMS Use Cases
01:00:00
2. Assessment
Quiz 1

Quiz
12:00

Gen AI for AMS/IMS and its use cases

Assessment
What's Next
Congratulations on completing the DP03 - GenAI in AMS/IMS course! As you continue your learning journey, as part of the GenAI in TDLC for Delivery Practitioner training, you can now choose to take up one of the following courses: