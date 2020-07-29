
class Task:

    def __init__(self, i, deadline, weight):
        self.index = i
        self.deadline = deadline
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'{self.index}'


def is_valid(schedules):
    total = 0
    for i in range(1, len(schedules)):
        total += schedules[i]
        if total > i:
            return False
    return True


def solve(tasks, max_deadline):
    tasks.sort(reverse=True)

    schedules = [0]*(max_deadline+1)  # index 0 is not used
    answers = []
    for task in tasks:
        # check if the answer contains this task
        schedules[task.deadline] += 1
        if is_valid(schedules):
            answers.append(task)
        else:
            schedules[task.deadline] -= 1

    return answers


if __name__ == '__main__':
    task_list = [(4, 70), (2, 60), (4, 50), (3, 40), (1, 30), (4, 20), (6, 10)]
    task_list = [Task(i+1, t[0], t[1]) for i, t in enumerate(task_list)]
    ans = solve(task_list, 6)
    print("answer")
    for a in ans:
        print(a)
    print("after deadline")
    for t in task_list:
        if t not in ans:
            print(t)
