#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


def add_log(logs, logs_by_type, timestamp, log_type, severity):
    logs.append((timestamp, log_type, severity))
    if log_type not in logs_by_type:
        logs_by_type[log_type] = []
    logs_by_type[log_type].append((timestamp, severity))

def compute_severity_stats(severities):
    if not severities:
        return 0.0, 0.0, 0.0
    min_sev = min(severities)
    max_sev = max(severities)
    mean_sev = sum(severities) / len(severities)
    return min_sev, max_sev, mean_sev

def query_log_type(logs_by_type, log_type):
    if log_type in logs_by_type:
        severities = [severity for _, severity in logs_by_type[log_type]]
        return compute_severity_stats(severities)
    return 0.0, 0.0, 0.0

def query_before_timestamp(logs, timestamp):
    severities = [severity for ts, _, severity in logs if ts < timestamp]
    return compute_severity_stats(severities)

def query_after_timestamp(logs, timestamp):
    severities = [severity for ts, _, severity in logs if ts > timestamp]
    return compute_severity_stats(severities)

def query_before_log_type_timestamp(logs_by_type, log_type, timestamp):
    if log_type in logs_by_type:
        severities = [severity for ts, severity in logs_by_type[log_type] if ts < timestamp]
        return compute_severity_stats(severities)
    return 0.0, 0.0, 0.0

def query_after_log_type_timestamp(logs_by_type, log_type, timestamp):
    if log_type in logs_by_type:
        severities = [severity for ts, severity in logs_by_type[log_type] if ts > timestamp]
        return compute_severity_stats(severities)
    return 0.0, 0.0, 0.0

def parse_input_line(line):
    parts = line.strip().split(maxsplit=1)
    if parts[0] == '1':
        timestamp, log_type, severity = parts[1].split(';')
        return 1, int(timestamp), log_type.strip(), float(severity)
    elif parts[0] == '2':
        return 2, parts[1].strip()
    elif parts[0] == '3':
        when, timestamp = parts[1].split()
        return 3, when, int(timestamp)
    elif parts[0] == '4':
        when, rest = parts[1].split(maxsplit=1)
        log_type, timestamp = rest.rsplit(maxsplit=1)
        return 4, when, log_type.strip(), int(timestamp)
    else:
        raise ValueError("Invalid input line format")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    logs = []
    logs_by_type = {}
    output_lines = []
    
    with open(input_file, 'r') as file:
        for line in file:
            parsed_line = parse_input_line(line)
            command = parsed_line[0]
            
            if command == 1:
                _, timestamp, log_type, severity = parsed_line
                add_log(logs, logs_by_type, timestamp, log_type, severity)
                output_lines.append("No output")
            
            elif command == 2:
                _, log_type = parsed_line
                min_sev, max_sev, mean_sev = query_log_type(logs_by_type, log_type)
                output_lines.append(f"Min: {min_sev:.6f}, Max: {max_sev:.6f}, Mean: {mean_sev:.6f}")
            
            elif command == 3:
                _, when, timestamp = parsed_line
                if when == 'BEFORE':
                    min_sev, max_sev, mean_sev = query_before_timestamp(logs, timestamp)
                elif when == 'AFTER':
                    min_sev, max_sev, mean_sev = query_after_timestamp(logs, timestamp)
                output_lines.append(f"Min: {min_sev:.6f}, Max: {max_sev:.6f}, Mean: {mean_sev:.6f}")
            
            elif command == 4:
                _, when, log_type, timestamp = parsed_line
                if when == 'BEFORE':
                    min_sev, max_sev, mean_sev = query_before_log_type_timestamp(logs_by_type, log_type, timestamp)
                elif when == 'AFTER':
                    min_sev, max_sev, mean_sev = query_after_log_type_timestamp(logs_by_type, log_type, timestamp)
                output_lines.append(f"Min: {min_sev:.6f}, Max: {max_sev:.6f}, Mean: {mean_sev:.6f}")
    
    with open(output_file, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')

if __name__ == '__main__':
    main()


# In[ ]:




