import pandas as pd

def main():
    df = pd.read_csv('Training/Dataset/synthetic_logs.csv')
    df = df.drop(columns=['complexity'])
    print(df)

if __name__ == "__main__":
    main()
