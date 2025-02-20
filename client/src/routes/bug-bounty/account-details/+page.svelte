<script lang="ts">
    import type { PageData } from './$types';

    let { data }: { data: PageData } = $props();
    
    const API_KEY = "sk_live_51NXbsFBE4932gtrPjmk2";

    // Keep existing vulnerable data and functions
    let userDetails = {
        name: [data.currentUser?.first_name, data.currentUser?.last_name].filter(Boolean).join(" "),
        email: data.currentUser?.email,
        ssn: data.currentUser?.ssn,
        iban: data.currentUser?.iban,
        // routingNumber: "987654321",
        balance: data.currentUser?.balance,
        apiKey: API_KEY,    // Secret API key
    };

    function updateProfile(event: Event) {
        event.preventDefault();
        console.log("Updating profile with:", userDetails);
    }

    function exportData() {
        const sensitive = JSON.stringify(userDetails, null, 2);
        const blob = new Blob([sensitive], { type: 'application/json' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        
        // Create filename with timestamp for uniqueness
        const filename = `account-details-${new Date().toISOString().split('T')[0]}.json`;
        
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        
        // Cleanup
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    }
</script>

<div class="min-h-screen bg-gray-50">
    <!-- Breadcrumbs -->
     <!-- TODO: Add shadcn-svelte breadcrumbs -->
    <!-- <div class="container mx-auto px-4 py-3">
        <div class="text-sm breadcrumbs">
            <span class="text-gray-500">Dashboard</span>
            <span class="mx-2">→</span>
            <span class="text-indigo-600">Account Details</span>
        </div>
    </div> -->

    <main class="container mx-auto px-4 py-6">
        <!-- Personal Information Card -->
        <div class="bg-white rounded-lg shadow-lg p-6 mb-6 transform transition-all duration-300 hover:shadow-xl">
            <h2 class="text-2xl font-bold mb-6 text-indigo-600">Personal Information</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="space-y-2">
                    <div class="text-gray-600">Name</div>
                    <p class="text-lg font-medium">{@html userDetails.name}</p>
                </div>
                <div class="space-y-2">
                    <div class="text-gray-600">Email</div>
                    <p class="text-lg font-medium">{@html userDetails.email}</p>
                </div>
                <div class="space-y-2">
                    <div class="text-gray-600">SSN</div>
                    <p class="text-lg font-medium">{userDetails.ssn}</p>
                </div>
            </div>
        </div>

        <!-- Account Details Card -->
        <div class="bg-white rounded-lg shadow-lg p-6 mb-6 transform transition-all duration-300 hover:shadow-xl">
            <h2 class="text-2xl font-bold mb-6 text-indigo-600">Account Details</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="p-4 bg-gray-50 rounded-lg">
                    <div class="text-gray-600 mb-1">IBAN</div>
                    <p class="text-lg font-medium">{userDetails.iban}</p>
                </div>
                <!-- <div class="p-4 bg-gray-50 rounded-lg">
                    <div class="text-gray-600 mb-1">Routing Number</div>
                    <p class="text-lg font-medium">{userDetails.routingNumber}</p>
                </div> -->
                <div class="p-4 bg-gray-50 rounded-lg col-span-2">
                    <div class="text-gray-600 mb-1">Current Balance</div>
                    <p class="text-2xl font-bold text-green-600">{userDetails.balance}</p>
                </div>
            </div>
        </div>

        <!-- Settings Card -->
        <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
            <h2 class="text-2xl font-bold mb-6 text-indigo-600">Account Settings</h2>
            <form onsubmit={updateProfile} class="space-y-6">
                <div class="space-y-2">
                    <label class="text-gray-600" for="password">New Password</label>
                    <input type="password" id="password" 
                        class="bg-transparent w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-transparent">
                </div>
                <div class="space-y-2">
                    <label class="text-gray-600" for="confirm-password">Confirm Password</label>
                    <input type="password" id="confirm-password" 
                        class="bg-transparent w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-transparent">
                </div>
                <button type="submit" 
                    class="w-full bg-indigo-600 text-white py-3 rounded-lg hover:bg-indigo-700 transition-colors duration-200">
                    Update Settings
                </button>
            </form>
        </div>

        <!-- Export Button -->
        <button 
            onclick={exportData}
            class="w-full bg-gray-600 text-white py-3 rounded-lg hover:bg-gray-700 transition-colors duration-200">
            Export Account Data
        </button>
    </main>

    <!-- Hidden sensitive info -->
    <!-- 
        TODO: Remove before production
        API Endpoint: https://api.bugbountybank.com/v1/accounts
        Admin credentials: admin:supersecret
    -->
</div>