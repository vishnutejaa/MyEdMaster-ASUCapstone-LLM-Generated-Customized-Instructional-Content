import os
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from autogen import AssistantAgent
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Self-Assessment Agent
self_assessment_agent = AssistantAgent(
    name="SelfAssessmentAgent",
    system_message=(
        "You are responsible for collecting self-assessment data from students in Maths, Physics, and Chemistry. "
        "Ask clear and concise questions about their skill level (Beginner, Intermediate, Advanced), strengths, and weaknesses."
        "Ensure the data is well-structured and ready for further use in assessments and profile generation."
    ),
    llm_config={"model": "gpt-4o"}  # or "gpt-3.5-turbo"
)

# **Self-Assessment Function**
def conduct_self_assessment(assessment_data):
    """
    Modified to accept JSON data from frontend instead of using input()
    """
    # Format the data for LLM processing
    user_input = (
        f"\nName: {assessment_data['personalInfo']['name']}, Grade: {assessment_data['personalInfo']['grade']}\n"
        + '\n'.join(
            f"{subject}: {data['skillLevel']}, "
            f"Strengths: {data['strengths']}, "
            f"Weaknesses: {data['weaknesses']}."
            for subject, data in assessment_data['subjects'].items()
        )
        + f"\nAdditional Information: {assessment_data['additionalInfo']}"
    )

    print("\n🔷 **Processing self-assessment...**")

    # LLM Verification and Enhancement
    response = self_assessment_agent.generate_reply(
        messages=[{
            "role": "user", 
            "content": f"""Please analyze the following student data and create a detailed, structured user profile:

            {user_input}

            For each subject (Maths, Physics, Chemistry):
            1. Validate and confirm the stated skill level
            2. Analyze the alignment between stated strengths/weaknesses and skill level
            3. Identify key areas that need assessment based on the profile
            4. Suggest specific topics to test their knowledge
            5. Format the response in a clear, structured way that can be used to generate targeted assessments

            Please ensure the profile highlights:
            - Areas where skill level may need verification
            - Topics where strengths can be challenged
            - Specific concepts within weak areas that need improvement
            - Cross-subject connections and prerequisites
            - Recommended assessment approach based on the profile"""
        }]
    )

    return response

# Add Flask endpoint to handle frontend requests
app = Flask(__name__)
# CORS(app)  # This enables CORS for all routes with default settings
CORS(app, origins=["http://localhost:3000","http://192.168.1.164:3000" ])

@app.route('/api/assess', methods=['POST'])
def assess():
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
            
        assessment_data = request.json
        print("Received data:", assessment_data)  # Debug print
        
        # Validate required fields
        if not assessment_data.get('personalInfo') or \
           not assessment_data['personalInfo'].get('name') or \
           not assessment_data['personalInfo'].get('grade'):
            return jsonify({'error': 'Missing required personal information'}), 400
            
        if not assessment_data.get('subjects'):
            return jsonify({'error': 'Missing subjects data'}), 400
            
        response = conduct_self_assessment(assessment_data)
        print("Generated response:", response)  # Debug print
        return jsonify({'profile': response})
        
    except Exception as e:
        print(f"Error processing assessment: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(debug=True, port=5000)