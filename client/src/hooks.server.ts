import { AuthService } from '$lib/api';
import { client } from '$lib/api/client.gen';
import type { Handle } from '@sveltejs/kit';

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/';

client.setConfig({
	baseURL: BASE_URL,
	withCredentials: true
});

export const handle: Handle = async ({ event, resolve }) => {
	// Flagged: No token verification
	const email = event.cookies.get('email');

	if (email) {
		const { data, error } = await AuthService.getCurrentUser({
			body: { email }
		});

		console.log('data: ', data);
		console.log('error: ', error);

		if (!error) {
			event.locals.user = data?.user || null;
		}
	}

	console.log('event.locals.user: ', event.locals.user);

	const response = await resolve(event);

	return response;
};
