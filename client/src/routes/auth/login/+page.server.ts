import { AuthService, type RegisterRequest, type UserResponse } from '$lib/api';
import { zLoginRequest } from '$lib/api/zod.gen';
import { fail, redirect, type Actions } from '@sveltejs/kit';

export const actions: Actions = {
	login: async ({ request, cookies, locals }) => {
		const formData = Object.fromEntries(await request.formData());
		const validateForm = zLoginRequest.safeParse(formData);

		if (!validateForm.success) {
			console.log('validateForm.error: ', validateForm.error);
			return { error: validateForm.error.message };
		}

		// Flagged: No admin login
		if (
			validateForm.data.email === 'admin@bugbountybank.com' &&
			validateForm.data.password === 'password'
		) {
			return {
				redirect: '/bug-bounty/home?admin=true',
				message: 'Login successful (Admin Priviliges)'
			};
		}

		const { data, error } = await AuthService.loginUser({
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

		return {
			type: 'success',
			redirect: '/bug-bounty/home',
			message: 'Login successful'
		};
	}
};
