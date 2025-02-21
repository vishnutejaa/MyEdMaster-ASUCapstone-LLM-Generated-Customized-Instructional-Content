import os
from langchain.agents import Tool
from autogen import AssistantAgent, UserProxyAgent


# New imports:
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

import faiss


# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# Vector Store for User Profiles
embeddings = OpenAIEmbeddings()

# texts = [
#     "Intermediate in Maths with strengths in algebra and calculus",
#     "Advanced in Physics with strengths in mechanics",
#     "Beginner in Chemistry with weaknesses in organic chemistry"
# ]
# vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# # Save the vectorstore to disk
# vectorstore.save_local("faiss_index")

# # Load the vectorstore from disk
# vectorstore = FAISS.load_local("faiss_index", embeddings)


# ------------------------------------------------
# 1. Self-Assessment Agent
# ------------------------------------------------
self_assessment_agent = AssistantAgent(
    name="SelfAssessmentAgent",
    system_message=(
        "You collect self-assessment data from students in Maths, Physics, and Chemistry. "
        "Ask questions about their skill level (Beginner, Intermediate, Advanced) and specific strengths/weaknesses."
    ),
    llm_config={"model": "gpt-4"}
)

# ------------------------------------------------
# 2. Profile Builder Agent
# ------------------------------------------------
profile_builder_agent = AssistantAgent(
    name="ProfileBuilderAgent",
    system_message=(
        "You build a structured user profile based on self-assessment data. "
        "The profile includes skill levels in Maths, Physics, and Chemistry, strengths, weaknesses, and confidence levels."
    ),
    llm_config={"model": "gpt-4"}
)

# ------------------------------------------------
# 3. Assessment Generator Agent
# ------------------------------------------------
assessment_generator_agent = AssistantAgent(
    name="AssessmentGeneratorAgent",
    system_message=(
        "You create personalized assessments based on the user's skill profile. "
        "Generate different types of questions with increasing difficulty."
    ),
    llm_config={"model": "gpt-4"}
)

# ------------------------------------------------
# 4. Assessment Evaluator Agent
# ------------------------------------------------
assessment_evaluator_agent = AssistantAgent(
    name="AssessmentEvaluatorAgent",
    system_message=(
        "You evaluate the user's performance on assessments and refine their skill profile based on results. "
        "Identify areas of improvement and adjust skill levels if needed."
    ),
    llm_config={"model": "gpt-4"}
)

# ------------------------------------------------
# 5. Content Recommender Agent
# ------------------------------------------------
content_recommender_agent = AssistantAgent(
    name="ContentRecommenderAgent",
    system_message=(
        "You recommend tailored course content based on the user's updated skill profile. "
        "Suggest tutorials, practice problems, and advanced concepts aligned with their level."
    ),
    llm_config={"model": "gpt-4"}
)

# ------------------------------------------------
# User Proxy Agent
# ------------------------------------------------
user_proxy = UserProxyAgent(
    name="UserProxy",
    system_message="You represent the student interacting with the system.",
    code_execution_config={"use_docker": False}
)





def run_learning_cycle(user_input):
    # 1. Self-Assessment
    self_assessment_response = self_assessment_agent.generate_reply(
        messages=[{"role": "user", "content": user_input}]
    )
    print("\n🔷 Self-Assessment Response:", self_assessment_response)

    # 2. Profile Creation
    profile_response = profile_builder_agent.generate_reply(
        messages=[{"role": "user", "content": self_assessment_response}]
    )
    print("\n🟢 User Profile:", profile_response)

    # Store profile in vector database
    # vectorstore.add_texts([profile_response])

    # 3. Generate Assessment
    assessment_response = assessment_generator_agent.generate_reply(
        messages=[{"role": "user", "content": profile_response}]
    )
    print("\n📚 Assessment Generated:", assessment_response)

    # 4. Simulate Assessment Results (In real use, collect user responses)
    assessment_results = "User scored 7/10 in Maths, 6/10 in Physics, and 8/10 in Chemistry."

    # 5. Refine Profile Based on Results
    refined_profile_response = assessment_evaluator_agent.generate_reply(
        messages=[{"role": "user", "content": f"Assessment results: {assessment_results}"}]
    )
    print("\n🔄 Updated Profile:", refined_profile_response)

    # Store updated profile in vector database
    # vectorstore.add_texts([refined_profile_response])

    # 6. Recommend Course Content
    content_response = content_recommender_agent.generate_reply(
        messages=[{"role": "user", "content": refined_profile_response}]
    )
    print("\n✅ Tailored Course Content:", content_response)

    return {
        "profile": refined_profile_response,
        "assessment": assessment_response,
        "content": content_response
    }





if __name__ == "__main__":
    user_self_assessment = """
    I consider myself intermediate in Maths, with strengths in algebra and calculus but weaknesses in probability.
    In Physics, I'm advanced in mechanics but need improvement in electromagnetism.
    In Chemistry, I have a beginner level, especially struggling with organic chemistry.
    """
    results = run_learning_cycle(user_self_assessment)
    retrieved_docs = vectorstore.similarity_search("Maths profile with intermediate skill")
    print("\n🔎 Retrieved User Profile:", retrieved_docs[0].page_content)
