import openai

# Replace 'your_api_key_here' with your actual OpenAI API key
OPENAI_API_KEY = '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'

# Initialize the OpenAI client with your API key
openai.api_key = OPENAI_API_KEY

def send_message_to_openai(prompt):
    try:
        # Send the prompt to OpenAI and store the response using the updated API method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust the model if needed based on your specific use case
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )

        # Extracting the text from the response
        text_response = response['choices'][0]['message']['content']
        return text_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = "What is the capital of France?"
    response = send_message_to_openai(prompt)
    print("Response from OpenAI:", response)
