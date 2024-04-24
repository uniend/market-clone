<script>
  import Footer from "../components/Footer.svelte";
  import { user$ } from "../store";


  const logOut = () => {
    // 로컬스토리지와 유저정보 지워주기 
    user$.set(null);
    localStorage.removeItem('token')
  }
</script>


<div>나의 당근</div>
<button on:click={logOut}>로그아웃</button>

<Footer location = 'my'/>


<style>
  button{
    cursor: pointer;
    border:  1px solid gray;
  }
</style>