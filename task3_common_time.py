# Решение задачи 3
from collections import namedtuple
from itertools import product


def time_overlap(interval1: namedtuple, interval2: namedtuple) -> namedtuple:
    if (interval1.start <= interval2.end) and (interval2.start <= interval1.end):
        Range = namedtuple('Range', ['start', 'end'])
        latest_start = max(interval1.start, interval2.start)
        earliest_end = min(interval1.end, interval2.end)
        result = Range(start=latest_start, end=earliest_end)
        return result


def appearance(intervals: dict) -> int:
    lesson, pupil, tutor = intervals['lesson'], intervals['pupil'], intervals['tutor']
    pupil = [pupil[el:2 + el] for el in range(0, len(pupil), 2)]
    tutor = [tutor[el:2 + el] for el in range(0, len(tutor), 2)]
    lesson = [lesson]
    intersection = product(lesson, pupil, tutor)
    count = 0
    for item in intersection:
        lesson_interval, pupil_interval, tutor_interval = item
        Range = namedtuple('Range', ['start', 'end'])
        lesson_range = Range(start=lesson_interval[0], end=lesson_interval[1])
        pupil_range = Range(start=pupil_interval[0], end=pupil_interval[1])
        tutor_range = Range(start=tutor_interval[0], end=tutor_interval[1])
        lesson_pupil_overlap = time_overlap(lesson_range, pupil_range)
        if lesson_pupil_overlap:
            lesson_pupil_tutor_overlap = time_overlap(lesson_pupil_overlap, tutor_range)
            if lesson_pupil_tutor_overlap:
                delta = (lesson_pupil_tutor_overlap[1] - lesson_pupil_tutor_overlap[0])
                count += delta
    return count


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
