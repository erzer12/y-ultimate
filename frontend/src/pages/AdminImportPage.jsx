import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import * as childrenService from '../services/childrenService';

function AdminImportPage() {
  const { user, logout } = useAuth();
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type === 'text/csv') {
      setFile(selectedFile);
      setError('');
    } else {
      setError('Please select a valid CSV file');
      setFile(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    try {
      setUploading(true);
      setError('');
      setResult(null);
      
      const data = await childrenService.importChildren(file);
      setResult(data);
      setFile(null);
      
      // Reset file input
      const fileInput = document.getElementById('file-input');
      if (fileInput) fileInput.value = '';
    } catch (err) {
      setError('Failed to import children: ' + (err.response?.data?.error || err.message));
      console.error(err);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <div className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">Y-Ultimate - Admin Dashboard</h1>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600">
              {user?.name} ({user?.role})
            </span>
            <button
              onClick={logout}
              className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
            >
              Logout
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <h2 className="text-xl font-semibold text-gray-800 mb-6">Import Children from CSV</h2>

        {error && (
          <div className="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}

        {result && (
          <div className="mb-6 p-4 bg-green-100 border border-green-400 rounded">
            <h3 className="text-lg font-semibold text-green-800 mb-2">Import Results</h3>
            <p className="text-green-700">
              ✅ Successfully imported: {result.imported} children
            </p>
            {result.errors > 0 && (
              <p className="text-red-700 mt-2">
                ⚠️ Errors: {result.errors} rows failed
              </p>
            )}
          </div>
        )}

        {/* Upload Form */}
        <div className="bg-white rounded-lg shadow p-6 mb-6">
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Select CSV File
            </label>
            <input
              id="file-input"
              type="file"
              accept=".csv"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-500
                file:mr-4 file:py-2 file:px-4
                file:rounded file:border-0
                file:text-sm file:font-semibold
                file:bg-blue-50 file:text-blue-700
                hover:file:bg-blue-100"
            />
            {file && (
              <p className="mt-2 text-sm text-gray-600">
                Selected: {file.name}
              </p>
            )}
          </div>

          <button
            onClick={handleUpload}
            disabled={!file || uploading}
            className="px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
          >
            {uploading ? 'Uploading...' : 'Upload and Import'}
          </button>
        </div>

        {/* CSV Format Instructions */}
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">CSV Format</h3>
          
          <p className="text-sm text-gray-600 mb-4">
            Your CSV file should have the following columns:
          </p>
          
          <div className="bg-gray-50 p-4 rounded mb-4 overflow-x-auto">
            <pre className="text-sm">
firstName,lastName,dateOfBirth,siteId
John,Doe,2010-05-15,1
Jane,Smith,2011-08-22,1
Michael,Johnson,2009-12-10,2
Emily,Brown,2010-03-05,2
            </pre>
          </div>

          <div className="space-y-2 text-sm text-gray-700">
            <p><strong>Required fields:</strong></p>
            <ul className="list-disc list-inside ml-4 space-y-1">
              <li><code className="bg-gray-100 px-1 rounded">firstName</code> - Child's first name</li>
              <li><code className="bg-gray-100 px-1 rounded">lastName</code> - Child's last name</li>
              <li><code className="bg-gray-100 px-1 rounded">siteId</code> - Site ID (1 = Downtown, 2 = Westside)</li>
            </ul>
            
            <p className="mt-4"><strong>Optional fields:</strong></p>
            <ul className="list-disc list-inside ml-4 space-y-1">
              <li><code className="bg-gray-100 px-1 rounded">dateOfBirth</code> - Format: YYYY-MM-DD</li>
            </ul>
          </div>

          <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded">
            <p className="text-sm text-blue-800">
              💡 <strong>Tip:</strong> Download the sample CSV template from the backend-node directory to get started quickly.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AdminImportPage;
