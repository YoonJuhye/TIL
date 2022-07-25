'use strict';

// Promise is a JavaScript object for asynchronous operation.
// 자바스크립트 안에 내장되어 있는 비동기를 간편하게 처리할 수 있도록 도와주는 오브젝트
// 비동기를 수행할 때 콜백함수 대신 유용하게 사용할 수 있음

// 정해진 장시간의 기능을 수행하고나서 정상적으로 기능이 수행됐다면, 
// 성공의 메시지와 함께 처리된 결과값을 전달해주고,
// 기능을 수행하다 예상치 못한 문제가 발생했다면 에러를 전달해줌 

// State: pending -> fulfilled or rejected
// Producer vs Consumer

// 1. Producer
// when new Promise is created, the executor runs automatically.
const promise = new Promise((resolve, reject) => {
  // doing some heavy work (network, read files)
  console.log('doing something...');
  setTimeout(() => {
    resolve('ellie');
    // reject(new Error('no network'));
  }, 2000);
}); 

// promise 사용하기
// 2. Consumers: then, catch, finally
promise //
  .then(value => {
    console.log(value);
  })
  .catch(error => {
    console.log(error);
  })
  .finally(() => {
    console.log('finally');
  });

// 3. Promise chaining
const fetchNumber = new Promise((resolve, reject) => {
  setTimeout(() => resolve(1), 1000);
});

// then은 값을 바로 전달해도 되고, 비동기인 promise를 전달해도 됨
fetchNumber
  .then(num => num * 2)
  .then(num => num * 3)
  .then(num => {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(num - 1), 1000);
    });
  })
  .then(num => console.log(num));

// 4. Error Handling
const getHen = () =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve('🐓'), 1000);
  });
const getEgg = hen =>
  new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error(`error! ${hen} => 🥚`)), 1000);
  });
const cook = egg =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(`${egg} => 🍳`), 1000);
  });

getHen() // .then(hen => getEgg(hen))
  .then(getEgg)
  .catch(error => {
    return '빵';
  }) // 바로 앞의 then 에러를 처리하고 싶을 때 바로 뒤에 catch문
  .then(cook)
  .then(console.log)
  .catch(console.log);