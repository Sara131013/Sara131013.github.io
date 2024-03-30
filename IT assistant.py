from openai import OpenAI
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
