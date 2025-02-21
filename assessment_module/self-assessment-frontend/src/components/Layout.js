import React from 'react';

export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-blue-50">
      <nav className="bg-white shadow-sm border-b border-blue-100">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-semibold text-gray-800">
            Academic Self Assessment
          </h1>
        </div>
      </nav>
      <main className="max-w-7xl mx-auto px-4 py-8">{children}</main>
    </div>
  );
} 