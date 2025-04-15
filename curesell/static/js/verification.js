document.getElementById('skip_verification').onclick = function() {
            window.location.href = 'homepage.html';
        };

        document.getElementById('send_code').onclick = function() {
            const email = document.getElementById('email').value;
            // Send a request to the server to send the verification code
            fetch('/send_verification_code/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: email }),
            }).then(response => {
                // Handle response, e.g., show a success message
                alert('Verification code sent to ' + email);
            });
        };