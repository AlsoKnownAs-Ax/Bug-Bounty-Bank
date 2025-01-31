<script lang="ts">
	import { goto } from "$app/navigation";

    let username = '';
    let password = '';

    function handleSubmit(event: Event) {
        event.preventDefault();
        // Vulnerability: Logging sensitive information
        console.log(`------------------- LOGS -------------------`);
        console.log(`Username: ${username}, Password: ${password}`);
        console.log(`------------------- LOGS -------------------`);
        // Vulnerability: Insecure authentication logic
        if (username === 'admin' && password === 'password') {
            alert('Login successful');
            goto('/bug-bounty/home')
        } else {
            alert('Invalid credentials');
        }
    }
</script>

<h1 class="text-2xl font-bold text-center my-4">Login</h1>
<form on:submit={handleSubmit} class="max-w-md mx-auto p-6 border border-gray-300 rounded-lg bg-white shadow-md">
    <div class="mb-4">
        <label for="username" class="block text-sm font-medium text-gray-700">Username:</label>
        <input type="text" id="username" bind:value={username} class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" />
    </div>
    <div class="mb-4">
        <label for="password" class="block text-sm font-medium text-gray-700">Password:</label>
        <input type="password" id="password" bind:value={password} class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" />
    </div>
    <button type="submit" class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Login</button>
    <p class="text-sm mt-10 text-center">Not having an account? <a href="/register" class="text-blue-500">Register now</a></p>

</form>