<script>
	import { goto } from "$app/navigation";
    import { userStore } from "$lib/store"; // store.ts에서 가져오기
    import { get } from "svelte/store";
    // import { env } from '$env/dynamic/private'; 

    
    let request_url = `https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=fzRHVgebnWqa3C2URcN8&redirect_uri=http://localhost:5173/naverLoginAPI`;
    
    let email = "";
    let password = "";
    let loginMessage = "";

    // console.log(request_url)
    

    async function handleLogin(event) {
        event.preventDefault();

        try {
        const response = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.user);

            userStore.set(data.user);
            console.log(get(userStore))
            goto('/naverLoginAPI')


            loginMessage = data.message; // 로그인 성공 메시지
            
        } else {
            const error = await response.json();
            loginMessage = error.detail; // 에러 메시지
        }
        } catch (error) {
        loginMessage = "로그인 요청 중 오류가 발생했습니다.";
        }
    }
    
</script>
  
  <main>
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
            <h2 class="mt-10 text-center text-2xl/10 font-bold tracking-tight text-indigo-600">
                고급프로그래밍실습
              </h2>
          <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
            REST API를 이용한 로그인 기능
          </h2>
        </div>

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form action="#" on:submit={handleLogin} method="POST" class="space-y-6">
            <div>
              <label htmlFor="email" class="block text-sm/6 font-medium text-gray-900">
                Email address
              </label>
              <div class="mt-2">
                <input
                  id="email"
                  name="email"
                  type="email"
                  required
                  autoComplete="email"
                  bind:value={email}

                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div>
              <div class="flex items-center justify-between">
                <label htmlFor="password" class="block text-sm/6 font-medium text-gray-900">
                  Password
                </label>
                <div class="text-sm">
                  <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">
                    Forgot password?
                  </a>
                </div>
              </div>
              <div class="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  required
                  autoComplete="current-password"
                  bind:value={password}

                  class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                />
              </div>
            </div>

            <div>
              <button
                type="submit"
                class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                로그인
              </button>
            </div>
            
          </form>
          <div class="mt-4 text-center text-sm text-gray-700">
            {#if loginMessage}
              <p>{loginMessage}</p>
            {/if}
          </div>
          <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
          <h2 class="text-center text-l font-bold tracking-tight text-gray-900">
            네이버 로그인 API
          </h2>
          <a href={request_url}>
          <div class="mt-3 w-full flex items-center justify-center  bg-[#03c75a] rounded">
            
            <button
              type="submit"
            >
            <img class="h-[35px]" src="../naver_login_logo.png" alt="Naver Login" />
            </button>
          </div>
        </a>

        <div>

          </div>
          <p class="mt-10 text-center text-sm/6 text-gray-500">
            Not a member?{' '}
            <a href="/registerPage" class="font-semibold text-indigo-600 hover:text-indigo-500">
              Register
            </a>
          </p>
        </div>
      </div>
    
  </main>
  