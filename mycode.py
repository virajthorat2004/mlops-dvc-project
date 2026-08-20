import os
import csv

os.makedirs("data", exist_ok=True)

file_path = "data/data.csv"

file_exists = os.path.exists(file_path)

with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["id", "name", "value"])

    writer.writerow([1, "A", 100])
    writer.writerow([2, "B", 200])
    writer.writerow([3, "C", 300])

print("Data generated successfully.")
