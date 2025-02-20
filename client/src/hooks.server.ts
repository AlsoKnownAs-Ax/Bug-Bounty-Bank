import { client } from '$lib/api/client.gen';

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/';

client.setConfig({
	baseURL: BASE_URL,
	withCredentials: true
});

// import type { Handle } from '@sveltejs/kit';

// export const handle: Handle = async ({ event, resolve }) => {
// 	const response = await resolve(event);

//     // Flagged: No token verification

// 	return response;
// };
