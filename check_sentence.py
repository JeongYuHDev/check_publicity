import json
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os

from prompt import check_sentence_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 문장이 포함된 CSV 파일 로드
df_1 = pd.read_csv("check_publicity\\testset\\public_name_sentence.csv")
df_2 = pd.read_csv("check_publicity\\testset\\common_name_sentence.csv")
df_3 = pd.read_csv("check_publicity\\testset\\team_name_sentence.csv")
df = pd.concat([df_1, df_2, df_3])

sample_df = df.sample(n=10)

prompt = check_sentence_prompt

def check_publicity(sentence):
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Check if this sentence contains any public figures and respond in JSON format: {sentence}"}
        ]
    )
    print(response.choices[0].message.content)
    return json.loads(response.choices[0].message.content)



results = []
num = 1
for _, row in df.iterrows():
    sentence = row['sentence']
    actual_publicity = row['publicity']
    prediction = check_publicity(sentence)
    predicted_publicity = prediction['result']
    identified_figures = prediction.get('public_figures', [])
    is_correct = actual_publicity == predicted_publicity
    results.append({
        "sentence": sentence,
        "actual_publicity": actual_publicity,
        "predicted_publicity": predicted_publicity,
        "identified_figures": identified_figures,
        "is_correct": is_correct
    })
    print(f"{num} : Processed: {sentence}...")
    print(f"Actual: {actual_publicity}, Predicted: {predicted_publicity}, Correct: {is_correct}")
    print(f"Identified figures: {identified_figures}")
    print("---")
    num += 1

results_df = pd.DataFrame(results)

# 정확도 계산
accuracy = (results_df['is_correct'].sum() / len(results_df)) * 100

print(f"\nAccuracy: {accuracy:.2f}%")

# 결과를 CSV 파일로 저장
results_df.to_csv("check_publicity\\results_sentence.csv", index=False)
print("\nResults saved to 'check_publicity\\results_sentence.csv'")
