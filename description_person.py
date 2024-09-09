import pandas as pd
import openai
from dotenv import load_dotenv
import os
import json

from prompt import route_description

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = route_description

df = pd.read_csv("check_publicity\\results\\results_sentence.csv")

# 5번째 문장 선택 -> 테스트 진행하고 싶을 때, 위 숫자 변경하기(130까지 가능)
sentence = df['sentence'][5]
public_figures = df['identified_figures'][5]

input_data = {
    "sentence": sentence,
    "public_figures": public_figures
}

input_data = str(input_data)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": input_data}
    ],
    response_format={"type": "json_object"}
)
print(response.choices[0].message.content)

with open("check_publicity\\results\\description.json", "w", encoding="utf-8") as json_file:
    json.dump(response.choices[0].message.content, json_file, ensure_ascii=False, indent=4)

print("Result also saved to 'check_publicity/results/description.json'")
