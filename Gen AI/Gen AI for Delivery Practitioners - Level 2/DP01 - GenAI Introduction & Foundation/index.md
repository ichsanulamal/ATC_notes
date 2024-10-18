# DP01 - GenAI Introduction & Foundation

## Leadership Message

### Training Overview
- Continuous application of skills in projects and client discussions.

### Training Types
1. **Delivery Practitioner** (CL 12 to CL 7)
   - Primary focus for most participants.
2. **Automation Architect** (CL 9 to CL 4)
   - Rigorous course for selected individuals.
3. **Project Management Path** (CL 6 and above)
   - Pathway to delivery leads or technology service leads.

### Course Content
- **Self-Learning Modules**:
  - **Talent Management**: Basics of AI and ML.
  - **Gen AI**: Overview, applications using APIs, and ChatGPT.
  - **JA I Essentials**: LLM models, responsible AI, legal and security aspects.
  - **Prompt Engineering**: Essential for Gen AI use cases.
  - **Vector Data Stores**: Basics and emerging tools.

- **Recommended Short Courses** (not mandatory for today's class):
  - Transformers architecture and embeddings.
  - Advanced prompt engineering with a focus on pair programming.
  - GitHub Copilot for developers.
  - Fine-tuning LLMs.

### Expectations from Participants
1. **Understanding Accenture’s Differentiation**:
   - Recognize Accenture's competitive advantages and be able to discuss these with clients.
  
2. **Adapting to Evolving Work Practices**:
   - Embrace automation and adapt to new workflows.
   - Focus on improving productivity and reducing costs through automation.

3. **Familiarity with Evolving Tools**:
   - Learn about various LLM models, when to use them, and implications of legal and security issues.
   - Acquire skills in prompt engineering, vector data stores, and embeddings.

4. **Productivity Improvement**:
   - Participate in pilots to assess the applicability of Gen AI in daily work.
   - Engage in discussions about embedding Gen AI into new and existing client contracts.

5. **Proactive Automation Initiatives**:
   - Identify AI and Gen AI automation opportunities in your projects.
   - Take initiative in applying these learnings within your engagements.

### Conclusion
- Be proactive in exploring Gen AI opportunities.
- Continuous learning and application are essential for maintaining leadership in the industry.

## Introduction to Generative AI

### Definition
- **Generative AI**: Focuses on generating new and original content, such as text, images, code, and audio.

### Key Differences from Traditional AI
1. **Core Functionality**:
   - **Traditional AI**: Predictive and diagnostic, performing specific tasks (e.g., defect classification).
   - **Generative AI**: Creates new content based on input.

2. **Applicability**:
   - **Traditional AI**: Limited to specific use cases.
   - **Generative AI**: Applicable to a wide range of scenarios.

3. **Training Data**:
   - **Traditional AI**: Trained on use case-specific data.
   - **Generative AI**: Pre-trained on vast amounts of public data.

4. **Output Quality**:
   - **Traditional AI**: Dependent on the quality of input data (garbage in, garbage out).
   - **Generative AI**: Context-dependent output, which may include hallucinations (non-realistic responses).

5. **Focus**:
   - **Traditional AI**: Emphasizes training data quality.
   - **Generative AI**: Prioritizes contextual understanding.

### Foundation Models
- **Foundation Models**: Large language models (LLMs) that support various capabilities, including:
  - Question answering
  - Summarization
  - Code generation
  - Content creation
  - Automation tasks

### Use Cases
1. **Text Generation**:
   - Create marketing content, summarize emails, or generate documentation.
2. **Code Generation**:
   - Write and convert code, assist with documentation, and generate test cases.
3. **Image Generation**:
   - Create graphics, diagrams, and advertising materials.
4. **Audio/Video Generation**:
   - Develop voiceovers, music, and multimedia content.

### Key Players in Generative AI
- **Azure OpenAI**
- **Google (Bard, PaLM, Vertex AI)**
- **AWS (Bedrock)**
- **Oracle (Cohere)**
- **NVIDIA**

### Popular Models
- **Text Models**: GPT-4, DeepMind Gopher, Google PaLM.
- **Code Models**: Codex, Tabnine, GitHub Copilot.
- **Image Models**: DALL-E, Stable Diffusion, Midjourney.
- **Audio/Video Models**: Various models for speech and multimedia generation.

### Conclusion
Generative AI is an evolving field with numerous applications across various domains. Familiarity with the capabilities and models available will enhance your ability to leverage this technology in practical scenarios.

## Generative AI Patterns in Technology Delivery Life Cycle (TDLC)

### Key Patterns in Generative AI
1. **Generation**:
   - Creating content such as surveys, templates, requirements with acceptance criteria, and test cases.

2. **Completion**:
   - Completing user stories or code snippets by providing missing information.

3. **Synthesis**:
   - Collating information from multiple sources into a coherent format (e.g., summarizing log files during job failures).

4. **Analysis**:
   - Analyzing synthesized information to identify root causes of issues.

5. **Summarization**:
   - Creating concise summaries from meetings or long documents.

6. **Sentiment Analysis**:
   - Determining the sentiment (positive, negative, neutral) of text inputs without extensive training.

7. **Remediation**:
   - Fixing identified issues in code, often using tools like SonarQube for code review.

8. **Segmentation**:
   - Clustering incident descriptions or other data for better organization.

9. **Translation**:
   - Converting text between languages or translating code from one programming language to another.

10. **Question and Answer (Q&A)**:
    - Responding to inquiries with relevant information.

11. **Classification**:
    - Categorizing defects or issues based on complexity (simple, medium, complex).

### Generative AI Opportunities in TDLC
- **Requirements Phase**:
  - Create and summarize requirements, generate prototypes, and develop design documents and architectural diagrams.

- **Development Phase**:
  - Generate, analyze, and remediate code.

- **Testing Phase**:
  - Generate test cases and optimize regression test suites.

- **Deployment Phase**:
  - Automate infrastructure provisioning and generate deployment scripts.

- **Support Phase**:
  - Automatically synthesize and analyze root causes, enrich ticket data, and generate documentation.

- **Collaboration**:
  - Enhance document search and knowledge management processes.

### Conclusion
Generative AI offers diverse applications across the technology delivery life cycle, improving efficiency and effectiveness in various processes. Understanding these patterns can help leverage AI capabilities in real-world scenarios.

## Simple Generative AI Application: GitHub Copilot

### Overview
GitHub Copilot is an AI-powered coding assistant that integrates with various Integrated Development Environments (IDEs), such as Eclipse for Java and Jupyter for Python.

### Key Features
1. **Code Generation**:
   - As a developer begins typing a function (e.g., "convert hexadecimal to color code"), Copilot automatically suggests relevant code snippets.

2. **Pair Programming**:
   - Functions as a virtual coding partner, allowing for rapid code creation and enhanced collaboration.

3. **Code Remediation**:
   - Assists in identifying and fixing issues within the code.

4. **Test Case Generation**:
   - Facilitates the creation of test cases, improving overall code quality.

### Conclusion
GitHub Copilot exemplifies a practical application of generative AI in software development, streamlining coding processes and enhancing productivity.

## Foundation Models: Augmentation and Orchestration

### Overview
Foundation models, such as GPT-3.5 and GPT-4, serve as the backbone for various generative AI applications. To effectively utilize these models, it's crucial to understand how to augment and orchestrate them for specific use cases.

### Conceptual Architecture
1. **Foundation Models**:
   - Base models like GPT-3.5 and GPT-4.

2. **Patterns and Applications**:
   - Define user needs (e.g., summarization, user story generation).
   - Use prompts to instruct the foundation model.

3. **User Interaction**:
   - Applications (e.g., chatbots, ITSM tools) interact with users.
   - Prompts are generated based on user input and application context.

### Role of Context
- For accurate responses, especially in specific domains (like banking or healthcare), context is crucial.
- Contextual information is stored in a **vector database**, which allows for effective retrieval.

### Vector Database and Embedding
1. **Embedding**:
   - Converts diverse data types (text, audio, video) into a machine-understandable numerical format.
   - Essential for searching and retrieving relevant context from the vector database.

2. **Vector Database**:
   - Stores data in a high-dimensional space, enabling semantic search and cosine similarity analysis.
   - Unlike traditional databases, it focuses on the relationships between data points.

### Retrieval-Augmented Generation (RAG)
- **RAG Process**:
   1. User queries are vectorized and searched in the vector database.
   2. Relevant context is extracted based on cosine similarity.
   3. The context is embedded in prompts sent to the foundation model.
   4. Responses are generated and formatted for the application.

### Use Case Scenarios
- **Generic Queries**:
   - For common knowledge (e.g., "What is the capital of France?"), a direct call to the foundation model suffices.
- **Domain-Specific Queries**:
   - For specific questions (e.g., "Why did a payment fail?"), context from the vector database is crucial to provide accurate responses.

### Summary
- Augmenting foundation models with context from vector databases enables precise and relevant responses.
- The integration of embedding processes enhances the application of generative AI across diverse domains, ensuring accuracy and relevancy in outputs.

## Generative AI Design: Key Components

### Overview
In the context of application development and system integration, particularly within a banking application, several key design components facilitate the creation and processing of user stories for modules like payment processing.

### Key Components

1. **User Story Creation**:
   - Example: "Create a new payment processing option for Country XYZ."
   - The user story serves as the foundational request that drives subsequent processes.

2. **Preprocessing**:
   - **Tokenization**: The user story is broken down into manageable parts.
   - **Feature Extraction**: Relevant features are identified for further analysis.
   - **Embedding**: The tokenized story is converted into a numerical format for storage in a vector database.

3. **Knowledge Graph Integration**:
   - **Functional and Nonfunctional Considerations**: The system examines both types of requirements, including security, scalability, and performance.
   - This helps to ensure that all relevant aspects are considered when developing the user story.

4. **Prompt Generation**:
   - After gathering context from the knowledge graph and vector database, a prompt is crafted for the large language model (LLM).

5. **LLM Orchestrator**:
   - **LChain Framework**: This orchestrator determines which LLM to use based on the nature of the input.
     - Example: For generating user stories, it might select GPT-3.5; for architectural designs, it might switch to GPT-4 or another model.
   - It ensures the appropriate model is used for optimal response generation.

6. **Response Formatting**:
   - Once a response is generated from the selected LLM, it is formatted to meet the requirements of the user interface.

7. **Integration with My Wizard Assets**:
   - The design leverages existing assets, such as:
     - Requirements readiness checkers.
     - Dependency identifiers.
   - This helps to align user stories with best practices, ensuring they adhere to the **INVEST** principles:
     - **Independent**: Stories should stand alone.
     - **Negotiable**: They can be discussed and changed.
     - **Valuable**: They must deliver value to the customer.
     - **Estimable**: They should be quantifiable in terms of effort.
     - **Small**: They need to be manageable in size.
     - **Testable**: Criteria for success must be defined.

### Summary
This generative AI design framework enhances the process of creating and refining user stories in application development. By integrating various components—from preprocessing to LLM orchestration and knowledge graph utilization—it ensures a comprehensive approach to addressing both functional and nonfunctional requirements while adhering to agile best practices.

## Introduction to Prompt Engineering

### Overview
Prompt engineering is a crucial technique in working with large language models (LLMs). It involves crafting specific instructions or queries to guide the model in generating accurate and relevant responses.

### What is a Prompt?
- A **prompt** is a set of instructions given to an LLM to elicit a desired response. 
- The quality and clarity of the prompt directly influence the model's output.

### Importance of Prompt Engineering
1. **Enhances Accuracy and Relevance**: 
   - Well-designed prompts lead to more precise and contextually appropriate responses.
   
2. **Tailors Responses**: 
   - Effective prompts align AI-generated content with user expectations and ethical standards.

3. **Optimizes Interaction**:
   - Crafting clear prompts ensures a user-friendly experience, making interactions with AI systems more reliable.

4. **Reduces Trial and Error**:
   - Thoughtful prompt engineering minimizes the back-and-forth often necessary to achieve the desired output, saving time and resources.

### Applications of Prompt Engineering
- **Content Generation**: Used throughout the technology delivery life cycle for generating various types of content.
- **Insights and Recommendations**: Facilitates the extraction of meaningful insights based on specific metrics.

### Mitigating Hallucinations
- Properly contextualized and finely tuned prompts help prevent LLMs from producing inaccurate or "hallucinated" information, ensuring outputs remain grounded in reality.

### Conclusion
Effective prompt engineering is essential for optimizing AI interactions. By carefully crafting prompts, users can harness the full potential of large language models, achieving desired results efficiently and ethically.

## Basic Constructs of Prompts

### Overview
The formulation of prompts consists of three fundamental components: content, instructions, and examples. Each plays a critical role in guiding large language models (LLMs) to produce accurate and relevant outputs.

### 1. Content
- **Definition**: The information provided to the LLM for task execution.
- **Types of Content**:
  - Text passages from documents.
  - Structured data like CSV files.
  
### 2. Instructions
- **Purpose**: Convey the specific tasks the LLM needs to accomplish.
- **Examples of Instructions**:
  - "Answer the question: What are the major steps to reprocess an invoice?"
  - "Generate a project management plan for an upcoming release."
  - "Summarize the call conversation between a user and a service desk agent."
  - "Analyze and process the sales data provided in a CSV file."

### 3. Examples
- **Importance**: Providing examples helps to ensure the output is formatted and tailored to specific requirements.
- **Types of Examples**:
  - "Provide a concise summary in bullet points."
  - "Focus on legal compliance aspects in the policy document."
  - "Extract SLA compliance data for incidents over the last six months from the provided CSV file, and format the output in a concise bulleted list or table."

### Summary
In crafting effective prompts:
- **Content** provides the task information.
- **Instructions** utilize generative AI patterns for task execution.
- **Examples** enhance understanding and specify output formats, ensuring that the responses align with specific requirements.

By effectively combining these three constructs, users can significantly improve the quality of outputs generated by LLMs. Thank you!

## In-Context Learning Techniques

In this segment, we explore three key in-context learning techniques that enhance the performance of large language models (LLMs): zero-shot learning, one-shot learning, and few-shot learning. Each technique plays a distinct role in how LLMs interpret and respond to prompts.

### 1. Zero-Shot Learning
- **Definition**: This technique allows the LLM to generate responses based solely on the instructions provided, without any examples.
- **Example**: Asking the model, "What is the capital of India?" The model can provide the correct answer (New Delhi) based on its pre-training, without needing any context or examples.

### 2. One-Shot Learning
- **Definition**: In this approach, the user provides one example alongside the prompt. The model uses this example to generate a relevant response.
- **Example**: If you instruct the model to "Generate a ticket data template with fields like ticket description, assigned to, and priority," including a single example helps the model understand the expected output structure.

### 3. Few-Shot Learning
- **Definition**: This method involves providing a few examples to guide the model in predicting outcomes for similar tasks.
- **Example**: When classifying defects, you might present a few examples (e.g., "Defect A: configuration defect," "Defect B: design defect"). The model uses these to generalize and classify additional defects correctly.

### Best Practices for Prompt Writing
To maximize the effectiveness of prompts, consider the following best practices:

1. **Provide Context**: Offer as much relevant information as possible to avoid hallucination and ensure the model understands the specifics of the request. For instance, a prompt about losing access keys should clearly specify the context.

2. **Explicit Instructions**: Encourage the model to think critically by asking it to weigh pros and cons or consider the implications of its recommendations. For example, when troubleshooting an application issue, prompt the model to evaluate the impact of actions like restarting a server.

3. **Use Examples**: Clearly outline how the output should be structured. Specify formats (e.g., lists, tables) and the aspects to focus on.

4. **Set Constraints**: Limit the response by specifying word counts or focus areas. For instance, ask the model to summarize a document in 250 words while emphasizing legal or security aspects.

5. **Explore Different Formats**: Experiment with the phrasing of prompts—ask questions, make statements, or adopt different perspectives to see how it affects the output.

6. **Iterate and Refine**: After receiving responses, assess their quality. If they fall short, refine the prompts continuously to improve accuracy and relevance.

By understanding these techniques and best practices, users can significantly enhance the interaction with LLMs, leading to more accurate and contextually appropriate outputs.

## Vector Search and Its Role in Generative AI

### Overview of Vector Embeddings
Vector embeddings are essential in bridging human-readable data and computational algorithms, enabling generative AI to process natural language queries effectively. When a user poses a question, such as "What are the potential root causes for the failure of job XYZ?", the generative AI must understand the query, apply computational algorithms, and provide a relevant response.

### What Are Vector Embeddings?
- **Definition**: Vector embeddings transform various data types, such as text and images, into numerical representations that AI can understand.
- **Functionality**: These embeddings capture similarities and relationships between different data points, allowing the AI to understand context and generate meaningful outputs efficiently.

### Key Concepts
1. **Vectors**: Fixed-length arrays of numbers representing points in space. Each dimension corresponds to a unique aspect of the data.
2. **Vector Embeddings**: Numerical representations of typically non-numerical data, capturing essential properties and relationships in a condensed format.
3. **Vector Store**: A specialized database designed to manage and store vectors for efficient retrieval.

### Knowledge Graphs
Knowledge graphs represent entities, attributes, and relationships, providing context and meaning to data. They enhance generative AI solutions by grounding responses in validated facts and linking diverse data sources together.

### Semantic Search
Semantic search goes beyond traditional keyword search by understanding the intent and context behind user queries. For example, the word "job" can have different meanings based on context, and semantic search ensures that responses are accurate and contextually relevant.

### Key Processes in Semantic Search
1. **Vector Search**: Encodes information into vectors to determine similarity.
2. **Query Transformation**: User queries are transformed into numerical representations (embeddings).
3. **Matching Process**: Algorithms (e.g., K-nearest neighbor) match query vectors to existing document vectors based on conceptual relevance.

### Retrieval-Augmented Generation (RAG)
RAG enhances large language models (LLMs) by integrating an information retrieval system. It allows LLMs to access external, relevant information during query response generation, ensuring accuracy and context relevance, especially for specific client queries.

### Use Case: Supermart X Incident Management
In a retail scenario, Accenture supports application maintenance through level two incident management. By automating root cause analysis using generative AI, historical incident data can help identify potential causes for new incidents.

### Process Breakdown
1. **Initial Vector Store Setup**: Extract incident details from a system (e.g., ServiceNow), preprocess text, tokenize descriptions, and encode features into dense vectors.
2. **Knowledge Graph Creation**: Identify entities (incidents, root causes) and define their relationships (e.g., "Incident 001 has a root cause of misconfiguration").
3. **New Incident Processing**: When a new incident arises, it undergoes preprocessing and encoding. A semantic search retrieves similar historical incidents using cosine similarity to determine potential root causes.
4. **Response Generation**: The AI synthesizes a response based on augmented prompts and retrieved information, which is then updated in the incident record.

### Conclusion
By integrating vector embeddings, knowledge graphs, semantic search, and retrieval-augmented generation, generative AI solutions can provide contextually accurate and efficient responses, unlocking significant business value in incident management and other applications.

## raw

Version 1.0


This course gives an Overview of Gen AI, Gen AI across TDLC and Overview of Prompt Engineering.



Last Updated 6 months ago

Managed by GenAI TDLC Team

Banner
1. Introduction and Leadership Message
This module is about course introduction and leadership message.

Lesson 1

Introduction and Leadership Message
9:00
2. Generative AI for TDLC Introduction and Recap
This module gives an introduction to Gen AI, Gen AI Patterns, Simple Gen AI application for Code generation and completion, Foundation Models and Gen AI design key components.

Lesson 1

Generative AI Introduction
13:00
Lesson 2

Generative AI across Technology Delivery Life Cycle
8:00
Lesson 3

Simple Gen AI Application
2:00
Lesson 4

Foundation Models
20:00
Lesson 5

Gen AI Key Design Components
5:00
Quiz 1

Quiz
10:00
3. Prompt Engineering Overview
This module gives an overview of prompt engineering, prompt engineering constructs and 3-in context learning techniques for better prompt.

Lesson 1

Prompt Engineering Introduction
3:00
Lesson 2

Prompt Engineering Constructs
3:00
Lesson 3

3 In-context Learning Techniques
8:00
Lab 1

Lab: Prompt Engineering - How to use it effectively in TDLC
20:00
Lesson 4

Vector Search
23:00
Quiz 1

Quiz
8:00
4. Assessment
Quiz 1

Quiz
20:00

Introduction and Leadership Message

Generative AI for TDLC Introduction and Recap

Prompt Engineering Overview

Assessment
What's Next
Congratulations on completing the DP01 - GenAI Introduction & Foundation course! As you continue your learning journey, as part of the GenAI in TDLC for Delivery Practitioner training, you can take up the next course: