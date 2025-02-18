<script lang="ts">
    import type { Snippet } from 'svelte';
    import type { LayoutData } from './$types';
    import { fade } from 'svelte/transition';
    import { page } from '$app/state';

    let { data, children }: { data: LayoutData, children: Snippet } = $props();
</script>

<div class="fixed inset-0 overflow-hidden">
    <main class="relative min-h-screen w-screen flex justify-center items-center py-8">
        <img 
            class="fixed inset-0 w-full h-full object-cover -z-10" 
            src="https://images.unsplash.com/photo-1669251921941-ae3645715017?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" 
            alt=""
        />
        <div class="w-full max-w-md mx-auto px-4">
            <div 
                class="relative bg-white shadow-xl rounded-lg px-8 pt-6 pb-8 mb-4 border border-gray-100"
            >
                {@render children()}
            </div>
        </div>
    </main>
</div>