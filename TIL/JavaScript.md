# 드림코딩 - 자바스크립트

| 강의명                                                       | 날짜       | 링크                         |
| ------------------------------------------------------------ | ---------- | ---------------------------- |
| 자바스크립트 1.  자바스크립트의 역사와 현재 그리고 미래      | 7/11 (월)  | https://youtu.be/wcsVjmHrUQg |
| 자바스크립트 2. 콘솔에 출력, script async 와 defer의 차이점  | 7/12 (화)  | https://youtu.be/tJieVCgGzhs |
| 자바스크립트 3. 데이터타입, data types, let vs var, hoisting | 7/17  (일) | https://youtu.be/OCCpGh4ujb8 |
| 자바스크립트 4. 코딩의 기본 operator, if, for loop 코드리뷰 팁 |            |                              |
| 자바스크립트 5. Arrow Function 함수의 선언과 표현            |            |                              |
| 자바스크립트 6. 클래스와 오브젝트의 차이점, 객체지향 언어 클래스 |            |                              |
| 자바스크립트 7. 오브젝트                                     |            |                              |
| 자바스크립트 8. 자바스크립트 배열 개념과 APIs                |            |                              |
| 자바스크립트 9. 10가지 배열함수, Array APIs                  |            |                              |
| 자바스크립트 10. JSON 개념 정리와 활용방법 및 유용한 사이트  |            |                              |
| 자바스크립트 11. 비동기 처리의 시작 콜백 이해                |            |                              |
| 자바스크립트 12. 프로미스 개념~활용                          |            |                              |
| 자바스크립트 13. 비동기의 꽃 JavaScript async와 await, 유용한 Promise APIs |            |                              |



## 1. 자바스크립트의 역사와 현재 그리고 미래 

- 1993, mosaic web browser (Marc Andreessen)
- 1994, Netscape Navigator (Marc Andreessen) - 정적인 웹사이트
- 동적인 웹사이트를 위해 scripting 언어를 추가

- 1994, 9, Moca - LiveScript 

- Java의 유명세에 힘입어 JavaScript로 명명
- 1995, Microsoft -> Reverse engineering -> Jscript

- JScript와 JavaScript의 혼란.
- 1997, 7 ECMAScript 표준화 논의
- 2000 Microsoft Internet Explorer 높은 시장 점유율

- 2004 모질라 Firefox -> ECMAScript4 표준화 논의
- 시장에 존재하는 다양한 브라우저에서 모두 작동하는 웹 페이지를 만들어야 하는 어려움
- 2004 AJAX 도입
- 다양한 브라우저의 동작, 웹 시장의 증가와 수요 증가
- JQuery, Dojo, 등 라이브러리가 많이 등장

- 2008, Google Chrome이라는 Just-In-Time compilation엔진 포함 브라우저 등장. 자바스크립트 작동 속도가 엄청 빨라짐
- 2008 7, 표준화 논의 시작
- ECMASciprt 5, 6
- 라이브러리 도움 없이 웹 API를 통해 작동 가능 

- 개발할 때는 최신 버전의 ECMAScript를 사용하고, 배포할 때만 JavaScript transcompiler Babel을 사용해서 변환
- SPA (Single Page Application): JavaScript를 쉽게 구현하기 위해 React, Angular, vue 등 다양한 라이브러리와 프레임워크 등장
- Node.js : javascript를 통해 back-end 서비스 구현을 위해 등장

---



## 2. Async vs defer 

- Head + async
  - parsing HTML executing js 
  - 정의된 순서는 상관 없이 다운로드 된 순서대로 실행이 됨.
- Head + defer 
  - 정의한 순서가 지켜지므로 원하는대로 지켜짐.

- 'use strict'; 를 사용하기 전에 선언해주면 좋음 (typestript를 사용할 때는 불필요함), 자바스크립트 엔진이 더 효율적으로 동작함.

---



## 3. 데이터타입, data types, let vs var, hoisting

- 프로그래밍 언어에서 가장 중요한 것
  - 입력, 연산, 출력
  - CPU에 최적화된 연산, 메모리 사용을 최소화