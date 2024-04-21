<div>로그인</div>
<form id="login-form" action="/login" method="POST">
  <div class="useridDiv">
    <label for="userid">아이디 </label>
    <input
      type="text"
      placeholder="아이디를 입력해주세요"
      name="userid"
      id="userid"
      required
    />
  </div>
  <div class="userpswDiv">
    <label for="userpsw">비밀번호</label>
    <input
      type="password"
      placeholder="비밀번호를 입력해주세요"
      name="userpsw"
      id="userpsw"
      required
    />
  </div>
  <div>
    <button type="submit">로그인</button>
  </div>
</form>

<div class="info"></div>