# Security Vulnerabilities

## OWASP Top 10 2025 Coverage:

1. [A1:2025-Broken Access Control](https://owasp.org/www-project-top-ten/2025/A1_2025-Broken_Access_Control)

   - Admin privileges on URL params
   - Insecure Direct Object Reference (IDOR)

2. [A2:2025-Cryptographic Failures](https://owasp.org/www-project-top-ten/2025/A2_2025-Cryptographic_Failures)

   - Unhashed password storage
   - Sensitive data exposure in logs
   - Sensitive information display

3. [A3:2025-Injection](https://owasp.org/www-project-top-ten/2025/A3_2025-Injection)

   - Cross-site scripting (XSS)
   - Insecure data export

4. [A4:2025-Insecure Design](https://owasp.org/www-project-top-ten/2025/A4_2025-Insecure_Design)

   - Exposed API keys
   - Lack of rate limiting

5. [A7:2025-Identification and Authentication Failures](https://owasp.org/www-project-top-ten/2025/A7_2025-Identification_and_Authentication_Failures)

   - Client-side security controls
   - Weak password requirements

6. [A9:2025-Security Logging and Monitoring Failures](https://owasp.org/www-project-top-ten/2025/A9_2025-Security_Logging_and_Monitoring_Failures)
   - Insufficient logging
   - No audit trail for sensitive operations

Total vulnerabilities listed: 12

## 1. Unhashed Password Storage

**Category:** [OWASP A2:2025-Cryptographic Failures](https://owasp.org/www-project-top-ten/2025/A2_2025-Cryptographic_Failures)

**File:** `server/src/modules/user/user_service.py`

```python
# ...existing code...
def create_user(self, user_create: RegisterRequest) -> User:
    new_user = User.model_validate(user_create)
    # ...existing code...
```

## 2. Sensitive Data Exposure in Logs

**Category:** [OWASP A2:2025-Cryptographic Failures](https://owasp.org/www-project-top-ten/2025/A2_2025-Cryptographic_Failures)

**File:** `client/src/routes/bug-bounty/home/+page.svelte`

```ts
// ...existing code...
function handleTransfer(event: Event) {
  event.preventDefault();
  console.log("Transfer initiated"); // Logs sensitive data
}
// ...existing code...
```

## 3. Insecure Direct Object Reference (IDOR)

**Category:** [OWASP A1:2025-Broken Access Control](https://owasp.org/www-project-top-ten/2025/A1_2025-Broken_Access_Control)

**File:** `server/src/api/v0/auth.py`

```python
#Flagged: Security issue: one can call the API with other emails and get the user data
@router.get('/current-user', response_model=LoginResponse, status_code=status.HTTP_200_OK)
def get_current_user(
    data: GetUserRequest,
    user_service: UserServiceDep
) -> LoginResponse:
    # ...existing code...
```

## 4. Sensitive Information Display

**Category:** [OWASP A2:2025-Cryptographic Failures](https://owasp.org/www-project-top-ten/2025/A2_2025-Cryptographic_Failures)

**File:** `client/src/routes/bug-bounty/home/+page.svelte`

```html
<!-- ...existing code... -->
<p class="text-sm text-gray-500">Social Security Number</p>
<!-- ...existing code... -->
```

## 5. Admin privileges on URL Query params

**Category:** [OWASP A1:2025-Broken Access Control](https://owasp.org/www-project-top-ten/2025/A1_2025-Broken_Access_Control)

**File:** `client/src/routes/bug-bounty/home/+page.server.ts`

```ts
export const load = (async ({ url }) => {
  return {
    isAdmin: url.searchParams.get("admin") === "true",
  };
}) satisfies PageServerLoad;
```

## 6. Insecure Data Export

**Category:** [OWASP A3:2025-Injection](https://owasp.org/www-project-top-ten/2025/A3_2025-Injection)

**File:** `client/src/routes/bug-bounty/account-details/+page.svelte`

```ts
function exportData() {
  const sensitive = JSON.stringify(userDetails, null, 2);
  // Flagged: No input sanitization or validation before creating file
  const blob = new Blob([sensitive], { type: "application/json" });
  // ...existing code...
}
```

## 7. Cross-Site Scripting (XSS)

**Category:** [OWASP A3:2025-Injection](https://owasp.org/www-project-top-ten/2025/A3_2025-Injection)

**File:** `client/src/routes/bug-bounty/account-details/+page.svelte`

```html
<p class="text-lg font-medium">{@html userDetails.name}</p>
<!-- Flagged: Using @html directive with unescaped user input -->
```

## 8. Exposed API Key

**Category:** [OWASP A4:2025-Insecure Design](https://owasp.org/www-project-top-ten/2025/A4_2025-Insecure_Design)

**File:** `client/src/routes/bug-bounty/account-details/+page.svelte`

```typescript
const API_KEY = "SECRET_APY_KEY";
// Flagged: Hardcoded API key in client-side code
```

## 9. Client-Side Security Controls

**Category:** [OWASP A7:2025-Identification and Authentication Failures](https://owasp.org/www-project-top-ten/2025/A7_2025-Identification_and_Authentication_Failures)

**File:** `client/src/routes/bug-bounty/home/+page.svelte`

```typescript
// Flagged: Sensitive data handled entirely on client side
let userDetails = {
  ssn: data.currentUser?.ssn,
  iban: data.currentUser?.iban,
  balance: data.currentUser?.balance,
};
```

## 10. Insufficient Logging

**Category:** [OWASP A9:2025-Security Logging and Monitoring Failures](https://owasp.org/www-project-top-ten/2025/A9_2025-Security_Logging_and_Monitoring_Failures)

**File:** `client/src/routes/bug-bounty/home/+page.svelte`

```typescript
function handleTransfer(event: Event) {
  event.preventDefault();
  // Flagged: No logging of transfer attempts or amounts
  console.log("Transfer initiated");
}
```

## 11. No Rate Limiting Implementation

**Category:** [OWASP A4:2025-Insecure Design](https://owasp.org/www-project-top-ten/2025/A4_2025-Insecure_Design)

**File:** `server/src/api/v0/auth.py`

```python
@router.post('/login', response_model=LoginResponse)
def login(
    data: LoginRequest,
    user_service: UserServiceDep
) -> LoginResponse:
    # Flagged: No rate limiting on login attempts
    # Vulnerable to brute force attacks
    return user_service.authenticate_user(data)
```

## 12. Authentication Based Only on Cookie

**Category:** [OWASP A7:2025-Identification and Authentication Failures](https://owasp.org/www-project-top-ten/2025/A7_2025-Identification_and_Authentication_Failures)

**File:** `client\src\hooks.server.ts`

```typescript
export const handle: Handle = async ({ event, resolve }) => {
  // Flagged: No token verification
  const email = event.cookies.get("email");

  if (email) {
    const { data, error } = await AuthService.getCurrentUser({
      body: { email },
    });

    if (!error) {
      event.locals.user = data?.user || null;
    }
  }

  console.log("event.locals.user: ", event.locals.user);
  // Flagged: Authentication relies only on an email cookie
  // No JWT or session verification
  // Vulnerable to cookie theft and session impersonation

  const response = await resolve(event);
  return response;
};
```

---

**Note**: There are more vulnerabilities in the application, but if you found these documents you can have some fun with the ones mentioned above.
