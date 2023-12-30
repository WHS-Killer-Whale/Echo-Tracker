# Echo- Tracker
포럼 유저를 검색하면 해당 유저가 활동하는 포럼 리스트를 볼 수 있는 CLI 툴

---

## ✅ Docker에서 실행(첫 번째 방법)

### 0️⃣ Git 저장소 복제
> 명령어: `git clone https://github.com/WHS-Killer-Whale/Echo-Tracker.git`
>
> 

### 1️⃣ WhatsMyName 폴더로 이동 후 Dockerfile BUILD
> 명령어: `cd Echo-Tracker/` >> `docker build -t echo-tracker .`
도커 로그인 후 실행
> 

### 2️⃣ 컨테이너 실행
> 명령어: `docker run -it echo-tracker`
>
> 

### ▶️ 실행 화면
![image](https://github.com/sunyou10/WhatsMyName/assets/145275007/01d62cf5-f324-4616-bd01-8bacab6bc319)


### ⏩ 재실행

> 명령어: `docker ps -a` >> `docker start -i {container_id}`
>

---


## ✅ Docker에서 실행(두 번째 방법)
Docker Hub에 배포된 컨테이너를 설치할 수도 있습니다.
> 아래 명령어를 실행합니다.
```
docker run -it hhtboy/whatsmyname_darkweb:1.0
```

### ⏩ 재실행

> 명령어: `docker ps -a` >> `docker start -i {container_id}`
>
---

## ✅ 주요 기능
> `USER NAME:`에 검색을 원하는 유저 네임을 입력하세요.
Echo- Tracker가 포럼 리스트 안의 포럼들에 해당 유저가 존재하는지 검색합니다.
>
> 

### 🚨 포럼 리스트
- crackedIo
- 0day
- 0x00sec
- 1877
- wasm
- redSecurity
- ramble
- infectedZone
- R0CREW
- hack5
- rootme
- megatop
- dark2web
- bdfClub
- Wjunction
- bhcforums
- enclavecc
- nulledBB
- hostingforums
- landzdown
- wilderssecurity
- breachForums
- 현재 총 21개 포럼 검색 지원

### ⚙️ 개발 환경
- `Python:3.10`
    - **Library: `requests` , `BeautifulSoup4` , `pyfiglet` , `clint`**
