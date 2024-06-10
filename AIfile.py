from openai import OpenAI
# importing all the required modules
import PyPDF2


conversation_history = []
filepath = "/home/akshay/geeksforgeeks/essay.pdf"

# creating a pdf reader object
reader = PyPDF2.PdfReader(filepath)

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())
text = reader.pages[1].extract_text()
while True:


    message = input("Enter your question here:   ")

    user_input = "User:" + message



    user_prompt = f"""
        1. You are an AI bot. you are to answer the users questions.
        2. Use the conversation history as your reference
        3. And respond to the user message

        conversation history is {conversation_history}
        user message is {message}
        This is the {text}
        """
    print(user_prompt)

    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_prompt}],
        stream=True,
    )

    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")

    # At the end of the stream, the response string should contain the full message
    ai_message = "AI: " + response

    conversation_history.append(user_input)
    conversation_history.append(ai_message)



    print("")
