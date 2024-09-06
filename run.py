import json
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os
import random

load_dotenv()

public_name = pd.read_csv("check_publicity\\testset\\public_name.csv")
common_name = pd.read_csv("check_publicity\\testset\\common_name.csv")

# 10개의 셀럽 이름과 10개의 일반인 이름을 선택
sample_public = public_name.sample(n=100)
sample_common = common_name.sample(n=200)

# 샘플 데이터 합치기
sample_data = pd.concat([sample_public, sample_common]).reset_index(drop=True)

# 이름 리스트를 섞습니다
sample_data = sample_data.sample(frac=1).reset_index(drop=True)

prompt = """
You're an investigator who is responsible for checking the user's inputs for check publicity issue.
Your job is to check the user's input using the following rule: 
if a name is found, you must check whether that name could cause a publicity issue.

if the name is a public figure, you should return True.
if the name is not a public figure, you should return False.

Please provide your response in JSON format as follows:
{
    "result": boolean
}
"""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def check_publicity(person_name):
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Check if this name is a public figure and respond in JSON format: {person_name}"}
        ]
    )
    
    return json.loads(response.choices[0].message.content)['result']

results = []
for _, row in sample_data.iterrows():
    name = row['name']
    actual_publicity = row['publicity']
    predicted_publicity = check_publicity(name)
    is_correct = actual_publicity == predicted_publicity
    results.append({
        "name": name,
        "actual_publicity": actual_publicity,
        "predicted_publicity": predicted_publicity,
        "is_correct": is_correct
    })
    print(f"Processed: {name}, Actual: {actual_publicity}, Predicted: {predicted_publicity}, Correct: {is_correct}")

print("\nFinal Results:")
print(results)

# 결과를 DataFrame으로 변환
results_df = pd.DataFrame(results)

# 정확도 계산
accuracy = (results_df['is_correct'].sum() / len(results_df)) * 100

print(f"\nAccuracy: {accuracy:.2f}%")

# 유명인과 일반인 각각의 정확도 계산
public_accuracy = results_df[results_df['actual_publicity'] == 1]['is_correct'].mean() * 100
common_accuracy = results_df[results_df['actual_publicity'] == 0]['is_correct'].mean() * 100

print(f"Public Figure Accuracy: {public_accuracy:.2f}%")
print(f"Common Person Accuracy: {common_accuracy:.2f}%")

# 결과를 CSV 파일로 저장
results_df.to_csv("check_publicity\\results.csv", index=False)
print("\nResults saved to 'check_publicity\\results.csv'")
