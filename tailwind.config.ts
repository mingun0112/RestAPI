import type { Config } from 'tailwindcss';
import flowbitePlugin from 'flowbite/plugin'

export default {
	content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],
	darkMode: 'selector',

	theme: {
		extend: {}
	},

	plugins: [
		flowbitePlugin
		
	]
} satisfies Config;