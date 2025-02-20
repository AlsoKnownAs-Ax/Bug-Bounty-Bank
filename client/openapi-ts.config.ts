import { defineConfig, defaultPlugins } from '@hey-api/openapi-ts';

export default defineConfig({
	input: {
		exclude: false, // TODO: Exclude auth routes?
		path: 'openapi.json'
	},
	output: {
		format: 'prettier',
		lint: 'eslint',
		path: './src/lib/api'
	},
	experimentalParser: true,
	plugins: [
		...defaultPlugins,
		'@hey-api/client-axios',
		'@hey-api/schemas',
		'zod',
		{
			name: '@hey-api/sdk',
			asClass: true,
			validator: true,
			methodNameBuilder: (operation) => {
				if (!operation.id) return '';
				let name = operation.id;

				//@ts-ignore
				const serviceTag = operation.tags?.[0]?.toLowerCase();
				if (serviceTag) {
					if (name.toLowerCase().startsWith(serviceTag)) {
						name = name.slice(serviceTag.length);
					}
				}
				return name.charAt(0).toLowerCase() + name.slice(1);
			}
		},
		{
			name: '@hey-api/typescript',
			enums: 'javascript'
		},
		{
			name: '@hey-api/transformers',
			dates: true
		}
	]
});
