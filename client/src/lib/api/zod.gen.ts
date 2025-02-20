// This file is auto-generated by @hey-api/openapi-ts

import { z } from 'zod';

export const zHttpValidationError = z.object({
	detail: z
		.array(
			z.object({
				loc: z.array(z.unknown()),
				msg: z.string(),
				type: z.string()
			})
		)
		.optional()
});

export const zLoginRequest = z.object({
	email: z.string(),
	password: z.string()
});

export const zLoginResponse = z.object({
	user: z.object({
		id: z.number().int(),
		email: z.string(),
		is_admin: z.boolean(),
		first_name: z.string(),
		last_name: z.string(),
		ssn: z.string(),
		balance: z.number(),
		iban: z.string()
	})
});

export const zRegisterRequest = z.object({
	email: z.string(),
	password: z.string(),
	first_name: z.string(),
	last_name: z.string(),
	ssn: z.string(),
	iban: z.string()
});

export const zRegisterResponse = z.object({
	user: z.object({
		id: z.number().int(),
		email: z.string(),
		is_admin: z.boolean(),
		first_name: z.string(),
		last_name: z.string(),
		ssn: z.string(),
		balance: z.number(),
		iban: z.string()
	})
});

export const zUserResponse = z.object({
	id: z.number().int(),
	email: z.string(),
	is_admin: z.boolean(),
	first_name: z.string(),
	last_name: z.string(),
	ssn: z.string(),
	balance: z.number(),
	iban: z.string()
});

export const zValidationError = z.object({
	loc: z.array(z.unknown()),
	msg: z.string(),
	type: z.string()
});

export const zAuthLoginUserResponse = zLoginResponse;

export const zAuthRegisterUserResponse = zRegisterResponse;
