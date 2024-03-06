# LLM Chatbot

This repository contains a chatbot application using an open-source LLM (Large Language Model), specifically the [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b-chat) model hosted on Hugging Face.

## Setup Instructions

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository

First, clone this repository to your local machine.

```bash
git clone (https://github.com/thepalashthakur/opensource-llm-article-generator.git)
```


### 2. Download the Model

After cloning the repository, download the Llama 2 70B model from the link provided above. Place the downloaded model files into the `models` directory within the cloned repository.

### 3. Install Dependencies

Navigate to the root directory of the cloned repository and run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

Note: Make sure you have Python and pip installed on your system. If you're using a virtual environment (which is recommended), activate it before running the above command.

### 4. Run the Application

To start the application on your local host, execute the following command:

```bash
streamlit run app.py
```

This will start a Streamlit server, and the application should be accessible via a web browser at the URL provided by Streamlit (usually `http://localhost:8501`).

## Additional Information

For more details on how to interact with the chatbot and customize its behavior, refer to the documentation within the application or the additional README files in the repository.

---

Thank you for trying out the LLM Chatbot. We hope you find it useful for your projects!
