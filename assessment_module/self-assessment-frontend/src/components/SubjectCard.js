import React from 'react';

export default function SubjectCard({ subject, data, onChange }) {
  return (
    <div className="bg-white shadow-md rounded-lg p-6 transition-all duration-200 hover:shadow-lg border border-gray-100">
      <h2 className="text-lg font-medium text-gray-900 mb-4 flex items-center">
        {subject === 'Maths' && '📐'}
        {subject === 'Physics' && '⚡'}
        {subject === 'Chemistry' && '🧪'}
        <span className="ml-2">{subject}</span>
      </h2>
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Skill Level
          </label>
          <select
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                     focus:border-blue-500 focus:ring-blue-500 transition-colors"
            value={data.skillLevel}
            onChange={(e) => onChange(subject, 'skillLevel', e.target.value)}
          >
            <option>Beginner</option>
            <option>Intermediate</option>
            <option>Advanced</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">
            Strengths
          </label>
          <textarea
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                     focus:border-blue-500 focus:ring-blue-500 transition-colors"
            rows="2"
            value={data.strengths}
            onChange={(e) => onChange(subject, 'strengths', e.target.value)}
            placeholder={`What are your strengths in ${subject}?`}
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">
            Areas for Improvement
          </label>
          <textarea
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                     focus:border-blue-500 focus:ring-blue-500 transition-colors"
            rows="2"
            value={data.weaknesses}
            onChange={(e) => onChange(subject, 'weaknesses', e.target.value)}
            placeholder={`What areas would you like to improve in ${subject}?`}
          />
        </div>
      </div>
    </div>
  );
} 