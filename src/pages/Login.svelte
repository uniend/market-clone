

<script>
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

const provider = new GoogleAuthProvider();
const auth = getAuth();


const loginWithGoogle =  async() => {
  try{
    const result = await signInWithPopup(auth, provider)
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    const user = result.user;
    user$.set(user)
    localStorage.setItem('token',token)
  }catch(error){
    console.log(error)
  }
}




</script>




<div>
  {#if $user$}
    <div>{$user$.displayName}</div>
  {/if}
  <div>로그인하기 </div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <img class="google_img" src="https://w7.pngwing.com/pngs/869/485/png-transparent-google-logo-computer-icons-google-text-logo-google-logo-thumbnail.png" alt="">
    <div>Google로 시작하기 </div>
  </button>
</div>


<style>
  .google_img{
    width: 20px;
  }
  .login-btn{
    height: 50px;
    width: 200px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid gray;
  }
</style>