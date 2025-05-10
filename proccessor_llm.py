from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq = Groq()
def classify_with_llm(log_message):
    # Define the prompt for classification
    prompt = f"""Classify the following log message into one of these categories: 'Workflow Error','Deprecation Warning' and if can't figure out category give 'Unknown'
    only return the category name. dont preamble
    .\n\nLog message: {log_message}"""
    
   

    chat_completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    log_message_1 = "Lead conversion failed for prospect ID 7842 due to missing contact information."
    log_message_2 = "API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."
    log_message_3 = "System encountered an unexpected state during operation 'UpdateRecords'."

    print(classify_with_llm(log_message_1))  # Example output: Workflow Error
    print(classify_with_llm(log_message_2))  # Example output: Deprecation Warning
    print(classify_with_llm(log_message_3))  # Example output: Unknown
