import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def analyze_resume(resume_text, job_description):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are an AI recruiter.

Compare the candidate's resume with the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide the following:

1. Match Score: Give a percentage from 0 to 100.
2. Matching Skills: List the skills the candidate has that match the job.
3. Missing Skills: List important skills from the job that are missing.
4. Strengths: Give 3 short points.
5. Recommendation: Suitable or Not Suitable.
6. Reason: Give a short explanation.

Keep the answer clear and concise.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


def extract_skills(resume_text):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
Extract the technical skills from this resume.

Resume:
{resume_text}

Return only a clean comma-separated list of technical skills.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content