# 드림코딩 - 자바스크립트

| 강의명                                                       | 날짜       | 링크                         |
| ------------------------------------------------------------ | ---------- | ---------------------------- |
| 자바스크립트 1.  자바스크립트의 역사와 현재 그리고 미래      | 7/11 (월)  | https://youtu.be/wcsVjmHrUQg |
| 자바스크립트 2. 콘솔에 출력, script async 와 defer의 차이점  | 7/12 (화)  | https://youtu.be/tJieVCgGzhs |
| 자바스크립트 3. 데이터타입, data types, let vs var, hoisting | 7/13  (수) | https://youtu.be/OCCpGh4ujb8 |
| 자바스크립트 4. 코딩의 기본 operator, if, for loop 코드리뷰 팁 | 7/14 (목)  |                              |
| 자바스크립트 5. Arrow Function 함수의 선언과 표현            | 7/15 (금)  |                              |
| 자바스크립트 6. 클래스와 오브젝트의 차이점, 객체지향 언어 클래스 | 7/17 (월)  |                              |
| 자바스크립트 7. 오브젝트                                     | 7/18 (화)  |                              |
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

- Use strict

  added in ES 5

  Use this for Valina Javascript.

  'use strict';

---



## 3. 데이터타입, data types, let vs var, hoisting

- 프로그래밍 언어에서 가장 중요한 것
  - 입력, 연산, 출력
  - CPU에 최적화된 연산, 메모리 사용을 최소화

#### Variable

- 어플리케이션이 실행되면 어플리케이션이 쓸 수 있는 메모리가 제한적으로 할당됨.

- let (added in ES6) : Mutable datatype 
- Block Scope : 블록 안에서 선언된 변수는 밖에서 접근할 수 없게 됨
- var (don't ever use this!)
  - var hoisting : 어디에 선언했느냐와 상관 없이 항상 제일 위로 선언을 끌어올려주는 것을 말함.
  - 선언도 하기 전에 값을 할당, 출력 가능함.
  - 블록 스코핑이 없음. 어디에서나 접근 가능(블록 안에서 변수를 선언해도 밖에서 접근 가능함)
  - 규모 있는 프로젝트에서는 선언하지 않은 값이 할당되는 단점 -> let 등장 

#### Constants

- Const : immutable type

- variable let은 포인터를 이용해서 값을 계속 변경할 수 있었음
- 하지만, constants는 이 포인터가 잠겨있어서 할당 이후엔 절대 변경할 수 없음
- favor immutable data type always for a few reasons:
  - secruity
  - Thread safety
  - reduce human mistakes



#### Variable types

- primitive, single item: number, string, boolean, null, undefined, symbol
- object, box container
- Function, first-class function

- 자바스크립트에서 value integer와 decimal number 차이 없이 type number로 출력됨
- bigInt
- string

- null
  - 비어있는 값이라고 지정하는 것 null로 값이 할당되어 있는것
- Undefined
  - 선언은 되어있지만, 아무런 값이 할당되지 않은 상태
  - 텅 비어있는지, 아직 할당되지 않은 것인지 모름

- Symbol, create unique identifiers for objects
  - 동일한 string을 작성했어도 다른 심볼로 만들어지기 때문에 고유한 식별자를 만들 때 이용



#### Dynamic typing

- Dynamically typed language
- 선언할 때 어떤 타입인지 선언하지 않고, runtime할 때 할당된 값에 따라서 값이 변경될 수 있음

- typeError의 문제가 생길 수 있어서 생긴 게 TypeScript



