
# Log Classification System

A hybrid log classification system that intelligently categorizes log messages using a combination of Regular Expressions (Regex), BERT-based embeddings with Logistic Regression, and Large Language Models (LLMs). This approach ensures accurate classification across simple, complex, and previously unseen log patterns.([GitHub][1])

## 🚀 Features

* **Regex-Based Classification**: Efficiently handles predictable and repetitive log patterns using predefined rules.
* **BERT + Logistic Regression**: Utilizes Sentence Transformers to generate embeddings for complex logs, followed by classification using Logistic Regression.
* **LLM Integration**: Employs Large Language Models to classify logs that don't match regex patterns and lack sufficient training data.
* **FastAPI Backend**: Provides a RESTful API for easy integration and deployment.
* **Modular Architecture**: Organized codebase facilitating maintenance and scalability.([GitHub][2], [GitHub][3], [GitHub][4])

## 🗂️ Project Structure

```bash
├── Resources/                 # Contains test datasets and sample outputs
├── Training/                  # Scripts and notebooks for training models
├── models/                    # Stores trained models (e.g., Logistic Regression)
├── classify.py                # Main script for classifying log messages
├── processor_bert.py          # Handles BERT-based embedding and classification
├── processor_llm.py           # Integrates LLM for classification
├── processor_regex.py         # Applies regex rules for classification
├── server.py                  # FastAPI server implementation
├── requirements.txt           # Lists project dependencies
├── arch.png                   # Architecture diagram of the system
└── readme.md                  # Project documentation
```



## ⚙️ Setup Instructions

### Prerequisites

* Python 3.7 or higher
* Git

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Avishri99/Log-Classification-system.git
   cd Log-Classification-system
   ```



2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```



## 🧪 Usage

### Running the FastAPI Server

```bash
uvicorn server:app --reload
```



* **API Documentation**: Access Swagger UI at `http://127.0.0.1:8000/docs`
* **ReDoc Documentation**: Access ReDoc at `http://127.0.0.1:8000/redoc`([GitHub][1])

### Classifying Logs

1. **Prepare Input File**

   Ensure your input CSV file (e.g., `test.csv`) is placed inside the `Resources/` directory. The file should contain a column named `log_message` with the log entries to be classified.

2. **Run Classification Script**

   ```bash
   python classify.py
   ```



The script will process the logs and output the results to a file named `output.csv` in the `Resources/` directory, adding a new column `target_label` with the predicted classifications.

## 🧠 Classification Workflow

The system follows a hierarchical approach to classify log messages:([GitHub][1])

1. **Regex Classification**: Attempts to match log messages against predefined regex patterns. If a match is found, assigns the corresponding label.
2. **BERT + Logistic Regression**: For logs not matched by regex, generates embeddings using BERT and predicts labels using a trained Logistic Regression model.
3. **LLM Classification**: If the above methods fail to classify the log, utilizes an LLM to infer the appropriate label.([GitHub][1])

This layered strategy ensures efficient and accurate classification across various log complexities.([GitHub][5])

## 📊 Example

Given an input log message:([GitHub][1])

```
User123 logged in from IP 192.168.1.1
```



The classification process would proceed as follows:

* **Regex**: Matches pattern `User\d+ logged in from IP .*` → Label: `User Login`
* **BERT + Logistic Regression**: Not invoked as regex matched.
* **LLM**: Not invoked as classification is complete.([GitHub][3])

## 📷 Architecture Diagram

![oaicite:87](arch.png)([GitHub][2])

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.([GitHub][6])

## 📬 Contact

For questions or suggestions, feel free to open an issue or contact [Avishri99](https://github.com/Avishri99).

---


[1]: https://github.com/Anshhb/Log-Classifier?utm_source=chatgpt.com "GitHub - Anshhb/Log-Classifier: Hybrid Log Classification using Regex ..."
[2]: https://github.com/codebasics/project-nlp-log-classification?utm_source=chatgpt.com "codebasics/project-nlp-log-classification - GitHub"
[3]: https://github.com/Sk0108/Log-Classification-System?utm_source=chatgpt.com "Sk0108/Log-Classification-System - GitHub"
[4]: https://github.com/priyanka-darshanam/Log-Classification?utm_source=chatgpt.com "A hybrid log classification system using Regex, Sentence ... - GitHub"
[5]: https://github.com/yashver025/Log-Classification-System/blob/main/Log_Classification_System.ipynb?utm_source=chatgpt.com "Log_Classification_System.ipynb - GitHub"
[6]: https://github.com/InchDs/Log-Classification-System-Using-Deepseek-R1-LLM-NLP-Regex-BERT/blob/main/README.md?utm_source=chatgpt.com "Log Classification System Using Deepseek R1 LLM, NLP, Regex, BERT - GitHub"
