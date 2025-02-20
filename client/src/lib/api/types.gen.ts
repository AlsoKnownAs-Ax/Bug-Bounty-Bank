// This file is auto-generated by @hey-api/openapi-ts

export type HttpValidationError = {
	detail?: Array<ValidationError>;
};

export type LoginRequest = {
	email: string;
	password: string;
};

export type LoginResponse = {
	user: UserResponse;
};

export type RegisterRequest = {
	email: string;
	password: string;
	first_name: string;
	last_name: string;
	ssn: string;
	iban: string;
};

export type RegisterResponse = {
	user: UserResponse;
};

export type UserResponse = {
	id: number;
	email: string;
	is_admin: boolean;
	first_name: string;
	last_name: string;
	ssn: string;
	balance: number;
	iban: string;
};

export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};

export type AuthLoginUserData = {
	body: LoginRequest;
	path?: never;
	query?: never;
	url: '/api/v0/auth/login';
};

export type AuthLoginUserErrors = {
	/**
	 * Validation Error
	 */
	422: HttpValidationError;
};

export type AuthLoginUserError = AuthLoginUserErrors[keyof AuthLoginUserErrors];

export type AuthLoginUserResponses = {
	/**
	 * Successful Response
	 */
	200: LoginResponse;
};

export type AuthLoginUserResponse = AuthLoginUserResponses[keyof AuthLoginUserResponses];

export type AuthRegisterUserData = {
	body: RegisterRequest;
	path?: never;
	query?: never;
	url: '/api/v0/auth/register';
};

export type AuthRegisterUserErrors = {
	/**
	 * Validation Error
	 */
	422: HttpValidationError;
};

export type AuthRegisterUserError = AuthRegisterUserErrors[keyof AuthRegisterUserErrors];

export type AuthRegisterUserResponses = {
	/**
	 * Successful Response
	 */
	201: RegisterResponse;
};

export type AuthRegisterUserResponse = AuthRegisterUserResponses[keyof AuthRegisterUserResponses];

export type DefaultHealthCheckData = {
	body?: never;
	path?: never;
	query?: never;
	url: '/api/v0/';
};

export type DefaultHealthCheckResponses = {
	/**
	 * Successful Response
	 */
	200: unknown;
};

export type ClientOptions = {
	baseURL: `${string}://openapi.json` | (string & {});
};
