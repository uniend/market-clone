const form = document.querySelector("#login-form");



async function handleLogin(e) {
  e.preventDefault();

  const loginForm = new FormData(form);

  // 암호화 하기
  const sha256Password = sha256(loginForm.get("userpsw"));
  loginForm.set("userpsw", sha256Password);

  const res = await fetch("/login", {
    method: "post",
    body: loginForm,
  });

  const data = await res.json();
  console.log(data)
  console.log(data.access_token)
  // 로컬 스토리지는 영구보관
  const accessToken = data.access_token;
  // 세션 스토리지는 브라우저 닫음 사라짐
  // window.sessionStorage.setItem('token',accessToken)

  if (res.status === 200) {
    alert("로그인에 성공했습니다. ");
    window.localStorage.setItem('token',accessToken)
    const infoDIv = document.querySelector(".info");
    const btn = document.createElement("button");
    btn.innerHTML = "아이템가져오기";
    infoDIv.appendChild(btn);
    infoDIv.addEventListener("click", async () => {
      const res = await fetch("/items",{
        headers: {
          Authorization: `Bearer ${accessToken}`
        },
      });
      const data = res.json();
      console.log(data);
    });
    window.location.pathname = '/'
  } else if (res.status === 401) {
    alert("아이디 혹은 패스워드가 틀렸습니다. ");
  }
}

form.addEventListener("submit", handleLogin);
