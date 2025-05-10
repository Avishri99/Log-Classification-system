from proccessor_regex import classify_with_regex
from proccessor_llm import classify_with_llm
from proccessor_bert import classify_with_bert
import pandas as pd

def classify(logs):
    labels = []
    for source, log in logs:
        label = classify_log(source, log)
        labels.append(label)
    return labels

def classify_log(source, log):
    if source == "LegacyCRM":
        label = classify_with_llm(log) #placeholder for llm classification
    else:
        label = classify_with_regex(log)
        if label is None:
            label = classify_with_bert(log) #placeholder for bert classification
    return label
        
def classify_csv(input_file):
    df = pd.read_csv(input_file)
    df['Target_label'] = classify(list(zip(df['source'], df['log_message'])))

    output_file = 'Resources/output.csv'
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    classify_csv('Resources/test.csv')
#     # Test cases for classify_with_regex function
#     test_cases = [
#     ("ModernCRM", "Email service experiencing issues with sending."),
#     ("ModernHR", "Critical system unit error: unit ID Component55."),
#     ("AnalyticsEngine", "Unauthorized access to data was attempted."),
#     ("BillingSystem", "User User1234 logged in."),
#     ("ThirdPartyAPI", "Multiple bad login attempts detected on user 8538 account."),
#     ("LegacyCRM", "Lead conversion failed for prospect ID 7842 due to missing contact information."),
#     ("LegacyCRM", "API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."),
#     ("LegacyCRM", "Error: unable to connect to database due to invalid credentials")
# ]

#     classified_logs = classify(test_cases)
#     print(classified_logs)