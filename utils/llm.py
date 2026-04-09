import openai
import os

# Set your API key in environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_suggestions(resume, jd):
    prompt = f"""
    Compare the resume with the job description.

    Resume:
    {resume}

    Job Description:
    {jd}

    Provide:
    1. Missing skills
    2. Resume improvements
    3. Rewritten strong bullet points
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional resume reviewer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']
