from app import create_app
import pytest

# Create an application instance using the 'Development' configuration
app = create_app('development')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
