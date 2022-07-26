import { useEffect, useState } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const getMovies = async () => {
    const json = await (
      await fetch(
        "https://yts.mx/api/v2/list_movies.json?minimum_rating=8.8&sort_by=year"
      )
    ).json();
    // const json = await response.json();
    setMovies(json.data.movies);
    setLoading(false);
  };
  // 보통 async-await 방식 사용
  useEffect(() => {
    // fetch(
    //   "https://yts.mx/api/v2/list_movies.json?minimum_rating=8.8&sort_by=year"
    // )
    //   .then((response) => response.json())
    //   .then((json) => {
    //     setMovies(json.data.movies);
    //     setLoading(false);
    //   });
  }, []);
  return <div>{loading ? <h1>Loading...</h1> : null}</div>;
}

export default App;
