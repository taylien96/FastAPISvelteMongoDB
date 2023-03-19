<script>
    import Navbar from "../lib/navbar.svelte";
    import Login from "../lib/login.svelte";
    import { page } from '$app/stores';  
    
    let notSignedIn = true
</script>

<Navbar />
{#if notSignedIn && $page.url.pathname=='/'}
<Login title={"Log in:"} />
{:else if notSignedIn}
<Login title={"You must log to view:"} />
{:else}
<slot></slot>
{/if}
