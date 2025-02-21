import React from 'react';

export default function AssessmentResult({ result }) {
  if (!result) return null;

  return (
    <div className="mt-8 bg-white shadow-lg rounded-lg p-6 border border-green-100">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">Assessment Results</h2>
      <div className="prose max-w-none">
        <pre className="whitespace-pre-wrap bg-gray-50 p-4 rounded-md">
          {result.profile}
        </pre>
      </div>
      <button
        onClick={() => window.print()}
        className="mt-4 inline-flex items-center px-4 py-2 border border-transparent 
                 text-sm font-medium rounded-md text-blue-700 bg-blue-100 
                 hover:bg-blue-200 focus:outline-none focus:ring-2 
                 focus:ring-offset-2 focus:ring-blue-500"
      >
        📄 Download PDF
      </button>
    </div>
  );
} 