import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		cors: {
			origin: "https://openapi.naver.com/v1/nid/me",
			credentials: true,

		  },
		}
});
