#!/bin/bash

echo "Starting SpotiLeak..."

# Start backend in background
echo "Starting backend..."
uvicorn backend.main:app --reload --port 8000 &
BACKEND_PID=$!

# Start frontend
echo "Starting frontend..."
cd frontend && npm start &
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
echo "Frontend: http://localhost:3000"
echo "Press CTRL+C to stop"

wait