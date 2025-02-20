<script lang="ts">
	import { enhance } from "$app/forms";
    import { goto } from "$app/navigation";
	import { formEnhance } from "$lib/core/formEnhance";
	import { toast } from "svelte-sonner";

    let email = '';
    let password = '';
    let errors: {[key: string]: string} = {};
</script>

<main>
    <div class="max-w-md w-full mx-auto">
        <!-- Logo Section -->
        <div class="text-center mb-8">
            <div class="bg-indigo-600 w-16 h-16 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
            </div>
            <h1 class="text-3xl font-bold text-gray-900">Welcome Back</h1>
            <p class="mt-2 text-gray-600">Sign in to your account</p>
        </div>

        <form 
            use:enhance={formEnhance}
            method="POST" 
            action="?/login" 
        >
            <div class="space-y-6">
                <div>
                    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                    <input 
                        bind:value={email}
                        type="text" 
                        id="email" 
                        name="email"
                        class="bg-transparent w-full px-4 py-2 border {errors.email ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="Enter your Email"
                    />
                    {#if errors.email}
                        <p class="mt-1 text-sm text-red-500">{errors.email}</p>
                    {/if}
                </div>

                <div>
                    <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
                    <input 
                        bind:value={password}
                        type="password" 
                        id="password" 
                        name="password"
                        class="bg-transparent w-full px-4 py-2 border {errors.password ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="••••••••"
                    />
                    {#if errors.password}
                        <p class="mt-1 text-sm text-red-500">{errors.password}</p>
                    {/if}
                </div>

                <!-- <div class="flex items-center justify-between flex-col">
                    <div class="flex items-center">
                        <input id="remember" type="checkbox" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded">
                        <label for="remember" class="ml-2 block text-sm text-gray-700">Remember me</label>
                    </div>
                    <a href="/auth/forgot-password" class="text-sm font-medium text-indigo-600 hover:text-indigo-500">
                        Forgot password?
                    </a>
                </div> -->

                <button 
                    type="submit" 
                    class="w-full bg-indigo-600 text-white py-3 px-4 rounded-lg font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors"
                >
                    Sign In
                </button>
            </div>

            <div class="mt-6 text-center">
                <p class="text-sm text-gray-600">
                    Don't have an account? 
                    <a href="register" class="font-medium text-indigo-600 hover:text-indigo-500 transition-colors">
                        Create one
                    </a>
                </p>
            </div>
        </form>
    </div>
</main>