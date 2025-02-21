import { useState } from 'react';
import Layout from './components/Layout';
import SubjectCard from './components/SubjectCard';
import AssessmentResult from './components/AssessmentResult';
import { submitAssessment } from './services/api';

function App() {
  const [formData, setFormData] = useState({
    personalInfo: {
      name: '',
      grade: ''
    },
    subjects: {
      Maths: { skillLevel: 'Beginner', strengths: '', weaknesses: '' },
      Physics: { skillLevel: 'Beginner', strengths: '', weaknesses: '' },
      Chemistry: { skillLevel: 'Beginner', strengths: '', weaknesses: '' }
    },
    additionalInfo: ''
  });

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      console.log('Submitting form data:', formData); // Debug log
      const response = await submitAssessment(formData);
      console.log('Received response:', response); // Debug log
      setResult(response);
    } catch (error) {
      console.error('Submission error:', error); // Debug log
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubjectChange = (subject, field, value) => {
    setFormData({
      ...formData,
      subjects: {
        ...formData.subjects,
        [subject]: {
          ...formData.subjects[subject],
          [field]: value
        }
      }
    });
  };

  return (
    <Layout>
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Personal Information */}
        <div className="bg-white shadow-md rounded-lg p-6 border border-gray-100">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Personal Information</h2>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <label className="block text-sm font-medium text-gray-700">Name</label>
              <input
                type="text"
                required
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                         focus:border-blue-500 focus:ring-blue-500 transition-colors"
                value={formData.personalInfo.name}
                onChange={(e) => setFormData({
                  ...formData,
                  personalInfo: { ...formData.personalInfo, name: e.target.value }
                })}
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Grade</label>
              <input
                type="text"
                required
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                         focus:border-blue-500 focus:ring-blue-500 transition-colors"
                value={formData.personalInfo.grade}
                onChange={(e) => setFormData({
                  ...formData,
                  personalInfo: { ...formData.personalInfo, grade: e.target.value }
                })}
              />
            </div>
          </div>
        </div>

        {/* Subject Assessments */}
        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          {Object.entries(formData.subjects).map(([subject, data]) => (
            <SubjectCard
              key={subject}
              subject={subject}
              data={data}
              onChange={handleSubjectChange}
            />
          ))}
        </div>

        {/* Additional Information */}
        <div className="bg-white shadow-md rounded-lg p-6 border border-gray-100">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Additional Information</h2>
          <textarea
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                     focus:border-blue-500 focus:ring-blue-500 transition-colors"
            rows="3"
            value={formData.additionalInfo}
            onChange={(e) => setFormData({...formData, additionalInfo: e.target.value})}
            placeholder="Any other information you'd like to share..."
          />
        </div>

        {error && (
          <div className="rounded-md bg-red-50 p-4">
            <div className="flex">
              <div className="text-sm text-red-700">{error}</div>
            </div>
          </div>
        )}

        <div className="flex justify-end">
          <button
            type="submit"
            disabled={isLoading}
            className={`inline-flex items-center px-6 py-2 border border-transparent 
                     text-base font-medium rounded-md text-white bg-blue-600 
                     hover:bg-blue-700 focus:outline-none focus:ring-2 
                     focus:ring-offset-2 focus:ring-blue-500 transition-colors
                     ${isLoading ? 'opacity-75 cursor-not-allowed' : ''}`}
          >
            {isLoading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Processing...
              </>
            ) : 'Submit Assessment'}
          </button>
        </div>
      </form>

      <AssessmentResult result={result} />
    </Layout>
  );
}

export default App;
