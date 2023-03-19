<script context="module">
    
let viewportW
</script>
<svelte:window bind:scrollY={viewportW}/>

<nav>
    <a href="/" class="logo">
      <div class="img-wrapper">
        <img src="https://cdn1.iconfinder.com/data/icons/seo-128/48/19-512.png" alt="Logo"/>
    </div>   
      Home
    </a>
    {#if viewportW >= 500}
    <ul>
      <li><a href="/movies">Movies</a></li>
      <li><a href="/pokemon">Pokemon</a></li>
      <li><a href="/profile">Profile</a></li>
    </ul>
    {:else}
    <div class="dropdown">
        <button class="dropbtn hover:text-rose-500">
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
            <li><a href="/movies">Movies</a></li>
            <li><a href="/pokemon">Pokemon</a></li>
            <li><a href="/profile">Profile</a>
        </div>
      </div>
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


    .dropdown {
  float: left;
  overflow: hidden;
}

/* Dropdown button */
.dropdown .dropbtn {
  font-size: 0.875rem;
line-height: 1.25rem;
text-decoration: inherit;
  font-weight: 500;/* Important for vertical align on mobile phones */
  margin: 0; /* Important for vertical align on mobile phones */
}

/* Add a red background color to navbar links on hover */
.dropdown a:hover, .dropdown:hover .dropbtn {
  background-color: rgb(255, 255, 255);
  color: #ff4561;
}

/* Dropdown content (hidden by default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

/* Show the dropdown menu on hover */

  </style>
  