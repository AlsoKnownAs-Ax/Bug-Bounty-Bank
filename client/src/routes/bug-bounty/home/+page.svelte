<script lang="ts">
    import type { PageData } from './$types';

    let { data }: { data: PageData } = $props();
    
    let balance = "$10,000.00";
    let username = "John Doe";
    
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
            <!-- Vulnerable: Direct HTML injection -->
            <p class="text-3xl font-bold text-green-600">{@html balance}</p>
            <p class="text-gray-600">Welcome back, {@html username}</p>
        </div>

        <!-- Quick Transfer -->
        <div class="bg-white p-6 rounded-lg shadow-md">
            <h3 class="text-lg font-semibold mb-4">Quick Transfer</h3>
            <form onsubmit={handleTransfer}>
                <input type="text" placeholder="Account Number" class="w-full p-2 mb-2 border rounded">
                <input type="number" placeholder="Amount" class="w-full p-2 mb-2 border rounded">
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
                <p>Server: Apache 2.4.1</p>
                <p>Database: MySQL 5.5</p>
            </div>
            <div>
                <h4 class="font-semibold mb-4">Admin</h4>
                <p>Internal Portal: admin.bugbountybank.local</p>
            </div>
        </div>
    </div>
</footer>