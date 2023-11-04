# 공공 빅데이터 분석 및 시각화 project

## 팀명 : 베라 (Benefit, Better, Best Life) 
### 기간 : 2023.11.3 -> 2023.12.1
### 주제 : 서울시 공공 데이터를 활용한 운동프로그램 추천 챗봇 구현
### 키워드 : 건강, 운동, 추천, 지자체, 체육센터, 선호도 등
### 사용 데이터 : (체육, 보건소 등)시설 사용 및 프로그램 인원수 모집 현황 등

# 프로젝트 개요 
1. 분석 배경 및 목적
   - 분석 배경 : 국민연금 고갈, 건강보험료 증가 등 고령인구 증가로 인한 의료비 지출 증가. 또한 건강관리에 대한 관심도 증가로 인한 치료 -> 예방 중심 헬스케어 사회로 변화.
   - 디지털 기술이 접목되어 기술의 활용도가 증가했으나, 디지털 리터러시 격차가 존재. 자세히는 건강 관리 관련 정보에 대한 접근이 젊은 인구에 한정적이고 고령인구에는 제한적이라는 문제점 존재.
   - 지자체별 운동 프로그램 활성화 및 정보 제공을 위한 추천 시스템 개발 및 GUI 구성을 통해 접근성을 높임.
   - 분석 목적 : 서울 시민들에게 구별로 운영되고 있는 운동-건강 프로그램 사용자 등록 현황을 파악&분석하고 이를 대시보드화하여 등록 가능한 프로그램을 추천할 수 있도록 함.
   
2. 분석 절차
   1) 데이터 정의 : 특화된 샘플 데이터가 아닌 공공데이터를 활용하여 샘플의 표준화
   2) 데이터 전처리 및 분석 : 프로젝트 정의서 참고
   3) 데이터 시각화 : tableau 사용
   4) 데이터 정규화(key값) : 운동 컨텐츠 필터링(데이터 점수, 단계, 비율, 인구통계 등)
   5) 데이터 모델링 : 실시간 데이터 크롤링(오픈 API), 통계자료 수집(CVS), 추천시스템(지역, 체육센터, 프로그램 이름, 전화번호, 나이, 연령층(초기에는 고령인구만)) 지도 위치(GUI)
   6) 데이터 예측 : 사용자 운동 정보 수집 또는 임의 생성(예비 선호도)
      
4. 활용방안
   - 챗봇 또는 인공지능 스피커 연동 서비스 제공
   - 공공기관(지자체)와 협업하여 서비스 제공
   - 지도서비스, 운동습관 점수, 운동 추천 앱 등 서비스 연계
