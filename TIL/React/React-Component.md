[생활코딩 React](https://www.youtube.com/watch?v=8hGqznPGVc0&list=PLuHgQVnccGMCRv6f8H9K5Xwsdyg4sFSdi&index=15)

- HTML 을 축약해서 쓸 수 있음
- Component 만들어두면 관리가 편해짐

```js
function Modal(){
	return (
		<div className="modal">
      <h2>제목</h2>
      <p>날짜</p>
      <p>상세내용</p>
		</div>	
	)
}
```

- Component 만드는 법

  1. 함수 만들고 이름 짓고
  2. 축약을 원하는 HTML 넣고
  3. 원하는 곳에서 <함수명 />

  - 이름은 대괄호로

  - return() 안에 있는건 태그 하나로 묶어야 함
  - 의미 없는 div 쓰기 싫으면 <> </> 사용

- 반복출현하는 HTML덩어리, 자주 변경되는 HTML UI들, 다른 페이지 만들 때
- State 쓸 때 복잡해짐 {} 
  - 상위 component에서 만든 state 쓰려면 Props문법 이용해야 함

```js
class Content extends Component {
  render() {
    return (
    	<article>
      	<h2>{this.props.title}</h2>
      	{this.props.desc}
  		</article>
    );
  }
}
class Subject extends Component {
	render(){
    return (
    	<header>
      	<h1>{this.props.title}</h1>
      	{this.props.sub}
  		</header>
    );
  }
}

class App extends Component {
  render() {
    return (
    	<div className="App">
      	<Subject title="WEB" sub="world wide web!"></Subject>
      	<Subject title="React" sub="For UI"></Subject>
      	<TOC></TOC>
      	<Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    );
  }
}
```



#### 컴포넌트 분리하기

- TOC.js

```js
Import React, { Component } from 'react';

class TOD extends Component {
  
}

export default TOC; // 다른 곳에서 TOC라는 class를 이용할 수 있게 함
```

- App.js

```js
import TOC from "./components/TOC"

class App extends Component {
  render() {
    return (
    	<div className="App">
      	<Subject title="WEB" sub="world wide web!"></Subject>
      	<TOC></TOC>
      	<Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    );
  }
}
```







- ProfileUser.js

```js
import React from 'react';
/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';
import styled from 'styled-components';
import common from '../../constants/commonStyle';
import colors from '../../constants/colors';
import TopNavigation from '../../components/Common/TopNavigation/TopNavigation';
import Button from '../../components/Common/Button/Button';
import BottomNavigation from '../../components/Common/BottomNavigation/BottomNavigation';
import { useParams } from 'react-router-dom';
import null_profile from '../../assets/null_profile_img.png';
import article_img from '../../assets/article_img.jpg';
const ProfileUser = () => {
	const { userId } = useParams();
	return (
		<>
			<TopNavigation
				backClick
				onBackClick={() => {
					alert('클릭');
				}}
				leftContent={<span>userId</span>}
			/>
			<div
				className="wrapper"
				style={{
					width: '100%',
					height: '100%',
				}}
			>
				{/* 프로필 바이오 */}
				<div
					css={css`
						display: flex;
						flex-direction: row;
						justify-content: space-around;
						align-items: center;
					`}
				>
					<img src={null_profile} alt="" />
					{/* 프로필 사진 옆 텍스트*/}
					<div
						css={css`
							display: flex;
							flex-direction: column;
							justify-content: center;
							align-items: center;
						`}
					>
						{/* 팔로워, 팔로잉 */}
						<div
							css={css`
								display: flex;
								flex-direction: row;
								justify-content: center;
								padding: 10px;
							`}
						>
							{/* 팔로워 */}
							<div
								css={css`
									display: flex;
									flex-direction: column;
									align-items: center;
									padding: 10px;
								`}
							>
								<span>602</span>
								<span>Followers</span>
							</div>
							{/* 팔로잉 */}
							<div
								css={css`
									display: flex;
									flex-direction: column;
									align-items: center;
									padding: 10px;
								`}
							>
								<sapn>290</sapn>
								<span>Following</span>
							</div>
						</div>
						{/* 옷 수 */}
						<div>
							<span>옷장에 80벌의 옷이 있습니다</span>
						</div>
					</div>
				</div>
				{/* 버튼 */}
				<div
					css={css`
						display: flex;
						flex-direction: row;
						justify-content: center;
						align-items: center;
						width: 80%;
						border-radius: 14px;
					`}
				>
					<Button type="active" label="Follow" style={{ padding: 10 }} />
					<Button type="active" label="Message" style={{ padding: 10 }} />
				</div>
			</div>
			{/* 옷장 사진 */}
			{/* <div
				css={css`
					position: relative;
					display: flex;
					flex-direction: column;
				`}
			>
				<div
					css={css`
						align-items: stretch;
						box-sizing: border-box;
						display: flex;
						flex-direction: row;
						flex-shrink: 0;
						position: relative;
					`}
				>
					<img src={article_img} alt="" />
					<img src={article_img} alt="" />
				</div>
				<div>
					<img src={article_img} alt="" />
					<img src={article_img} alt="" />
				</div>
			</div> */}
			<BottomNavigation />
		</>
	);
};

export default ProfileUser;

```



```
import React from 'react';
import { useParams } from 'react-router-dom';

const ProfileUser = () => {
	const { userId } = useParams();
	return <div>프로필 : {userId}</div>;
};

export default ProfileUser;
```

