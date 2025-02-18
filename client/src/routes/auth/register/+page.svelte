<script lang="ts">
    import { goto } from "$app/navigation";

    let email = '';
    let password = '';
    let confirmPassword = '';
    let errors: {[key: string]: string} = {};

    function validateForm() {
        errors = {};
        
        if (!email) errors.email = 'Email is required';
        if (!password) errors.password = 'Password is required';
        if (password !== confirmPassword) errors.confirmPassword = 'Passwords do not match';
        if (password.length < 8) errors.password = 'Password must be at least 8 characters';
        
        return Object.keys(errors).length === 0;
    }

    function handleSubmit(event: Event) {
        event.preventDefault();
        if (validateForm()) {
            // Handle registration logic
        }
    }
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
            <h1 class="text-3xl font-bold text-gray-900">Create Account</h1>
            <p class="mt-2 text-gray-600">Join our secure bug bounty platform</p>
        </div>

        <form on:submit={handleSubmit}>
            <div class="space-y-6">
                <div>
                    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                    <input 
                        bind:value={email}
                        type="email" 
                        id="email" 
                        class="w-full px-4 py-2 border {errors.email ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="you@example.com"
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
                        class="w-full px-4 py-2 border {errors.password ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="••••••••"
                    />
                    {#if errors.password}
                        <p class="mt-1 text-sm text-red-500">{errors.password}</p>
                    {/if}
                </div>

                <div>
                    <label for="confirm_password" class="block text-sm font-medium text-gray-700 mb-1">Confirm Password</label>
                    <input 
                        bind:value={confirmPassword}
                        type="password" 
                        id="confirm_password" 
                        class="w-full px-4 py-2 border {errors.confirmPassword ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="••••••••"
                    />
                    {#if errors.confirmPassword}
                        <p class="mt-1 text-sm text-red-500">{errors.confirmPassword}</p>
                    {/if}
                </div>

                <button 
                    type="submit" 
                    class="w-full bg-indigo-600 text-white py-3 px-4 rounded-lg font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors"
                >
                    Create Account
                </button>
            </div>

            <div class="mt-6 text-center">
                <p class="text-sm text-gray-600">
                    Already have an account? 
                    <a href="/auth/login" class="font-medium text-indigo-600 hover:text-indigo-500 transition-colors">
                        Sign in
                    </a>
                </p>
            </div>
        </form>
    </div>
</main>