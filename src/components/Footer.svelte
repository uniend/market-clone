
<script>
  export let location; 

  const moveHome = () => {
    window.location.hash = '/'
  }

  const moveMypage = () => {
    window.location.hash = '/my'
  }

</script>


<footer>
  <div class="footer--container">
    <button class="footer--icons" on:click={moveHome}>
      {#if location === 'home'}
      <img src="asset/home.svg" alt="home" />
      {:else }
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
      </svg>
      {/if}
      <span>홈</span>
    </button>
    <button class="footer--icons">
      <img src="asset/docu.svg" alt="docu" />
      <span>동네생활</span>
    </button>
    <button class="footer--icons">
      <img src="asset/loca.svg" alt="loca" />
      <span>내 근처</span>
    </button>
    <button class="footer--icons">
      <img src="asset/chat.svg" alt="chat" />
      <span>채팅</span>
    </button>
    <button class="footer--icons" on:click={moveMypage}>
      {#if location === 'my'}
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
        <path fill-rule="evenodd" d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z" clip-rule="evenodd" />
      </svg>
      {:else}      
      <img src="asset/user.svg" alt="user" />
      {/if}
      <span>나의 당근</span>
    </button>
  </div>
</footer>