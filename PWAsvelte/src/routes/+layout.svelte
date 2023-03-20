<script>
    import Navbar from "../lib/navbar.svelte";
    import Login from "../lib/login.svelte";
    import { page } from '$app/stores';  
    import { loggedIn } from './Store.js'
    let notSignedIn
    loggedIn.subscribe(value => {
		notSignedIn = value;
	});
</script>

<Navbar />
{#if !notSignedIn && $page.url.pathname=='/'}
<Login title={"Log in:"} />
{:else if !notSignedIn}
<Login title={"You must log to view:"} />
{:else}
<slot></slot>
{/if}
