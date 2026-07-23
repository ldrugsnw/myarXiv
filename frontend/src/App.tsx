import { useState } from "react";
import type {Paper} from "./types/paper"

function App() {
  const [query, setQuery] = useState("");
  // query는 문자열이어서 " "가 맞는데
  // useState <- 이 변수들은 화면이랑 연결된 변수이다.

  const [papers, setPapers] = useState<Paper[]>([]);
  // papers는 리스트라..

  return (
  <div>
    <h1>MyArxiv</h1>


  <input 
    value={query} 
    onChange={(e)=> setQuery(e.target.value)} // e <= event
    />


  <button onClick={searchPapers}>
    검색
  </button>

  {
    papers.map((paper) => (
        <div key={paper.id}>
            {paper.title}
        </div>
    ))
}

  </div>
  );

  function searchPapers(){
    fetch(`https://ideal-trout-7v7wxxqvgw6xhrgvq-8000.app.github.dev/papers?query=${query}`)
      .then((res)=> res.json())
      .then((data)=>setPapers(data.papers))
  }
}

export default App;