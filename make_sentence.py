from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd

from prompt import make_sentence

load_dotenv()

# 클라이언트 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 문장 생성 프롬프트 설정
prompt = make_sentence

# 데이터 불러오기
df_1 = pd.read_csv("check_publicity\\testset\\public_name.csv")
df_2 = pd.read_csv("check_publicity\\testset\\common_name.csv")

# 유명인 이름 문장 생성
sentences = []
booleans = []

celeb_df = df_1.sample(n=50)  # 50개의 행만 랜덤으로 선택
num = 1
for _, row in celeb_df.iterrows():
    name = row['name']
    boolean = row['publicity']
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": name}
        ])

    sentence = response.choices[0].message.content
    print(f"{num} : {sentence}")
    sentences.append(sentence)
    booleans.append(boolean)
    num += 1

celeb_df["sentence"] = sentences
celeb_df["publicity"] = booleans
celeb_df.to_csv("check_publicity\\testset\\public_name_sentence.csv", index=False)

# 일반인 이름 문장 생성
sentences = []  # 새로운 리스트 초기화
booleans = []   # 새로운 리스트 초기화

no_celeb_df = df_2.sample(n=50)
num = 1
for _, row in no_celeb_df.iterrows():
    name = row['name']
    boolean = row['publicity']
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": name}
        ])

    sentence = response.choices[0].message.content
    print(f"{num} : {sentence}")
    sentences.append(sentence)
    booleans.append(boolean)
    num += 1

no_celeb_df["sentence"] = sentences
no_celeb_df["publicity"] = booleans
no_celeb_df.to_csv("check_publicity\\testset\\common_name_sentence.csv", index=False)