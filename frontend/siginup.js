// 노드와 npm으 사용하지 않기때문에 cdn을 사용해야한다.
// 따라서 패키지를 직접 주입해줘야한다.

const SiginForm = document.querySelector("#siginup-form");



// async function handleSingup(e) {
//   e.preventDefault();
//   const body = new FormData(SiginForm);
//   console.log(sha256("hi"));
//   const res = await fetch("/siginup", {
//     method: "POST",
//     body,
//   });
// }

// SiginForm.addEventListener("submit", handleSingup);



// 비교의 결과값을 아직 선언되지 않은 함수가 써야하니깐 리턴으로 내보내기 
const passwordCheck = () => {
  const formData = new FormData(SiginForm);
  const pw1 = formData.get('userpsw');
  const pw2 = formData.get('userpsw2');

  if(pw1 === pw2){
    return true
  }else return false
}


const div = document.querySelector('.info');



// 회원가입 로직 
async function handleSingup(e) {
  e.preventDefault();
  const formData = new FormData(SiginForm);
  const sha256Password = sha256(formData.get('userpsw'))
  formData.set('userpsw',sha256Password);


  // formDatata는 name속성으로, 개별적으로 다룰 수있다. 
  // get으로 조회하고 set으로 넣을 수있다. 


  if(passwordCheck()){
    const res = await fetch("/siginup", {
      method: "POST",
      body: formData,
    });

    const data = await res.json()
    if(data === '200'){
      div.innerHTML = '회원가입에 성공했습니다.';
      div.style.color = 'blue';
      alert('회원가입에 성공했습니다.')
      window.location.pathname = 'login.html'
    }
  }else{
    div.innerHTML = '비밀번호가 틀렸습니다.'
    div.style.color ='red';
  }

}

SiginForm.addEventListener("submit", handleSingup);