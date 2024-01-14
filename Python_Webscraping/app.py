from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    try:
        # Check if a command-line argument is provided
        if len(sys.argv) > 1:
            port = int(sys.argv[1])
            
            # Ensure the provided port is within the valid range
            if 49152 <= port <= 65535:
                app.run(host='0.0.0.0', port=port)
            else:
                print("Error: Please provide a valid port number in the range 49152 to 65535.")
        else:
            print("Error: Please provide a port number as a command-line argument.")
    except ValueError:
        print("Error: Please provide a valid integer for the port number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
                        
