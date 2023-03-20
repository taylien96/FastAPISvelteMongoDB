<script >
  
    import { slide } from 'svelte/transition';

  
    let hidden = true;
    
    const toggleMenu = () => {
      hidden = !hidden;
    };
  
    let user
  
    function clickOutside(node, { enabled: initialEnabled, cb }) {
      const handleOutsideClick = ({ target }) => {
        if (!node.contains(target)) {
          cb();
        }
      };
  
      function update({ enabled }) {
        if (enabled) {
          window.addEventListener('click', handleOutsideClick);
        } else {
          window.removeEventListener('click', handleOutsideClick);
        }
      }
  
      update({ enabled: initialEnabled });
      return {
        update,
        destroy() {
          window.removeEventListener('click', handleOutsideClick);
        }
      };
    }
  </script>

<div class="whole">
<div  use:clickOutside={{ enabled: !hidden, cb: () => (hidden = true) }}>
<button class="outline-none mobile-menu-button pl-8 " on:click={toggleMenu}>
<div id="navMenu" class:active={!hidden}>
<span /><span /><span />
</div>
</button>
</div>
{#if !hidden}
<div
transition:slide
class="md:hidden absolute w-screen mobile-menu border px-8 bg-gray-100 text-gray-700"

>
<ul class="text-center">
  <li>
    <a
      on:click={toggleMenu}
      class="block py-6"
      href="/movies">Movies</a>
  </li>
  <li>
    <a
      on:click={toggleMenu}
      class="block py-6"
      href="/pokemon">Pokemon</a>
  </li>
  {#if user}
      <!-- <button on:click={logout}> -->
    <li>
     <a href="/profile"
     on:click={toggleMenu}
     class="block py-6">Profile</a>
    </li>
    {:else}
      <li >
        <a on:click={toggleMenu}
        class="block py-6"
        href="/">Login</a>
      </li>
    {/if}
    </ul>
  </div>
  {/if}
</div>

<style>
#navMenu > span {
    display: block;
    width: 28px;
    height: 2px;
    border-radius: 9999px;
    background-color: rgb(104, 104, 104);
  }

  #navMenu > span:not(:last-child) {
    margin-bottom: 7px;
  }

  #navMenu,
  #navMenu > span {
    transition: all 0.2s ease-in-out;
  }

  #navMenu.active {
    transition-delay: 0.4s;
    transform: rotate(45deg);
  }
  #navMenu.active > span:nth-child(2) {
    width: 0;
  }

  #navMenu.active > span:nth-child(1),
  #navMenu.active > span:nth-child(3) {
    transition-delay: 0.2s;
  }

  #navMenu.active > span:nth-child(1) {
    transform: translateY(9px);
  }

  #navMenu.active > span:nth-child(3) {
    transform: translateY(-9px) rotate(90deg);
  }




.mobile-menu {
text-align: center;
  position: fixed;
  transform: translateY(100px);
  top: 0;
  left: 0;
  width: 100%;
  height: 35%;
  background-color: rgb(255, 255, 255);
  z-index: 9999;
}

.mobile-menu-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  transition: transform 0.3s ease-in-out;
}

a {
display: block;
padding-top: 1.5rem;
padding-bottom: 1.5rem;
}


</style>