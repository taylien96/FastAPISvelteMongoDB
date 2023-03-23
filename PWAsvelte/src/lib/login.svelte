<script>
    export let title = "Login";
    import { loggedIn } from '../routes/Store.js'
    let username = "";
    let password = "";
  
    function handleSubmit() {
      onSubmit(username, password );
      username = "";
      password = "";
    }
    async function onSubmit(u, p){
        try{
        let login = await fetch(url, {method: 'POST', headers: {
        'Content-Type': 'application/json'
        },
        body: 
        JSON.stringify({ username, password })
        })
        console.log(login)
        
        }catch(error){
            console.log(error)
        }
    }
  </script>



    <div class="login-box">
      <div class="login-box-header">
        <h2>{title}</h2>
      </div>
      <form on:submit|preventDefault={handleSubmit}>
        <div class="login-box-body">
          <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" bind:value={username}>
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" bind:value={password}>
          </div>
          <button type="submit">Submit</button>
          <button class="sign-up">Sign up</button>
        </div>
      </form>
    </div>

  
  
  
  <style>
    .login-box {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 400px;
      border: 1px solid #ccc;
      background-color: #f2f2f2;
    }
  
    .login-box-header {
      padding: 10px;
      background-color: #333;
      color: #fff;
      text-align: center;
    }
  
    h2 {
      margin-top: 0;
    }
  
    .login-box-body {
      padding: 20px;
    }
  
    .form-group {
      margin-bottom: 10px;
    }
  
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
  
    input[type="text"],
    input[type="password"] {
      width: 100%;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 3px;
    }
    .sign-up {
        align-self: self-end;
        border: #333 solid 1px;
        color: #333;
        background-color: transparent;
    }
    button {
      background-color: #333;
      color: #fff;
      padding: 5px 10px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
    }
  
    button:hover {
      background-color: #444;
    }
  </style>
  