<script>
	import { goto } from '$app/navigation';
    import { Datepicker } from 'flowbite-svelte';

    export let profileData = {
      name: "",
      email: "",
      birthday: "",
      birthyear: "",
      gender: "",
      mobile: "",
      password: ""
    };
  
    let selectedDate = null;

    const register = async () => {
      if (selectedDate) {
        const year = selectedDate.getFullYear();
        const month = String(selectedDate.getMonth() + 1).padStart(2, "0"); 
        const day = String(selectedDate.getDate()).padStart(2, "0");
  
        profileData.birthyear = year.toString();
        profileData.birthday = `${month}-${day}`;
      }

      try {
      const response = await fetch("http://localhost:8000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(profileData)
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      console.log("등록 성공:", result);
      alert("회원가입 성공!");
      goto('/');
    } catch (error) {
      console.error("에러 발생:", error);
      alert("회원가입 중 문제가 발생했습니다.");
    }
  
      console.log(profileData);
    };
  </script>
  
  
  <div class="bg-gray-50 dark:bg-gray-900">
      <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
          <a href="/" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
            <h2 class="mt-10 text-center text-2xl/10 font-bold tracking-tight text-indigo-600">
                고급프로그래밍실습
              </h2>
          </a>
          <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
              <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                  <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                      회원 가입
                  </h1>
                  <form class="space-y-4 md:space-y-6" action="#">
                      <div>
                          <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">이름</label>
                          <input type="text" name="name" id="name" bind:value={profileData.name} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="이름을 입력하세요" required>
                      </div>
                      <div>
                          <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">이메일</label>
                          <input type="email" autoComplete="email" name="email" id="email" bind:value={profileData.email} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="이메일을 입력하세요" required>
                      </div>

                      <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">비밀번호</label>
                        <input type="password" name="password" id="password" bind:value={profileData.password} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="비밀번호를 입력하세요" required>
                    </div>
                      <div>
                          <label for="birthday" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">생일</label>
                          <div class="relative max-w-sm">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                              <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                              </svg>
                            </div>
                            <!-- <input datepicker id="default-datepicker" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Select date"> -->
                            <Datepicker bind:value={selectedDate} />
                        </div>
                      </div>
  
                      <div>
                          <label for="gender" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">성별</label>
                          <!-- <input type="text" name="gender" id="gender" bind:value={profileData.gender} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="성별을 입력하세요" required> -->
                          <div >
                            <label class="inline-flex items-center text-sm">
                              <input bind:group={profileData.gender} type="radio" class="form-radio" name="accountType" value="M">
                              <span class="ml-2">Man</span>
                            </label>
                            <label class="inline-flex items-center ml-6 text-sm">
                              <input bind:group={profileData.gender} type="radio" class="form-radio" name="accountType" value="W">
                              <span class="ml-2">Woman</span>
                            </label>
                          </div>
                        </div>

  
                      <div>
                          <label for="mobile" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">전화 번호</label>
                          <input type="text" name="mobile" id="mobile" bind:value={profileData.mobile} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="번호를 입력하세요" required>
                      </div>
  
                     
                      <button 
                      type="button"
                      class="w-full text-indigo-600 bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                      on:click={register}
                    >
                      Register
                    </button>
                      
                    </form>
              </div>
          </div>
      </div>
  </div>
  