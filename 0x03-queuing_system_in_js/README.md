# Queuing System in JavaScript with Redis and Kue

This project implements a queuing system using Redis and Kue in JavaScript, integrated with an Express server for handling asynchronous tasks.

## Learning Objectives

By completing this project, you will gain practical experience and understanding of:

- Running a Redis server on your local machine
- Basic operations with the Redis client
- Using a Redis client with Node.js for asynchronous operations
- Storing hash values in Redis
- Implementing async operations with Redis
- Utilizing Kue as a queue system for managing jobs
- Building a basic Express application interacting with Redis
- Building an Express app with Redis and a job queue integration

## Requirements

- Ubuntu 18.04, Node.js 12.x, and Redis 5.0.7
- All files should use the `.js` extension
- Each file should end with a new line

## Installation

To install dependencies, run:

```
npm install
```

## Setup

1. **Install Redis**:
   ```
   sudo apt update
   sudo apt install redis-server
   ```
2. **Start Redis server:**

```
  redis-server 
  ```
3. **Redis Client Interface**
Use Redis CLI to interact with Redis server:

```bash
  redis-cli
  ```
4. **Redis Client for Node.js**
Redis client for Node.js is redis package:

```bash
   npm install redis
   ```
5. **Kue (Deprecated but still used)**
Kue is a deprecated job queue for Node.js. Install with:

```bash
   npm install kue
   ```
## Usage

**Development mode:**

To start the server, run:

```
npm run dev <filename>.js
```

Replace `<filename>` with the name of the JavaScript file containing the server setup.

**Testing:**

```
npm test <test_file>.js
```

## Project Structure

The project includes several tasks implemented progressively:

### Task 0: Install Redis and Kue

Install and set up Redis and Kue on your local machine. Ensure Redis is running on port 6379.

### Task 1: Create a Basic Redis Client

Implement basic Redis client operations in Node.js for connecting to and interacting with Redis.

### Task 2: Store a Hash in Redis

Store and retrieve hash values in Redis using the Redis client in Node.js.

### Task 3: Promisify Redis Operations

Convert callback-based Redis operations into promise-based using `util.promisify` for better async handling.

### Task 4: Redis Node Client

Integrate Redis client operations into an Express application to fetch and display stored hash values.

### Task 5: Node Redis Client

Enhance the Express application to include async operations using Redis for fetching and updating hash values.

### Task 6: Node Kue

Implement a basic job creator using Kue for queuing jobs in an Express application.

### Task 7: Node Kue progress and errors

Track job progress and errors using Kue in an Express application with async job processing.

### Task 8: Node Kue job creation function

Create a function for dynamically generating Kue jobs based on input data and queue them in an Express application.

### Task 9: Node Kue job creation test

Write tests for job creation function using mocha and chai to ensure proper queue functioning in an Express application.

### Task 10: Node Kue Job reservation system

Implement a reservation system using Redis and Kue to manage seat reservations in an Express application.

### Task 11: Node Kue Test creator

Write tests for seat reservation system using mocha and chai to verify proper functionality in an Express application.

### Task 12: Node Redis client

Implement a Redis client in an Express application to manage and display available products with reservation capabilities.

### Task 13: Node Redis client

Enhance the Redis client in the Express application to include seat reservation system with queue processing and status updates.

## Resources

- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://redis.io/clients)
- [Redis Client for Node.js](https://github.com/NodeRedis/node_redis)
- [Kue Deprecated but Still Used in Industry](https://github.com/Automattic/kue)

## License

ISC License

---

Make sure to update `<filename>.js` with the appropriate file you want to run, based on the task you're working on. This README.md provides a comprehensive overview of each task, installation instructions, and usage guidelines for running your Express server with Redis and Kue integration.
