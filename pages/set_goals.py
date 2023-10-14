import streamlit as st

# Create a to-do list for course goals
st.title("Online Course To-Do List")

# Create an empty list to store the user's goals
course_goals = []

# Input field to add a new goal
new_goal = st.text_input("Add a new goal for your course:")

# Add button to add a new goal to the list
if st.button("Add Goal"):
    if new_goal:
        course_goals.append(new_goal)
        new_goal = ""  # Clear the input field after adding

# Display the current list of goals
st.header("Your Course Goals:")
for i, goal in enumerate(course_goals, start=1):
    st.write(f"{i}. {goal}")

# Checkbox to mark goals as completed
completed_goals = st.checkbox("Mark goal as completed")
if completed_goals:
    goal_index = st.number_input("Enter the goal number:", min_value=1, max_value=len(course_goals), value=1)
    if st.button("Mark as Completed"):
        if 1 <= goal_index <= len(course_goals):
            course_goals.pop(goal_index - 1)

# Clear all goals
if st.button("Clear All Goals"):
    course_goals = []

# Save and load goals from a text file
if st.button("Save Goals"):
    with open("course_goals.txt", "w") as file:
        for goal in course_goals:
            file.write(f"{goal}\n")
    st.success("Goals saved to 'course_goals.txt'")

if st.button("Load Goals"):
    with open("course_goals.txt", "r") as file:
        course_goals = [line.strip() for line in file]

# Provide a link to the online course portal
st.sidebar.header("Online Course Portal")
course_url = st.sidebar.text_input("Enter the course URL:")
if st.sidebar.button("Visit Course"):
    st.sidebar.write(f"Visit the course [here]({course_url}).")

# Optionally, you can add more features like due dates and priority levels to the goals.
