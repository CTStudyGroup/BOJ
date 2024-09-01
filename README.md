
# 🔥코딩 테스트 스터디🔥
- 2024 하반기에 진행되는 코딩테스트 스터디입니다.  
    - 기본 알고리즘 문제 풀이 : 24.09.02 ~ 24.10.06 (휴식 기간 : 24.09.14 ~ 24.09.18)  
    - 실전 알고리즘 문제 풀이 : ... (python 코테 강의 실전 문제 풀이 예정)  
- 하루에 정해진 한 문제를 반드시 풀어야합니다.  
- 그 날 푼 알고리즘에 해당하는 다른 문제를 푼 경우, 해당 문제의 이슈,브랜치 생성 후 폴더,README를 추가해서 PR을 올립니다.  
    - 해당 문제는 모든 팀원이 다 풀기 전까지 이슈를 삭제하지 않습니다.   
- 각 문제에 대한 리뷰 마감 기한은 PR기준 익일 자정 12시까지입니다.  

# 🔸 참여 방법
## 🔹 소스 코드 업로드 및 리뷰 요청 방법
Main branch에서 새 branch를 생성한다.  
본인이 해결한 문제의 소스 코드를 본인의 branch에 push한다.  
Pull Request를 통해 코드 리뷰를 요청한다.  

## 🔹 Code Review 규칙
자유롭게 의견을 제시한다.  
잘했다고 생각하는 부분 칭찬하기  
피드백 할 게 없으면 칭찬해 주세요👍  
다른 풀이 방법 공유하기  
코드 전체를 공유하는 것이 아닌, 키워드나 간단한 소개만 해 주세요.  
개선이 필요한 부분 설명하기  
단, 개선이 필요한 이유를 충분히 설명해 주세요.  
정답 코드를 알려주기 보다는, 스스로 고민하고 개선 방법을 선택할 수 있게 해 주세요.  
리뷰 과정이 숙제 검사가 아닌, 학습 과정으로 느낄 수 있게 해 주세요.  
궁금한 부분 물어보기  
오픈 커뮤니케이션 지향  
ex) ~ 하는 게 어떨까요? / ~ 하는 것을 제안합니다. / ~ 부분은 ~ 문제가 있는 것 같은데 괜찮을까요?  

코드 작성자에게 피드백하는 것이 아닌, 코드 자체를 피드백한다는 생각으로 리뷰한다.

## 🔹 Pull Request 규칙
PR 템플릿에 맞게 작성한다.  
문제를 푸는 과정에서 본인이 생각한 내용을 작성한다.  
코드 설명을 작성한다. (단, 주석에 작성한 경우 생략한다.)  
특히 리뷰를 받고 싶은 부분을 작성한다.  
Markdown Codeblock을 이용하여 코드 일부를 발췌해서 작성한다.  
특히 리뷰를 받고 싶은 부분은, 리뷰어의 시간을 아낄 수 있게 본인 코드를 충분히 설명해 주세요.  
Reviewer는 본인을 제외한 2명을 추가한다.  
모든 스터디원에게 리뷰를 받은 후, 코드 수정이 완료되었으면 Label을 Merge Request로 변경한다.  
Main branch에 병합되면, 병합된 branch는 삭제시킨다.  

## 🔹 Commit Message 컨벤션
type : subject  

### ✔ Type
Feat: REAME.md, 폴더 추가  
Add: 소스 코드 파일(python) 추가  
Refactor: 소스 코드 수정  
Style: 소스 코드 형식(format) 수정, 변수 네이밍 수정, 주석 추가/삭제 등  
(코드 동작에 영향이 없는 수정)  
Chore: 그 외 기타 작업  
### ✔ Subject
50자 이하의 간단한 제목을 사용한다.  
ex) Add: 홍길동.py  
ex) Refactor: 완전 탐색 -> 이분 탐색  
ex) Style: 함수명 변경  

## 🔹 Branch Naming 컨벤션
본인_이름(영어_이니셜⭕, 한글❌)/이슈_번호(문제_번호❌)  
ex) hyolim/1  

branch 이름에 한글이 들어가면 문제가 생겨서 반드시 ⭐본인 이름을 영어 이니셜⭐로 branch를 생성해 주세요!  
문제 번호가 아닌, ⭐이슈 번호⭐로 branch를 생성해 주세요!  
각 문제마다 branch를 새롭게 생성해서, 소스 코드를 push 후 리뷰 요청하는 방식  

## 🔹 Python File Naming 컨벤션
본인이름(영어).py  
ex) Hyolim.py  

## 🔹 Directory 구조
└── 📂BFS  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂문제_이름  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾...  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── README.md  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂...  
&nbsp;&nbsp;&nbsp;&nbsp;└── 📂문제_이름  
└── 📂BinarySearch  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂문제_이름  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾...  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── README.md  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂...  
&nbsp;&nbsp;&nbsp;&nbsp;└── 📂문제_이름  
└── 📂BruteForce  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂문제_이름  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾...  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── README.md  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂...  
&nbsp;&nbsp;&nbsp;&nbsp;└── 📂문제_이름  
└── 📂Combination  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂문제_이름  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;├── 💾...  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── 💾홍길동.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── README.md  
&nbsp;&nbsp;&nbsp;&nbsp;├── 📂...  
&nbsp;&nbsp;&nbsp;&nbsp;└── 📂문제_이름  
└── ...



## 🔸 참여자
* 김은진 : https://github.com/Eunjin3395
* 이효림 : https://github.com/rimi3226
* 장현지 : https://github.com/hzee97