import { useState, useEffect } from "react";

function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");
  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  useEffect(() => {
    console.log("I run only once.");
  }, []);
  useEffect(() => {
    // if (keyword !== "" && keyword.length > 5) {
    //   console.log("SEARCH FOR", keyword);
    // }
    console.log("I run when 'keyword' changes.");
  }, [keyword]); // keyword가 변화할 때 코드 실행
  useEffect(() => {
    console.log("I run when 'counter' changes.");
  }, [counter]);
  // 이를 사용하면 무엇이 변화할 때 특정 코드 실행 가능해짐.
  useEffect(() => {
    console.log("I run when keyword & counter changes.");
  }, [keyword, counter]);
  return (
    <div>
      <input
        value={keyword}
        onChange={onChange}
        type="text"
        placeholder="Search here..."
      />
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}

export default App;

// useState function
// className을 랜덤하게 생성 -> 컴포넌트, 스타일 독립적
// 컴포넌트를 분리해서 만들 수 있고, 컴포넌트를 위한 CSS를 만들 수 있음

// useEffect function : 우리 코드가 딱 한번만 실행될 수 있도록 보호해줌
