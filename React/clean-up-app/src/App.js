import { useState, useEffect } from "react";

function Hello() {
  function byFn() {
    console.log("bye :(");
  }
  function hiFn() {
    console.log("Hi :)");
    return byFn;
  }
  useEffect(hiFn, []);
  // useEffect(() => {
  //   return () => console.log("destroyed :("); //clean up function 컴포넌트가 없어졌을 때, 이벤트리스너를 지우거나 콘솔에 보낼 수 있음.
  // }, []);
  return <h1>Hello</h1>;
}

function App() {
  const [showing, setShowing] = useState(false);
  const onClick = () => setShowing((prev) => !prev);
  return (
    <div>
      {showing ? <Hello /> : null}
      <button onClick={onClick}>{showing ? "Hide" : "Show"}</button>
    </div>
  );
}

export default App;
