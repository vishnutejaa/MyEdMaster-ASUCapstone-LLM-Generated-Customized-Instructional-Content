from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CustomCourseGenerator:
    """Crew for generating customized course content for high school students."""

    # Paths to the YAML configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def skill_assessment_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['skill_assessment_agent'],
            verbose=True
        )

    @agent
    def course_designer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['course_designer_agent'],
            verbose=True
        )

    @agent
    def content_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_generator_agent'],
            verbose=True
        )

    @agent
    def engagement_feedback_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['engagement_feedback_agent'],
            verbose=True
        )

    @task
    def skill_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['skill_assessment_task'],
        )

    @task
    def curriculum_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_design_task'],
        )

    @task
    def content_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_generation_task'],
        )

    @task
    def engagement_feedback_task(self) -> Task:
        return Task(
            config=self.tasks_config['engagement_feedback_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CustomCourseGenerator crew."""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
