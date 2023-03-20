<script>
    import MobileDropdown from "./mobileDropdown.svelte";
    let innerWidth = 0
    $: condition =innerWidth

</script>
<svelte:window bind:innerWidth/>

<nav>
    <a href="/" class="logo">
      <div class="img-wrapper">
        <img src="https://cdn1.iconfinder.com/data/icons/seo-128/48/19-512.png" alt="Logo"/>
    </div>   
      Home
    </a>
    {#if condition >= 500}
    <ul>
      <li><a href="/movies">Movies</a></li>
      <li><a href="/pokemon">Pokemon</a></li>
      <li><a href="/profile">Profile</a></li>
    </ul>
   {:else}
   <MobileDropdown/>
    {/if}
  </nav>
  
  <style>
    nav {
      background-color: rgb(150, 150, 150);
      color: #fff;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 10px; 
      font-size: larger;
    }
  
    .logo {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: #fff;
    }
    .img-wrapper{
    max-height: 50px;
    overflow: hidden;
    }

    .img-wrapper img{
    height: 100px;
    margin-right: 10px;
    overflow: hidden;
    transform: translate(0px, -25px);
    }
  
    ul {
      display: flex;
      list-style: none;
      margin: 0;
      padding: 0;
    }
  
    li {
      margin-right: 10px;
    }
  
    a {
      color: #fff;
      text-decoration: none;
    }
  
    a:hover {
      text-decoration: underline;
    }
  
    /* Shift the links to the right */
    ul {
      margin-left: auto;
    }



  </style>
  