# Author: Jigesh Sheoran
# Last Modified : 06 / 03 / 2026
# Experiment: Job Sequencing with Deadlines

def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)

    total_profit = 0
    scheduled_jobs = []

    for job in jobs:
        job_id, deadline, profit = job

        for d in range(deadline, 0, -1):
            if slots[d] == -1:
                slots[d] = job_id
                total_profit += profit
                scheduled_jobs.append(job_id)
                break

    return scheduled_jobs, total_profit


# user input 
print("Job Sequencing with Deadlines Program")

n = int(input("Enter number of jobs:\n"))

jobs = []
print("Enter jobs in format: job_id deadline profit")

for i in range(n):
    job_id, deadline, profit = input(f"Job {i+1}: ").split()
    jobs.append((job_id, int(deadline), int(profit)))

scheduled, profit = job_sequencing(jobs)

print("\nScheduled Jobs:", scheduled)
print("Maximum Profit:", profit)

print("Program executed successfully.")
