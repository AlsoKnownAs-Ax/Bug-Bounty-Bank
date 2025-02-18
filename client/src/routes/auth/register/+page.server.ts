import type { Actions } from '@sveltejs/kit';

export const actions: Actions = {
	register: async ({ request, cookies }) => {
		const formData = Object.fromEntries(await request.formData());
		console.log('server action triggered');
		console.log('formData: ', formData);
	}
};
