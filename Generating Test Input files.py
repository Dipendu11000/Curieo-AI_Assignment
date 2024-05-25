#!/usr/bin/env python
# coding: utf-8
# %%

# %%





# %%


import random
import time
log_types = [
    "INTERNAL_SERVER_ERROR", 
    "BAD_REQUEST", 
    "NOT_FOUND", 
    "SERVICE_UNAVAILABLE", 
    "UNAUTHORIZED"
]
def generate_timestamp(start, end):
    return random.randint(start, end)
def generate_severity():
    return round(random.uniform(1.0, 100.0), 2)
def generate_log_entries(num_entries, start_timestamp, end_timestamp):
    entries = []
    for _ in range(num_entries):
        timestamp = generate_timestamp(start_timestamp, end_timestamp)
        log_type = random.choice(log_types)
        severity = generate_severity()
        entries.append(f"1 {timestamp}; {log_type}; {severity}")
    return entries
def generate_commands(num_commands, start_timestamp, end_timestamp):
    commands = []
    for _ in range(num_commands):
        command = random.choice(["2", "3", "4"])
        if command == "2":
            log_type = random.choice(log_types)
            commands.append(f"{command} {log_type}")
        else:
            direction = random.choice(["BEFORE", "AFTER"])
            timestamp = generate_timestamp(start_timestamp, end_timestamp)
            if command == "3":
                commands.append(f"{command} {direction} {timestamp}")
            elif command == "4":
                log_type = random.choice(log_types)
                commands.append(f"{command} {direction} {log_type} {timestamp}")
    return commands

if __name__ == "__main__":
    num_log_entries = 1000 
    num_commands = 400 
    
    start_timestamp = int(time.time() * 1000)
    end_timestamp = start_timestamp + 1000000

    log_entries = generate_log_entries(num_log_entries, start_timestamp, end_timestamp)
    commands = generate_commands(num_commands, start_timestamp, end_timestamp)
    input_lines = log_entries + commands
    random.shuffle(input_lines)    # Shufflng the combined input to mix commands and log entries
    
    with open("input.txt", "w") as f:
        for line in input_lines:
            f.write(line + "\n")


# %%




