// 시간 변환 코드
// 중요 포인트 자바스크립트 내장 객체인 FromData를 통해 시간을 함꼐 보내면
//세계시간기준이기떄문에 , 아래의 한국시간을 세계시간으로 변경해야한다.
// 세계시간과 한국시간은 9시간 차이
function calcTime(timestemp) {
  const nowTime = new Date().getTime() - 9 * 60 * 60 * 1000;
  const time = new Date(nowTime - timestemp);
  const hour = time.getHours();
  const min = time.getMinutes();
  const second = time.getSeconds();

  if (hour > 0) return `${hour}시간 전 `;
  else if (min > 0) return `${min}분전`;
  else if (second > 0) return `${second}초전 `;
  else "방금 전 ";
}

const rederData = (data) => {
  const main = document.querySelector("main");
  // 서버는 쌓인순으로 데이터를 보내주기 떄문에 최신순으로 바꿀려면 reverse
  data.reverse().forEach(async (obj) => {
    const itmeListDiv = document.createElement("div");
    itmeListDiv.className = "item-list";

    const imgDiv = document.createElement("img");
    const res = await fetch(`/images/${obj.id}`);
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    imgDiv.className = "item-list__img";
    imgDiv.src = url;

    const itemListInfoDiv = document.createElement("div");
    itemListInfoDiv.className = "item-list__info";

    const itemListInfoTitleDiv = document.createElement("div");
    itemListInfoTitleDiv.className = "item-list__info__title";
    itemListInfoTitleDiv.innerText = obj.title;

    const itemListInfoMetaDiv = document.createElement("div");
    itemListInfoMetaDiv.className = "item-list__info__meta";
    itemListInfoMetaDiv.innerText = obj.place + " " + calcTime(obj.insertAt);

    const itemListInfoPlaceDiv = document.createElement("div");
    itemListInfoPlaceDiv.className = "item-list__info__palce";
    itemListInfoPlaceDiv.innerText = obj.price;

    itemListInfoDiv.appendChild(itemListInfoTitleDiv);
    itemListInfoDiv.appendChild(itemListInfoMetaDiv);
    itemListInfoDiv.appendChild(itemListInfoPlaceDiv);
    itmeListDiv.appendChild(imgDiv);
    itmeListDiv.appendChild(itemListInfoDiv);
    main.appendChild(itmeListDiv);
  });
};

const fetchList = async () => {
  const res = await fetch("/items");
  const data = await res.json();
  rederData(data);
};

fetchList();
