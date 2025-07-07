import pandas as pd

def main():
    data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
    df = pd.DataFrame(data)
    print("Sample DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
