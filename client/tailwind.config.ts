import forms from '@tailwindcss/forms';
import type { Config } from 'tailwindcss';

export default {
	content: [
		'./src/**/*.{svelte,js,ts}',
		'./src/routes/**/*.{svelte,js,ts}',
		'./src/lib/**/*.{svelte,js,ts}'
	],

	theme: {
		extend: {}
	},

	plugins: [forms]
} satisfies Config;
