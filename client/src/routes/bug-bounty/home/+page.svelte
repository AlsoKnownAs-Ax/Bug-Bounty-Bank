<script lang="ts">
    import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Separator } from '$lib/components/ui/separator';
    import type { PageData } from './$types';

    let { data }: { data: PageData } = $props();

    const isAdmin = data.isAdmin;    
    const balance = data.currentUser?.balance;
    const username = [data.currentUser?.first_name, data.currentUser?.last_name].filter(Boolean).join(" ");
    const iban = data.currentUser?.iban;
    const ssn = data.currentUser?.ssn;

    let transactions = [
        { id: 1, date: "2024-03-20", description: "Salary Deposit", amount: "+$5,000.00" },
        { id: 2, date: "2024-03-19", description: "Shopping", amount: "-$150.00" },
        { id: 3, date: "2024-03-18", description: "Transfer", amount: "-$500.00" }
    ];

    // Vulnerable quick transfer function
    function handleTransfer(event: Event) {
        event.preventDefault();
        console.log("Transfer initiated"); // Logs sensitive data
    }
</script>



<!-- Hero Section -->
<section class="bg-white py-12">
    <div class="container mx-auto px-4">
        <div class="text-center">
            <h2 class="text-4xl font-bold text-gray-800 mb-4">Welcome to Bug Bounty Bank</h2>
            <p class="text-xl text-gray-600">The most trusted bank in financial services</p>
        </div>
    </div>
</section>

<!-- Account Overview -->
<section class="container mx-auto px-4 py-8">
    <div class="grid md:grid-cols-2 gap-6">
        <!-- Balance Card -->
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-lg font-semibold mb-2">Account Balance</h3>
            <p class="text-3xl font-bold text-green-600">{balance}</p>
            <p class="text-gray-600 mb-3">Welcome back, {username}</p>
            <Separator />
            <div class="space-y-4">
                <div class="pt-3">
                    <p class="text-sm text-gray-500">IBAN</p>
                    <p class="font-mono text-gray-700">{iban}</p>
                </div>
                <div>
                    <p class="text-sm text-gray-500">Social Security Number</p>
                    <p class="font-mono text-gray-700 group relative cursor-help">
                        <span class="inline-block">XXX-XX-{ssn?.slice(-4) ?? '****'}</span>
                        <span class="absolute left-0 -top-8 bg-gray-900 text-white px-2 py-1 rounded text-sm opacity-0 group-hover:opacity-100 transition-opacity duration-200">
                            {ssn ?? 'Not available'}
                        </span>
                    </p>
                </div>
            </div>
        </div>

        <!-- Quick Transfer -->
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-lg font-semibold mb-4">Quick Transfer</h3>
            <form onsubmit={handleTransfer} class="space-y-4">
                {#if isAdmin}
                    <div>
                        <Label for="fromAccount" class="text-gray-600">From Account (Admin)</Label>
                        <Input type="text" id="fromAccount" placeholder="Account Number" class="bg-transparent w-full p-2 mb-2 border rounded" />
                        <p class="text-muted-foreground text-sm">Please specify the source account for the transfer</p>
                    </div>
                {/if}
                <Input type="text" placeholder="Account Number" class="bg-transparent w-full p-2 mb-2 border rounded" />
                <Input type="number" placeholder="Amount" class="[appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none bg-transparent w-full p-2 mb-2 border rounded" />
                <button type="submit" class="w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-700">
                    Transfer
                </button>
            </form>
        </div>
    </div>
</section>

<!-- Transactions -->
<section class="container mx-auto px-4 py-8">
    <h3 class="text-xl font-semibold mb-4">Recent Transactions</h3>
    <div class="bg-white rounded-lg shadow-md overflow-hidden">
        <table class="w-full">
            <thead class="bg-gray-50">
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Date</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Description</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Amount</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
                {#each transactions as transaction}
                    <tr>
                        <td class="px-6 py-4 whitespace-nowrap">{transaction.date}</td>
                        <td class="px-6 py-4">{transaction.description}</td>
                        <td class="px-6 py-4">{transaction.amount}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</section>

<!-- Footer with sensitive information -->
<footer class="bg-gray-800 text-white py-8 mt-12">
    <div class="container mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div>
                <h4 class="font-semibold mb-4">Contact</h4>
                <p>Email: admin@bugbountybank.com</p>
                <p>Phone: (555) 123-4567</p>
            </div>
            <div>
                <h4 class="font-semibold mb-4">Technical Info</h4>
                <p>Server: Raspberry pi</p>
                <p>Database: SQLite 3.37.1</p>
            </div>
            <div>
                <h4 class="font-semibold mb-4">Admin</h4>
                <p>Internal Portal: Soon</p>
            </div>
        </div>
    </div>
</footer>