#!/usr/bin/env python
import sys
from datetime import datetime
from custom_course_generator.crew import CustomCourseGenerator
from crewai import LLM

llm = LLM(
    model="ollama/deepseek-r1:8b",
    base_url="http://localhost:11434"
)

def run():
    """
    Run the crew with specified inputs.
    """
    inputs = {
        'student_name': 'John Doe',
        'assessment_results': {
            'math': 'intermediate',
            'science': 'beginner',
            'literature': 'advanced'
        },
        'preferred_learning_style': 'visual',
        'current_year': str(datetime.now().year)
    }
    
    try:
        CustomCourseGenerator().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'student_name': 'John Doe',
        'assessment_results': {
            'math': 'intermediate',
            'science': 'beginner',
            'literature': 'advanced'
        },
        'preferred_learning_style': 'visual'
    }
    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 10
        filename = sys.argv[2] if len(sys.argv) > 2 else 'training_data.pkl'
        CustomCourseGenerator().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        print(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        task_id = sys.argv[1] if len(sys.argv) > 1 else None
        if task_id:
            CustomCourseGenerator().crew().replay(task_id=task_id)
        else:
            print("Please provide a task_id to replay.")
    except Exception as e:
        print(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        'student_name': 'John Doe',
        'assessment_results': {
            'math': 'intermediate',
            'science': 'beginner',
            'literature': 'advanced'
        },
        'preferred_learning_style': 'visual'
    }
    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        openai_model_name = sys.argv[2] if len(sys.argv) > 2 else 'gpt-4'
        CustomCourseGenerator().crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)
    except Exception as e:
        print(f"An error occurred while testing the crew: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: main.py [run|train|replay|test] [additional arguments]")
    else:
        command = sys.argv[1].lower()
        if command == 'run':
            run()
        elif command == 'train':
            train()
        elif command == 'replay':
            replay()
        elif command == 'test':
            test()
        else:
            print(f"Unknown command: {command}")
