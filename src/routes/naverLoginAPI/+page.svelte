<script>
import { onMount } from 'svelte';
import { userStore } from "$lib/store";
import { get } from 'svelte/store';


  let user = null;

  const unsubscribe = userStore.subscribe((value) => {
    user = value;
  });

let profileData = null;

onMount(async () => {
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');

  if (code) {
    const response = await fetch(`http://localhost:8000/callback?code=${code}`);
    const data = await response.json();
    profileData = data;
    console.log(profileData)
    
    userStore.set(profileData.response)
    console.log(get(userStore))
  }
});
</script>

<main>
    {#if user}
      <p>환영합니다, {user.name}님!</p>
      <p>이메일: {user.email}</p>
      <p>생년월일: {user.birthyear}-{user.birthday}</p>
    {:else}
      <p>로그인되지 않았습니다.</p>
    {/if}
  </main>