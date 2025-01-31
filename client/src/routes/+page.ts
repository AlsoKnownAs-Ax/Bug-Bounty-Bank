import type { PageLoad } from './$types';
import { goto } from '$app/navigation';
import { redirect } from '@sveltejs/kit';

export const load = (async () => {
	throw redirect(302, '/login');
}) satisfies PageLoad;
