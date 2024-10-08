import pandas as pd
import os

os.makedirs('testset', exist_ok=True)

celebrity_names = [
    "송강호", "전지현", "이병헌", "김태리", "공유", "손예진", "이정재", "김연아", "박서준", "아이유",
    "브래드 피트", "안젤리나 졸리", "레오나르도 디카프리오", "스칼렛 요한슨", "톰 크루즈", "제니퍼 로렌스", "조니 뎁", "엠마 왓슨", "로버트 다우니 주니어", "크리스 에반스",
    "크리스 헴스워스", "마고 로비", "라이언 고슬링", "에마 스톤", "톰 홀랜드", "젠데이아", "벤 애플렉", "갤 가돗", "헨리 카빌", "제이슨 모모아",
    "윌 스미스", "마이클 B. 조던", "샤를리즈 테론", "맷 데이먼", "크리스 프랫", "안나 켄드릭", "밀라 요보비치", "키아누 리브스", "샤를리즈 테론", "샤를리즈 테론",
    "제니퍼 애니스톤", "줄리아 로버츠", "산드라 블록", "니콜 키드먼", "케이트 윈슬렛", "나탈리 포트만", "앤 해서웨이", "리암 니슨", "휴 잭맨", "러셀 크로우",
    "다니엘 크레이그", "레이첼 와이즈", "주드 로", "케이트 블란쳇", "크리스틴 스튜어트", "로버트 패틴슨", "제시카 차스테인", "에이미 아담스", "브리 라슨", "엘리자베스 올슨",
    "폴 러드", "마크 러팔로", "제레미 레너", "스칼렛 요한슨", "톰 히들스턴", "벤딕트 컴버배치", "채드윅 보스만", "톰 하디", "마이클 패스벤더", "제임스 맥어보이",
    "제니퍼 로페즈", "비욘세", "테일러 스위프트", "아리아나 그란데", "리한나", "카디 비", "레이디 가가", "셀레나 고메즈", "저스틴 비버", "에드 시런",
    "드웨인 존슨", "빈 디젤", "제이슨 스타뎀", "실베스터 스탤론", "아놀드 슈워제네거", "브루스 윌리스", "리암 니슨", "피어스 브로스넌", "숀 코너리", "로저 무어",
    "마이클 케인", "게리 올드먼", "콜린 퍼스", "휴 그랜트", "주드 로", "이완 맥그리거", "다니엘 래드클리프", "루퍼트 그린트", "엠마 왓슨", "헬레나 본햄 카터",
    "기무라 타쿠야", "아라가키 유이", "사와지리 에리카", "후쿠야마 마사하루", "아야세 하루카", "니노미야 카즈나리", "마츠모토 준", "우에노 주리", "이시하라 사토미", "야마시타 토모히사",
    "호리키타 마키", "타케우치 유코", "오구리 슌", "시바사키 코우", "나가사와 마사미", "카리나", "미즈하라 키코", "타케이 에미", "사토 타케루", "카미키 류노스케"
]

public_name = set(celebrity_names)
marker_1 = [True] * len(public_name)
df = pd.DataFrame({'name': list(public_name), 'publicity': marker_1})
df.to_csv(r'testset\public_name.csv', index=False)

def main():
    name = input("이름을 입력하세요: ")

