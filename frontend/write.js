

const form = document.querySelector('#write-form');



async function handleSunmitForm(e) {

  // form에 포함되지 않는 데이터 form 데이터와 함께 제출하기 
  // 예시 ) 작성한 시간데이터 
  const body = new FormData(form);
  body.append('insertAt', new Date().getTime());
  e.preventDefault();
  try{
    const res = await fetch('/items',{
      method: 'POST',
      // 폼데이터만 보낼떄 
      // body: new FormData(form),
      // 폼데이터 외 데이터도 함꼐 보낼때 
      body
    })
    const data = await res.json();
    if(data === '200') window.location.pathname = '/';
  }catch(e){
    console.log(e)
  }
}

form.addEventListener('submit', handleSunmitForm)