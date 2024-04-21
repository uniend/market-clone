
<script>
  import Router from 'svelte-spa-router'

  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import NotFound from './pages/NotFound.svelte';
  import './css/style.css'



  const routes = {
    '/' : Main,
    '/login' : Login,
    '/Signup' : Signup,
    '/Write' :  Write,
    '*' : NotFound

  }
</script>

<body>
  <Router {routes}/>
</body>

<style>

</style>
