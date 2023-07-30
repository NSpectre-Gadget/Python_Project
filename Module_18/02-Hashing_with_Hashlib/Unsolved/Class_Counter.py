# Imports
from dataclasses import dataclass
from datetime import datetime
from typing import Any
import hashlib

# Create a data class called Counter
@dataclass
class Counter:
    count: int = 0

# Create the data class called Counter
# Include a method called update_count
@dataclass
class Counter:
    count: int = 0
    def update_count(self):
        self.count = self.count + 1

# Create a new instance of Counter
new_counter = Counter()

# Update the count by calling update_count
new_counter.update_count()
new_counter.update_count()

# Print the updated value of count
print("The current count is: ", new_counter.count)

