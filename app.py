from openai import OpenAI
import requests
import time
OPENAI_API_KEY='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'
client = OpenAI(
    api_key= OPENAI_API_KEY
)

#assistant_id = 'asst_EUDnnIsh40O1FTFRrbjk2AJw'
sutudent_question = input(print('Type your query: '))

# Open the file in binary mode and upload it
# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open('now.pdf', "rb"),
  purpose='assistants'
)
print(file)

assistant = client.beta.assistants.create(
  
  instructions="you are an IT students` advisor, answer the students questions based on now.pdf file ",
  model="gpt-3.5-turbo-0125",
  tools=[{"type": "retrieval"}],
  file_ids=[file.id]

)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": sutudent_question,
      "file_ids": [file.id]
    }
  ]
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,

)
print('Run created: ', run.id)

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id= thread.id, run_id= run.id)
    print(' Run Status: ', run.status)
    time.sleep(1)
else:
    print('Run Completed')

message_response = client.beta.threads.messages.list(thread_id= thread.id)
messages = message_response.data
latest_message = messages[0]
print('Response: ', latest_message.content[0].text.value)




# flask : 
from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        student_question = request.form.get('query')
        # For simplicity, redirecting directly with query in URL
        return redirect(url_for('response', query=student_question))
    return render_template('welcome.html')

@app.route('/response')
def response():
    student_question = request.args.get('query', '')

    # Simplified placeholder for response processing
    # Implement your OpenAI interaction logic here, 
    # ideally moving long-running operations out of the request-response cycle
    example_response = "This is a placeholder for the OpenAI response."

    return render_template('response.html', response=example_response)

if __name__ == "__main__": 
    app.run(debug=True)
