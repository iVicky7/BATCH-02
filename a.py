import random
import time
import matplotlib.pyplot as plt

# Parameters
NUM_NODES = 20
NUM_TASKS = 100
DISASTER_SCENARIOS = 10
SIMULATION_TIME = 10  # Time in seconds for each task allocation

# Load balancing algorithms
def round_robin(nodes, tasks):
    assignments = {}
    node_idx = 0
    for task in tasks:
        assignments[task] = nodes[node_idx]
        node_idx = (node_idx + 1) % len(nodes)
    return assignments

def least_loaded(nodes, tasks):
    assignments = {}
    load = {node: 0 for node in nodes}
    for task in tasks:
        least_loaded_node = min(load, key=load.get)
        assignments[task] = least_loaded_node
        load[least_loaded_node] += 1
    return assignments

def random_assignment(nodes, tasks):
    assignments = {}
    for task in tasks:
        assignments[task] = random.choice(nodes)
    return assignments

def measure_latency(assignments):
    # Simulate processing time for each task on its assigned node
    start_time = time.time()
    for task, node in assignments.items():
        # Simulating task processing with a random delay
        time.sleep(random.uniform(0.05, 0.15))
    return time.time() - start_time

def simulate_disaster_scenario(nodes, tasks):
    # Simulate a disaster scenario by altering nodes and tasks
    if random.random() > 0.5:
        nodes = random.sample(nodes, k=max(len(nodes)//2, 1))
    if random.random() > 0.5:
        tasks = tasks[:max(len(tasks)//2, 1)]
    return nodes, tasks

def main():
    nodes = [f"Node_{i}" for i in range(NUM_NODES)]
    tasks = [f"Task_{i}" for i in range(NUM_TASKS)]

    algorithms = {
        "Round-Robin": round_robin,
        "Least-Loaded": least_loaded,
        "Random": random_assignment
    }

    results = {algo: [] for algo in algorithms.keys()}

    for scenario in range(DISASTER_SCENARIOS):
        print(f"Scenario {scenario + 1}:")
        nodes, tasks = simulate_disaster_scenario(nodes, tasks)
        
        for algo_name, algo_func in algorithms.items():
            print(f"  Algorithm: {algo_name}")
            assignments = algo_func(nodes, tasks)
            latency = measure_latency(assignments)
            results[algo_name].append(latency)
            print(f"    Latency: {latency:.2f} seconds")

    # Plot results
    plt.figure(figsize=(12, 8))
    for algo_name, latencies in results.items():
        plt.plot(range(1, DISASTER_SCENARIOS + 1), latencies, marker='o', linestyle='-', label=algo_name)
    
    plt.xlabel('Disaster Scenario')
    plt.ylabel('Latency (seconds)')
    plt.title('Latency Comparison of Load Balancing Algorithms in FANET')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()