common_names = [
    "김민준", "이서연", "박지훈", "최수민", "정예은", "강동훈", "윤서영", "임현우", "신미래", "오태양",
    "존 스미스", "제인 도우", "마이클 존슨", "에밀리 데이비스", "윌리엄 브라운", "올리비아 윌슨", "제임스 테일러", "아바 앤더슨", "벤자민 토마스", "샬럿 무어",
    "리암 마틴", "아멜리아 잭슨", "노아 해리스", "이사벨라 클락", "메이슨 로빈슨", "미아 리", "엘리야 워커", "소피아 홀", "로건 영", "에밀리 스콧",
    "루카스 그린", "릴리 아담스", "잭슨 베이커", "에이바 넬슨", "에이든 카터", "엘라 미첼", "그레이슨 페레즈", "하퍼 로저스", "제이든 로스", "에블린 리드",
    "가브리엘 쿠퍼", "아리아나 콕스", "매튜 리처드슨", "스칼렛 워드", "세바스찬 베넷", "조이 베일리", "카메론 켈리", "페넬로페 브룩스", "제이콥 샌더스", "클로이 프라이스",
    "다니엘 파웰", "레이첼 벨", "헨리 제임스", "그레이스 리", "오스카 밀러", "에바 에드워즈", "잭슨 모건", "릴리안 쿠퍼", "사무엘 리", "에밀리슨 콜린스",
    "루카스 리", "아멜리아 리", "메이슨 리", "이사벨라 리", "에이든 리", "미아 리", "엘리야 리", "소피아 리", "로건 리", "에밀리 리",
    "루카스 리", "릴리 리", "잭슨 리", "에이바 리", "에이든 리", "엘라 리", "그레이슨 리", "하퍼 리", "제이든 리", "에블린 리",
    "가브리엘 리", "아리아나 리", "매튜 리", "스칼렛 리", "세바스찬 리", "조이 리", "카메론 리", "페넬로페 리", "제이콥 리", "클로이 리",
    "다니엘 리", "레이첼 리", "헨리 리", "그레이스 리", "오스카 리", "에바 리", "잭슨 리", "릴리안 리", "사무엘 리", "에밀리슨 리",
    "김민준", "이서연", "박지훈", "최수민", "정예은", "강동훈", "윤서영", "임현우", "신미래", "오태양",
    "존 스미스", "제인 도우", "마이클 존슨", "에밀리 데이비스", "윌리엄 브라운", "올리비아 윌슨", "제임스 테일러", "아바 앤더슨", "벤자민 토마스", "샬럿 무어",
    "리암 마틴", "아멜리아 잭슨", "노아 해리스", "이사벨라 클락", "메이슨 로빈슨", "미아 리", "엘리야 워커", "소피아 홀", "로건 영", "에밀리 스콧",
    "루카스 그린", "릴리 아담스", "잭슨 베이커", "에이바 넬슨", "에이든 카터", "엘라 미첼", "그레이슨 페레즈", "하퍼 로저스", "제이든 로스", "에블린 리드",
    "가브리엘 쿠퍼", "아리아나 콕스", "매튜 리처드슨", "스칼렛 워드", "세바스찬 베넷", "조이 베일리", "카메론 켈리", "페넬로페 브룩스", "제이콥 샌더스", "클로이 프라이스",
    "다니엘 파웰", "레이첼 벨", "헨리 제임스", "그레이스 리", "오스카 밀러", "에바 에드워즈", "잭슨 모건", "릴리안 쿠퍼", "사무엘 리", "에밀리슨 콜린스",
    "사토 타로", "스즈키 하나", "타나카 유키", "와타나베 사쿠라", "이토 다이치", "야마모토 아야", "나카무라 히로시", "코바야시 미사키", "카토 타쿠미", "요시다 리나",
    "야마다 켄", "사사키 유미", "이노우에 쇼", "마츠모토 나나", "시마무라 타쿠야", "오카다 유이", "하라다 타카시", "키무라 아오이", "미야자키 준", "후지타 마이",
    "니시무라 코지", "모리 유카", "호소다 타쿠", "사이토 리에", "카와사키 유타", "오노 미유", "카네코 타카시", "후지모토 사야카", "마에다 히로키", "카와무라 아키라",
    "알렉스 존슨", "에밀리 클락", "마이클 브라운", "사라 데이비스", "데이비드 윌슨", "리사 테일러", "크리스 앤더슨", "제시카 토마스", "브라이언 무어", "메건 홀",
    "조슈아 마틴", "에바 잭슨", "매튜 해리스", "소피아 클락", "제이콥 로빈슨", "에밀리 리", "루카스 워커", "릴리 홀", "제임스 영", "에이바 스콧",
    "그레이슨 그린", "하퍼 아담스", "제이든 베이커", "에블린 넬슨", "가브리엘 카터", "아리아나 미첼", "매튜 페레즈", "스칼렛 로저스", "세바스찬 로스", "조이 리드",
    "김지훈", "박서연", "이민호", "최지우", "정수빈", "강민호", "윤지우", "임수정", "신동엽", "오지호",
    "김하늘", "이준호", "박지민", "최지우", "정수빈", "강민호", "윤지우", "임수정", "신동엽", "오지호",
    "존 도우", "제인 스미스", "마이클 브라운", "에밀리 존슨", "윌리엄 데이비스", "올리비아 테일러", "제임스 앤더슨", "아바 토마스", "벤자민 윌슨", "샬럿 무어",
    "리암 해리스", "아멜리아 클락", "노아 로빈슨", "이사벨라 스콧", "메이슨 워커", "미아 홀", "엘리야 영", "소피아 그린", "로건 아담스", "에밀리 베이커",
    "루카스 넬슨", "릴리 카터", "잭슨 미첼", "에이바 페레즈", "에이든 로저스", "엘라 로스", "그레이슨 리드", "하퍼 쿠퍼", "제이든 콕스", "에블린 리처드슨",
    "가브리엘 워드", "아리아나 베넷", "매튜 베일리", "스칼렛 켈리", "세바스찬 브룩스", "조이 샌더스", "카메론 프라이스", "페넬로페 파웰", "제이콥 벨", "클로이 제임스",
    "다니엘 리", "레이첼 밀러", "헨리 에드워즈", "그레이스 모건", "오스카 쿠퍼", "에바 콜린스", "잭슨 리", "릴리안 리", "사무엘 리", "에밀리슨 리",
    "사토 타로", "스즈키 하나", "타나카 유키", "와타나베 사쿠라", "이토 다이치", "야마모토 아야", "나카무라 히로시", "코바야시 미사키", "카토 타쿠미", "요시다 리나",
    "야마다 켄", "사사키 유미", "이노우에 쇼", "마츠모토 나나", "시마무라 타쿠야", "오카다 유이", "하라다 타카시", "키무라 아오이", "미야자키 준", "후지타 마이",
    "니시무라 코지", "모리 유카", "호소다 타쿠", "사이토 리에", "카와사키 유타", "오노 미유", "카네코 타카시", "후지모토 사야카", "마에다 히로키", "카와무라 아키라",
    "알렉스 존슨", "에밀리 클락", "마이클 브라운", "사라 데이비스", "데이비드 윌슨", "리사 테일러", "크리스 앤더슨", "제시카 토마스", "브라이언 무어", "메건 홀"
]

common_name = set(common_names)
marker_2 = [False] * len(common_name)
df = pd.DataFrame({'name': list(common_name), 'publicity': marker_2})
df.to_csv(r'testset\common_name.csv', index=False)

df3 = load_csv("testset\team_name.csv", index=False)
team_name = set(df3['name'])
df = pd.DataFrame({'name': list(team_name)})
df.to_csv(r'testset\team_name.csv', index=False)


