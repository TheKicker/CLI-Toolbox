import random
import time
from datetime import datetime

def random_log_message():
    messages = [
        "Quantum backdoor initiated, bypassing subatomic encryption protocols",
        "Executing a cosmic ray injection attack on the data storage matrix",
        "Compiling a hyper-threaded virus to infiltrate the nanobot defense grid",
        "Hijacking the interstellar signal using a celestial man-in-the-middle attack",
        "Deploying a self-replicating algorithm to exploit the code vulnerability in the universal source code repository",
        "Initiating a darknet transaction to acquire a zero-gravity exploit kit",
        "Integrating the extraterrestrial API to breach the intergalactic authentication layer",
        "Engaging the singularity-based fuzzy logic to bypass the event horizon firewall",
        "Quantum superposition achieved for simultaneous infiltration and exfiltration",
        "Synchronizing the parallel universes to create a diversionary time dilation attack",
        "Injecting a self-aware AI into the cloud infrastructure to manipulate the server farm",
        "Initiating a reverse-engineered black hole algorithm to warp spacetime for stealth maneuvers",
        "Executing a polymorphic metamorphic code injection to confuse the anti-virus defenses",
        "Utilizing a galactic-scale DDoS attack to overload the subspace communication channels",
        "Engaging the virtual reality worm to navigate through the immersive firewall defenses",
        "Conducting a gravitational anomaly exploit to bend the laws of physics for unauthorized access",
        "Quantum entropic disruption protocol engaged to induce entropy in the target system",
        "Deploying an interdimensional trojan horse to breach the quantum encryption barrier",
        "Activating the dark matter encryption keys to obfuscate communication signals",
        "Initiating a spectral analysis of the electromagnetic spectrum to discover hidden network nodes",
        "Conducting a cosmic string man-in-the-middle attack to intercept data transmissions",
        "Executing a bio-digital virus to infiltrate the biological components of the sentient network",
        "Engaging the time-traveling AI to retrieve future exploits and vulnerabilities",
        "Quantum tunneling through the fabric of reality to access the higher-dimensional data plane",
        "Deploying a self-evolving neural network to adapt to evolving security protocols",
    ]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {random.choice(messages)}"


def random_time_interval():
    return random.randint(10, 30)

def random_speed_change():
    return random.randint(1, 3)

def progress_bar(percent):
    percent = min(percent, 100)  # Ensure percent does not exceed 100
    progress_length = 20
    filled_length = int(percent / 5)
    empty_length = progress_length - filled_length
    print(f"[{'=' * filled_length}{' ' * empty_length}] {percent:.1f}%")

def main():
    target = input("Enter the target to hack: ")
    print(f"Starting the hack on {target}...")
    progress_bar(0)
    current = 0

    while current <= 85:
        random_number = random.randint(1,12)
        random_sleep = random.randint(3,8)
        current += random_number
        progress_bar(current)
        print(random_log_message())
        time.sleep(random_sleep)

    # Ensure the final progress bar is printed
    progress_bar(100)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} // SUCCESS - User is logged into {target} as system administrator")

if __name__ == "__main__":
    main()

