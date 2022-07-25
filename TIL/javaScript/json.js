'use strict';
// HTTP 하이퍼텍스트를 어떻게 주고 받을 수 있는지 규약 클라이언트 request <-> response 서버
// Hypertext
// AJAX : Asynchronous JavaScript And XML 동적으로 서버에게 데이터를 주고받을 수 있음 
// XHR(XMLHttpRequest) fetch() API를 통해 간편하게 데이터를 주고받을 수 있음 (internet Explore에서 지원 x) 
// JSON
// JavaScript Object Notation : 
// 브라우저 뿐만 아니라 모바일에서 데이터를 주고받을 때, 서버와 통신하지 않아도 파일을 저장할 때.
// - 데이터를 주고받을 수 있는 가장 간단한 포맷
// - 읽기 편하고, Key와 value, 직렬화하고 데이터를 전송할 때 씀.
// - 프로그램 언어와 플랫폼과 상관 없이 사용 가능
// 1. 오브젝트를 어떻게 직렬화해서 serialize json으로 변환할지
// 2. 직렬화된 json을 어떻게 deserialize해서 오브젝트로 변환할지

// 1. Object to JSON 
// stringfy(obj)
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json);

const rabbit = {
  name: 'tori',
  color: 'white',
  size: null,
  birthDate: new Date(),
  jump: function () {
    console.log(`${this.name} can jump!`);
  },
};

json = JSON.stringify(rabbit);
console.log(json);

// json데이터에 jump라는 함수는 포함되지 않음. + symbol도 포함되지 않음 

json = JSON.stringify(rabbit, ['name', 'color', 'size']);
console.log(json);

json = JSON.stringify(rabbit, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'name' ? 'ellie' : value;
});
console.log(json);

// 2. JSON to Object
// parse(json)
console.clear();
json = JSON.stringify(rabbit);
console.log(json);
const obj = JSON.parse(json, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'birthDate' ? new Date(value) : value;
});
console.log(obj);
rabbit.jump();
// obj.jump();
// json으로 변환할 때 함수는 포함되지 않았으므로 다시 object로 변환할 때 포함되지 않음

console.log(rabbit.birthDate.getDate());
console.log(obj.birthDate.getDate());
// birthDate는 string. return value r