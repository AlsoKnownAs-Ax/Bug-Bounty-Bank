import { AuthService, type RegisterRequest, type UserResponse } from '$lib/api';
import { zRegisterRequest } from '$lib/api/zod.gen';
import { fail, redirect, type Actions } from '@sveltejs/kit';

export const actions: Actions = {
	register: async ({ request, cookies, locals }) => {
		const formData = Object.fromEntries(await request.formData());
		const validateForm = zRegisterRequest.safeParse(formData);

		if (!validateForm.success) {
			console.log('validateForm.error: ', validateForm.error);
			return { error: validateForm.error.message };
		}

		const { data, error } = await AuthService.registerUser({
			body: validateForm.data
		});

		if (error) return fail(400, { error: error.detail });

		cookies.set('email', data.user.email, {
			path: '/',
			httpOnly: true,
			// secure: !dev, # Flagged: No secure cookie
			sameSite: 'strict',
			maxAge: 60 * 60 * 24 * 7 // 1 week
		});

		throw redirect(303, '/bug-bounty/home');
	}
};
