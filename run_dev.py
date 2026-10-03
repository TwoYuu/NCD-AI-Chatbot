import subprocess
import sys
import os
import time

def main():
    print("========================================")
    print("Starting Mentor NCD AI Chatbot Servers")
    print("========================================")

    # 1. Determine the correct python executable to use (checks for .venv)
    venv_python = os.path.join(".venv", "Scripts", "python.exe") if os.name == 'nt' else os.path.join(".venv", "bin", "python")
    python_exe = venv_python if os.path.exists(venv_python) else sys.executable

    print(f"[INFO] Using Python executable: {python_exe}")

    # 2. Start the Backend (FastAPI via Uvicorn)
    print("[STARTING] Backend Server (Port 8000)...")
    backend_process = subprocess.Popen(
        [python_exe, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"],
        cwd="backend"
    )

    # 3. Start the Frontend (Simple HTTP Server)
    print("[STARTING] Frontend Server (Port 5500)...")
    frontend_process = subprocess.Popen(
        [python_exe, "-m", "http.server", "5500", "--bind", "0.0.0.0", "--directory", "frontend"]
    )

    print("========================================")
    print("All servers are running!")
    print("Local access (this computer): http://localhost:5500")
    print("Network access (other devices): Use your computer's local IP on port 5500")
    print("Press Ctrl+C to stop both servers.")
    print("========================================")

    # 4. Wait indefinitely until interrupted
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[STOPPING] Shutting down servers...")
        backend_process.terminate()
        frontend_process.terminate()
        backend_process.wait()
        frontend_process.wait()
        print("[STOPPED] Both servers have been stopped gracefully.")

if __name__ == "__main__":
    main()
