const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

export const submitAssessment = async (assessmentData) => {
  try {
    console.log('Submitting assessment:', assessmentData); // Debug log
    const response = await fetch(`${API_BASE_URL}/assess`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(assessmentData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Assessment submission failed');
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error); // Debug log
    throw new Error(error.message || 'Failed to connect to the server');
  }
}; 