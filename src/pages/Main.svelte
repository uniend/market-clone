
<script>
  import { onMount } from "svelte";
  import Footer from "../components/Footer.svelte";
  import { getDatabase, ref, onValue } from "firebase/database";

  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  function calcTime(timestemp) {
  const nowTime = new Date().getTime() - 9 * 60 * 60 * 1000;
  const time = new Date(nowTime - timestemp);
  const hour = time.getHours();
  const min = time.getMinutes();
  const second = time.getSeconds();

  if (hour > 0) return `${hour}시간 전 `;
  else if (min > 0) return `${min}분전`;
  else if (second > 0) return `${second}초전 `;
  else return "방금 전 ";
}

  $: items  = []

  
  const db = getDatabase();
  const starCountRef = ref(db, 'items/' );

  onMount(()=>{
    onValue(starCountRef, (snapshot) => {
      const data = snapshot.val();
      items = Object.values(data).reverse();
    });
  });



</script>






    <header>
      <div class="info-bar">
        <div class="info-bar__time">  {hour} : {min}</div>
        <div class="info-bar__icons">
          <img src="asset/cart-bar.svg" alt="cart-bar" />
          <img src="asset/wifi.svg" alt="wifi" />
          <img src="asset/batter.svg" alt="batter" />
        </div>
      </div>

      <div class="menu-bar">
        <div class="menu-bar__location">
          <div>역삼1동</div>
          <div class="menu-bar__location--icons">
            <img src="asset/arrow-down.svg" alt="arrow-down" />
          </div>
        </div>

        <div class="menu-bar__icons">
          <img src="asset/search.svg" alt="search" />
          <img src="asset/bar.svg" alt="bar" />
          <img src="asset/bell.svg" alt="bell" />
        </div>
      </div>
    </header>

    <main>
      {#each items as item}
        <div class="item-list">
          <img src={item.urlImg} alt="이미지" class="item-list__img">
          <div class="item-list__info">
            <div class="item-list__info__title">{item.title}</div>
            <div class="item-list__info__meta">{item.place} {calcTime(item.insertAt)}</div>
            <div class="item-list__info__palce">{item.price}</div>
          </div>
        </div>
      {/each} 

      <!-- <div class="item-list">
        <img src="asset/img.svg" alt="" class="item-list__img" />
        <div class="item-list__info">
          <div class="item-list__info__title">게이밍 pc 팝니다.</div>
          <div class="item-list__info__meta">역삼동 19초 전</div>
          <div class="item-list__info__palce">100만원</div>
        </div>
      </div>
      <div class="item-list">
        <img src="asset/img.svg" alt="" class="item-list__img" />
        <div class="item-list__info">
          <div class="item-list__info__title">게이밍 pc 팝니다.</div>
          <div class="item-list__info__meta">역삼동 19초 전</div>
          <div class="item-list__info__palce">100만원</div>
        </div>
      </div>
      <div class="item-list">
        <img src="asset/img.svg" alt="" class="item-list__img" />
        <div class="item-list__info">
          <div class="item-list__info__title">게이밍 pc 팝니다.</div>
          <div class="item-list__info__meta">역삼동 19초 전</div>
          <div class="item-list__info__palce">100만원</div>
        </div>
      </div>
      <div class="item-list">
        <img src="asset/img.svg" alt="" class="item-list__img" />
        <div class="item-list__info">
          <div class="item-list__info__title">게이밍 pc 팝니다.</div>
          <div class="item-list__info__meta">역삼동 19초 전</div>
          <div class="item-list__info__palce">100만원</div>
        </div>
      </div>
      <div class="item-list">
        <img src="asset/img.svg" alt="" class="item-list__img" />
        <div class="item-list__info">
          <div class="item-list__info__title">게이밍 pc 팝니다.</div>
          <div class="item-list__info__meta">역삼동 19초 전</div>
          <div class="item-list__info__palce">100만원</div>
        </div>
      </div>
      <div class="item-list">
        <img src="asset/img.svg" alt="" class="item-list__img" />
        <div class="item-list__info">
          <div class="item-list__info__title">게이밍 pc 팝니다.</div>
          <div class="item-list__info__meta">역삼동 19초 전</div>
          <div class="item-list__info__palce">100만원</div>
        </div>
      </div> -->
    </main>

    <Footer location = 'home'/>

    <a href="#/Write"  class="write">+ 글쓰기</a>

    <div class="media-msg">화면 사이즈를 줄여주세요</div>
