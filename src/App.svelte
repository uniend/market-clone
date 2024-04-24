
<script>
  import Router from 'svelte-spa-router'

  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import NotFound from './pages/NotFound.svelte';
  import './css/style.css'
  import { GoogleAuthProvider, getAuth, signInWithCredential } from "firebase/auth";
  import { user$ } from './store';
  import { onMount } from 'svelte';
  import Loding from './pages/loding.svelte';
  import Mypage from './pages/Mypage.svelte';


  const auth = getAuth();

  let isloding = true;

  const checkLogin = async () => {
  const token = localStorage.getItem('token');
  if (!token) return (isloding = false);

  const credential = GoogleAuthProvider.credential(null, token);
  const result = await signInWithCredential(auth, credential)
  const user = result.user;
  user$.set(user);
  isloding = false;
  }


  const routes = {
    '/' : Main,
    '/Signup' : Signup,
    '/Write' :  Write,
    '/my' : Mypage,
    '*' : NotFound

  }

  onMount(()=> checkLogin())
</script>

<body>
  {#if isloding}
    <Loding/>
  {:else if !$user$}
    <Login/>
  {:else}
  <Router {routes}/>
  {/if}
</body>

<style>

</style>
