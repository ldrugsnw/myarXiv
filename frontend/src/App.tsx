import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  // useState <- 이 변수들은 화면이랑 연결된 변수이다.

  useEffect(() => {
    // fetch는 주문하기!!! 주방! 데이터 좀 주세요!
    fetch("https://ideal-trout-7v7wxxqvgw6xhrgvq-8000.app.github.dev/")
      .then((res) => {
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }
    return res.json();
    })
    .then((data) => {
      setMessage(data.message);
    })
    .catch((err) => {
      console.error(err);
      setMessage(err.message);
    });
      }, []);

  return (
    <div>
      <h1>MyArxiv</h1>
      <h2>{message}</h2>
    </div>
  );
}

export default App;