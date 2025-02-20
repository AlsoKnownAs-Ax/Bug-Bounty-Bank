// See https://svelte.dev/docs/kit/types#app.d.ts

import type { UserResponse } from '$lib/api';

// for information about these interfaces
declare global {
	namespace App {
		interface Locals {
			user: UserResponse | null;
		}
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export {};
