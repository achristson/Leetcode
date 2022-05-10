"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

idea:
since the courses have relationships to other courses we can represent this as a directed graph
once we have the graph we can then try to create a topological sort 
if this is possible, then we can assume that we will be able to take all courses
if it is not possible then we can assume that we will not be able to take all courses

let v = number of courses
let e = number of dependencies
Time: O(v + e)
Space: O(v + e)
Link: https://leetcode.com/problems/course-schedule/solution/

[[1,0]]
{1: [0]
 0: []}
top sort = {0: 0
            1: 0}
courses = []
queue = []
add course to courses if we have no incoming edges
if the length of courses is the same as the number of courses then we can take all courses
if the length of courses is less than the number of courses then we cannot take all courses
"""
from collections import deque


def course_schedule(num_courses, prerequisites):
    graph = {course: [] for course in range(num_courses)}

    for src, dest in prerequisites:
        graph[src].append(dest)

    def get_parents():
        parent_count = {course: 0 for course in range(num_courses)}
        for parent in graph:
            for course in graph[parent]:
                parent_count[course] += 1
        return parent_count

    def top_sort():
        queue = deque()
        parent_count = get_parents()
        for course in parent_count:
            if parent_count[course] == 0:
                queue.append(course)
        sorted_courses_count = 0
        while queue:
            course = queue.popleft()
            sorted_courses_count += 1
            for neighbor in graph[course]:
                parent_count[neighbor] -= 1
                if parent_count[neighbor] == 0:
                    queue.append(neighbor)
        if sorted_courses_count == num_courses:
            return True
        return False
    return top_sort()

