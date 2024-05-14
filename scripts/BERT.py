from bertopic import BERTopic
import pandas as pd

def main():
    input_file = input("Enter the path to your input file (csv). It needs to contain a column 'text': ")
    output_file = input("Enter the output file path and name for saving the BERTopic model: ")

    # Load the documents from the input file
    try:
        docs = pd.read_csv(input_file)
        docs = docs['text'].dropna().tolist()
        print("Input document is OK. BERTopic is running now...")  # Indicate BERTopic is starting
    except Exception as e:
        print(f"Failed to load documents from {input_file}. Error: {e}")
        return
    
    # Create and fit the BERTopic model
    try:
        topic_model = BERTopic()
        topics, probs = topic_model.fit_transform(docs)
        print("BERTopic model has been created.")  # Indicate successful creation
    except Exception as e:
        print(f"Failed to create the BERTopic model. Error: {e}")
        return
    
    # Save the BERTopic model
    try:
        topic_model.save(output_file)
        print(f"BERTopic model has been saved to {output_file}.")
    except Exception as e:
        print(f"Failed to save the BERTopic model. Error: {e}")

if __name__ == "__main__":
    main()
