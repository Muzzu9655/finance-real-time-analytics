import pandas as pd
from datetime import datetime

# --------------------------
# CONFIGURATION
# --------------------------
INPUT_FILE = "../sample_data/transactions_stream.csv"
OUTPUT_FILE = "../sample_data/processed_transactions.csv"

# Threshold for suspicious transaction
FRAUD_THRESHOLD = 10000  # Example: Flag any transaction >= 10,000

# --------------------------
# LOAD TRANSACTIONS
# --------------------------
print("Loading transactions...")
try:
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded {len(df)} transactions")
except FileNotFoundError:
    print("Error: Input CSV file not found!")
    exit()

# --------------------------
# PROCESS TRANSACTIONS
# --------------------------
print("Processing transactions...")

# Add a fraud flag
df['fraud_flag'] = df['amount'].apply(lambda x: 'Yes' if x >= FRAUD_THRESHOLD else 'No')

# Add a processing timestamp
df['processed_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Aggregate totals for summary (credits vs debits)
summary = df.groupby('type')['amount'].sum().reset_index()
print("\n--- Transaction Summary ---")
print(summary)

# --------------------------
# SAVE PROCESSED DATA
# --------------------------
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nProcessed file saved as {OUTPUT_FILE}")
