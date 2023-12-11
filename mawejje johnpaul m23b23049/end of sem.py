
python
class StudentQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, student):
        self._queue.append(student)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)


# Example usage:

student_queue = StudentQueue()

# Enqueue some students to the queue.
student_queue.enqueue("Alice")
student_queue.enqueue("Bob")
student_queue.enqueue("Carol")

# Serve the first student in the queue.
served_student = student_queue.dequeue()
print(f"The first student to be served is: {served_student}")

# Check if the queue is empty.
is_empty = student_queue.is_empty()
print(f"Is the queue empty? {is_empty}")

# Get the current size of the queue.
queue_size = student_queue.size()
print(f"The current size of the queue is: {queue_size}")






*Explanation:*

The StudentQueue class simulates a queue data structure for managing the student queue at the university's student dining hall. It has four methods:

* enqueue(): Enqueues a student to the queue.
* dequeue(): Dequeues the first student in the queue and returns it.
* is_empty(): Checks if the queue is empty.
* size(): Returns the current size of the queue.

The example usage of the StudentQueue class shows how students can be enqueued to the queue, served, and the size of the queue can be ascertained.     *Question 3 (20 Marks)*

*Design and run 2 sorting algorithms of your choice that sorts the list, unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23] and provide the complexity class (as a Python comment) of the implemented algorithms.*

*Python code for selection sort:*

python
def selection_sort(unsorted_list):
  """Sorts a list in ascending order using the selection sort algorithm.

  Args:
    unsorted_list: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  for i in range(len(unsorted_list) - 1):
    min_index = i
    for j in range(i + 1, len(unsorted_list)):
      if unsorted_list[j] < unsorted_list[min_index]:
        min_index = j

    unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

  return unsorted_list


# Example usage:

unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23]
sorted_list = selection_sort(unsorted_list)

print(sorted_list)




python
def insertion_sort(unsorted_list):
  """Sorts a list in ascending order using the insertion sort algorithm.

  Args:
    unsorted_list: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  for i in range(1, len(unsorted_list)):
    current_element = unsorted_list[i]
    j = i - 1
    while j >= 0 and unsorted_list[j] > current_element:
      unsorted_list[j + 1] = unsorted_list[j]
      j -= 1

    unsorted_list[j + 1] = current_element

  return unsorted_list


# Example usage:

unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23]
sorted_list = insertion_sort(unsorted_list)

print(sorted_list)


