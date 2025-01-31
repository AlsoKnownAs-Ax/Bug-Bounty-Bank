<script lang="ts">
    import type { Snippet } from 'svelte';
    import type { LayoutData } from './$types';
	import { goto } from '$app/navigation';

    let { data, children }: { data: LayoutData, children: Snippet } = $props();
</script>
<main class="min-h-screen bg-gray-50">
    <!-- Navigation Bar -->
    <nav class="bg-indigo-600 text-white p-4">
        <div class="container mx-auto flex justify-between items-center">
            <a class="text-xl font-bold" href="/bug-bounty/home">Bug Bounty Bank</a>
            <div class="space-x-4">
                <a href="account-details" class="hover:text-gray-200">Account</a>
            </div>
        </div>
    </nav>
    {@render children()}
</main>