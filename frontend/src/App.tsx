import React, { useState } from 'react';
import './App.css';
import QueryForm from './components/QueryForm';
import ResponseDisplay from './components/ResponseDisplay';
import FileUpload from './components/FileUpload';

interface QueryResponse {
  answers: string[];
}

function App() {
  const [response, setResponse] = useState<QueryResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [processingStage, setProcessingStage] = useState<string>('');

  const handleQuerySubmit = async (questions: string[]) => {
    if (!selectedFile) {
      setError('Please upload a PDF file first');
      return;
    }

    setLoading(true);
    setError('');
    setResponse(null);

    try {
      setProcessingStage('Processing document and generating embeddings...');
      
      // Create FormData for file upload
      const formData = new FormData();
      formData.append('file', selectedFile);
      formData.append('questions', JSON.stringify(questions));

      const response = await fetch('http://localhost:8000/api/v1/hackrx/upload', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer 4dfcfce5ebbd83a273f4c22b2b300878f060ee00becb274279f1e7b814edf8d9'
        },
        body: formData
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      setProcessingStage('Getting AI responses...');
      const data = await response.json();
      setResponse(data);
      setProcessingStage('Complete!');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      setProcessingStage('');
    } finally {
      setLoading(false);
      setTimeout(() => setProcessingStage(''), 2000);
    }
  };

  const handleFileSelect = (file: File | null) => {
    setSelectedFile(file);
    setError('');
    setResponse(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>LLM Query System</h1>
        <p>Upload PDF documents and ask questions to get AI-powered answers</p>
      </header>
      
      <main className="App-main">
        <FileUpload 
          onFileSelect={handleFileSelect} 
          selectedFile={selectedFile}
        />
        <QueryForm onSubmit={handleQuerySubmit} loading={loading} />
        {loading && processingStage && (
          <div className="processing-status">
            <div className="loading-spinner"></div>
            <p>{processingStage}</p>
          </div>
        )}
        <ResponseDisplay 
          response={response} 
          loading={loading} 
          error={error} 
        />
      </main>
    </div>
  );
}

export default App;