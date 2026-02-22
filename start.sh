#!/bin/bash

echo "Starting SpotiLeak..."

# Start backend in background
echo "Starting backend..."
cd backend
uvicorn main:app --reload --port 8000 &
cd ..
BACKEND_PID=$!

# Start Electron app (React + Electron)
echo "Starting Electron app..."
cd frontend && npm run dev &
FRONTEND_PID=$!

# Function to cleanup background processes
cleanup() {
    echo "Stopping SpotiLeak..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit
}

# Trap CTRL+C
trap cleanup SIGINT

# Wait for user to stop
echo "SpotiLeak is running!"
echo "Backend: http://localhost:8000"
echo "Electron app launching..."
echo "Press CTRL+C to stop"

wait