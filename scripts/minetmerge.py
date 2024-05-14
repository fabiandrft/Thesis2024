import subprocess
import os
import pandas as pd
import glob

# Configuration
chat_names_file = 'new/seed2.txt'  # Path to the text file with chat names
output_folder = 'new/output/'  # Folder where the individual CSV files will be stored
log_file = 'new/processed_chats.log'  # Log file to track processed chats
final_output_csv = 'new/final_output.csv'  # Path for the final merged CSV file

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Ensure the log file exists
with open(log_file, 'a') as f:
    pass

# Read the log file to get a list of processed chats
with open(log_file, 'r') as f:
    processed_chats = set(f.read().splitlines())

# Read chat names from the text file
with open(chat_names_file, 'r') as f:
    chat_names = f.read().splitlines()

# Process each chat
for chat in chat_names:
    if chat not in processed_chats:
        output_file = os.path.join(output_folder, f"{chat}.csv")  # Construct the output file path for each chat
        try:
            # Execute the minet command for each chat with the specified output file
            subprocess.run([
                'minet', 'telegram', 'channel-messages', 
                chat, '-o', output_file
            ], check=True)

            # If successful, log the chat name
            with open(log_file, 'a') as f:
                f.write(f"{chat}\n")
            print(f"Processed and logged chat: {chat} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing chat {chat}: {e}")

# After processing all chats, merge all CSV files into one
csv_files = glob.glob(os.path.join(output_folder, "*.csv"))
combined_df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
combined_df.to_csv(final_output_csv, index=False)

print(f"All chats merged into {final_output_csv}. Processing complete.")
