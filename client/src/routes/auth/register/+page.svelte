<script lang="ts">
	import { enhance } from "$app/forms";

    let email = 'test@example.com';
    let password = 'example1234';
    let confirmPassword = 'example1234';
    let firstName = 'John';
    let lastName = 'Doe';
    let ssn = '';
    let errors: {[key: string]: string} = {};

    function validateForm(event: SubmitEvent) {
        errors = {};
        
        if (!firstName) errors.firstName = 'First name is required';
        if (!lastName) errors.lastName = 'Last name is required';
        if (!email) errors.email = 'Email is required';
        if (!password) errors.password = 'Password is required';
        if (!ssn) errors.ssn = 'Social Security Number is required';
        if (password !== confirmPassword) errors.confirmPassword = 'Passwords do not match';
        if (password.length < 8) errors.password = 'Password must be at least 8 characters';
        
        if (Object.keys(errors).length > 0) {
            event.preventDefault();
            return false;
        }
        
        return true;
    }

    // function handleSubmit(event: Event) {
    //     event.preventDefault();
    //     if (validateForm()) {
    //         // Handle registration logic
    //     }
    // }

    function formatSSN(value: string) {
        // Remove all non-digits
        const cleaned = value.replace(/\D/g, '');
        
        // Format as XXX-XX-XXXX
        if (cleaned.length >= 9) {
            return `${cleaned.slice(0,3)}-${cleaned.slice(3,5)}-${cleaned.slice(5,9)}`;
        }
        return cleaned;
    }

    // Modify the SSN input handler
    function handleSSNInput(event: Event) {
        const input = event.target as HTMLInputElement;
        ssn = formatSSN(input.value);
    }
</script>

<main>
    <div class="max-w-md w-full mx-auto">
        <!-- Logo Section -->
        <div class="text-center mb-8">
            <div class="bg-indigo-600 size-12 rounded-full mx-auto mb-4 flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
            </div>
            <h1 class="text-2xl font-bold text-gray-900">Create Account</h1>
            <p class="mt-2 text-gray-600">Join our secure bug bounty platform</p>
        </div>

        <form
            use:enhance={({ cancel }) => {
                const valid = validateForm(new SubmitEvent('submit'));
                if (!valid) {
                    cancel();
                }
            }} 
            method="POST" 
            action="?/register" 
        >
            <div class="space-y-4">
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label for="first_name" class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
                        <input 
                            bind:value={firstName}
                            type="text" 
                            id="first_name" 
                            name="first_name"
                            class="bg-transparent w-full px-4 py-1.5 border {errors.firstName ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                            placeholder="John"
                        />
                        {#if errors.firstName}
                            <p class="mt-1 text-sm text-red-500">{errors.firstName}</p>
                        {/if}
                    </div>
    
                    <div>
                        <label for="last_name" class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
                        <input 
                            bind:value={lastName}
                            type="text" 
                            id="last_name" 
                            name="last_name"
                            class="bg-transparent w-full px-4 py-1.5 border {errors.lastName ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                            placeholder="Doe"
                        />
                        {#if errors.lastName}
                            <p class="mt-1 text-sm text-red-500">{errors.lastName}</p>
                        {/if}
                    </div>
                </div>
                <div>
                    <label for="ssn" class="block text-sm font-medium text-gray-700 mb-1">Social Security Number</label>
                    <input 
                        bind:value={ssn}
                        type="text" 
                        id="ssn" 
                        name="ssn"
                        class="bg-transparent w-full px-4 py-1.5 border {errors.ssn ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="XXX-XX-XXXX"
                        on:input={handleSSNInput}
                        minlength="11"
                        maxlength="11"
                    />
                    {#if errors.ssn}
                        <p class="mt-1 text-sm text-red-500">{errors.ssn}</p>
                    {/if}
                </div>
                <div>
                    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                    <input 
                        bind:value={email}
                        type="email" 
                        id="email" 
                        name="email"
                        class="bg-transparent w-full px-4 py-1.5 border {errors.email ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
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
                        name="password"
                        class="bg-transparent w-full px-4 py-1.5 border {errors.password ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
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
                        class="bg-transparent w-full px-4 py-1.5 border {errors.confirmPassword ? 'border-red-500' : 'border-gray-300'} rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-colors" 
                        placeholder="••••••••"
                    />
                    {#if errors.confirmPassword}
                        <p class="mt-1 text-sm text-red-500">{errors.confirmPassword}</p>
                    {/if}
                </div>

                <button 
                    type="submit" 
                    class="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors"
                >
                    Create Account
                </button>
            </div>

            <div class="mt-6 text-center">
                <p class="text-sm text-gray-600">
                    Already have an account? 
                    <a href="login" class="font-medium text-indigo-600 hover:text-indigo-500 transition-colors">
                        Sign in
                    </a>
                </p>
            </div>
        </form>
    </div>
</main>