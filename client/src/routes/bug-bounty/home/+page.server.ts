import type { PageServerLoad } from './$types';

export const load = (async ({ url }) => {
	return {
		isAdmin: url.searchParams.get('admin') === 'true'
	};
}) satisfies PageServerLoad;
