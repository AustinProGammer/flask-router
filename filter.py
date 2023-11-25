from flask import Flask, request, abort

# Read private IPs from file
with open('private_ips.txt', 'r') as file:
    private_ips = [ip.strip() for ip in file.readlines()]

# Create Flask web application
app = Flask(__name__)

# Define route to handle incoming requests
@app.route('/')
def filter_requests():
    client_ip = request.remote_addr
    request_content = request.data.decode('utf-8')  # Read request content
    print(f"Received request from {client_ip} with content:\n{request_content}")

    if client_ip in private_ips:
        # Process the request and return HTML
        return "<html><body><h1>Hello, this is your custom router!</h1></body></html>"
    else:
        # Abort the request for non-private IPs
        abort(403)

# Run the application on a specific port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
