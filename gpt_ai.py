import openai

def generate_chat_response(text):
    # Set up OpenAI API credentials
    openai.api_key = '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'
    request='''I would like to extract relevant information from a received email. For coding purposes, I want to separate these pieces of information using '|' as a delimiter.
    I am only interested in the information itself and not its description. The relevant information should be in the same language (English or French) as the email. If any of the fields don't contain any information, please use '0' as a placeholder. You can repeat the response generation as many times as needed, as long as it remains correct. If the content of the email does not pertain to a job or internship offer, please return "0" as the final output.
    The fields I need are as follows:
    First email present in the letter
    Mail region (if the email ends with ".com" or ".tn," the region is Tunisia; otherwise, the region is determined by the mail domain)
    Type of offer (summer internship/job/internship for final project)
    Name of the company/organization
    Required skills (separated by commas)
    Duration of the internship (if it is an internship)
    Department (IT or Electromechanique or génie civil): use your knowledge to determine this field
    -Here is the letter: \n'''
    input_text=request+text
    '''# Generate response using ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=1100,
        temperature=0.7,
        n=1,
        stop=None,
    )'''
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input_text}])
    # Extract the generated response from the API response
    generated_text = chat_completion['choices'][0]['message']['content']
    
    if generated_text== "0":
        return None
    else:
        return generated_text